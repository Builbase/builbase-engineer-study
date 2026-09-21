# エンジニア勉強会 第2回（2026-09-28 / 60分）

「AIに仕事を任せるとき、AIの中で何が起きているか」。
ほぼ非エンジニアの学生向けに、コンテキスト、CLAUDE.md、rules、memory、エージェントループ、
ループエンジニアリング、ハーネス、skills、hooks、settings.jsonを、日常の言葉（机の上、申し送りメモ、日記、
手順書、見張り、許可リスト、手綱と柵）で言い換えて、AIが「何を読み、どう動き、どう縛られるか」の順に置く。
第4章で講師の環境の実物と、柵を足すときの考え方4つを見せる。全34枚。テーマCSSは第1回の`../theme/deck.css`をそのまま使い、第2回だけの部品は`slides.md`の`style:`に置く。

## ファイル

| ファイル | 中身 |
|---|---|
| `slides.md` | Marp本体（全34枚） |
| `content-notes.md` | **話す内容の正本** |
| `demo-script.md` | 2回の実演と時間調整 |
| `scripts-blur.py` | スクリーンショットの指定範囲を塗りつぶす（ffmpeg。ぼかしは復元されうるので不透明で塗る） |
| `assets/shots/` | 加工済みスクリーンショットの置き場。`raw/`は元画像でgit管理外 |
| `build/` | HTML、PDF、PNGの出力先（git管理外） |

## 60分の構成

| 範囲 | 内容 | 時間 |
|---|---|---:|
| 1–5 | 導入。設定で結果が変わる例、4章の予告、今日のAIの定義 | 4分 |
| 6–10 | 1. 机の上（コンテキスト）。頼む前の中身、積み上がり、片づけ | 8分 |
| 実演1 | 自分のClaude Codeで`/context`を見せる | 3分 |
| 11–13 | 申し送りメモ、条件つきメモ、日記 | 6分 |
| 14–17 | 2. 繰り返し、終わりの条件、回す仕組み | 6分 |
| 18–22 | 3. 手綱と柵、事前と事後、手順書、見張り | 8分 |
| 23 | 見張りが止めた実例（スクリーンショット） | 2分 |
| 実演2 | 23枚目の実例を自分の環境で再現する | 3分 |
| 24–25 | 設定ファイル、確実に守らせたいものほど下の段へ | 3分 |
| 26–32 | 4. 私の環境。全体像、考え方4つ、柵を作る順番 | 9分 |
| 33–34 | 言葉の一覧、今日から試す3つ | 3分 |
| 質疑 | 途中で扱えなかった質問 | 5分 |

本編49分、実演6分、質疑5分。
時間が押した場合は、17枚目（回す仕組み）と33枚目（言葉の一覧）を口頭の一言に縮める。実演2は23枚目のスクリーンショットで代替できる。

当日のチェックポイント:

| 経過 | 到達点 |
|---|---|
| 0:04 | 6枚目、第1章 |
| 0:12 | 実演1 |
| 0:15 | 11枚目、申し送りメモ |
| 0:21 | 14枚目、第2章 |
| 0:27 | 18枚目、第3章 |
| 0:35 | 23枚目、見張りの実例 |
| 0:37 | 実演2 |
| 0:40 | 24枚目、設定ファイル |
| 0:43 | 26枚目、第4章 |
| 0:52 | 33枚目、言葉の一覧 |
| 0:55 | 質疑へ移る |
| 1:00 | 終了 |

## ビルド

`vol2/`の中で実行する。

```sh
# スクリーンショットはHTMLから相対参照するので build/ へ複製する（PDF/PNGは --allow-local-files で埋め込む）
mkdir -p build/assets/shots && cp assets/shots/*.png build/assets/shots/

# HTML
marp slides.md -o build/slides.html --theme ../theme/deck.css --html < /dev/null

# PDF
marp slides.md -o build/slides.pdf --theme ../theme/deck.css --html --allow-local-files < /dev/null

# PNG
marp slides.md --images png -o build/png/s.png --theme ../theme/deck.css --html --allow-local-files < /dev/null

# 安全域からのはみ出しを機械で確認する
python3 ../scripts-check-margins.py

# 34枚を一覧表示
ffmpeg -y -pattern_type glob -i 'build/png/s.0*.png' -vf "scale=640:360,tile=3x12" -frames:v 1 build/sheet/contact.png
```

表記の確認は第1回の`README.md`と同じコマンドを使う。

## 内容上の前提

- 用語の説明は、この勉強会で使う整理であり、製品の正式な分類ではない。
  出典は各スライドのMarpコメント`[Sources]`に置く（投影には出ない）
- 事実の正本はClaude Code公式ドキュメント（memory、context-window、hooks、skills、settings、costs）、
  ハーネスの定義はBirgitta Böckeler（martinfowler.com、2026-04）、
  ループエンジニアリングはAddy Osmaniの記事とFindy Team+の解説
- 8枚目は2026-09-21に自分の環境で`/context`を実行した実画面。9枚目の開始時の値（34k）はその合計、
  以降の各行は公式ドキュメントのシミュレーションにある代表値で、話す内容にそう断っている
- 23枚目は同日に自分の環境で「.envの中身を表示して」と頼み、PreToolUse hookが拒否した実画面
- 第4章の実数（申し送りメモ11行、共通原則49行、日記87件、rules 4本、skills 20本、hooks 20本、
  deny 21件、ask 19件、allow 49件）は2026-09-21に`~/.claude`と`~/.agents`を数えた値。秘密の値は含まない
- 用語は投影面では日常の言葉で言い、正式名は括弧で添える。用語一覧（33枚目）が対応表
- 「ハーネスは製品側と利用者側の2段」「強制力の3段」は、学生が置き場を選べるようにするための整理

## デザインの約束

第1回の`README.md`の「デザインの約束」をそのまま守る。
加えて第2回では次を守った。

- 表は26枚目の1枚だけ。Marp既定の`section table`は`display:block; width:max-content`なので、
  全幅に伸ばすときは`display:table; width:100%`と`colgroup`で列幅を指定する
- `content-center`のページで`.rule`を使うときは`box-sizing:border-box`が要る（左右28pxずつはみ出す）
- 3段の`layer-stack`＋注記1行は既定の高さでは下へ36pxはみ出す。`tight`で1段92pxに詰める
- 循環（15枚目）、圧縮前後（10枚目）、入れ子（19枚目）、段（25枚目）はインラインSVGで描く。
  文字は本文と同じ書体、色はテーマのCSS変数の実値
- 製品名にはアイコンを添える。第2回で GitHub、npm、Supabase、Next.js、Git を追加した。
  取得元は simple-icons 16.28.0、色は同梱データの実値。`../scripts-build-icons.py`に登録し
  `../theme/deck.css` へ埋め込む（第1回の既存行は変わらない）。黒地では `filter: invert(1)` で反転する

## スクリーンショット

8枚目（`/context`の内訳）と23枚目（PreToolUse hookの拒否）は、2026-09-21に自分の環境で撮った実画面。

撮り方: ローカルのターミナルを`ttyd`でブラウザに映し、Claude in Chromeで操作と撮影をした
（画面自動化のcmux-cuaは権限未設定で使えなかった）。手順は`demo-script.md`の「撮影の手順」。

加工した箇所:

- `assets/shots/hook-deny.png`: コマンド内のホームディレクトリ以下のフルパス2箇所を不透明で塗りつぶし
- 第4章（27枚目）の中身の例は、`~/.claude/CLAUDE.md`・共通原則・hooksの実物から、秘密を含まない範囲で要約した
- `assets/shots/context-categories.png`: 内訳の部分だけを切り出し（塗りつぶしなし。パスや名前は写っていない）
- `assets/shots/hook-deny-crop.png`: 指示から拒否メッセージまでを切り出し
- 元画像は`assets/shots/raw/`（git管理外）

差し替えるときは、元画像を`raw/`へ置き、`python3 scripts-blur.py raw/x.png x.png --box x,y,w,h`で塗り、
`ffmpeg -i x.png -vf crop=W:H:X:Y x-crop.png`で切り出し、上の一覧に加工内容を1行足す。
