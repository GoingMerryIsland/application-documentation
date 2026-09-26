#!/usr/bin/env python3
"""Check documentation artifact files. Browser/visual QA remains a separate gate."""
import argparse
import json
import re
import sys
import zipfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET


class PreviewParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.references = []
        self.inline_css = []
        self.in_style = False
        self.content_tags = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('main', 'article', 'section', 'h1', 'h2', 'p', 'table', 'svg', 'img', 'canvas', 'pre'):
            self.content_tags += 1
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        if tag == 'style':
            self.in_style = True
        if attrs.get('style'):
            self.inline_css.append(attrs['style'])
        for key in ('src', 'href', 'poster', 'xlink:href', 'data'):
            if key == 'data' and tag != 'object':
                continue
            if key in attrs:
                resource = tag not in ('a', 'area')
                self.references.append((attrs[key], resource, tag))
        # srcset can contain data URLs with commas: leave these to browser QA.
        if attrs.get('srcset') and 'data:' not in attrs['srcset']:
            for entry in attrs['srcset'].split(','):
                parts = entry.strip().split()
                if parts:
                    self.references.append((parts[0], True, tag))

    def handle_endtag(self, tag):
        if tag == 'style':
            self.in_style = False

    def handle_data(self, data):
        if self.in_style:
            self.inline_css.append(data)


def validate(root, required, offline=False):
    root = Path(root).resolve()
    result = {'root': str(root), 'errors': [], 'warnings': [], 'files': [],
              'browser_verification': 'not performed by this structural validator'}
    errors, warnings = result['errors'], result['warnings']
    index = root / 'index.html'
    if not index.is_file():
        errors.append('Missing index.html')
        return result
    parser = PreviewParser()
    try:
        parser.feed(index.read_text(encoding='utf-8-sig'))
    except (OSError, UnicodeError, ValueError) as exc:
        errors.append(f'Cannot parse index.html: {exc}')
        return result
    if not parser.content_tags:
        errors.append('index.html has no recognizable documentation content')
    duplicates = [key for key, n in Counter(parser.ids).items() if n > 1]
    if duplicates:
        errors.append('Duplicate HTML ids: ' + ', '.join(duplicates))
    linked = set()

    def reference(value, base, resource, tag='resource'):
        if not value or value == '#':
            return
        try:
            parsed = urlsplit(value)
        except ValueError:
            errors.append(f'Invalid {tag} reference: {value}')
            return
        if parsed.scheme == 'javascript':
            errors.append(f'Executable URL in {tag}: {value}')
            return
        if parsed.scheme in ('data', 'blob', 'mailto', 'tel'):
            return
        if parsed.scheme or parsed.netloc:
            if resource and offline:
                errors.append(f'Network/absolute resource prevents portable offline use: {value}')
            return
        if not parsed.path:
            if base == index and parsed.fragment and unquote(parsed.fragment) not in parser.ids:
                errors.append(f'Broken in-page anchor: {value}')
            return
        path = (base.parent / unquote(parsed.path)).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            errors.append(f'Reference escapes artifact folder: {value}')
            return
        if not path.exists():
            errors.append(f'Missing linked file: {value}')
            return
        linked.add(path)

    for value, resource, tag in parser.references:
        reference(value, index, resource, tag)

    css_pattern = re.compile(r'url\(\s*[\'"]?([^\)\'\"]+)[\'"]?\s*\)|@import\s+[\'"]([^\'"]+)[\'"]', re.I)
    css_sources = [(index, '\n'.join(parser.inline_css))]
    for path in root.rglob('*.css'):
        if path.resolve().is_relative_to(root):
            try:
                css_sources.append((path, path.read_text(encoding='utf-8-sig')))
            except (OSError, UnicodeError) as exc:
                errors.append(f'Cannot read stylesheet {path.name}: {exc}')
    for path, text in css_sources:
        for match in css_pattern.finditer(text):
            reference((match.group(1) or match.group(2)).strip(), path, True, 'CSS')

    for svg in root.rglob('*.svg'):
        if not svg.resolve().is_relative_to(root):
            errors.append(f'SVG symlink escapes artifact folder: {svg.name}')
            continue
        try:
            doc = ET.parse(svg)
            for element in doc.iter():
                tag = element.tag.rsplit('}', 1)[-1]
                if tag.lower() == 'script':
                    errors.append(f'Active script in SVG: {svg.relative_to(root)}')
                for key, value in element.attrib.items():
                    attribute = key.rsplit('}', 1)[-1].lower()
                    if attribute.startswith('on'):
                        errors.append(f'Active event handler in SVG: {svg.relative_to(root)}')
                    if attribute in ('href', 'src'):
                        reference(value, svg, tag != 'a', 'SVG')
                    if attribute == 'style':
                        for match in css_pattern.finditer(value):
                            reference((match.group(1) or match.group(2)).strip(), svg, True, 'SVG CSS')
                if tag.lower() == 'style' and element.text:
                    for match in css_pattern.finditer(element.text):
                        reference((match.group(1) or match.group(2)).strip(), svg, True, 'SVG CSS')
        except (OSError, ET.ParseError) as exc:
            errors.append(f'Invalid SVG {svg.name}: {exc}')

    extensions = {'pdf': 'pdf', 'pptx': 'pptx', 'png': 'png', 'jpg': 'jpg', 'jpeg': 'jpg'}
    counts = Counter()
    export_root = root / 'exports'
    paths = sorted(p for p in export_root.rglob('*') if p.is_file()) if export_root.exists() else []
    for path in paths:
        fmt = extensions.get(path.suffix.lower().lstrip('.'))
        if not fmt:
            continue
        if not path.resolve().is_relative_to(root):
            errors.append(f'Export symlink escapes artifact folder: {path.name}')
            continue
        record = {'path': path.relative_to(root).as_posix(), 'format': fmt}
        result['files'].append(record)
        counts[fmt] += 1
        try:
            data = path.read_bytes()
            record['bytes'] = len(data)
            if fmt == 'pdf':
                if not data.startswith(b'%PDF-') or b'%%EOF' not in data[-4096:]:
                    raise ValueError('Missing PDF header or final EOF marker')
                try:
                    from pypdf import PdfReader
                except ImportError:
                    warnings.append('pypdf unavailable: PDF structure/page count not verified')
                else:
                    reader = PdfReader(path)
                    if reader.is_encrypted or not reader.pages:
                        raise ValueError('PDF is encrypted or has no pages')
                    record['pages'] = len(reader.pages)
            elif fmt == 'pptx':
                with zipfile.ZipFile(path) as archive:
                    bad = archive.testzip()
                    if bad:
                        raise ValueError(f'Corrupt ZIP member: {bad}')
                    names = archive.namelist()
                    for required_member in ('[Content_Types].xml', '_rels/.rels', 'ppt/presentation.xml', 'ppt/_rels/presentation.xml.rels'):
                        if required_member not in names:
                            raise ValueError(f'Missing PPTX member: {required_member}')
                    pres = ET.fromstring(archive.read('ppt/presentation.xml'))
                    ns = {'p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
                    listed_slides = pres.findall('./p:sldIdLst/p:sldId', ns)
                    slides = [n for n in names if re.fullmatch(r'ppt/slides/slide\d+\.xml', n)]
                    if not listed_slides or len(listed_slides) != len(slides):
                        raise ValueError('Missing slides or presentation/slide count mismatch')
                    editable = 0
                    for slide in slides:
                        doc = ET.fromstring(archive.read(slide))
                        editable += sum(bool((el.text or '').strip()) for el in doc.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t'))
                    try:
                        from pptx import Presentation
                    except ImportError:
                        warnings.append('python-pptx unavailable: PowerPoint relationship loading not verified')
                    else:
                        deck = Presentation(path)
                        if len(deck.slides) != len(slides):
                            raise ValueError('PowerPoint parser slide count mismatch')
                    record.update(slides=len(slides), editable_text_runs=editable)
                    if not editable:
                        errors.append(f'{record["path"]}: no editable slide text')
            else:
                expected = b'\x89PNG\r\n\x1a\n' if fmt == 'png' else b'\xff\xd8\xff'
                if not data.startswith(expected):
                    raise ValueError(f'File signature does not match {fmt}')
                try:
                    from PIL import Image
                except ImportError:
                    warnings.append('Pillow unavailable: image decoding/dimensions not verified')
                else:
                    with Image.open(path) as img:
                        img.verify()
                    with Image.open(path) as img:
                        img.load()
                        record['dimensions'] = list(img.size)
                        if min(img.size) < 2:
                            raise ValueError('Image is empty-sized or a placeholder pixel')
                        if fmt == 'jpg' and img.mode not in ('RGB', 'L'):
                            raise ValueError('JPEG is not browser-friendly RGB/grayscale')
        except Exception as exc:  # Preserve other file results if a decoder rejects one export.
            errors.append(f'{record["path"]}: {type(exc).__name__}: {exc}')

    for fmt in required:
        if not counts[fmt]:
            errors.append(f'Missing required {fmt} export under exports/')
    unlinked = [r['path'] for r in result['files'] if (root/r['path']).resolve() not in linked]
    if unlinked:
        warnings.append('Exports without static HTML links; verify dynamic controls in browser: ' + ', '.join(unlinked))
    warnings.append('Static checks cannot prove offline JavaScript, export freshness, layout, or working controls; complete browser and visual QA.')
    result['warnings'] = list(dict.fromkeys(warnings))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--required', nargs='*', choices=('pdf','pptx','png','jpg'), default=['pdf','pptx','png','jpg'])
    parser.add_argument('--offline', action='store_true')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = validate(args.directory, args.required, args.offline)
    output = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output + '\n', encoding='utf-8')
    print(output)
    return 1 if result['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
