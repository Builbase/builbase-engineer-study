# エンジニア勉強会 第2回（2026-09-28 / 60分）

「AIエージェントの用語を、仕組みの順に理解する」。
コンテキスト、CLAUDE.md、rules、memory、エージェントループ、ループエンジニアリング、
ハーネス、skills、hooks、settings.jsonを、AIが「何を読み、どう動き、どう縛られるか」の順に置く。
全28枚。テーマCSSは第1回の`../theme/deck.css`をそのまま使い、第2回だけの部品は`slides.md`の`style:`に置く。

## ファイル

| ファイル | 中身 |
|---|---|
| `slides.md` | Marp本体（全28枚） |
| `content-notes.md` | **話す内容の正本** |
| `demo-script.md` | 2回の実演と時間調整 |
| `scripts-blur.py` | スクリーンショットの指定範囲を塗りつぶす（ffmpeg。ぼかしは復元されうるので不透明で塗る） |
| `assets/shots/` | 加工済みスクリーンショットの置き場。`raw/`は元画像でgit管理外 |
| `build/` | HTML、PDF、PNGの出力先（git管理外） |

## 60分の構成

| 範囲 | 内容 | 時間 |
|---|---|---:|
| 1–4 | 導入。環境で結果が変わる例、3章の予告 | 4分 |
| 5–9 | 1. コンテキスト。開始時の中身、積み上がり、圧縮 | 9分 |
| 実演1 | 自分のClaude Codeで`/context`を見せる | 3分 |
| 10–12 | CLAUDE.md、rules、memory | 7分 |
| 13–18 | 2. エージェントループ、ツールとMCP、完了条件、ループエンジニアリング | 11分 |
| 19–22 | 3. ハーネスの定義、案内と検査、skills | 7分 |
| 23–24 | hooksと、PreToolUse hookが止めた実例（スクリーンショット） | 3分 |
| 実演2 | 24枚目の実例を自分の環境で再現する | 4分 |
| 25–26 | settings.json、強制力の段 | 4分 |
| 27–28 | 用語の一覧、今日から試す3つ | 3分 |
| 質疑 | 途中で扱えなかった質問 | 5分 |

本編48分、実演7分、質疑5分。
時間が押した場合は、18枚目（ループの3分類）と27枚目（用語一覧）を口頭の一言に縮める。実演2は24枚目のスクリーンショットで代替できる。

当日のチェックポイント:

| 経過 | 到達点 |
|---|---|
| 0:04 | 5枚目、第1章 |
| 0:13 | 実演1 |
| 0:16 | 10枚目、CLAUDE.md |
| 0:23 | 13枚目、第2章 |
| 0:34 | 19枚目、第3章 |
| 0:41 | 23枚目、hooks |
| 0:44 | 実演2 |
| 0:48 | 25枚目、settings.json |
| 0:52 | 27枚目、用語一覧 |
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

# 28枚を一覧表示
ffmpeg -y -pattern_type glob -i 'build/png/s.0*.png' -vf "scale=640:360,tile=3x10" -frames:v 1 build/sheet/contact.png
```

表記の確認は第1回の`README.md`と同じコマンドを使う。

## 内容上の前提

- 用語の説明は、この勉強会で使う整理であり、製品の正式な分類ではない。
  出典は各スライドのMarpコメント`[Sources]`に置く（投影には出ない）
- 事実の正本はClaude Code公式ドキュメント（memory、context-window、hooks、skills、settings、costs）、
  ハーネスの定義はBirgitta Böckeler（martinfowler.com、2026-04）、
  ループエンジニアリングはAddy Osmaniの記事とFindy Team+の解説
- 7枚目は2026-09-21に自分の環境で`/context`を実行した実画面。8枚目の開始時の値（34k）はその合計、
  以降の各行は公式ドキュメントのシミュレーションにある代表値で、話す内容にそう断っている
- 24枚目は同日に自分の環境で「.envの中身を表示して」と頼み、PreToolUse hookが拒否した実画面
- 「ハーネスは製品側と利用者側の2段」「強制力の3段」は、学生が置き場を選べるようにするための整理

## デザインの約束

第1回の`README.md`の「デザインの約束」をそのまま守る。
加えて第2回では次を守った。

- 表は26枚目の1枚だけ。Marp既定の`section table`は`display:block; width:max-content`なので、
  全幅に伸ばすときは`display:table; width:100%`と`colgroup`で列幅を指定する
- `content-center`のページで`.rule`を使うときは`box-sizing:border-box`が要る（左右28pxずつはみ出す）
- 3段の`layer-stack`＋注記1行は既定の高さでは下へ36pxはみ出す。`tight`で1段92pxに詰める
- 循環（14枚目）、圧縮前後（9枚目）、入れ子（20枚目）、段（25枚目）はインラインSVGで描く。
  文字は本文と同じ書体、色はテーマのCSS変数の実値
- 製品名にはアイコンを添える。第2回で GitHub、npm、Supabase、Next.js、Git を追加した。
  取得元は simple-icons 16.28.0、色は同梱データの実値。`../scripts-build-icons.py`に登録し
  `../theme/deck.css` へ埋め込む（第1回の既存行は変わらない）。黒地では `filter: invert(1)` で反転する

## スクリーンショット

7枚目（`/context`の内訳）と24枚目（PreToolUse hookの拒否）は、2026-09-21に自分の環境で撮った実画面。

撮り方: ローカルのターミナルを`ttyd`でブラウザに映し、Claude in Chromeで操作と撮影をした
（画面自動化のcmux-cuaは権限未設定で使えなかった）。手順は`demo-script.md`の「撮影の手順」。

加工した箇所:

- `assets/shots/hook-deny.png`: コマンド内のホームディレクトリ以下のフルパス2箇所を不透明で塗りつぶし
- `assets/shots/context-categories.png`: 内訳の部分だけを切り出し（塗りつぶしなし。パスや名前は写っていない）
- `assets/shots/hook-deny-crop.png`: 指示から拒否メッセージまでを切り出し
- 元画像は`assets/shots/raw/`（git管理外）

差し替えるときは、元画像を`raw/`へ置き、`python3 scripts-blur.py raw/x.png x.png --box x,y,w,h`で塗り、
`ffmpeg -i x.png -vf crop=W:H:X:Y x-crop.png`で切り出し、上の一覧に加工内容を1行足す。
