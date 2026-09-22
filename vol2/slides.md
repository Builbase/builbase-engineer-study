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
  /* たとえの行を足した枚は、用紙と説明の縦を詰める */
  section:has(.analogy) .plan-paper { padding: 18px 28px; }
  section:has(.analogy) .plan-paper > div:not(.plan-paper-title) { padding: 8px 0; }
  section:has(.analogy) .plan-paper-title { margin-bottom: 10px; }
  section:has(.analogy) .numbered { gap: 12px; }
  section:has(.analogy) .numbered > div { padding: 8px 0 8px 20px; }
  .terminal-screen .ico { width: 22px; height: 22px; vertical-align: -0.25em; margin: 0 6px 0 0; }
  .terminal-screen .ico.i-github { filter: invert(1); }
  .card .ico { width: 22px; height: 22px; vertical-align: -0.25em; margin: 0 0 0 4px; }
  /* Marp既定の section table は display:block・width:max-content。表として全幅に伸ばす */
  .tablewrap { flex: none; }
  .glossary { display: table; width: 100%; font-size: 17px; }
  .glossary th, .glossary td { padding: 5px 12px; }
  .glossary tbody th { font-size: 17px; }
  .glossary thead th { font-size: 17px; }
  /* content-center は .fig の子を width:100% にする。.rule は padding 込みで幅を収める */
  section.content-center .fig > .rule { box-sizing: border-box; }
  .terminal-screen code.dim { color: #b8b8b8; margin: 0 0 16px 18px; }
  /* 用語のたとえ。第1回の「エディタは、ファイルを読んで書く作業台」と同じ役割 */
  .analogy { box-sizing: border-box; flex: none; margin-bottom: 20px; padding: 12px 22px; border-left: 8px solid var(--green); background: #f1f8f4; font-size: 21px; line-height: 1.5; }
  .analogy b { color: var(--green); margin-right: 12px; }
  /* 3段のlayer-stack＋注記1行は既定の高さでは下へ36pxはみ出す */
  .layer-stack.tight { gap: 12px; }
  .layer-stack.tight .layer { min-height: 86px; padding: 12px 28px; }
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
第2回 AIエージェントの仕組み：コンテキスト、ループ、ハーネス<br>
2026-09-28
</p>

---

<!-- header: 'はじめに' -->
# この勉強会で持ち帰ること

<div class="fig">
<div class="row c2">
<div class="card">
<span class="gi lg g-doc"></span>
<div class="t">AIが何を読んで動いているかが分かる</div>
<div class="d">同じ指示でも、読んでいるものが違えば結果が変わる</div>
</div>
<div class="card on">
<span class="gi lg g-bolt dark"></span>
<div class="t">守らせたいことを、どこに書くか選べる</div>
<div class="d">指示で頼む、条件つきで渡す、機械で止める</div>
</div>
</div>
</div>

<!--
[話すこと] 用語は初出で一言だけ説明し、以降はそのまま使う。33枚目に一覧がある
-->

---

<!-- _class: content-center -->

# 同じ指示でも、AIが読んでいるものが違えば結果が変わる

<div class="fig">
<div class="pair">
<div class="pair-side">
<b>設定A</b>
<span>「ログインのバグを直して」<br>→ 修正して「完了」と報告。テストは実行していない</span>
</div>
<div class="pair-link">vs</div>
<div class="pair-side on">
<b>設定B</b>
<span>同じAI、同じ指示<br>→ 修正後に自分でnpm test（動作テスト）を実行し、失敗を直してから報告</span>
</div>
</div>
<div class="rule">違いは指示文ではなく、AIが読んでいる設定にある</div>
</div>

<!--
[話すこと] 設定BにはCLAUDE.mdに「変更後はnpm testを実行し、通るまで直す」とある。
第1回の「処理の終了と作業の完了は別」を、設定の側から解く回だと位置づける
-->

---

# 今日の内容

<div class="fig">
<div class="row c4">
<div class="card">
<div class="t">1. AIが見ているもの</div>
<div class="d">コンテキスト、CLAUDE.md、rules、memory</div>
</div>
<div class="card">
<div class="t">2. AIの動き方</div>
<div class="d">エージェントループ、完了条件</div>
</div>
<div class="card">
<div class="t">3. ハーネス</div>
<div class="d">skills、hooks、settings.json</div>
</div>
<div class="card on">
<div class="t">4. 私の環境</div>
<div class="d">実物と、こう作っている理由</div>
</div>
</div>
</div>

---

<!-- _class: content-center -->

# 今日扱うのは、パソコンの中で作業するAI

<div class="fig">
<div class="pair">
<div class="pair-side">
<b>チャットのAI</b>
<span>質問すると答えが返る<br>手元のファイルは、添付したものしか見えない</span>
</div>
<div class="pair-link">vs</div>
<div class="pair-side on">
<div class="logos chips"><span class="ico ico-lg i-claude"></span><span class="ico ico-lg i-codex"></span></div>
<b>CLIエージェント（Claude Code、Codex）</b>
<span>ターミナル（文字で操作する画面）で動く<br>ファイルを読み書きし、コマンドを実行し、結果を見て作業を続ける</span>
</div>
</div>
<div class="rule">一般知識は持っている。手元の仕事の情報は、渡したものしか知らない</div>
</div>

<!--
[話すこと] CLIはCommand Line Interfaceの略で、文字で操作する方式のこと。
Claude CodeはAnthropic、CodexはOpenAIの製品。第1回で触ったもの
-->

---

<!-- _class: chapter -->
<!-- header: '1. AIが見ているもの' -->

<div class="n">CHAPTER 1</div>

# AIが見ているもの

AIは何を知っていて、何を知らないのか

---

# コンテキストは、AIの作業机。今回の仕事の資料はここだけ

<div class="fig">
<div class="analogy"><b>たとえると</b>机に広げた資料。一般知識は頭の中にあるが、今回の仕事の中身は机にある分しか分からない</div>
<div class="layer-stack tight">
<div class="layer">
<span class="layer-no">1</span>
<div><b>システムプロンプト</b><small>ツールの使い方や振る舞いの基本。製品側が入れる。利用者には見えない</small></div>
<div></div>
</div>
<div class="layer on">
<span class="layer-no">2</span>
<div><b>設定とメモ</b><small>利用者が書いた指示（CLAUDE.md、rules）、AIが書いた学び（memory）、skillsの一覧</small></div>
<div></div>
</div>
<div class="layer">
<span class="layer-no">3</span>
<div><b>会話とツールの結果</b><small>指示、読んだファイル、実行したコマンドの出力</small></div>
<div></div>
</div>
</div>
<p class="cap">机の広さには上限がある（コンテキストウィンドウ）。量の単位はトークンで、日本語なら1〜2文字で1トークン</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/context-window
- https://code.claude.com/docs/en/costs
[話すこと] AIは返答のたびに、この全部を読み直している
-->

---

# 指示を打つ前に、すでに読み込まれているものがある

<div class="fig">
<div class="scene-grid">
<img class="shot" src="assets/shots/context-categories.png" alt="Claude Codeで/contextを実行した画面の内訳。System prompt、System tools、MCP tools、Custom agents、Memory files、Skills、Messages、Free space">
<div class="numbered">
<div><b>1. 製品が用意するもの</b><span>System prompt、System tools（ツールの説明）</span></div>
<div><b>2. 利用者が置いたもの</b><span>Memory files（CLAUDE.mdとmemory）、Skills</span></div>
<div><b>3. まだほとんど空</b><span>Messages（会話）。ここから増えていく</span></div>
<div><b>4. 合計</b><span>Messagesを除いた上の6行で約34k</span></div>
</div>
</div>
<p class="cap">2026-09-21に私の環境で/contextを実行した実画面。kは千トークン。上限は約100万トークン。MCP toolsとCustom agentsは今日は扱わない</p>
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
<div><span>開始時点（前ページの6行の合計）</span><i class="g" style="width:36%"></i><span>34k</span></div>
<div><span>指示</span><i class="k" style="width:2%"></i><span>0.05k</span></div>
<div><span>Read src/api/auth.ts</span><i style="width:12%"></i><span>2.4k</span></div>
<div><span><span class="cond">条件つきの指示ファイル</span>が1枚（12枚目）</span><i style="width:2%"></i><span>0.4k</span></div>
<div><span>Read auth.test.ts</span><i style="width:8%"></i><span>1.6k</span></div>
<div><span>Edit auth.ts</span><i style="width:2%"></i><span>0.4k</span></div>
<div><span>npm testの出力</span><i style="width:6%"></i><span>1.2k</span></div>
<div><span>AIの返答</span><i class="k" style="width:2%"></i><span>0.4k</span></div>
</div>
<div class="rule">返答のたびに、ここまでの全部をモデルへ送り直す</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/context-window
- https://code.claude.com/docs/en/costs
[話すこと] 開始時点の34kは前ページの実画面の合計、以降の各行は公式ドキュメントの例。
会話が長いほど、返答1回の時間と費用が増える。関係ない作業へ移るときは/clearで空にする
-->

---

<!-- _class: content-center -->

# 机がいっぱいになると、古い会話は要約に差し替えられる

<div class="fig">
<div class="analogy"><b>たとえると</b>机の古い書類を「A社と契約した」の1枚にまとめて置き直す。細かい経緯は消える</div>
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
<rect x="440" y="230" width="260" height="64" fill="#d9e6ff"/>
<text x="570" y="270" text-anchor="middle" class="navy">最近使ったファイル最大5件</text>
<rect x="700" y="230" width="380" height="64" fill="none" stroke="#cccccc" stroke-width="2" stroke-dasharray="6 6"/>
<text x="890" y="270" text-anchor="middle" class="s">空いた分に、続きの会話が入る</text>
</svg>
</div>
<div class="rule">残したい指示は、会話ではなくファイルに書く</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/context-window#what-survives-compaction
- https://code.claude.com/docs/en/memory#instructions-seem-lost-after-compact
[話すこと] この置き換えを圧縮（compaction）と呼ぶ。自動でも走るし、/compactで自分でも起こせる。
CLAUDE.md、条件なしのrules、memoryはファイルなので読み直される。会話で言っただけの指示は要約に溶ける。
読み書きしたファイルは、更新が新しい最大5件だけ再読込される
-->

---

# CLAUDE.mdは、新しく入った人に渡す申し送りメモ

<div class="fig">
<div class="analogy"><b>たとえると</b>出社したらまず読む申し送り。何のプロジェクトで、どう動いてほしいかを書いておく</div>
<div class="plan-layout">
<div class="plan-paper">
<div class="plan-paper-title">CLAUDE.md</div>
<div><b>概要</b><span>Todoアプリ。<span class="ico i-nextjs"></span>Next.jsと<span class="ico i-supabase"></span>Supabase</span></div>
<div><b>コマンド</b><span><span class="ico i-npm"></span>npm run dev（起動）、npm test（動作テスト）</span></div>
<div><b>守ること</b><span>変更後はnpm testを通す。src/db/は触らない</span></div>
<div><b>参照</b><span>@docs/api.md（別ファイルを取り込む）</span></div>
</div>
<div class="numbered">
<div><b>1. 場所</b><span>自分用はホームフォルダの~/.claude/、プロジェクト用はそのフォルダの直下</span></div>
<div><b>2. 読まれる時</b><span>セッションの開始時。圧縮のあとにも読み直される</span></div>
<div><b>3. 書き方</b><span>短く、具体的に。200行以内が目安</span></div>
</div>
</div>
<p class="cap">AGENTS.mdは、他のツールと共通で使える同じ役割のファイル</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/costs#move-instructions-from-claudemd-to-skills
[話すこと] セッション＝claudeを起動してから終えるまでの1回。長い手順はskillsへ移す（第3章）
-->

---

<!-- _class: content-center -->

# rulesは、その棚を開けたときだけ目に入る注意書き

<div class="fig">
<div class="analogy"><b>たとえると</b>「この棚を開けたら、中のものは必ず元に戻す」と棚の扉に貼った紙</div>
<div class="scene-grid">
<div class="ticket code">
<div><b>場所</b><span>.claude/rules/api.md</span></div>
<div><b>条件</b><span>paths: ["src/api/**/*.ts"]</span></div>
<div><b>本文</b><span>APIを変えたら、必ずテストを通す</span></div>
</div>
<div class="numbered">
<div><b>1. 条件なし</b><span>壁に貼る。CLAUDE.mdと同じく、いつも読まれる</span></div>
<div><b>2. 条件あり</b><span>棚に貼る。対象のファイルを読んだときだけ入る</span></div>
<div><b>3. 分ける理由</b><span>関係のない作業では読ませず、コンテキストを軽く保つ</span></div>
</div>
</div>
<p class="cap">「src/api/**/*.ts」は「src/apiの下にある.tsファイル全部」の意味。~/.claude/rules/に置くと全プロジェクトに効く</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory#organize-rules-with-clauderules
-->

---

# memoryは、AIが書き、人も直せる業務日誌

<div class="fig">
<div class="analogy"><b>たとえると</b>「あの人はこう直された」と書き留めておく日誌。次の出社時に見出しだけ読み返す</div>
<div class="plan-layout paper-wide">
<div class="plan-paper">
<div class="plan-paper-title">~/.claude/projects/&lt;project&gt;/memory/</div>
<div><b>MEMORY.md</b><span>索引。1件1行。開始時に読む</span></div>
<div><b>user_*.md</b><span>利用者の役割、好み</span></div>
<div><b>feedback_*.md</b><span>利用者からの訂正、認めた進め方</span></div>
<div><b>project_*.md</b><span>経緯や期限。ほかに参照先を残すreference_*.mdも</span></div>
</div>
<div class="numbered">
<div><b>1. 誰が書くか</b><span>AIが書く。利用者に訂正されたときなどに残す</span></div>
<div><b>2. いつ読むか</b><span>開始時に索引の先頭200行か25KBの早い方まで。詳細は必要なときに開く</span></div>
<div><b>3. どう直すか</b><span>/memoryで中身を見て、人が書き換えてよい</span></div>
</div>
</div>
<p class="cap">CLAUDE.mdは人が書く申し送り、memoryはAIが書く日誌。私の環境には87件ある</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory#auto-memory
[話すこと] ファイル名は例。分類はファイル先頭のtypeで記録される
-->

---

<!-- _class: chapter -->
<!-- header: '2. AIの動き方' -->

<div class="n">CHAPTER 2</div>

# AIの動き方

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
<text x="610" y="228" text-anchor="middle" class="s">Read、Edit、Bash、Grep。外部サービスへの接続はMCP</text>
</svg>
</div>
<div class="rule">この繰り返しがエージェントループ。料理して、味見して、直すのと同じ</div>
</div>

<!--
[Sources]
- https://www.anthropic.com/engineering/building-effective-agents
- https://code.claude.com/docs/en/how-claude-code-works
[話すこと] チャットは1往復で終わる。エージェントは「読んだ→足りない→もう1つ読む」を自分で続ける。
MCPはModel Context Protocolの略で、GitHubやDBなど外部サービスをツールとして見せる共通の約束事
-->

---

<!-- _class: content-center -->

# 完了条件は、AIに渡す「どうなったら終わりか」の取り決め

<div class="fig">
<div class="pair">
<div class="pair-side">
<b>完了条件なし</b>
<span>「ログインを直して」だけ<br>→ 修正して「直しました」で止まる。動くかどうかは人が確かめる</span>
</div>
<div class="pair-link">vs</div>
<div class="pair-side on">
<b>完了条件あり</b>
<span>CLAUDE.mdに「変更後はnpm testを通す」がある<br>→ テストを実行し、失敗があれば直し、通ってから止まる</span>
</div>
</div>
<div class="rule">完了条件は、指示に書いても、CLAUDE.mdに書いてもよい</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/costs#work-efficiently-on-complex-tasks
[話すこと] 3枚目の設定AとBの差は、ここに落ちる。第1回の「指示の4項目」の完了条件も同じ役割。
AIは条件を自分で確かめる材料にする
-->

---

# ループエンジニアリングは、人が指示を打つ代わりに仕組みを回す

<div class="fig">
<div class="quote-layout">
<div class="quote">
<p>I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do.</p>
<small>「もうClaudeに指示は打たない。Claudeに指示を出し、次を決めるループを回している」<br>Boris Cherny（Claude Code責任者）の発言。Addy Osmaniの記事より引用</small>
</div>
<div class="numbered">
<div><b>1. 起動のきっかけ</b><span>決まった時刻、PR（変更の提案）が届いたとき、テストの失敗。人が指示を打たなくても動く</span></div>
<div><b>2. 確かめる手段</b><span>テスト、lint（書き方の自動点検）、別のエージェントによるレビュー</span></div>
<div><b>3. 記録と引き継ぎ</b><span>進み具合をファイルに残し、次の周に渡す</span></div>
</div>
</div>
<p class="cap">前ページのループを、人の代わりに外から回す仕組み。人の仕事は、設計と最終判断になる</p>
</div>

<!--
[Sources]
- https://addyosmani.com/blog/loop-engineering/
- https://jp.findy-team.io/blogs/loop-engineering/
[話すこと] 2026年に広まった言い方。例: 毎朝issueを分類、PRが来たらレビュー、テストが通るまで修正。
どれも最終判断は人に残す
-->

---

<!-- _class: chapter -->
<!-- header: '3. ハーネス' -->

<div class="n">CHAPTER 3</div>

# ハーネス

毎回お願いしなくても、守らせるには

---

<!-- _class: content-center -->

# ハーネスは、エージェントのうちモデル以外の全部

<div class="fig">
<div class="svgfig">
<svg width="1152" height="380" viewBox="0 0 1152 380" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="1152" height="380" rx="14" fill="#e8f1fe" stroke="#0031d8" stroke-width="3"/>
<text x="28" y="40" class="b navy">利用者が足すハーネス（この後、1つずつ見る）</text>
<text x="28" y="70" class="s">読んで従うもの: CLAUDE.md、rules、memory、skills。機械で止めるもの: hooks、settings.jsonのdeny</text>
<rect x="140" y="96" width="872" height="260" rx="12" fill="#ffffff" stroke="#cccccc" stroke-width="2"/>
<text x="168" y="134" class="b">製品が持つハーネス</text>
<text x="168" y="162" class="s">システムプロンプト、標準ツール、圧縮、権限の確認</text>
<rect x="356" y="188" width="440" height="140" rx="10" fill="#1a1a1a"/>
<text x="576" y="250" text-anchor="middle" class="b w">モデル</text>
<text x="576" y="284" text-anchor="middle" class="s" style="fill:#e6e6e6">文章を読んで、次の行動を決める本体</text>
</svg>
</div>
<div class="rule">ハーネスは馬具の意味。同じ馬でも、手綱と鞍の付け方で走り方が変わる</div>
</div>

<!--
[Sources]
- https://martinfowler.com/articles/harness-engineering.html
[話すこと] ハーネスは馬具の意味。Birgitta Böckeler（Thoughtworks、2026-04）の定義で「Agent = Model + Harness」。
3枚目の設定AとBの差はここ
-->

---

<!-- _class: content-center -->

# ハーネスには、動く前に効くものと、動いたあとに効くものがある

<div class="fig">
<div class="pair">
<div class="pair-side on">
<b>事前（動く前に効く）</b>
<span>CLAUDE.md、rules、skills、実行前のhook、settings.jsonのdeny</span>
</div>
<div class="pair-link">vs</div>
<div class="pair-side">
<b>事後（動いたあとに効く）</b>
<span>実行後のhook、テスト、lint（書き方の自動点検）、人のレビュー</span>
</div>
</div>
<div class="rule">この2つを設計するのが、ハーネスエンジニアリング</div>
</div>

<!--
[Sources]
- https://martinfowler.com/articles/harness-engineering.html
[話すこと] 原文はguides（feedforward）とsensors（feedback）。人の確認をなくすのではなく、確認が要る場所へ人の目を集める。
hookの正式名（PreToolUse、PostToolUse）は22枚目で出す。settings.jsonは25枚目
-->

---

<!-- _class: content-center -->

# skillsは、棚にしまってある手順書。必要なときだけ開く

<div class="fig">
<div class="analogy"><b>たとえると</b>背表紙（説明文）はいつも見えていて、中身は使うときだけ開くマニュアル</div>
<div class="scene-grid">
<div class="ticket code">
<div><b>場所</b><span>~/.claude/skills/gijiroku/SKILL.md</span></div>
<div><b>説明</b><span>description: 会議メモから決定事項と担当・期限を抜き出す</span></div>
<div><b>本文</b><span>決定事項を拾い、担当と期限を表にし、未決を別に…</span></div>
</div>
<div class="numbered">
<div><b>1. 常に読まれるもの</b><span>説明文だけ。AIはこれを見て、使う場面を判断する</span></div>
<div><b>2. 呼ばれたとき</b><span>本文を読む。人が/gijirokuと打っても、AIが自分で選んでもよい</span></div>
<div><b>3. CLAUDE.mdとの分担</b><span>いつも必要な事実はCLAUDE.md、手順はskills</span></div>
</div>
</div>
<p class="cap">私の環境には20本。議事録のほか、スライド作り、レビュー、税金の相談など</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/skills
[話すこと] disable-model-invocation: true にすると説明文も常駐せず、人が呼ぶまで入らない（発展）
-->

---

<!-- _class: content-center -->

# hooksは、決まった場面で自動で動く装置

<div class="fig">
<div class="analogy"><b>たとえると</b>改札のゲート。切符がなければ、駅員の判断に関係なく閉じる。下のPreToolUseがこれにあたる</div>
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
<div><b>1. 何か</b><span>決めた場面で、シェルスクリプトなどを自動で実行する仕組み。上の緑と赤の点が、その場面</span></div>
<div><b>2. 止め方</b><span>PreToolUse（ツール実行の直前）で拒否を返すと、そのツールは実行されない</span></div>
</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/hooks
[話すこと] スクリプトはAIに書かせてもよい。止めるだけでなく、文脈を足したり記録したりもする
-->

---

<!-- _class: content-center -->

# PreToolUse hookは、AIが実行しようとした瞬間に止める

<div class="fig">
<img class="shot" src="assets/shots/hook-deny-crop.png" alt="Claude Codeに.envの中身を表示するよう頼んだ画面。Bashの実行前にPreToolUse hookがエラーを返し、機密ファイルの読み取りが禁止されている">
<div class="numbered three">
<div><b>1. 頼んだこと</b><span>「.env（APIキーなどが入るファイル）の中身を表示して」</span></div>
<div><b>2. AIの動き</b><span>コマンドを組み立てて実行しようとした</span></div>
<div><b>3. hookの動き</b><span>実行の直前に拒否を返し、コマンドは実行されなかった</span></div>
</div>
<p class="cap">2026-09-21に私の環境で撮影。AIは自分でも「値は読まない」と気をつけたが、hookはAIの判断と関係なく止める</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/hooks
[実演2] 可能なら自分の環境で再現して見せる。3分
-->

---

<!-- _class: content-center -->

# hookの中身は、短いスクリプトと、settings.jsonへの登録

<div class="fig">
<div class="scene-grid">
<div class="ticket code">
<div><b>スクリプト</b><span>~/.claude/scripts/hooks/block-secret-bash-read.sh</span></div>
<div><b>中身</b><span>渡されたコマンドが「.env」などを読もうとしていたら、拒否を返して終わる</span></div>
<div><b>登録</b><span>settings.jsonのhooksに、場面（PreToolUse）、対象ツール（matcher）、実行するコマンド（command）を書く</span></div>
</div>
<div class="numbered">
<div><b>1. 書く量</b><span>数行から。最初は1つの条件だけでよい</span></div>
<div><b>2. 誰が書くか</b><span>AIに書かせてよい。前ページの画面も、AIに書かせたhookが止めている</span></div>
<div><b>3. 止まらなかったら</b><span>条件を足す。抜け道が見つかるたびに育てる</span></div>
</div>
</div>
<p class="cap">前ページの画面を止めたのが、このhook。私のhookは20本あるが、始まりはどれも数行だった</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/hooks
[話すこと] block-secret-bash-read.shは実在のhook。Bash経由の読み取りを止める条件を足していったら今の形になった。
ファイルを直接編集する経路は別のhook（block-env.sh）が見ている。
学生には「1つの条件から始めればよい」が伝わればよい
-->

---

<!-- _class: content-center -->

# settings.jsonは、AIの運用設定をまとめた1枚

<div class="fig">
<div class="analogy"><b>たとえると</b>permissionsは入館証。入れる部屋、入れない部屋、受付に聞く部屋を決めておく</div>
<div class="scene-grid">
<div class="ticket code">
<div><b>permissions</b><span>allow（許す）、deny（禁じる）、ask（毎回聞く）</span></div>
<div><b>hooks</b><span>どの場面でどのhookを走らせるか</span></div>
<div><b>env</b><span>AIが使う環境変数</span></div>
<div><b>model</b><span>既定のモデル</span></div>
</div>
<div class="numbered">
<div><b>1. 自分用</b><span>~/.claude/settings.json。全プロジェクトに効く</span></div>
<div><b>2. プロジェクト用</b><span>.claude/settings.json。リポジトリで共有する</span></div>
<div><b>3. 私の環境の実数</b><span>allow 49件、deny 21件、ask 19件</span></div>
</div>
</div>
<p class="cap">denyに書いた操作は、AIがやりたがっても実行されない。ただし、書き方に穴があると抜けられる（第4章）</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/settings
[話すこと] 優先順位は 組織 > コマンド引数 > プロジェクト（local > 共有） > 自分用
-->

---

<!-- _class: content-center -->

# 確実に守らせたいものほど、下の段へ置く

<div class="fig">
<div class="svgfig">
<svg width="1152" height="360" viewBox="0 0 1152 360" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="384" height="120" fill="#f2f2f2"/>
<text x="24" y="44" class="b">1. 指示で頼む</text>
<text x="24" y="76" class="s">CLAUDE.md、memory</text>
<text x="24" y="102" class="s">AIが読んで従う。忘れることもある</text>
<rect x="384" y="120" width="384" height="120" fill="#e6e6e6"/>
<text x="408" y="164" class="b">2. 条件つきで渡す</text>
<text x="408" y="196" class="s">rules（paths）、skills</text>
<text x="408" y="222" class="s">必要なときだけ読ませる。効き方は1と同じ</text>
<rect x="768" y="240" width="384" height="120" fill="#000071"/>
<text x="792" y="284" class="b w">3. 機械で止める</text>
<text x="792" y="316" class="s w">PreToolUse hook、settings.jsonのdeny</text>
<text x="792" y="342" class="s w">AIの判断と関係なく効く</text>
<path d="M0 120 H384 V240 H768 V360" fill="none" stroke="#0031d8" stroke-width="4"/>
<text x="1140" y="30" text-anchor="end" class="s">下へ行くほど、AIの解釈が入る余地が減る</text>
</svg>
</div>
<div class="rule">口頭で注意する、張り紙をする、鍵をかける、の順</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory#claudemd-vs-auto-memory
[話すこと] 公式ドキュメントも「CLAUDE.mdとmemoryは文脈であって強制ではない。必ず止めたいならPreToolUse hookを」と書いている
-->

---

<!-- _class: chapter -->
<!-- header: '4. 私の環境' -->

<div class="n">CHAPTER 4</div>

# 私の環境

実物と、こう作っている理由

---

# 私の環境の全体像。指示は短く、止めるものは機械で

<div class="fig">
<div class="layer-stack tight">
<div class="layer">
<span class="layer-no">1</span>
<div><b>指示で頼む</b><small>「日本語で要点から答える」「秘密は読まない」「commitは頼まれたときだけ」。memoryには訂正の記録</small></div>
<div></div>
</div>
<div class="layer">
<span class="layer-no">2</span>
<div><b>条件つきで渡す</b><small>rules「Gitを触るときだけ読む」、skills「スライド作り」「議事録」</small></div>
<div></div>
</div>
<div class="layer on">
<span class="layer-no">3</span>
<div><b>機械で止める</b><small>hooks「.envを読むコマンドを止める」「終わる前に別のAIの検品を挟む」</small></div>
<div class="logos chips"><span class="ico ico-lg i-claude"></span><span class="ico ico-lg i-codex"></span></div>
</div>
</div>
<p class="cap">共通原則は、ClaudeとCodexの両方から読む共通のファイル。実数（2026-09-21）: memory 87件、rules 4本、skills 20本、hooks 20本、deny 21件</p>
</div>

<!--
[話すこと] 最初からこうだったわけではない。困ったことが起きるたびに1つずつ足した。次の4枚で、足すときの考え方を話す。
Claude（Anthropic）とCodex（OpenAI）の2製品で同じ設定を使い回している
-->

---

<!-- _class: content-center -->

# 考え方1: 3回言ったことは、指示をやめてhookにする

<div class="fig">
<div class="incident">
<div><span class="w">1回目</span><b>訂正する</b><span class="d">「本番の設定ファイルは私が管理するから触らないで」→ AIがmemoryに残す</span></div>
<div><span class="w">2回目</span><b>それでも触る</b><span class="d">memoryやCLAUDE.mdは読まれても、解釈が割れることがある</span></div>
<div class="bad"><span class="w">3回目</span><b>hookにする</b><span class="d">「そのファイルへの書き込みは、どのツールからでも止める」を機械で強制する</span></div>
<div><span class="w">おまけ</span><b>穴が見つかる</b><span class="d">今日の撮影中に、別のツール経由で書き換えられた。その日のうちにhookを足した</span></div>
</div>
<div class="rule">指示は忘れられる。実害が出たことは、機械で止める側へ移す</div>
</div>

<!--
[話すこと] 実例: 本番の設定ファイル（render.yaml）、.env、作業用の一時フォルダの3つが、訂正→hookへ移ったもの。
今日の撮影中に、denyの穴（Editは止まるがBashのsed -iは通る）が見つかり、hookを1本足した
-->

---

<!-- _class: content-center -->

# 考え方2: 秘密は「読ませない」。1本では足りないので3重にする

<div class="fig">
<div class="row c3">
<div class="card">
<span class="gi lg g-doc"></span>
<div class="t">Readツールを禁じる</div>
<div class="d">settings.jsonのdenyで、鍵やパスワードのフォルダを読めなくする</div>
</div>
<div class="card on">
<span class="gi lg g-bolt dark"></span>
<div class="t">コマンド経由も止める</div>
<div class="d">「cat .env」のように、Bashで中身を表示する経路もhookで止める</div>
</div>
<div class="card">
<span class="gi lg g-split"></span>
<div class="t">プログラム経由も止める</div>
<div class="d">「python -c」などに読ませる抜け道もhookで止める</div>
</div>
</div>
<p class="cap">AIは悪気なく「確認のため」に読もうとする。読まれた文章はAI会社のサーバーへ送られ、記録にも残る。だから読む前に止める</p>
</div>

<!--
[話すこと] 実際に一度、ツールのAPIキーが会話の記録へ流れたことがあり、コマンド経由のhookを足した。
その後、python -c経由の抜け道が見つかり、3本目を足した
-->

---

<!-- _class: content-center -->

# 考え方3: AIが「終わりました」と言う前に、hookで確かめさせる

<div class="fig">
<div class="flow">
<div class="step">AIが作業を終える</div><div class="arw">→</div><div class="step on">hookが止める</div><div class="arw">→</div><div class="step">別のAIが検品</div><div class="arw">→</div><div class="step">直してから報告</div>
</div>
<div class="numbered" style="margin-top:32px">
<div><b>1. レビューを挟むhook</b><span>コードを変えたまま終わろうとしたら、別製品のAI（Codex）に検品させてから報告させる</span></div>
<div><b>2. 別の案を探すhook</b><span>新しいアイデアを共有したら、作り始める前に「もっと良い方法はないか」を1回調べさせる</span></div>
<div><b>3. 実状態を確かめるhook</b><span>commitやpushのあとに、実際の状態を別のコマンドで確認させる</span></div>
</div>
</div>

<!--
[話すこと] 1は今日のスライド作りでも何度も発火し、そのたびに事実の誤りが見つかった。
3は、以前「マージ完了」と報告されたのに実際は完了していなかった事故から生まれた
-->

---

<!-- _class: content-center -->

# 考え方4: 毎回読ませる量は減らし、要るときだけ読ませる

<div class="fig">
<div class="pair">
<div class="pair-side">
<b>最初のころ</b>
<span>CLAUDE.mdに全部書く<br>→ 長くなり、関係のない作業でも毎回読む。守られにくくなる</span>
</div>
<div class="pair-link">→</div>
<div class="pair-side on">
<b>今</b>
<span>CLAUDE.mdは11行＋共通原則49行。手順はskills、条件つきの指示はrulesへ<br>→ 開始時点は約34k。必要なときだけ増える</span>
</div>
</div>
<div class="rule">まず10行から始めて、増やしすぎない</div>
</div>

<!--
[話すこと] 共通原則（49行）は別ファイルにして、ClaudeとCodexの両方から同じものを読ませている。
2製品で方針が食い違わないようにするため
-->

---

<!-- _class: content-center -->

# ハーネスを作る順番。困ったことが起きてから、1段ずつ下げる

<div class="fig">
<div class="closing-path">
<div><span class="gi lg g-chat"></span><b>まず訂正する</b><small>AIがmemoryに残す。多くはこれで足りる</small></div>
<span class="closing-arrow">→</span>
<div><span class="gi lg g-doc"></span><b>繰り返すならファイルに書く</b><small>CLAUDE.md、rules、skills</small></div>
<span class="closing-arrow">→</span>
<div class="on"><span class="gi lg g-bolt dark"></span><b>実害が出たらhookにする</b><small>機械で止め、抜け道が見つかったら足す</small></div>
</div>
<p class="cap">最初から全部は作らない。柵が多すぎると、AIも人も動きにくくなる</p>
</div>

<!--
[話すこと] hookは「善意の事故」を止める柵で、悪意のある回避を完全に防ぐものではない、と割り切っている
-->

---

<!-- header: 'まとめ' -->

# 今日の用語を、1枚にまとめる

<div class="fig">
<div class="tablewrap">
<table class="compare glossary">
<colgroup><col style="width:24%"><col style="width:40%"><col style="width:15%"><col style="width:21%"></colgroup>
<thead><tr><th></th><th>一言で</th><th>誰が書く</th><th>いつ効く</th></tr></thead>
<tbody>
<tr><th>コンテキスト</th><td>AIが1回の返答で読める文章の全部</td><td>製品と人と会話</td><td>毎回</td></tr>
<tr><th>CLAUDE.md</th><td>セッションの最初に読まれる指示ファイル</td><td>人</td><td>開始時と圧縮後</td></tr>
<tr><th>rules</th><td>1話題ごとに分けた指示。条件も付けられる</td><td>人</td><td>常に。条件付きなら対象を読んだとき</td></tr>
<tr><th>memory</th><td>AIが自分で残す学び</td><td>AI</td><td>開始時に索引を読む</td></tr>
<tr><th>skills</th><td>必要なときだけ読む手順書</td><td>人</td><td>呼ばれたとき</td></tr>
<tr><th>hooks</th><td>決めた場面で自動で走るスクリプト</td><td>人</td><td>条件に合う場面で自動で</td></tr>
<tr><th>settings.json</th><td>権限、hooks、環境変数の置き場</td><td>人</td><td>常に</td></tr>
<tr class="on"><th>ハーネス</th><td>モデル以外の全部。上の全部と、事後の検品を含む</td><td>製品と人</td><td>常に</td></tr>
<tr class="on"><th>エージェントループ</th><td>考える、ツールを使う、結果を読む、の繰り返し</td><td>製品</td><td>指示のあと</td></tr>
<tr class="on"><th>ループエンジニアリング</th><td>そのループを外から自動で回す設計</td><td>人</td><td>時刻や出来事で</td></tr>
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
<div><span class="gi lg g-split"></span><b>AIを1回訂正する</b><small>例：「返事は日本語で」。/memoryで残ったか確かめる。ChatGPTでも試せる</small></div>
<span class="closing-arrow">→</span>
<div class="on"><span class="gi lg g-bolt dark"></span><b>/contextを打ってみる</b><small>Memory filesとSkillsの行が、自分の置いたファイル</small></div>
</div>
<p class="cap">Claude Codeを入れたパソコンで。入れ方は勉強会のあとに案内する</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/context-window
[話すこと] hookを作るのは、困ったことが起きてからでよい（33枚目）
-->
