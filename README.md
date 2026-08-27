# エンジニア勉強会 第1回（2026-08-28 / 60分）

「ターミナルとエディタ」「AIを複数体動かす」の2本立て。全31枚。

ページ番号は出さない設定（`paginate: false`）。
スライドは1枚1メッセージに絞り、詳しい説明は`content-notes.md`と口頭で補う。

## ファイル

| ファイル | 中身 |
|---|---|
| `slides.md` | Marp本体（31枚） |
| `theme/deck.css` | テーマと図版用CSS |
| `content-notes.md` | **話す内容の正本** |
| `demo-script.md` | 2回の実演と時間調整 |
| `assets/icons/` | 各ツールのロゴ |
| `scripts-build-icons.py` | ロゴをdata URIにしてCSSへ埋め込む |
| `build/` | HTML、PDF、PNGの出力先 |

## 60分の構成

| 範囲 | 内容 | 時間 |
|---|---|---:|
| 1–4 | 導入 | 4分 |
| 5–9 | 3層の整理と、ターミナル／エディタの違い | 7分 |
| 実演1 | 同じプロジェクトをエディタとターミナルで見る | 3分 |
| 10–17 | ツール比較と選び方 | 12分 |
| 18–21 | 違うプロジェクトで複数体を動かす | 6分 |
| 22–25 | 4つの担当と、並べてよい作業 | 8分 |
| 実演2 | UI・バックエンド・DBへ別の指示を渡す | 4分 |
| 26–30 | 指示、競合、レビューの進め方 | 11分 |
| 31 | まとめ、質問 | 5分 |

山場は24、25、29枚目。
4つの担当、同時に進めてよい範囲、レビュー担当の仕事に時間を使う。

## ビルド

```sh
# HTML
marp slides.md -o build/slides.html --theme theme/deck.css --html < /dev/null

# PDF
marp slides.md -o build/slides.pdf --theme theme/deck.css --html --allow-local-files < /dev/null

# PNG
marp slides.md --images png -o build/png/s.png --theme theme/deck.css --html --allow-local-files < /dev/null

# 31枚を一覧表示
ffmpeg -y -pattern_type glob -i 'build/png/s.*.png' -vf "scale=384:216,tile=5x7" -frames:v 1 build/sheet/contact1.png
```

`< /dev/null`はMarpが標準入力を待つ環境で必要。
`--html`はHTMLで組んだ図を描画するために必要。

## 内容上の前提

この資料では、道具を次の3層に分ける。

1. エディタ: ファイルとプロジェクトを読み書きする作業空間
2. ターミナル環境: 文字による入出力を表示する作業空間
3. CLIエージェント: ターミナル上で調査、編集、コマンド実行を行うプログラム

ターミナルとシェルは同じものではない。
ターミナルは入出力を表示し、シェルは入力を解釈してプログラムを起動する。
Claude CodeとCodexはターミナルそのものではなく、そこで動くCLIエージェントとして扱う。

複数体AIでは、同時に動かすこと自体を目的にしない。
UI、バックエンド、DB、レビューの担当を先に決める。
互いを待たず、同じファイルを触らない作業だけを同時に進める。
branchやworktreeは発展事項として口頭で補足する。

## 出典の扱い

外部事実を含むスライドには、Marpのコメントとして`[Sources]`を付けている。
コメントは投影画面には出ない。
主な出典はMIT Missing Semester、VS Code公式動画・文書、各ツールの公式文書、OpenAIとAnthropicの公式文書、Git公式文書。

## デザインの約束

- 色は`theme/deck.css`のCSS変数から選ぶ
- ウェイトは400と700を基本にする
- 1スライド1メッセージ
- 2枚続けて表やカードグリッドを使わない
- 主要な図は1枚につき3要素程度に絞る
- 全角スペースを使わない
- 英数字と日本語の間に不要な空白を入れない
- 英単語同士の空白は残す（`VS Code`、`Claude Code`、`Plan Mode`）

確認コマンド:

```sh
rg -n '　|──' slides.md
rg -n '[A-Za-z0-9] [ぁ-んァ-ヶ一-龥]' slides.md
rg -n '[ぁ-んァ-ヶ一-龥] [A-Za-z0-9]' slides.md
```

## ロゴとフォント

各ロゴは識別のための引用で、権利は各社・各プロジェクトに帰属する。
ロゴはCSSへ埋め込んでいるため、HTML、PDF、PNGで相対パスが壊れない。
`assets/icons/`を変更したら`python3 scripts-build-icons.py`を実行する。

この環境ではHiragino Sansで描画される。
別環境では見た目が変わる可能性があるため、配布はPDFを使う。
