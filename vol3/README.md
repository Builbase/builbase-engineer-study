# エンジニア勉強会 第3回（2026-10-26 / 60分）

「エンジニアの基礎」。開発プロセス、Webの仕組み、DB、クラウド、セキュリティの5章で、
Webサービスを作って動かすまでに必要な基本を一周する。DBとクラウドは、主なツールと選び方まで扱う。
聴衆は学生エンジニア（ほぼ非エンジニア）。各ページの上に「ひとことで」（平易な言い換え）か「たとえると」（日常の例え。各章の入口と難しい概念だけ）を1行置き、
用語は平易な言葉に正式名を括弧で添える。発展的な5枚（分離レベル、N+1、CSR/SSR/SSG、リージョンとAZ、3大クラウドの対応表）は削った（2026-10-20に決定）。

全41枚（表紙1、目次1、章扉5、本文33、まとめ1）。テーマCSSは第1回の`../theme/deck.css`を使い、第3回だけの部品は`slides.md`の`style:`に置く。

## ファイル

| ファイル | 中身 |
|---|---|
| `slides.md` | Marp本体（全41枚）。各ページのコメントに`[話すこと]`と`[Sources]` |
| `content-notes.md` | 構成、時間配分、事実確認の記録 |
| `demo-script.md` | 2回の実演と時間調整 |
| `build/` | HTML、PDF、PNGの出力先（git管理外） |

## 60分の構成

| 範囲 | 内容 | 時間 |
|---|---|---:|
| 1–2 | 表紙、目次 | 1分 |
| 3–10 | 1. 開発プロセス | 8分 |
| 11–16 | 2. Webの仕組み | 8分 |
| 実演1 | DevToolsのNetworkタブ | 2分 |
| 17–27 | 3. DB | 12分 |
| 実演2 | SupabaseのTable EditorとEXPLAIN ANALYZE | 2分 |
| 28–35 | 4. クラウド | 11分 |
| 36–40 | 5. セキュリティ | 9分 |
| 41 | まとめ | 2分 |
| 質疑 | | 5分 |

本文1枚あたり約1.5分。
時間が押した場合は、次を口頭の一言に縮める: V字モデル（5枚目）、NoSQLの4種（23枚目）、構成の例（34枚目）。

当日のチェックポイント:

| 経過 | 到達点 |
|---|---|
| 0:09 | 11枚目、第2章 |
| 0:17 | 実演1 |
| 0:19 | 17枚目、第3章 |
| 0:31 | 実演2 |
| 0:33 | 28枚目、第4章 |
| 0:44 | 36枚目、第5章 |
| 0:53 | 41枚目、まとめ |
| 0:55 | 質疑へ移る |

## ビルド

`vol3/`の中で実行する。

```sh
# HTML
marp slides.md -o build/slides.html --theme ../theme/deck.css --html < /dev/null

# PDF
marp slides.md -o build/slides.pdf --theme ../theme/deck.css --html --allow-local-files < /dev/null

# PNG
marp slides.md --images png -o build/png/s.png --theme ../theme/deck.css --html --allow-local-files < /dev/null

# 安全域からのはみ出しを機械で確認する
python3 ../scripts-check-margins.py

# 41枚を一覧表示
ffmpeg -y -pattern_type glob -i 'build/png/s.0*.png' -vf "scale=640:360,tile=4x11" -frames:v 1 build/sheet/contact.png
```

表記の確認は第1回の`README.md`と同じコマンドを使う。

## デザインの約束

第1回の`README.md`の「デザインの約束」を守る。第3回で加えたこと:

- 横並びの工程（`.flow.sm`、`.flow.agenda`、`.flow.eq`）は等幅のflexにする。既定の`.flow`は内容幅のgridなので、5〜6段並べると1文字ずつ折り返す
- 全ページを同じ順に組む: 見出し → 一言（`.lead`、たとえは`.lead.ana`）→ 主役の図（残りの高さを使い切る）→ まとめの1行（`.rule`）。`content-center`は使わない
- 手順や工程は、横並びではなく番号付きの縦の行（`.vsteps`）にする。横並びは1枚あたりの幅が狭く、1文字ずつ折り返す
- 左右の比較（`.pair`）は見出しと箇条書きを左にそろえ、縦は中央に置く
- 長い注記は投影に出さず、コメントの`[話すこと]`へ移す。`text-wrap: pretty`で1〜2文字だけの行を防ぐ
- 表は`.compare.full`（`display:table; width:100%`）と`colgroup`で列幅を指定する
- ロゴを11件追加した（PostgreSQL、MySQL、SQLite、MongoDB、Redis、Firebase、Google Cloud、Vercel、Render、Cloudflare、Neon）。
  取得元はsimple-icons 16.28.0、色は同梱データの実値。AWSとAzureはsimple-iconsに収録が無いため、文字で表す
