#!/usr/bin/env python3
"""ロゴと人型グリフを data URI にして theme/deck.css へ埋め込む。

data URI にする理由: Marp の HTML / PDF / PNG のどれで出しても
相対パスの解決先が変わらないため。--allow-local-files への依存も消える。

ロゴの色の出どころ（推測していない）:
  SVG は simple-icons の単色パス。fill は simple-icons のブランド色データ
  （cdn.jsdelivr.net/npm/simple-icons@16.28.0/data/simple-icons.json）の実値。
  データに hex が無い OpenAI はマークが黒なので本文色 #1a1a1a を当てる。
  PNG は各プロジェクトの公式アイコンそのもの。色は加工していない。
"""
import base64, pathlib, re, urllib.parse

ICONS = pathlib.Path('assets/icons')
CSS   = pathlib.Path('theme/deck.css')

LOGOS = {
    'claude':  ('claude.svg',  '#D97757'),
    'codex':   ('openai.svg',  '#1a1a1a'),
    'cursor':  ('cursor.svg',  '#000000'),
    'copilot': ('copilot.svg', '#000000'),
    'zed':     ('zed.svg',     '#084CCF'),
    'tmux':    ('tmux.svg',    '#1BB91F'),
    'vscode':  ('vscode.png',  None),
    'ghostty': ('ghostty.png', None),
    'cmux':    ('cmux.png',    None),
    'herdr':   ('herdr.png',   None),
    'macterminal': ('macterminal.png', None),   # macOS 標準の Terminal.app から抽出
    'winterminal': ('winterminal.png', None),   # microsoft/terminal の公式アイコン
}

# AI を人に見立てるグリフ。頭＋肩の標準的な人型
PERSON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
          '<circle cx="32" cy="19" r="12" fill="{c}"/>'
          '<path d="M6 60c0-13.8 11.6-24 26-24s26 10.2 26 24z" fill="{c}"/>'
          '</svg>')


# 内容を表すための汎用アイコン（ツールのロゴではない）
GLYPHS = {
    'growth':   '<path d="M8 44h8v12H8zm14-8h8v20h-8zm14-6h8v26h-8z" fill="{c}"/><path d="M10 34 24 20l10 8 18-18" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="square" stroke-linejoin="miter"/><path d="M42 10h12v12" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="square" stroke-linejoin="miter"/>',
    'bolt':     '<path d="M34 4 12 36h14l-4 24 22-32H30z" fill="{c}"/>',
    'chat':     '<path d="M8 10h48a4 4 0 0 1 4 4v28a4 4 0 0 1-4 4H26L12 58V46H8a4 4 0 0 1-4-4V14a4 4 0 0 1 4-4z" fill="{c}"/>',
    'calendar': '<path d="M12 10h40a4 4 0 0 1 4 4v40a4 4 0 0 1-4 4H12a4 4 0 0 1-4-4V14a4 4 0 0 1 4-4z" fill="{c}"/><path d="M8 24h48v6H8z" fill="#ffffff"/><path d="M18 4h6v12h-6zm22 0h6v12h-6z" fill="{c}"/>',
    'doc':      '<path d="M14 4h26l12 12v44a4 4 0 0 1-4 4H14a4 4 0 0 1-4-4V8a4 4 0 0 1 4-4z" fill="{c}"/><path d="M18 30h28v4H18zm0 10h28v4H18zm0 10h18v4H18z" fill="#ffffff"/>',
    'split':    '<path d="M4 28h20v8H4zm36-16h20v8H40zm0 32h20v8H40z" fill="{c}"/><path d="M20 30h6v-14h18v4H30v10h-6zm0 4h6v14h18v-4H30V34h-6z" fill="{c}"/>',
}

PEOPLE = {
    'blue':  '#0031d8',
    'navy':  '#000071',
    'green': '#197a4b',
    'gray':  '#949494',
    'ink':   '#1a1a1a',
}


def uri_svg(markup: str) -> str:
    return 'data:image/svg+xml,' + urllib.parse.quote(re.sub(r'\s+', ' ', markup).strip(), safe='')


def uri_file(path: pathlib.Path, fill: str | None) -> str:
    if path.suffix == '.svg':
        s = re.sub(r'<title>.*?</title>', '', path.read_text(), flags=re.S)
        if fill:
            s = s.replace('<svg ', f'<svg fill="{fill}" ', 1)
        return uri_svg(s)
    return 'data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode()


lines = ['/* === GENERATED:BEGIN (scripts-build-icons.py が生成。手で編集しない) === */']

missing = []
for name, (fn, fill) in LOGOS.items():
    p = ICONS / fn
    if not p.exists():
        missing.append(fn)
        continue
    lines.append(f'.i-{name} {{ background-image: url("{uri_file(p, fill)}"); }}')

for name, hexv in PEOPLE.items():
    lines.append(f'.ai.{name} .glyph {{ background-image: url("{uri_svg(PERSON.format(c=hexv))}"); }}')

WRAP = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{body}</svg>'
for name, body in GLYPHS.items():
    lines.append(f'.g-{name} {{ background-image: url("{uri_svg(WRAP.format(body=body.format(c="#0031d8")))}"); }}')
    lines.append(f'.g-{name}.dark {{ background-image: url("{uri_svg(WRAP.format(body=body.format(c="#000071")))}"); }}')

lines.append('/* === GENERATED:END === */')

block = '\n'.join(lines) + '\n'
css = CSS.read_text()
pat = re.compile(r'/\* === GENERATED:BEGIN.*?/\* === GENERATED:END === \*/\n', re.S)
css = pat.sub(block, css) if pat.search(css) else css.rstrip() + '\n\n' + block
CSS.write_text(css)

print(f'ロゴ {len(LOGOS) - len(missing)}/{len(LOGOS)} 件・人型 {len(PEOPLE)} 色を埋め込み')
if missing:
    print('見つからなかったファイル:', missing)
