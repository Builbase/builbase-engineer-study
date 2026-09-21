# 第2回 勉強会の話す内容

このファイルを内容の正本とする。
`slides.md`は、ここにある主張を1枚1メッセージへ圧縮したもの。

## 0. この勉強会で持ち帰ってほしいこと

用語をバラバラに覚えるのではなく、「AIが何を読み、どう動き、どう縛られるか」の順に位置づけられるようになること。
守らせたい度の高さで「頼む（CLAUDE.md、memory）」「条件で効かせる（rules、skills）」「機械で止める（hooks、permissions）」の置き場を選べるようになること。

用語の説明は、この勉強会で使う整理であり、製品の正式な分類ではない。
本編48分、実演7分、質疑5分。

## 導入（1〜4枚目）

同じ「ログインのバグを直して」でも、環境Aは直して報告だけ、環境Bはnpm testを回して通してから報告する。
違いは指示文ではなく、AIが最初に読む設定ファイル（CLAUDE.mdに「変更後はnpm testを通す」とある）と、動作を縛る仕組み。
第1回の「処理の終了と作業の完了は別」を、今回は環境の側から解く。

## 1. AIが見ているもの（5〜12枚目）

### コンテキスト

AIが1回の返答で読める文章の全部。上限があり、これをコンテキストウィンドウと呼ぶ。
中身は3種類に分けて説明する。

1. システムプロンプト。製品側が入れる。利用者には見えない
2. 設定とメモ。CLAUDE.md、rules、memory、skillの説明文。利用者が置いたファイル
3. 会話とツールの結果。指示、読んだファイル、実行したコマンドの出力

毎回の返答で、この全部を送り直している。だから会話が長いほど、1つの質問が重くなる。

### 開始時点の中身（実演1）

`/context`で、指示を打つ前に読み込まれているものが見える。
7枚目は2026-09-21に自分の環境で実行した実画面。System prompt 4.9k、System tools 17.6k、MCP tools 632、Custom agents 1.1k、Memory files 3.9k、Skills 6.2k。合計約34k。
8枚目の開始時の値はこの合計、以降の各行は公式ドキュメントの代表値。実演では当日の実物を見せる。

### 積み上がりと圧縮

ファイルを読むたび、コマンドを実行するたびに結果が足される。
上限に近づくと、古い会話は要約に置き換わる。これを圧縮（compaction）と呼ぶ。自動でも走るし、`/compact`で自分でも起こせる。
圧縮のあとに残るものと残らないものの違いが、どこに指示を書くべきかを決める。

- 読み直されるもの: CLAUDE.md、条件なしのrules、memory、Plan Modeの計画
- 要約になるもの: 会話の中で伝えた指示、読んだファイルの中身（更新が新しい5件だけは再読込される）、hookが足した文脈

結論は「残したい指示は、会話ではなくファイルへ書く」。

### CLAUDE.md

毎回最初に読まれる指示書。`~/.claude/CLAUDE.md`は自分用、リポジトリ直下はプロジェクト用。
セッション開始時に読まれ、圧縮のあとも読み直される。
短く、具体的に。公式は200行以内を目安にしている。長い手順はskillへ移す。
`@path`で別ファイルを取り込める。AGENTS.mdは他のツールとも共通で使える同じ役割のファイル。

### rules

`.claude/rules/`に置く、1ファイル1話題の指示。
frontmatterに`paths`を書くと、対象のファイルを読んだときだけ読み込まれる。`paths`がなければCLAUDE.mdと同じく常に読まれる。効き方（AIが読んで従う）はCLAUDE.mdと同じで、強制力が上がるわけではない。
関係ない作業のときに読ませないことで、いつもの文脈を軽くする。
`~/.claude/rules/`に置くと、すべてのプロジェクトに効く。

### memory

AIが自分で書き、次の回に読み直すメモ。利用者が訂正したときなどにAIが残す。
場所は`~/.claude/projects/<project>/memory/`。`MEMORY.md`が索引で、開始時に読まれるのは索引の先頭200行または25KBまで。
詳細は`user_*.md`、`feedback_*.md`、`project_*.md`、`reference_*.md`に分かれ、必要なときに開く。
CLAUDE.mdは人が書く指示、memoryはAIが書く学び。`/memory`で中身を見て直せる。

## 2. AIがどう動くか（13〜18枚目）

### エージェントループ

指示を受ける、考える、道具を使う、結果を読む、を終わったと判断するまで繰り返す。
チャットは1往復で終わるが、エージェントは道具の結果を見て次を決める。
1周ごとに結果がコンテキストへ足される。第1章の「積み上がる」はこのループの跡。

### ツールとMCP

標準のツールはRead、Edit、Bash、Grepなど。MCPはGitHub、DB、ブラウザなど外部サービスへの接続口。
使えるツールの一覧は開始時から読まれている（MCPの詳細定義は既定で遅延読み込み）。

### 完了条件

完了条件が、ループの止まる位置を決める。
「直して」だけなら修正して報告で止まる。「npm testが通るまで直して」なら、テストを回し、失敗を読み、直し、通ってから止まる。
第1回の「4項目」の完了条件は、AIが自分で確かめる材料になる。

### ループエンジニアリング

人が毎回プロンプトを打つ代わりに、AIを回すループそのものを設計する考え方。
Boris Cherny（Claude Code責任者）の「I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do.」という発言を、Addy Osmaniが記事にまとめた。2026年に広まった言い方。

設計するのは3つ。

1. 起動のきっかけ。時刻、PR作成、テスト失敗など。人が打たない
2. 確かめる手段。テスト、lint、別のエージェントによるレビュー
3. 記録と引き継ぎ。進み具合をファイルへ残し、次の周へ渡す

Osmaniは自動実行、worktree、skills、MCP、サブエージェント、状態のメモリを整備すべき土台に挙げている。学生には「人が打たなくても回る」までで十分。
きっかけで分けると、定期（毎朝issueを分類）、きっかけ待ち（PRが来たらレビュー）、条件を満たすまで（テストが通るまで修正）の3つ。14枚目のループ（製品が回す内側の繰り返し）と、ここで言うループ（人が設計して外から回す自動化）は別物で、17枚目で切り替えを一言入れる。
どれも、結果の確認と最終判断は人に残す。

## 3. 人が枠を作る（19〜26枚目）

### ハーネス

エージェントのうち、モデル以外の全部。Birgitta Böckeler（Thoughtworks、2026-04）の定義で、「Agent = Model + Harness」。
製品が持つハーネス（システムプロンプト、標準ツール、圧縮、権限の確認）と、利用者が作るハーネス（CLAUDE.md、rules、memory、skills、hooks、settings.json）の2段で説明する。
同じモデルでも、利用者側の作り方で結果が変わる。冒頭の環境AとBの差はここ。

### ハーネスエンジニアリング

先回りの案内（原文はguides、feedforward）と、後からの検査（sensors、feedback）を設計する。

- 案内: CLAUDE.md、rules、skills、PreToolUse hook、permissionsのdeny。動く前に効く
- 検査: PostToolUse hook、テスト、lint、CI、レビュー。動いたあとに効く

hooksは場面によって前にも後にも置ける。PreToolUseは実行前に止め、PostToolUseは実行後に検査する。

人の確認をなくすのではなく、確認が要る場所へ人の目を集める。
原文には「ハーネス作りはコンテキストエンジニアリングの一種」ともある。

### skills

必要なときだけ読む手順書。`~/.claude/skills/<name>/SKILL.md`。
既定で常に読まれるのはfrontmatterの説明文だけで、AIはそれで使い所を判断する（`disable-model-invocation: true`なら説明文も常駐せず、人が呼ぶまで入らない）。本文は呼ばれたときに読む。`/name`で人が呼んでも、AIが選んでもよい。
いつも要る事実はCLAUDE.md、手順はskill、と分ける。

### hooks（実演2）

決めた場面で、シェルのスクリプトなどを自動で実行する仕組み。AIの判断に関係なく動く。
場面の例はUserPromptSubmit（文脈を足す）、PreToolUse（止められる）、PostToolUse（lintを流す）、Stop（記録する）。
PreToolUseで拒否を返すと、そのツール実行は起きない。

24枚目は実例。「.envの中身を表示して」と頼むと、AIはBashでコマンドを組み立てたが、PreToolUse hookが実行前に拒否し、AIは「表示できない」と答えて代わりの手順を人へ返した。
口頭で添える注意: 同じ環境で「render.yamlにコメントを足して」と頼むと、Editツールのdenyは効いたのにBashの`sed -i`で書き換えられた。denyやhookは「どの経路を塞ぐか」まで決めないと抜ける。

### settings.json

権限（allow、deny、ask）、環境変数、hooks、既定モデルの置き場。
`~/.claude/settings.json`は自分用で全プロジェクトに効く。`.claude/settings.json`はプロジェクト用でリポジトリで共有する。
優先順位は、組織の設定、コマンド引数、`.claude/settings.local.json`、`.claude/settings.json`、`~/.claude/settings.json`の順。permissionsのようなリストは上書きでなく結合される。
denyに書いた操作は、AIが望んでも実行されない。

### 強制力の段

守らせたい度が高いほど、下の段へ置く。

1. 頼む。CLAUDE.md、memory。AIが読んで従う。忘れることも、解釈が割れることもある
2. 条件で効かせる。rules（paths）、skills。対象のときだけ読ませる。効き方は1と同じで、常に読ませる量を減らすための段
3. 機械で止める。PreToolUse hook、permissionsのdeny。AIの判断と無関係に効く

公式ドキュメントも「CLAUDE.mdとmemoryは文脈であって強制ではない。必ず止めたいならPreToolUse hookを」と書いている。

## まとめ（27〜28枚目）

27枚目は用語の一覧。配布用に残す。
28枚目は今日から試す3つ。CLAUDE.mdを10行書く、訂正を1つファイルに残す（memoryに残ったか`/memory`で見る）、hookを1本入れる（触られたくないファイルの編集を止める）。

## 出典

- https://code.claude.com/docs/en/context-window
- https://code.claude.com/docs/en/costs
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/mcp
- https://www.anthropic.com/engineering/building-effective-agents
- https://martinfowler.com/articles/harness-engineering.html
- https://addyosmani.com/blog/loop-engineering/
- https://jp.findy-team.io/blogs/loop-engineering/
