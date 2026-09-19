#!/usr/bin/env python3
"""Check shipped font integrity and local CSS/document references. No dependencies."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []


def local_reference(source: Path, reference: str) -> None:
    reference = reference.strip().strip('<>')
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return
    target = (source.parent / unquote(parsed.path)).resolve()
    if not target.is_relative_to(ROOT) or not target.exists():
        errors.append(f'{source.relative_to(ROOT)}: unresolved local reference {reference}')


themes = sorted(path.name for path in (ROOT / 'themes').glob('*.css'))
expected = sorted(['cutelemon6-day.css', 'cutelemon6-night.css', 'cutelemon6-editorial.css'])
if themes != expected:
    errors.append(f'Expected exactly three theme entries, got {themes}')

manifest = json.loads((ROOT / 'font-manifest.json').read_text(encoding='utf-8'))
for record in manifest:
    path = ROOT / record['file']
    if not path.is_file():
        errors.append(f'Missing font: {record["file"]}')
    elif hashlib.sha256(path.read_bytes()).hexdigest() != record['sha256']:
        errors.append(f'Font hash mismatch: {record["file"]}')

for source in (ROOT / 'themes').rglob('*.css'):
    text = source.read_text(encoding='utf-8')
    for reference in re.findall(r'url\(["\']?([^\)"\']+)', text):
        local_reference(source, reference)

for source in ROOT.rglob('*.md'):
    if '.git' in source.parts:
        continue
    for reference in re.findall(r'\]\(([^)]+)\)', source.read_text(encoding='utf-8')):
        local_reference(source, reference)

preview = ROOT / 'preview/index.html'
for reference in re.findall(r'(?:href|src)=["\']([^"\']+)', preview.read_text(encoding='utf-8')):
    local_reference(preview, reference)

license_dir = ROOT / 'themes/cutelemon6/licenses'
for name in ['Open-Sans-Apache-2.0.txt', 'Source-Han-Sans-OFL.txt', 'Source-Han-Serif-OFL.txt', 'Source-Serif-4-OFL.txt']:
    if not (license_dir / name).is_file():
        errors.append(f'Missing font license: {name}')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'OK: 3 themes, {len(manifest)} font hashes, local references, and font licenses.')
