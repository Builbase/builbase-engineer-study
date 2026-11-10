# エンジニア勉強会 第4回（2026-11-11 / 60分）

「パーソナルエージェントとAI組織：Muse、dots、Duet、Grok Botの設計と使い分け」。
2026年8〜10月に出た4つのパーソナルエージェント（Grok Bot、Muse、dots、Claude Duet）を、設計（実行環境、起動、承認）、モデル、連携数、提供地域、料金で比べる。
そのうえで、会社が自前で組んできた「AI社員」「AI組織」の作り方（単一エージェント、ワークフロー、マルチエージェント）と使い分けを整理する。

**エンジニア向けに書く**（2026-11-10、ユーザーの指示）。VM、OAuth、MCP、オーケストレーターなどの用語は言い換えずにそのまま使う。
第3回の「ひとことで」「たとえると」と日常の例えは使わず、各ページの上の1行は「要点」にする。

全30枚（表紙1、目次1、章扉4、本文23、まとめ1）。章末の問いは入れない（2026-11-10、ユーザーの指示）。テーマCSSは第1回の`../theme/deck.css`、部品は第3回の`style:`を引き継ぎ、第4回だけの部品は`style:`の末尾に置く。

## ファイル

| ファイル | 中身 |
|---|---|
| `slides.md` | Marp本体（全30枚）。各ページのコメントに`[話すこと]`と`[Sources]` |
| `content-notes.md` | 構成の判断と事実確認の記録 |
| `demo-script.md` | 2回の実演と時間調整 |
| `build/` | HTML、PDF、PNGの出力先（git管理外） |

## 60分の構成

| 範囲 | 内容 | 時間 |
|---|---|---:|
| 1–2 | 表紙、目次 | 1分 |
| 3–8 | 1. パーソナルエージェントの設計（5枚目が全体の地図、7枚目が構成図） | 9分 |
| 9–10 | 2. 4製品の比較（Museまで） | 2分 |
| 実演1 | Museに用事を頼み、承認を求める画面まで見せる | 3分 |
| 11–18 | 2. 続き（dots〜選び方） | 12分 |
| 19–22 | 3. AI社員とAI組織の作り方（組み方まで） | 6分 |
| 実演2 | AI社員の設定画面を見せる | 3分 |
| 23–25 | 3. 続き（制御フロー、5つのパターン、トークン） | 5分 |
| 26–29 | 4. 使い分け | 6分 |
| 30 | まとめ | 2分 |
| 質疑 | | 5分 |

本編49分＋予備6分。
時間が押した場合は、次を口頭の一言に縮める: 承認の境界（8枚目）、使用量の上限（17枚目）、トークンの比較（25枚目）。

当日のチェックポイント:

| 経過 | 到達点 |
|---|---|
| 0:10 | 9枚目、第2章 |
| 0:12 | 実演1（10枚目のあと） |
| 0:27 | 19枚目、第3章 |
| 0:33 | 実演2（22枚目のあと） |
| 0:41 | 26枚目、第4章 |
| 0:47 | 30枚目、まとめ |
| 0:55 | 質疑へ移る（予備を使い切った場合） |

## ビルド

`vol4/`の中で実行する。

```sh
# HTML
marp slides.md -o build/slides.html --theme ../theme/deck.css --html < /dev/null

# PDF
marp slides.md -o build/slides.pdf --theme ../theme/deck.css --html --allow-local-files < /dev/null

# PNG
marp slides.md --images png -o build/png/s.png --theme ../theme/deck.css --html --allow-local-files < /dev/null

# 安全域からのはみ出しを機械で確認する
python3 ../scripts-check-margins.py

# 30枚を一覧表示
ffmpeg -y -pattern_type glob -i 'build/png/s.0*.png' -vf "scale=480:270,tile=4x8" -frames:v 1 build/contact.png
```

2026-11-10時点、Homebrewの`marp`はNode.js 26で起動しない（yargsの`require is not defined`）。
`/opt/homebrew/opt/node@24/bin/node /opt/homebrew/lib/node_modules/@marp-team/marp-cli/marp-cli.js`で同じ引数を渡すと動く。

## ロゴとアイコン

第4回で10件を追加した（`scripts-build-icons.py`で`theme/deck.css`へ埋め込み）。

- Muse、Claude Duet、Grok Bot、ChatGPT: App Storeの公式アプリアイコン（iTunes Search APIの`artworkUrl`を256pxで取得、2026-11-10）
- dotsは単独のアプリが無く、ChatGPTの中の機能なので、ChatGPTのアイコンで表す
- n8n、Dify、CrewAI、LangGraph、Zapier、Make: simple-icons 16.28.0。色は同梱データの実値
- simple-iconsの最新（16.37.0）にも、Muse、dots、Duet、Grok Botの収録は無かった

各ロゴは識別のための引用で、権利は各社・各プロジェクトに帰属する。

## デザインの約束

第1回と第3回の`README.md`の約束を守る。第4回で加えた部品:

- `.tl`: 発表日の年表。1社1行で、日付、アイコン、名前、会社、ひとことを横に並べる
- `.profile`と`.pf`: 製品紹介。左にアイコンと名前、右に「得意なこと、使える場所、日本、料金、特徴」の5行。4製品で同じ順にそろえる
- `.map`: 言葉の地図（起動の主体×対象の範囲）。5枚目
- `.quad`: 2軸の4象限（生活の用事か仕事か、1人かチームか）。軸の名前も製品の説明も横書きで1行に収める
- 狭い枠に文字を縦に積まない。短い説明は`white-space: nowrap`で1行に固定し、入らなければ文言を短くする（2026-11-10、ユーザーの指摘）
- `.compare.prod`: 列見出しにアイコンを置く比較表
