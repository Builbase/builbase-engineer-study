# 第4回 勉強会の内容メモ

ページごとの話す内容は`slides.md`の各ページのコメント（`[話すこと]`）を正本とする。
このファイルには、構成の判断と事実確認の記録を置く。

## 決まっていること（2026-11-10）

- 日時: 2026-11-11、60分（本編55分、質疑5分）。形式は第3回と同じ
- 聴衆: 学生エンジニア。当初は第3回と同じく非エンジニア向けに平易化したが、無理に噛み砕いて分かりにくくなったため、2026-11-10のユーザーの指示でエンジニア向けに書き直した（用語は言い換えない、例えは使わない）
- 依頼の内容: Muse、dots、Duet、Grok Botの深掘り。使える環境と金額感、得意なタスク、製品の特徴、使い分けを明確にする。従来のAI社員・AI組織とは何か、主流の作り方、パーソナルエージェントとの違い
- 製品やツールには実物のアイコンを使う（ユーザーの指示）

## 各章で持ち帰ること

1. パーソナルエージェント: 専用のクラウドPCで動き続け、取り消せない操作（送信、支払い、署名、削除）の前で許可を待つ
2. 4つの製品: 日本で使えるのはMuseとdots（dotsは発表者が2026-11-10に確認）。Grok Botは未確認、Duetは米国のみ。料金は月額より使える量の枠で見る
3. AI社員とAI組織: AI社員は1つの業務に配属したAI、AI組織は分担とまとめ役。手順が決まっていればワークフローで足り、AI組織は分けられる仕事だけ
4. 使い分け: 自分の用事は既製品を契約、会社の業務は作る。境目は近づいている（専門のdots、チームのGrok Bot）

## 自分で決めたこと（依頼に無かったもの）

- 題名「代わりに働くAI」と4章の構成
- 4製品の位置づけの軸（生活か仕事か、1人かチームか）。各社の発表で強調している用途から置いた
- AI社員・AI組織の作り方を「指示と資料を持たせる／手順を図で組む／役割を持つAIをコードで組む」の3通りに分けた。業界の正式な分類ではない
- ワークフローとエージェントの区別は、Anthropicの「Building effective agents」の定義を使った
- Gemini Spark（Google）など、ほかのパーソナルエージェントは扱わない

## 事実確認の記録

2026-11-10に確認。一次資料（各社の発表）を優先し、取れなかったものは報道か第三者の整理で補った。

| 内容 | ページ | 確認先 | 種類 |
|---|---|---|---|
| Museの機能、専用VMとSentinel、承認、学習のオプトアウト、米国でiOS・Android・Web・WhatsApp | 4、7、8、10 | about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ | 公式 |
| Museの日本提供（10月23日）、パワー月2,799円・マキシマム月13,990円、週のMuseトークン | 10、13、17 | pc.watch.impress.co.jp/docs/news/2150743.html | 報道 |
| dotsの概要、Pro・Business Premium、ChatGPTとCodexから起動、Slack・Teams、専門のdots | 4、11、28 | techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/ | 報道（公式ページは403で読めず） |
| dotsは最初1人1体、他者への送信は下書き止まり | 8、17 | Axiosの報道（検索結果の抜粋のみ。本文は403） | 報道・未読 |
| dotsの日本での扱い、円の価格（Pro 16,800円〜、Business Premium 19,250円） | 11、13 | 第三者の整理（smartscope.blog、ai.zenken.co.jp） | 第三者・要確認 |
| ChatGPT Pro 100ドル（2026-04新設） | 11、13 | macrumors.com/2026/04/09/openai-pro-subscription-tiers/（検索結果） | 報道 |
| Claude Duetの対象（米国のPro、Max、Ultra、順番待ち）、iOS・Android・claude.ai、承認、ブロックされる操作、例、限界 | 4、8、12、17 | claude.com/resources/articles/claude-duet | 公式 |
| Duetの朝の要約、数時間ごとの確認 | 12 | macrumors.com/2026/10/21/anthropic-claude-duet/ | 報道 |
| Grok Botの概要、用途の例、使用量は別枠、ベータ | 4、14、17、28 | x.ai/news/introducing-grok-bot | 公式 |
| X Subscriptionの価格（2026-10-12） | 14、13 | x.ai/news/x-subscription | 公式 |
| Grok BotはPremium、Super、Ultraに含まれる（Plusは対象外） | 13、14 | docs.x.ai/x-subscription/grok-bot | 公式 |
| X Subscriptionの日本円（Web: Plus 1,280円、Premium 5,280円、Super 17,800円、Ultra 34,800円）。日本でも契約できる | 13 | gamebusiness.jp/article/2026/10/14/28307.html | 報道 |
| GPT-6.1 Terra（2026-10-26、ChatGPTとCodexに追加）。dotsのモデルが変わったかは不明 | 11（コメント） | 9to5mac.com、OpenAIのX投稿 | 報道・公式SNS |
| ワークフローとエージェントの定義、単純な形から始める | 23 | anthropic.com/engineering/building-effective-agents | 公式 |
| エージェントはチャットの約4倍、マルチエージェントは約15倍のトークン。多くのコーディングは並行しにくい。まとめ役と担当の型 | 21、25 | anthropic.com/engineering/multi-agent-research-system | 公式 |
| 4製品とも先回りする（Muse "suggestions unprompted"、dots "before you even think to ask"、Duet "comes to you first"、Grok Bot "picking up work before you need to ask"） | 4、6、7 | 各社の発表（Meta、Al Jazeera経由のOpenAI、claude.com、x.ai） | 公式 |
| 連携の数: dots 4,000以上 | 15 | theprint.inなどの報道（OpenAIの発表ページは403） | 報道・公式の引用 |
| 連携の数: Duet 6,000以上（マーケット全体のコネクタとプラグイン） | 15 | claude.com/resources/articles/claude-duet | 公式 |
| 連携の数: Museは総数非公表。小さな会社向けに15を名指し、"dozens of tools"、独自の接続 | 15 | about.fb.com/news/2026/09/introducing-muse-small-business/ | 公式 |
| Museの連携の第三者の実数（54、2026-10-07） | 15（コメントのみ） | metamuseai.site/connectors/ | 第三者 |
| Grok Botの連携の数は非公表。APIやMCPの無いツールも使う | 15 | x.ai/news/introducing-grok-bot | 公式 |
| 5つのパターン（Prompt chaining、Routing、Parallelization、Orchestrator-workers、Evaluator-optimizer） | 24 | anthropic.com/engineering/building-effective-agents | 公式 |
| 各製品のモデル（Muse Spark、GPT-6 Astra、Claude Opus 5.5、Grok Botは非公表） | 10〜14 | 各社の発表、TechCrunch | 公式・報道 |
| CrewAIのエージェント定義（role、goal、backstory） | 22 | docs.crewai.com/en/concepts/agents | 公式 |

## 当日の朝に確かめること（2026-11-10に調べた結果）

- Grok Botの対象プラン: 公式ドキュメントでPremium、Super、Ultraと確認した。日本の円の価格は報道（Web版Premium月5,280円）で、日本でも新プランを契約できると報じられている
- dotsのモデル: GPT-6.1 Terraは10月26日にChatGPTとCodexへ追加されたが、dotsのモデルが変わったという公式の説明は見つからなかった。スライドは「GPT-6 Astra（発表時）」のまま
- 料金と提供地域の変更: 11月10日時点で、Museの値上げやDuetの日本提供の発表は見つからなかった。Metaは11月9日に軽量モデルMuse Emberを発表したが、Museのエージェントへの影響は書かれていない
- 当日の朝は、各社の公式ページで前日からの変更が無いかだけ見ればよい

## 聴衆役のレビュー（2026-11-10）

投影される文字だけを学生の立場で読ませ、12件の指摘を受けた。全件を投影面の文言で反映した（アプリの「鍵」を「代わりに使う許可。パスワードは渡さない」へ、トークンの説明、Codex・Slack・Teamsの言い換え、ワークフローにもAIを使うこと、問いの条件の追加など）。
その後、ユーザーの指示で章末の問い4枚を外した（全27枚）。
続けて、ユーザーの指示で「普通のAIエージェントとの違い（先回りは4製品共通の前提）」と「連携できるアプリの数」の2枚を足した（全29枚）。
