# 第5回 勉強会の内容メモ

ページごとの話す内容は`slides.md`の各ページのコメント（`[話すこと]`）を正本とする。
このファイルには、構成の判断と事実確認の記録を置く。

## 決まっていること（2026-11-25）

- 日時: 2026-11-26、60分（本編55分、質疑5分）。形式は第4回と同じ（ユーザーの回答）
- 聴衆: 学生エンジニア。第4回と同じくエンジニア向けに書く（用語は言い換えない、例えは使わない）
- 今回から、冒頭の約10分で前回のおさらいと、その後のアップデートを話す（ユーザーの指示）
- おさらいの範囲: パーソナルエージェント、AI組織、AI社員。加えて、ADEのOrcaが出したOrca Botsとその特徴（ユーザーの指示）
- 本編: 「AIというより、エンジニア寄りの内容」（ユーザーの指示）。候補3つ（Gitとチーム開発、作って公開するまで、テストと品質）から「Gitとチーム開発」をユーザーが選んだ

## 各章で持ち帰ること

0. おさらい: Grok Botは正式版になりチームで使える。Orca Botsは各社のクラウドではなく自分のマシンで、自分のClaude CodeやCodexを動かし、成果物はPRになる
1. Gitの仕組み: commitはスナップショットと親、branchはcommitを指すref。共有した履歴はrevertで直す
2. GitHubでのチーム開発: 小さなPR、レビュー、CI。mainへの入口をbranch保護で絞る
3. AIエージェントとGit: 1エージェントに1つのworktree、branch、PR。並列にできるかはタスクの分け方で決まる

## 自分で決めたこと（依頼に無かったもの）

- 題名「Gitとチーム開発：branch、PR、CI、worktree」と、おさらいを第0章とする4章の構成
- おさらいは第4回の地図（5枚目）を再掲し、要点を2枚に圧縮した
- 本編の最後の章で、Orcaのworktreeと第4回の「多くのコーディングは並列化しにくい」へ戻す流れにした
- 実演を2回（ターミナルでのconflict、GitHubのPR画面）入れた。どちらも未リハーサル
- rebaseの操作手順、submodule、Git LFS、tagとリリースは扱わない
- PRの大きさの目安は、Googleのeng-practices（約100行は妥当、1000行は大きすぎ）を使った。業界の決まりではない

## 事実確認の記録

2026-11-25に確認。一次資料を優先し、取れなかったものは報道か第三者で補った。

| 内容 | ページ | 確認先 | 種類 |
|---|---|---|---|
| Grok Bot 1.0（11/11）。Team Bots、Slack・Teams、会議に参加、確認してから実行 | 7 | x.ai/news/grok-bot-1-0、docs.x.ai/grok-bot/team-bots | 公式 |
| dots: ChatGPT Walletでの購入（11/13、米国のPro、18歳以上）、Health連携とdot専用タブ（11/19） | 7 | help.openai.com/en/articles/6825453-chatgpt-release-notes | 公式 |
| dots: GPT-6.1 Terraを併用（11/3の追記） | 7（コメント） | openai.com/index/introducing-dots/ | 公式 |
| dots: Plusの一部で試験中 | 7（コメント） | engadget.com | 報道のみ |
| Muse: 豪州（11/17）、英国（11/24）。カナダで音声とLoblaw（11/18） | 7 | about.fb.com/news/2026/11/ の各記事 | 公式 |
| Muse: 音声とアバター（11/5）、spaces（11/6） | 7（コメント） | about.fb.com | 公式 |
| Duet: 10/23の注記以降、変更なし。米国の順番待ち | 7 | claude.com/resources/articles/claude-duet | 公式 |
| 日本の料金と提供範囲の変更なし | 7 | 上の各公式発表に日本の記載なし | 公式の範囲 |
| Orca Bots: 2026-11-19のv1.4.265で"Introducing Orca Bots (Beta)" | 8 | github.com/stablyai/orca/releases/tag/v1.4.265 | 公式 |
| Orca Bots: 依頼の窓口（Slack、GitHub、Linear、Gmail、webhook、スケジュール）、テスト済みのPRを返す、Needs you | 8 | orca.dev/bots、orca.dev/docs/bots | 公式 |
| 自分のマシンのフォルダで動く。寝ている間は止まり、依頼は最大1日待つ。自分のClaude Code、Codexの契約で、上乗せなし | 8、9 | orca.dev/docs/bots、orca.dev/bots（FAQ） | 公式 |
| Orca Cloudを通るのはSlack、GitHub、Linear、webhookだけ。インフラの場所は非公表 | 8（コメント） | orca.dev/docs/bots/security | 公式 |
| 権限モードは既定でFull access、頼める人は既定で本人だけ、一部のルールはモデルへの指示だけ | 8（コメント） | orca.dev/docs/bots/security | 公式 |
| group roomで@名前で引き継ぐ（v1.4.269、11/21） | 8（コメント） | GitHubのリリースノート | 公式 |
| Orca: MIT、無料、macOS・Windows・Linux、対応CLIエージェント41件、worktreeは本物のgit worktree | 8、10 | github.com/stablyai/orca、orca.dev/docs/agents/supported、orca.dev/docs/model/worktrees | 公式 |
| 公式Xの告知 | — | 取得できず（HTTP 402） | 未確認 |
| commitの中身、conflict、worktreeの出力（branchの中身は14枚目の話者メモ） | 12、16、27 | 使い捨てリポジトリでの実出力（git 2.56.1） | 実測 |
| 分岐した状態のgit pullは、統合方法を設定するまで止まる | 19（コメント） | 実測（git 2.56.1、"Need to specify how to reconcile divergent branches."） | 実測 |
| Snapshots, Not Differences、Three States | 12、13 | git-scm.com/book | 公式 |
| fast-forwardと3-way merge、conflict | 15、16 | git-scm.com/book Basic Branching and Merging | 公式 |
| 共有したcommitをrebaseしない | 17 | git-scm.com/book Rebasing | 公式 |
| GitHub flow | 20 | docs.github.com github-flow | 公式 |
| PRの大きさ、説明の書き方 | 21 | google.github.io/eng-practices | 公式（Google） |
| レビューで見ること | 22 | google.github.io/eng-practices/review/reviewer/looking-for.html | 公式（Google） |
| mergeの3方式 | 23 | docs.github.com about-merge-methods-on-github | 公式 |
| actions/checkout v7.0.1（2026-07-20）、actions/setup-node v7.1.0（2026-10-08） | 24 | GitHub releases（gh apiで取得） | 公式 |
| rulesetとprotected branch。FreeのPrivateでは使えない | 25 | docs.github.com | 公式 |

## レビュー（2026-11-25）

Codexに12枚目以降の技術面を見せ、6件の指摘を受けて全件を反映した。

- git pullを「fetchしてmerge」と言い切っていた → 分岐時は統合方法を決めるまで止まる、に直した（実測で確認）
- branch保護が「全員に効く」 → 管理者やbypassの例外設定を確かめる、を話者メモに足した
- worktreeが「.gitを共有」 → commitとbranchは共有し、作業ツリー、HEAD、indexはフォルダごと、に直した
- GitHub flowでCIを必須のように書いていた → レビューを受けてからmainへ、CIもここで回す、に直した
- conflictの見出し → 「同じ行を違う内容に変えると」に条件を足した
- branchが「1行のファイル」 → 「commitを指す名札（ref）」に直し、packed-refsの注記を足した
