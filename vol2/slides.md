---
marp: true
theme: deck
paginate: false
size: 16:9
title: AIエージェントの用語を、仕組みの順に理解する
description: builbaseエンジニア勉強会 第2回（60分）
author: seiji
style: |
  /* 第2回だけで使う部品。共通テーマ theme/deck.css の変数と寸法に合わせる */
  .grow { display: grid; gap: 8px; }
  .grow > div { display: grid; grid-template-columns: 300px 1fr 110px; align-items: center; gap: 18px; font-size: 21px; }
  .grow > div > span:last-child { text-align: right; color: var(--gray-536); font-size: 19px; }
  .grow i { display: block; height: 24px; border-radius: 4px; background: var(--blue-100); }
  .grow i.k { background: var(--blue); }
  .grow i.g { background: var(--gray-200); }
  .grow .cond { color: var(--green); font-weight: 700; }
  .quote-layout { display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 48px; align-items: center; }
  .quote { border-left: 8px solid var(--blue); padding: 8px 0 8px 28px; }
  .quote p { margin: 0; font-size: 26px; font-weight: 700; line-height: 1.6; color: var(--navy); }
  .quote small { display: block; margin-top: 14px; font-size: 18px; color: var(--gray-536); }
  .hookflow { display: grid; grid-auto-flow: column; align-items: center; justify-content: center; gap: 10px; }
  .hookflow .step { border: 1px solid var(--gray-200); border-radius: 10px; padding: 18px 14px; font-size: 20px; font-weight: 700; text-align: center; min-width: 96px; }
  .hookflow .hook { display: flex; flex-direction: column; align-items: center; gap: 6px; font-size: 16px; color: var(--gray-536); text-align: center; min-width: 128px; }
  .hookflow .hook b { font-size: 17px; color: var(--green); }
  .hookflow .hook.stop b { color: var(--red); }
  .hookflow .hook i { display: block; width: 14px; height: 14px; border-radius: 50%; background: var(--green); }
  .hookflow .hook.stop i { background: var(--red); }
  .ticket.code span { font-family: ui-monospace, Menlo, monospace; font-size: 19px; overflow-wrap: anywhere; }
  .paper-wide .plan-paper > div:not(.plan-paper-title) { grid-template-columns: 170px 1fr; }
  .plan-paper .ico { width: 22px; height: 22px; vertical-align: -0.25em; margin: 0 4px 0 2px; }
  .terminal-screen .ico { width: 22px; height: 22px; vertical-align: -0.25em; margin: 0 6px 0 0; }
  .terminal-screen .ico.i-github { filter: invert(1); }
  .card .ico { width: 22px; height: 22px; vertical-align: -0.25em; margin: 0 0 0 4px; }
  /* Marp既定の section table は display:block・width:max-content。表として全幅に伸ばす */
  .tablewrap { flex: none; }
  .glossary { display: table; width: 100%; font-size: 18px; }
  .glossary th, .glossary td { padding: 5px 14px; }
  .glossary tbody th { font-size: 19px; }
  .glossary thead th { font-size: 17px; }
  /* content-center は .fig の子を width:100% にする。.rule は padding 込みで幅を収める */
  section.content-center .fig > .rule { box-sizing: border-box; }
  .terminal-screen code.dim { color: #b8b8b8; margin: 0 0 16px 18px; }
  /* 3段のlayer-stack＋注記1行は既定の高さでは下へ36pxはみ出す */
  .layer-stack.tight { gap: 12px; }
  .layer-stack.tight .layer { min-height: 92px; padding: 14px 28px; }
  .layer-stack.tight .layer small { font-size: 19px; }
  .layer-stack.tight + .cap { margin-top: 18px; }
  .numbered.three { grid-template-columns: repeat(3, 1fr); margin-top: 24px; }
  .shot { width: 100%; border-radius: 12px; box-shadow: 0 4px 16px 3px rgba(0,0,0,0.1), 0 1px 6px 0 rgba(0,0,0,0.3); }
  /* 図版（インラインSVG）。文字は本文と同じ書体で描く */
  .svgfig { display: flex; justify-content: center; }
  .svgfig svg { font-family: var(--sans); }
  .svgfig text { font-size: 20px; fill: var(--ink); }
  .svgfig text.b { font-weight: 700; font-size: 22px; }
  .svgfig text.s { font-size: 17px; fill: var(--gray-700); }
  .svgfig text.w { fill: #ffffff; }
  .svgfig text.navy { fill: var(--navy); }
---

<!-- _class: title -->

# エンジニア勉強会

<p>
第2回 AIエージェントの用語を、仕組みの順に理解する<br>
2026-09-28
</p>

---

<!-- header: 'はじめに' -->
# この勉強会で持ち帰ること

<div class="fig">
<div class="row c2">
<div class="card">
<span class="gi lg g-doc"></span>
<div class="t">用語を、仕組みのどこに当たるかで覚える</div>
<div class="d">AIが何を読み、どう動き、どう縛られるか、の順に並べて説明する</div>
</div>
<div class="card on">
<span class="gi lg g-bolt dark"></span>
<div class="t">確実に守らせたいかで、置き場を選ぶ</div>
<div class="d">頼む、条件で効かせる、機械で止める</div>
</div>
</div>
</div>

---

<!-- _class: content-center -->

# 同じ指示でも、AIが読んでいるものが違えば結果が変わる

<div class="fig">
<div class="pair">
<div class="pair-side">
<b>環境A</b>
<span>「ログインのバグを直して」<br>→ 直して「完了」と報告。テストは実行していない</span>
</div>
<div class="pair-link">vs</div>
<div class="pair-side on">
<b>環境B</b>
<span>同じ指示<br>→ 直したあと自分で<span class="ico i-npm"></span>npm testを回し、失敗を直してから報告</span>
</div>
</div>
<div class="rule">違いは指示文ではなく、AIが最初に読む設定ファイルと、動作を止める仕組みにある</div>
</div>

<!--
[話すこと] 環境BにはCLAUDE.mdに「変更後はnpm testを実行し、通るまで直す」とある。
第1回の「処理の終了と作業の完了は別」を、環境側から解く回だと位置づける。
npm testは「テストを実行するコマンド」と一言添える
-->

---

# 今日の内容

<div class="fig">
<div class="row c3">
<div class="card">
<div class="t">1. AIが見ているもの</div>
<div class="d">コンテキスト、CLAUDE.md、rules、memory</div>
</div>
<div class="card">
<div class="t">2. AIがどう動くか</div>
<div class="d">エージェントループ、ツール、ループエンジニアリング</div>
</div>
<div class="card on">
<div class="t">3. 人が枠を作る</div>
<div class="d">ハーネス、skills、hooks、settings.json</div>
</div>
</div>
</div>

---

<!-- _class: chapter -->
<!-- header: '1. AIが見ているもの' -->

<div class="n">CHAPTER 1</div>

# AIが見ているもの

AIは何を知っていて、何を知らないのか

---

# コンテキストは、AIが返答のたびに読み込む文字の全部

<div class="fig">
<div class="layer-stack tight">
<div class="layer">
<span class="layer-no">1</span>
<div><b>システムプロンプト</b><small>ツールの使い方や振る舞いの基本。製品側が入れる。利用者には見えない</small></div>
<div></div>
</div>
<div class="layer on">
<span class="layer-no">2</span>
<div><b>設定とメモ</b><small>CLAUDE.md、rules、memory、skillsの一覧。あなたが置いたファイル</small></div>
<div></div>
</div>
<div class="layer">
<span class="layer-no">3</span>
<div><b>会話とツールの結果</b><small>あなたの指示、読んだファイル、実行したコマンドの出力</small></div>
<div></div>
</div>
</div>
<p class="cap">入る量には上限がある（コンテキストウィンドウ）。量はトークンで数え、1トークンは日本語で1〜2文字ほど</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/context-window
- https://code.claude.com/docs/en/costs
-->

---

# 指示を打つ前に、すでに読み込まれているものがある

<div class="fig">
<div class="scene-grid">
<img class="shot" src="assets/shots/context-categories.png" alt="Claude Codeで/contextを実行した画面の内訳。System prompt、System tools、MCP tools、Custom agents、Memory files、Skills、Messages、Free space">
<div class="numbered">
<div><b>1. 製品が入れるもの</b><span>System prompt、System tools</span></div>
<div><b>2. あなたの環境にあるもの</b><span>Memory files（CLAUDE.mdとmemory）、Skills、MCP tools</span></div>
<div><b>3. まだほぼ空のもの</b><span>Messages。会話はここから増えていく</span></div>
</div>
</div>
<p class="cap">2026-09-21に自分の環境で/contextを実行した実画面（k＝千トークン）。数値は環境によって変わる</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/context-window
[実演1] ここで自分のClaude Codeを開き、/contextの実物を見せる。3分
-->

---

# 作業が進むほど、読んだファイルと結果が積み上がる

<div class="fig">
<div class="grow">
<div><span>開始時に入っているもの（前ページの実測）</span><i class="g" style="width:36%"></i><span>34k</span></div>
<div><span>あなたの指示</span><i class="k" style="width:2%"></i><span>0.05k</span></div>
<div><span>Read src/api/auth.ts</span><i style="width:12%"></i><span>2.4k</span></div>
<div><span><span class="cond">rules</span> api-conventions.md（11枚目）</span><i style="width:2%"></i><span>0.4k</span></div>
<div><span>Read auth.test.ts</span><i style="width:8%"></i><span>1.6k</span></div>
<div><span>Edit auth.ts</span><i style="width:2%"></i><span>0.4k</span></div>
<div><span>npm testの出力</span><i style="width:6%"></i><span>1.2k</span></div>
<div><span>AIの返答</span><i class="k" style="width:2%"></i><span>0.4k</span></div>
</div>
<div class="rule">毎回、ここまでの全部がモデルへ送り直される。会話が長いほど、1つの質問にかかる量が増える</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/context-window
- https://code.claude.com/docs/en/costs
[話すこと] 開始時の34kは前ページの実画面の合計、以降の各行は公式ドキュメントの例。rulesは対象ファイルを読んだときだけ入る（11枚目で扱う）。
関係ない作業へ移るときは/clearで空にする
-->

---

<!-- _class: content-center -->

# 上限に近づくと圧縮され、古い会話は要約に置き換わる

<div class="fig">
<div class="svgfig">
<svg width="1152" height="300" viewBox="0 0 1152 300" xmlns="http://www.w3.org/2000/svg">
<text x="0" y="32" class="b">圧縮前</text>
<rect x="0" y="48" width="180" height="64" fill="#000071"/>
<text x="90" y="88" text-anchor="middle" class="w">設定とメモ</text>
<rect x="180" y="48" width="900" height="64" fill="#d9e6ff"/>
<text x="630" y="88" text-anchor="middle" class="navy">会話とツールの結果（指示、読んだファイル、実行結果、AIの返答）</text>
<line x1="1080" y1="36" x2="1080" y2="124" stroke="#ec0000" stroke-width="3" stroke-dasharray="8 6"/>
<text x="1090" y="88" class="s" style="fill:#ec0000">上限</text>
<path d="M576 130 v40" stroke="#949494" stroke-width="3"/>
<path d="M566 162 l10 12 l10 -12" fill="none" stroke="#949494" stroke-width="3"/>
<text x="0" y="214" class="b">圧縮後</text>
<rect x="0" y="230" width="180" height="64" fill="#000071"/>
<text x="90" y="270" text-anchor="middle" class="w">設定とメモ</text>
<rect x="180" y="230" width="260" height="64" fill="#949494"/>
<text x="310" y="270" text-anchor="middle" class="w">会話の要約</text>
<rect x="440" y="230" width="150" height="64" fill="#d9e6ff"/>
<text x="515" y="270" text-anchor="middle" class="navy">新しい最大5件</text>
<rect x="590" y="230" width="490" height="64" fill="none" stroke="#cccccc" stroke-width="2" stroke-dasharray="6 6"/>
<text x="835" y="270" text-anchor="middle" class="s">空いた分に、続きの会話が入る</text>
</svg>
</div>
<div class="rule">ファイルにあるものは読み直される。会話にしかない指示は要約に溶ける。残したい指示はファイルへ</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/context-window#what-survives-compaction
- https://code.claude.com/docs/en/memory#instructions-seem-lost-after-compact
[話すこと] 圧縮（compaction）は自動でも走るし、/compactで自分でも起こせる。
読み直されるのはCLAUDE.md、条件なしのrules、memory。読んだファイルは更新の新しい5件だけ再読込される
-->

---

# CLAUDE.mdは、セッションの最初に読まれる指示書

<div class="fig">
<div class="plan-layout">
<div class="plan-paper">
<div class="plan-paper-title">CLAUDE.md</div>
<div><b>概要</b><span>Todoアプリ。<span class="ico i-nextjs"></span>Next.jsと<span class="ico i-supabase"></span>Supabase</span></div>
<div><b>コマンド</b><span><span class="ico i-npm"></span>npm run dev、npm test</span></div>
<div><b>守ること</b><span>変更後はnpm testを通す。src/db/は触らない</span></div>
<div><b>参照</b><span>@docs/api.md</span></div>
</div>
<div class="numbered">
<div><b>1. 場所</b><span>~/.claude/は自分用、リポジトリ直下はプロジェクト用</span></div>
<div><b>2. 読まれる時</b><span>セッション開始時。圧縮のあとも読み直す</span></div>
<div><b>3. 書き方</b><span>短く、具体的に。200行以内が目安</span></div>
</div>
</div>
<p class="cap">「参照」の@は別ファイルを取り込む書き方。AGENTS.mdは、他のツールとも共通で使える同じ役割のファイル</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/costs#move-instructions-from-claudemd-to-skills
[話すこと] セッション＝claudeを起動してから終えるまでの1回。長くなったら手順はskillsへ移す（第3章）
-->

---

<!-- _class: content-center -->

# rulesは、条件を付けると、対象のファイルを読むときだけ効く指示

<div class="fig">
<div class="scene-grid">
<div class="ticket code">
<div><b>場所</b><span>.claude/rules/api.md</span></div>
<div><b>条件</b><span>paths: ["src/api/**/*.ts"]</span></div>
<div><b>本文</b><span>すべてのAPIに入力検証を付ける</span></div>
</div>
<div class="numbered">
<div><b>1. 条件なし</b><span>CLAUDE.mdと同じく、いつも読まれる</span></div>
<div><b>2. 条件あり</b><span>対象のファイルを読んだときだけ入る</span></div>
<div><b>3. 分ける理由</b><span>1ファイル1話題にし、関係ない作業のときは読ませない</span></div>
</div>
</div>
<p class="cap">条件の「src/api/**/*.ts」は「src/api/の下にある.tsファイル全部」の意味。~/.claude/rules/に置くと全プロジェクトに効く</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory#organize-rules-with-clauderules
-->

---

# memoryは、AIが自分で書き、次の回に読み直すメモ

<div class="fig">
<div class="plan-layout paper-wide">
<div class="plan-paper">
<div class="plan-paper-title">~/.claude/projects/&lt;project&gt;/memory/</div>
<div><b>MEMORY.md</b><span>索引。1件1行。開始時に読む</span></div>
<div><b>user_*.md</b><span>あなたの役割、好み</span></div>
<div><b>feedback_*.md</b><span>あなたからの訂正、認めた進め方</span></div>
<div><b>project_*.md</b><span>コードから分からない経緯、期限</span></div>
</div>
<div class="numbered">
<div><b>1. 誰が書くか</b><span>AIが書く。あなたが訂正したときなどに残す</span></div>
<div><b>2. いつ読むか</b><span>開始時に索引の先頭200行か25KBの早い方まで。詳細は必要なときに開く</span></div>
<div><b>3. どう直すか</b><span>/memoryで中身を見て、人が書き換えてよい</span></div>
</div>
</div>
<p class="cap">CLAUDE.mdは人が書く指示、memoryはAIが書く学び</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory#auto-memory
-->

---

<!-- _class: chapter -->
<!-- header: '2. AIがどう動くか' -->

<div class="n">CHAPTER 2</div>

# AIがどう動くか

指示のあと、AIの中で何が起きているのか

---

<!-- _class: content-center -->

# エージェントは、考えてツールを使い、結果を読んでまた考える

<div class="fig">
<div class="svgfig">
<svg width="1152" height="330" viewBox="0 0 1152 330" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#949494"/></marker>
</defs>
<rect x="0" y="120" width="180" height="80" rx="10" fill="none" stroke="#cccccc" stroke-width="2"/>
<text x="90" y="168" text-anchor="middle" class="b">指示を受ける</text>
<line x1="180" y1="160" x2="256" y2="160" stroke="#949494" stroke-width="3" marker-end="url(#ah)"/>
<rect x="260" y="120" width="180" height="80" rx="10" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="350" y="168" text-anchor="middle" class="b navy">考える</text>
<line x1="440" y1="160" x2="516" y2="160" stroke="#949494" stroke-width="3" marker-end="url(#ah)"/>
<rect x="520" y="120" width="180" height="80" rx="10" fill="none" stroke="#cccccc" stroke-width="2"/>
<text x="610" y="168" text-anchor="middle" class="b">ツールを使う</text>
<line x1="700" y1="160" x2="776" y2="160" stroke="#949494" stroke-width="3" marker-end="url(#ah)"/>
<rect x="780" y="120" width="180" height="80" rx="10" fill="none" stroke="#cccccc" stroke-width="2"/>
<text x="870" y="168" text-anchor="middle" class="b">結果を読む</text>
<path d="M870 200 v60 H350 v-52" fill="none" stroke="#0031d8" stroke-width="3" marker-end="url(#ah)"/>
<text x="610" y="292" text-anchor="middle" class="navy" style="font-weight:700">終わったと判断するまで、ここへ戻る</text>
<line x1="960" y1="160" x2="1056" y2="160" stroke="#949494" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#ah)"/>
<rect x="1060" y="130" width="92" height="60" rx="10" fill="#f2f2f2"/>
<text x="1106" y="168" text-anchor="middle">終了</text>
<text x="610" y="70" text-anchor="middle" class="s">1周ごとに、ツールの結果がコンテキストへ足される（第1章の「積み上がる」）</text>
</svg>
</div>
<div class="rule">この繰り返しがエージェントループ。チャットとの違いは、結果を見て次を決めること</div>
</div>

<!--
[Sources]
- https://www.anthropic.com/engineering/building-effective-agents
- https://code.claude.com/docs/en/how-claude-code-works
-->

---

# ツールには、標準のものと、外へつなぐMCPがある

<div class="fig">
<div class="scene-grid">
<div class="terminal-screen">
<div class="terminal-bar"><span>CLIエージェント</span><div class="mock-tools"><span class="ico i-claude"></span><span class="ico i-codex"></span></div></div>
<code><span class="prompt">&gt;</span> 未対応のissueを調べて</code>
<code class="output">Bash   <span class="ico i-git"></span>git log --oneline -5</code>
<code class="output">Read   src/api/issues.ts</code>
<code class="output">MCP    <span class="ico i-github"></span>github: list_issues</code>
<code class="output">Grep   "TODO" src/</code>
</div>
<div class="numbered">
<div><b>1. 標準のツール</b><span>Read、Edit、Bash、Grep。ファイルとコマンド</span></div>
<div><b>2. MCP</b><span>GitHub、DB、ブラウザなど外部サービスへの接続口</span></div>
<div><b>3. どちらも一覧がコンテキストに入る</b><span>使えるツールの説明文は、開始時から読まれている</span></div>
</div>
</div>
<p class="cap">MCPはModel Context Protocolの略。外部サービスをAIのツールとして見せる共通の約束事</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/context-window
[話すこと] 画面はClaude Codeの表記。Codexもツールの種類は同じ考え方で、表記が違う
-->

---

<!-- _class: content-center -->

# 完了条件が、ループの止まる位置を決める

<div class="fig">
<div class="pair">
<div class="pair-side">
<b>完了条件なし</b>
<span>「ログインを直して」だけ<br>→ 修正して「直しました」で止まる。動くかは人が確かめる</span>
</div>
<div class="pair-link">vs</div>
<div class="pair-side on">
<b>完了条件あり</b>
<span>CLAUDE.mdに「変更後はnpm testを通す」がある<br>→ テストを回し、失敗を読み、直し、通ってから止まる</span>
</div>
</div>
<div class="rule">完了条件は指示に書いても、CLAUDE.mdに書いてもよい。書いた条件を、AIは自分で確かめる材料にする</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/costs#work-efficiently-on-complex-tasks
[話すこと] 3枚目の環境AとBの差は、ここに落ちる。第1回で渡した「指示の4項目」の完了条件も同じ役割。
公式も「検証の目標（テスト、期待する出力）を渡すとAIが自分で確かめる」と書いている
-->

---

# ループエンジニアリングは、人が打つ指示を、回る仕組みへ変える

<div class="fig">
<div class="quote-layout">
<div class="quote">
<p>I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do.</p>
<small>「もうClaudeに指示は打たない。Claudeに指示を出し、次を決めるループを回している」<br>Boris Cherny（Claude Code責任者）の発言。Addy Osmaniの記事より引用</small>
</div>
<div class="numbered">
<div><b>1. 起動のきっかけ</b><span>時刻、PR作成、テスト失敗など。人が指示を打たなくても起動する</span></div>
<div><b>2. 確かめる手段</b><span>テスト、lint、別のエージェントによるレビュー</span></div>
<div><b>3. 記録と引き継ぎ</b><span>進み具合をファイルへ残し、次の周へ渡す</span></div>
</div>
</div>
<p class="cap">前のページのループを、人の代わりに外から回す仕組み。人は設計と、判断が要る場面の確認に回る</p>
</div>

<!--
[Sources]
- https://addyosmani.com/blog/loop-engineering/
- https://jp.findy-team.io/blogs/loop-engineering/
[話すこと] 2026年に広まった言い方。Osmaniは自動実行、worktree、skills、MCP、サブエージェント、
状態のメモリを整備すべき土台に挙げている。学生には「人が打たなくても回る」までで十分。
PR＝変更をレビューしてもらう単位、lint＝書き方の自動検査、と一言添える
-->

---

# ループは、きっかけの種類で3つに分けられる

<div class="fig">
<div class="row c3">
<div class="card">
<span class="gi lg g-calendar"></span>
<div class="t">定期</div>
<div class="d">毎朝、新しいissueを分類して担当を提案する</div>
</div>
<div class="card on">
<span class="gi lg g-chat dark"></span>
<div class="t">きっかけ待ち</div>
<div class="d"><span class="ico i-github"></span>GitHubにPRが作られたらレビューし、指摘をコメントする</div>
</div>
<div class="card">
<span class="gi lg g-growth"></span>
<div class="t">条件を満たすまで</div>
<div class="d">テストが通るまで、修正と実行を繰り返す</div>
</div>
</div>
<p class="cap">どれも、結果の確認と最終判断は人に残す</p>
</div>

<!--
[Sources]
- https://addyosmani.com/blog/loop-engineering/
- https://code.claude.com/docs/en/scheduled-tasks
-->

---

<!-- _class: chapter -->
<!-- header: '3. 人が枠を作る' -->

<div class="n">CHAPTER 3</div>

# 人が枠を作る

毎回お願いしなくても、守らせるには

---

<!-- _class: content-center -->

# ハーネスは、エージェントのうちモデル以外の全部

<div class="fig">
<div class="svgfig">
<svg width="1152" height="380" viewBox="0 0 1152 380" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="1152" height="380" rx="14" fill="#e8f1fe" stroke="#0031d8" stroke-width="3"/>
<text x="28" y="40" class="b navy">あなたの環境にあるハーネス</text>
<text x="28" y="70" class="s">CLAUDE.md、rules、memory、skills、hooks、settings.json</text>
<rect x="140" y="96" width="872" height="260" rx="12" fill="#ffffff" stroke="#cccccc" stroke-width="2"/>
<text x="168" y="134" class="b">製品が持つハーネス</text>
<text x="168" y="162" class="s">システムプロンプト、標準ツール、圧縮、権限の確認</text>
<rect x="356" y="188" width="440" height="140" rx="10" fill="#1a1a1a"/>
<text x="576" y="250" text-anchor="middle" class="b w">モデル</text>
<text x="576" y="284" text-anchor="middle" class="s" style="fill:#e6e6e6">文章を読んで、次の行動を決める本体</text>
</svg>
</div>
<p class="cap">同じモデルでも、外側の作り方で結果が変わる。3枚目の環境AとBの差はここ</p>
</div>

<!--
[Sources]
- https://martinfowler.com/articles/harness-engineering.html
[話すこと] Birgitta Böckeler（Thoughtworks、2026-04）の定義。「Agent = Model + Harness」。
「製品」はClaude CodeやCodexのこと。memoryはAIが書くが、置き場と使い方を決めるのは利用者側
-->

---

<!-- _class: content-center -->

# ハーネスエンジニアリングは、動く前の案内と、動いたあとの検査を作る

<div class="fig">
<div class="pair">
<div class="pair-side on">
<b>案内（動く前に効く）</b>
<span>CLAUDE.md、rules、skills、PreToolUse hook、permissionsのdeny</span>
</div>
<div class="pair-link">vs</div>
<div class="pair-side">
<b>検査（動いたあとに効く）</b>
<span>PostToolUse hook、テスト、lint、CI、レビュー</span>
</div>
</div>
<div class="rule">人の確認をなくすのではなく、確認が要る場所へ人の目を集める</div>
</div>

<!--
[Sources]
- https://martinfowler.com/articles/harness-engineering.html
[話すこと] 原文はguides（feedforward）とsensors（feedback）。
「ハーネス作りはコンテキストエンジニアリングの一種」ともある。hooksとpermissionsは次の3枚で扱う。
CI＝pushのたびにサーバーでテストを自動実行する仕組み
-->

---

<!-- _class: content-center -->

# skillsは、必要なときだけ読む手順書

<div class="fig">
<div class="scene-grid">
<div class="ticket code">
<div><b>場所</b><span>~/.claude/skills/release/SKILL.md</span></div>
<div><b>説明</b><span>description: PRをマージし、デプロイを確認する</span></div>
<div><b>本文</b><span>CIを確認し、マージし、デプロイを見る</span></div>
</div>
<div class="numbered">
<div><b>1. 常に読まれるもの</b><span>既定では説明文だけ。AIはこれで使い所を判断する</span></div>
<div><b>2. 呼ばれたとき</b><span>本文を読む。/releaseと打って呼ぶこともできるし、AIが自分で選ぶこともある</span></div>
<div><b>3. CLAUDE.mdとの分担</b><span>いつも要る事実はCLAUDE.md、手順はskills</span></div>
</div>
</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/skills
[話すこと] disable-model-invocation: true にすると説明文も常駐せず、人が呼ぶまで入らない（発展）
-->

---

<!-- _class: content-center -->

# hooksは、AIの判断に関係なく機械で動く

<div class="fig">
<div class="hookflow">
<div class="step">指示</div>
<div class="hook"><i></i><b>UserPromptSubmit</b>文脈を足す</div>
<div class="step on">考える</div>
<div class="hook stop"><i></i><b>PreToolUse</b>止められる</div>
<div class="step">ツール</div>
<div class="hook"><i></i><b>PostToolUse</b>lintを流す</div>
<div class="step">返答</div>
<div class="hook"><i></i><b>Stop</b>記録する</div>
</div>
<div class="numbered" style="margin-top:32px">
<div><b>1. 何か</b><span>決めた場面で、シェルのスクリプトなどを自動で実行する仕組み。上の緑と赤の点が場面の例</span></div>
<div><b>2. 止め方</b><span>PreToolUse（ツールを使う直前）で拒否を返すと、そのツール実行は起きない</span></div>
</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/hooks
[実演2] 次のページの実例を、可能なら自分の環境で再現して見せる。4分
-->

---

<!-- _class: content-center -->

# PreToolUse hookは、AIが実行しようとした瞬間に止める

<div class="fig">
<img class="shot" src="assets/shots/hook-deny-crop.png" alt="Claude Codeに.envの中身を表示するよう頼んだ画面。Bashの実行前にPreToolUse hookがエラーを返し、機密ファイルの読み取りが禁止されている">
<div class="numbered three">
<div><b>1. 頼んだこと</b><span>「.envの中身を表示して」</span></div>
<div><b>2. AIの動き</b><span>コマンドを組み立てて実行しようとした</span></div>
<div><b>3. hookの動き</b><span>実行前に拒否を返し、コマンドは走らなかった</span></div>
</div>
<p class="cap">2026-09-21に自分の環境で撮影。パスは塗りつぶしている。AIは値を避けてキー名だけ確認するコマンドを組み立てたが、それもhookが止めた</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/hooks
[話すこと] 同じセッションで「render.yamlにコメントを足して」と頼むと、Editツールのdenyは効いたが
Bashのsedで書き換えられた。denyやhookは「どの経路を塞ぐか」まで決めないと抜けがある、という実例として話す
-->

---

<!-- _class: content-center -->

# settings.jsonは、権限、環境変数、hooksなどの置き場

<div class="fig">
<div class="scene-grid">
<div class="ticket code">
<div><b>permissions</b><span>allow、deny、askを並べる</span></div>
<div><b>env</b><span>AIが使う環境変数</span></div>
<div><b>hooks</b><span>場面ごとのスクリプト</span></div>
<div><b>model</b><span>既定のモデル</span></div>
</div>
<div class="numbered">
<div><b>1. 自分用</b><span>~/.claude/settings.json。全プロジェクトに効く</span></div>
<div><b>2. プロジェクト用</b><span>.claude/settings.json。リポジトリで共有する</span></div>
<div><b>3. 優先順位</b><span>組織 ＞ コマンド引数 ＞ プロジェクト（local ＞ 共有） ＞ 自分用</span></div>
</div>
</div>
<p class="cap">denyに書いた操作は、AIが望んでも実行されない</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/settings
[話すこと] 正確には組織 > CLI引数 > .claude/settings.local.json > .claude/settings.json > ~/.claude/settings.json。
permissionsのようなリストは上書きでなく結合される
-->

---

<!-- _class: content-center -->

# 確実に守らせたいものほど、下の段へ置く

<div class="fig">
<div class="svgfig">
<svg width="1152" height="360" viewBox="0 0 1152 360" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="384" height="120" fill="#f2f2f2"/>
<text x="24" y="44" class="b">1. 頼む</text>
<text x="24" y="76" class="s">CLAUDE.md、memory</text>
<text x="24" y="102" class="s">AIが読んで従う。忘れることもある</text>
<rect x="384" y="120" width="384" height="120" fill="#e6e6e6"/>
<text x="408" y="164" class="b">2. 条件で効かせる</text>
<text x="408" y="196" class="s">rules（paths）、skills</text>
<text x="408" y="222" class="s">対象のときだけ読ませる。効き方は1と同じ</text>
<rect x="768" y="240" width="384" height="120" fill="#000071"/>
<text x="792" y="284" class="b w">3. 機械で止める</text>
<text x="792" y="316" class="s w">PreToolUse hook、permissionsのdeny</text>
<text x="792" y="342" class="s w">AIの判断と無関係に効く</text>
<path d="M0 120 H384 V240 H768 V360" fill="none" stroke="#0031d8" stroke-width="4"/>
<text x="1140" y="30" text-anchor="end" class="s">下へ行くほど、AIの解釈が入る余地が減る</text>
</svg>
</div>
<p class="cap">公式ドキュメントも「CLAUDE.mdとmemoryは文脈であって強制ではない。必ず止めたいならPreToolUse hookを」と書いている</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory#claudemd-vs-auto-memory
-->

---

<!-- header: 'まとめ' -->

# 今日の用語を、1枚にまとめる

<div class="fig">
<div class="tablewrap">
<table class="compare glossary">
<colgroup><col style="width:19%"><col style="width:39%"><col style="width:19%"><col style="width:23%"></colgroup>
<thead><tr><th></th><th>一言で</th><th>誰が書く</th><th>いつ効く</th></tr></thead>
<tbody>
<tr><th>コンテキスト</th><td>AIが返答のたびに読み込む文字の全部</td><td>製品とあなたと会話</td><td>毎回</td></tr>
<tr><th>CLAUDE.md</th><td>セッションの最初に読まれる指示書</td><td>あなた</td><td>開始時と圧縮後</td></tr>
<tr><th>rules</th><td>1話題ごとに分けた指示</td><td>あなた</td><td>常に。条件付きなら対象を読んだとき</td></tr>
<tr><th>memory</th><td>AIが自分で残す学び</td><td>AI</td><td>開始時に索引を読む</td></tr>
<tr><th>skills</th><td>必要なときだけ読む手順書</td><td>あなた</td><td>呼ばれたとき</td></tr>
<tr><th>hooks</th><td>場面ごとに自動で走るスクリプト</td><td>あなた</td><td>決めた場面で、必ず</td></tr>
<tr><th>settings.json</th><td>権限、環境変数、hooksの置き場</td><td>あなた</td><td>常に</td></tr>
<tr class="on"><th>ハーネス</th><td>モデル以外の全部。上の全部を含む</td><td>製品とあなた</td><td>常に</td></tr>
<tr class="on"><th>エージェントループ</th><td>考える、ツール、結果を読むの繰り返し</td><td>製品</td><td>指示のあと</td></tr>
<tr class="on"><th>ループエンジニアリング</th><td>そのループを外から回す仕組みの設計</td><td>あなた</td><td>時刻や出来事で</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/settings
- https://martinfowler.com/articles/harness-engineering.html
- https://addyosmani.com/blog/loop-engineering/
-->

---

<!-- _class: content-center -->

# 今日から試す3つ

<div class="fig">
<div class="closing-path">
<div><span class="gi lg g-doc"></span><b>CLAUDE.mdを10行書く</b><small>概要、コマンド、守ること</small></div>
<span class="closing-arrow">→</span>
<div><span class="gi lg g-split"></span><b>AIを1回訂正する</b><small>memoryに残ったか/memoryで確かめる</small></div>
<span class="closing-arrow">→</span>
<div class="on"><span class="gi lg g-bolt dark"></span><b>hookを1本入れる</b><small>触られたくないファイルの編集を止める</small></div>
</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/hooks
-->
