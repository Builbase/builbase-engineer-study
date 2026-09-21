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
  .glossary { display: table; width: 100%; font-size: 17px; }
  .glossary th, .glossary td { padding: 5px 12px; }
  .glossary tbody th { font-size: 17px; }
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
第2回 AIに仕事を任せるとき、AIの中で何が起きているか<br>
2026-09-28
</p>

---

<!-- header: 'はじめに' -->
# この勉強会で持ち帰ること

<div class="fig">
<div class="row c2">
<div class="card">
<span class="gi lg g-doc"></span>
<div class="t">AIは「何を読んで」動いているかが分かる</div>
<div class="d">同じ頼み方でも、AIが読んでいるものが違えば結果が変わる</div>
</div>
<div class="card on">
<span class="gi lg g-bolt dark"></span>
<div class="t">守らせたいことの「置き場」を選べる</div>
<div class="d">お願いする、条件つきで渡す、機械で止める。強さが違う</div>
</div>
</div>
</div>

<!--
[話すこと] 今日は専門用語を覚える回ではなく、AIの「机の上」と「手綱」を見る回。
英語の名前（CLAUDE.md、hooksなど）は、あとで検索できるように添えるだけ
-->

---

<!-- _class: content-center -->

# 同じ頼み方でも、AIが読んでいるものが違えば結果が変わる

<div class="fig">
<div class="pair">
<div class="pair-side">
<b>設定A</b>
<span>「ログインの不具合を直して」<br>→ 直して「終わりました」と報告。動くかどうかは確かめていない</span>
</div>
<div class="pair-link">vs</div>
<div class="pair-side on">
<b>設定B</b>
<span>同じAI、同じ頼み方<br>→ 直したあと、自分で動作チェックを走らせ、失敗を直してから報告</span>
</div>
</div>
<div class="rule">違いは頼み方ではなく、AIが最初に読む「申し送りメモ」と、AIを縛る「柵」。今日はこの2つを見る</div>
</div>

<!--
[話すこと] 設定Bには申し送りメモ（CLAUDE.md）に「直したら動作チェックを通してから報告」と書いてある。
動作チェック＝プログラムが正しく動くか自動で確かめるコマンド（npm testなど）。
第1回の「処理の終了と作業の完了は別」を、環境側から解く回だと位置づける
-->

---

# 今日の内容

<div class="fig">
<div class="row c4">
<div class="card">
<div class="t">1. AIの机の上</div>
<div class="d">AIが読んでいるもの。申し送りメモ、日記</div>
</div>
<div class="card">
<div class="t">2. AIの動き方</div>
<div class="d">考えて、やって、確かめる、の繰り返し</div>
</div>
<div class="card">
<div class="t">3. 手綱と柵</div>
<div class="d">手順書、見張り、許可リスト</div>
</div>
<div class="card on">
<div class="t">4. 私の環境</div>
<div class="d">実物と、こう作っている理由</div>
</div>
</div>
</div>

---

<!-- _class: content-center -->

# 今日のAIは、チャットではなく、パソコンの中で手を動かすAI

<div class="fig">
<div class="pair">
<div class="pair-side">
<b>チャットのAI</b>
<span>質問すると答えが返る。会話が中心<br>手元のファイルは、添付した分しか見えない</span>
</div>
<div class="pair-link">vs</div>
<div class="pair-side on">
<div class="logos chips"><span class="ico ico-lg i-claude"></span><span class="ico ico-lg i-codex"></span></div>
<b>今日のAI（Claude Code、Codex）</b>
<span>パソコンの中でファイルを読み書きし、コマンドを実行し、結果を見て続ける</span>
</div>
</div>
<div class="rule">一般知識は頭の中にある。今回の仕事に関する情報は、机の上に置いてあるものだけ</div>
</div>

<!--
[話すこと] Claude CodeはAnthropic、CodexはOpenAIの製品。どちらもターミナル（文字で命令する画面）で動く。
第1回で触った学生には「あのとき使ったもの」と一言
-->

---

<!-- _class: chapter -->
<!-- header: '1. AIの机の上' -->

<div class="n">CHAPTER 1</div>

# AIの机の上

AIは何を知っていて、何を知らないのか

---

# AIは、机の上に置いてある文章しか読めない

<div class="fig">
<div class="layer-stack tight">
<div class="layer">
<span class="layer-no">1</span>
<div><b>取扱説明書</b><small>道具の使い方や振る舞いの基本。製品側が最初から置いている。私たちには見えない</small></div>
<div></div>
</div>
<div class="layer on">
<span class="layer-no">2</span>
<div><b>申し送りメモと日記</b><small>私たちが書いた指示、AIが自分で書いた学び、手順書（あとで説明）の目次</small></div>
<div></div>
</div>
<div class="layer">
<span class="layer-no">3</span>
<div><b>会話と作業の結果</b><small>頼んだこと、読んだファイル、実行した結果</small></div>
<div></div>
</div>
</div>
<p class="cap">この「机の上の全部」をコンテキストと呼ぶ。机には広さの上限があり、量は「トークン」（文字数のような単位）で数える</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/context-window
- https://code.claude.com/docs/en/costs
[話すこと] 1トークンは日本語で1〜2文字ほど。「机の広さ」がコンテキストウィンドウ。
AIは返事をするたびに、机の上を全部読み直している
-->

---

# 頼む前から、机の上にはもう置いてあるものがある

<div class="fig">
<div class="scene-grid">
<img class="shot" src="assets/shots/context-categories.png" alt="Claude Codeで/contextを実行した画面の内訳。System prompt、System tools、MCP tools、Custom agents、Memory files、Skills、Messages、Free space">
<div class="numbered">
<div><b>1. 製品が置いたもの</b><span>取扱説明書（System prompt）、道具の説明（System tools）</span></div>
<div><b>2. 私が置いたもの</b><span>申し送りメモと日記（Memory files）、手順書の目次（Skills）</span></div>
<div><b>3. まだほぼ空</b><span>会話（Messages）。ここから増えていく。読めない英語の行は飛ばしてよい</span></div>
</div>
</div>
<p class="cap">2026-09-21に私の環境で「/context」と打った実画面。k＝千トークン。机の広さは約100万トークンで、頼む前から約34k（3%）が載っている</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/context-window
[実演1] ここで自分のClaude Codeを開き、/contextの実物を見せる。3分
-->

---

# 作業が進むほど、机の上は積み上がる

<div class="fig">
<div class="grow">
<div><span>頼む前から載っているもの（前ページ）</span><i class="g" style="width:36%"></i><span>34k</span></div>
<div><span>あなたの頼みごと</span><i class="k" style="width:2%"></i><span>0.05k</span></div>
<div><span>ファイルを1つ読む</span><i style="width:12%"></i><span>2.4k</span></div>
<div><span><span class="cond">条件つきメモ</span>が1枚入る（12枚目）</span><i style="width:2%"></i><span>0.4k</span></div>
<div><span>もう1つファイルを読む</span><i style="width:8%"></i><span>1.6k</span></div>
<div><span>ファイルを書き換える</span><i style="width:2%"></i><span>0.4k</span></div>
<div><span>動作チェックの結果</span><i style="width:6%"></i><span>1.2k</span></div>
<div><span>AIの返事</span><i class="k" style="width:2%"></i><span>0.4k</span></div>
</div>
<div class="rule">返事のたびに、机の上を全部読み直す。会話が長いほど、返事1回に時間とお金がかかる</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/context-window
- https://code.claude.com/docs/en/costs
[話すこと] 先頭の34kは前ページの実画面の合計、以降の各行は公式ドキュメントの例。
関係ない作業に移るときは/clearで机を片づける
-->

---

<!-- _class: content-center -->

# 机がいっぱいになると、製品が古い会話を「要約」に片づける

<div class="fig">
<div class="svgfig">
<svg width="1152" height="300" viewBox="0 0 1152 300" xmlns="http://www.w3.org/2000/svg">
<text x="0" y="32" class="b">片づけ前</text>
<rect x="0" y="48" width="180" height="64" fill="#000071"/>
<text x="90" y="88" text-anchor="middle" class="w">メモと日記</text>
<rect x="180" y="48" width="900" height="64" fill="#d9e6ff"/>
<text x="630" y="88" text-anchor="middle" class="navy">会話と作業の結果（頼みごと、読んだファイル、実行結果、AIの返事）</text>
<line x1="1080" y1="36" x2="1080" y2="124" stroke="#ec0000" stroke-width="3" stroke-dasharray="8 6"/>
<text x="1090" y="88" class="s" style="fill:#ec0000">上限</text>
<path d="M576 130 v40" stroke="#949494" stroke-width="3"/>
<path d="M566 162 l10 12 l10 -12" fill="none" stroke="#949494" stroke-width="3"/>
<text x="0" y="214" class="b">片づけ後</text>
<rect x="0" y="230" width="180" height="64" fill="#000071"/>
<text x="90" y="270" text-anchor="middle" class="w">メモと日記</text>
<rect x="180" y="230" width="260" height="64" fill="#949494"/>
<text x="310" y="270" text-anchor="middle" class="w">会話の要約</text>
<rect x="440" y="230" width="260" height="64" fill="#d9e6ff"/>
<text x="570" y="270" text-anchor="middle" class="navy">最近使ったファイル最大5件</text>
<rect x="700" y="230" width="380" height="64" fill="none" stroke="#cccccc" stroke-width="2" stroke-dasharray="6 6"/>
<text x="890" y="270" text-anchor="middle" class="s">空いた分に、続きの会話が入る</text>
</svg>
</div>
<div class="rule">メモと日記は読み直される。会話で言っただけのことは要約に溶ける。残したい指示はファイルへ</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/context-window#what-survives-compaction
- https://code.claude.com/docs/en/memory#instructions-seem-lost-after-compact
[話すこと] この片づけを「圧縮（compaction）」と呼ぶ。自動でも走るし、/compact で自分でも起こせる。
読んだファイルは、更新が新しい最大5件だけ読み直される
-->

---

# 申し送りメモ（CLAUDE.md）は、作業を始めるたびに読まれる

<div class="fig">
<div class="plan-layout">
<div class="plan-paper">
<div class="plan-paper-title">CLAUDE.md</div>
<div><b>これは何</b><span>Todoアプリ。<span class="ico i-nextjs"></span>Next.jsと<span class="ico i-supabase"></span>Supabaseで作っている</span></div>
<div><b>よく使う操作</b><span><span class="ico i-npm"></span>npm run dev（起動）、npm test（動作チェック）</span></div>
<div><b>守ること</b><span>直したら動作チェックを通す。src/db/は触らない</span></div>
<div><b>参照</b><span>@docs/api.md（別のファイルも読ませる）</span></div>
</div>
<div class="numbered">
<div><b>1. 置き場所</b><span>自分用は~/.claude/、プロジェクト用はそのフォルダの直下</span></div>
<div><b>2. 読まれる時</b><span>作業を始めるとき。机を片づけたあとも読み直す</span></div>
<div><b>3. 書き方</b><span>短く、具体的に。200行以内が目安</span></div>
</div>
</div>
<p class="cap">レポート作成なら「引用は出典つき」「ですます調」「下書きはdrafts/へ」のように書く。Next.jsなどの名前は覚えなくてよい</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/costs#move-instructions-from-claudemd-to-skills
[話すこと] 新しく入った人に渡す「このプロジェクトの申し送り」と同じ。AGENTS.mdという名前でも同じ役割。
「作業を始めるとき」＝claudeを起動してから終えるまでの1回（セッション）。「~/」はホームフォルダ。長い手順は手順書（第3章）へ移す
-->

---

<!-- _class: content-center -->

# 条件つきメモ（rules）は、当てはまるファイルを開いたときだけ読む

<div class="fig">
<div class="scene-grid">
<div class="ticket code">
<div><b>置き場所</b><span>.claude/rules/server.md</span></div>
<div><b>条件</b><span>paths: ["src/server/**"]</span></div>
<div><b>本文</b><span>このフォルダのプログラムを変えたら、必ず動作チェックを通す</span></div>
</div>
<div class="numbered">
<div><b>1. 条件なし</b><span>申し送りメモと同じで、いつも読まれる</span></div>
<div><b>2. 条件あり</b><span>その場所のファイルを開いたときだけ机に載る</span></div>
<div><b>3. 分ける理由</b><span>関係ない作業のときに読ませず、机を軽く保つ</span></div>
</div>
</div>
<p class="cap">条件の「src/server/**」は「src/serverフォルダの下にある全部」の意味</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory#organize-rules-with-clauderules
-->

---

# AIの日記（memory）は、AIが自分で書き、次の回に読み直す

<div class="fig">
<div class="plan-layout paper-wide">
<div class="plan-paper">
<div class="plan-paper-title">AIの日記の置き場（ファイル名は例）</div>
<div><b>MEMORY.md</b><span>目次。1件1行。作業を始めるときに読む</span></div>
<div><b>user_*.md</b><span>あなたの役割、好み</span></div>
<div><b>feedback_*.md</b><span>あなたからの訂正、認めた進め方</span></div>
<div><b>project_*.md</b><span>経緯や期限。ほかに参照先を残すreference_*.mdも</span></div>
</div>
<div class="numbered">
<div><b>1. 誰が書くか</b><span>AI。あなたが訂正したときなどに残す</span></div>
<div><b>2. いつ読むか</b><span>始めるときに目次だけ。詳しい中身は必要なときに開く</span></div>
<div><b>3. どう直すか</b><span>日記といっても時系列ではなく、テーマごとの覚え書き。「/memory」で見て、人が直してよい</span></div>
</div>
</div>
<p class="cap">申し送りメモは人が書く。日記はAIが書く。ファイル名の「*」は「何でも」の意味（user_好み.mdなど）</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory#auto-memory
[話すこと] 目次は先頭200行か25KBまでしか読まれない。だからAIは目次を1行にまとめ、詳細は別ファイルへ分ける
-->

---

<!-- _class: chapter -->
<!-- header: '2. AIの動き方' -->

<div class="n">CHAPTER 2</div>

# AIの動き方

頼んだあと、AIの中で何が起きているのか

---

<!-- _class: content-center -->

# AIは、考えて、道具を使い、結果を見て、また考える

<div class="fig">
<div class="svgfig">
<svg width="1152" height="330" viewBox="0 0 1152 330" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#949494"/></marker>
</defs>
<rect x="0" y="120" width="180" height="80" rx="10" fill="none" stroke="#cccccc" stroke-width="2"/>
<text x="90" y="168" text-anchor="middle" class="b">頼まれる</text>
<line x1="180" y1="160" x2="256" y2="160" stroke="#949494" stroke-width="3" marker-end="url(#ah)"/>
<rect x="260" y="120" width="180" height="80" rx="10" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="350" y="168" text-anchor="middle" class="b navy">考える</text>
<line x1="440" y1="160" x2="516" y2="160" stroke="#949494" stroke-width="3" marker-end="url(#ah)"/>
<rect x="520" y="120" width="180" height="80" rx="10" fill="none" stroke="#cccccc" stroke-width="2"/>
<text x="610" y="168" text-anchor="middle" class="b">道具を使う</text>
<line x1="700" y1="160" x2="776" y2="160" stroke="#949494" stroke-width="3" marker-end="url(#ah)"/>
<rect x="780" y="120" width="180" height="80" rx="10" fill="none" stroke="#cccccc" stroke-width="2"/>
<text x="870" y="168" text-anchor="middle" class="b">結果を見る</text>
<path d="M870 200 v60 H350 v-52" fill="none" stroke="#0031d8" stroke-width="3" marker-end="url(#ah)"/>
<text x="610" y="292" text-anchor="middle" class="navy" style="font-weight:700">終わったと判断するまで、ここへ戻る</text>
<line x1="960" y1="160" x2="1056" y2="160" stroke="#949494" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#ah)"/>
<rect x="1060" y="130" width="92" height="60" rx="10" fill="#f2f2f2"/>
<text x="1106" y="168" text-anchor="middle">終了</text>
<text x="610" y="70" text-anchor="middle" class="s">1周ごとに、道具の結果が机の上に足される（第1章の「積み上がる」）</text>
<text x="610" y="228" text-anchor="middle" class="s">ファイルを読む・書く、コマンドを実行する、Webを見る</text>
</svg>
</div>
<div class="rule">この繰り返しがエージェントループ。「読んだ→足りない→もう1つ読む」を自分で続ける</div>
</div>

<!--
[Sources]
- https://www.anthropic.com/engineering/building-effective-agents
- https://code.claude.com/docs/en/how-claude-code-works
[話すこと] 「道具」は、ファイルを読む・書く、コマンドを実行する、検索する、など。
外部サービス（GitHubなど）につなぐ道具はMCPという仕組みで足せる。名前だけ覚えておけばよい
-->

---

<!-- _class: content-center -->

# 「終わったかどうか」の決め方が、AIの止まる位置を決める

<div class="fig">
<div class="pair">
<div class="pair-side">
<b>終わりの条件を渡していない</b>
<span>「ログインを直して」だけ<br>→ 直して「直しました」で止まる。動くかは人が確かめる</span>
</div>
<div class="pair-link">vs</div>
<div class="pair-side on">
<b>終わりの条件を渡した</b>
<span>申し送りメモに「直したら動作チェックを通す」とある<br>→ チェックを走らせ、失敗を読み、直し、通ってから止まる</span>
</div>
</div>
<div class="rule">終わりの条件は、その場で打っても、メモに書いてもよい。AIはそれを自分で確かめる材料にする</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/costs#work-efficiently-on-complex-tasks
[話すこと] 3枚目の環境AとBの差は、ここに落ちる。第1回の「指示の4項目」の完了条件も同じ役割
-->

---

# 人が毎回頼む代わりに、AIを「回す仕組み」を作る考え方がある

<div class="fig">
<div class="quote-layout">
<div class="quote">
<p>I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do.</p>
<small>「もうClaudeに指示は打たない。Claudeに指示を出し、次を決める仕組みを回している」<br>Boris Cherny（Claude Code責任者）の発言。Addy Osmaniの記事より引用</small>
</div>
<div class="numbered">
<div><b>1. 動き出すきっかけ</b><span>毎朝9時、仲間がプログラムを直したとき、チェックが失敗したとき。人が打たなくても動く</span></div>
<div><b>2. 確かめる手段</b><span>動作チェック、書き方の自動点検、別のAIによる見直し</span></div>
<div><b>3. 記録と引き継ぎ</b><span>どこまで進んだかをファイルに残し、次の周へ渡す</span></div>
</div>
</div>
<p class="cap">これを「ループエンジニアリング」と呼ぶ。人の仕事は、毎回の指示から、仕組みの設計と最終判断へ移る</p>
</div>

<!--
[Sources]
- https://addyosmani.com/blog/loop-engineering/
- https://jp.findy-team.io/blogs/loop-engineering/
[話すこと] 2026年に広まった言い方。前のページのループ（AIの中の繰り返し）を、外から自動で回す仕組み。
例: 毎朝の問い合わせ分類、変更が届いたら見直す、チェックが通るまで直す。どれも最終判断は人に残す
-->

---

<!-- _class: chapter -->
<!-- header: '3. 手綱と柵' -->

<div class="n">CHAPTER 3</div>

# 手綱と柵

毎回お願いしなくても、守らせるには

---

<!-- _class: content-center -->

# AIは「頭脳」と「手綱・柵」でできている

<div class="fig">
<div class="svgfig">
<svg width="1152" height="380" viewBox="0 0 1152 380" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="1152" height="380" rx="14" fill="#e8f1fe" stroke="#0031d8" stroke-width="3"/>
<text x="28" y="40" class="b navy">私が足した手綱と柵（この後、1つずつ見る）</text>
<text x="28" y="70" class="s">手綱＝AIが読んで従うもの（申し送りメモ、条件つきメモ、日記、手順書）。柵＝機械で止めるもの（見張り、許可リスト）</text>
<rect x="140" y="96" width="872" height="260" rx="12" fill="#ffffff" stroke="#cccccc" stroke-width="2"/>
<text x="168" y="134" class="b">製品が最初から持っている手綱と柵</text>
<text x="168" y="162" class="s">取扱説明書、標準の道具、机の片づけ、危ない操作の確認</text>
<rect x="356" y="188" width="440" height="140" rx="10" fill="#1a1a1a"/>
<text x="576" y="250" text-anchor="middle" class="b w">頭脳（モデル）</text>
<text x="576" y="284" text-anchor="middle" class="s" style="fill:#e6e6e6">文章を読んで、次にやることを決める本体</text>
</svg>
</div>
<p class="cap">頭脳以外の全部を「ハーネス」（馬具の意味）と呼ぶ。同じ頭脳でも、手綱と柵の作り方で結果が変わる。3枚目の差はここ</p>
</div>

<!--
[Sources]
- https://martinfowler.com/articles/harness-engineering.html
[話すこと] Birgitta Böckeler（Thoughtworks、2026-04）の定義。「Agent = Model + Harness」。
「製品」はClaude CodeやCodexのこと
-->

---

<!-- _class: content-center -->

# ハーネスには、動く前に効くものと、動いたあとに効くものがある

<div class="fig">
<div class="pair">
<div class="pair-side on">
<b>事前（動く前に効く）</b>
<span>申し送りメモ、条件つきメモ、手順書、実行前の見張り、許可リストの「禁じる」</span>
</div>
<div class="pair-link">vs</div>
<div class="pair-side">
<b>事後（動いたあとに効く）</b>
<span>実行後の見張り、動作チェック、書き方の自動点検、人の見直し</span>
</div>
</div>
<div class="rule">事前と事後を組み合わせる設計を、ハーネスエンジニアリングと呼ぶ</div>
</div>

<!--
[Sources]
- https://martinfowler.com/articles/harness-engineering.html
[話すこと] 原文はguides（feedforward）とsensors（feedback）。人の確認をなくすのではなく、確認が要る場所へ人の目を集める、が原文の趣旨。
見張り（hooks）と許可リスト（settings.json）は次の3枚で扱う
-->

---

<!-- _class: content-center -->

# 手順書（skills）は、必要なときだけ開く

<div class="fig">
<div class="scene-grid">
<div class="ticket code">
<div><b>置き場所</b><span>~/.claude/skills/gijiroku/SKILL.md</span></div>
<div><b>1行の説明</b><span>会議メモから、決定事項と担当・期限を抜き出す</span></div>
<div><b>本文</b><span>決定事項を拾い、担当と期限を表にし、未決を別に…</span></div>
</div>
<div class="numbered">
<div><b>1. いつも机に載るもの</b><span>1行の説明だけ。AIはこれで「今この手順書が要る」と判断する</span></div>
<div><b>2. 開いたとき</b><span>本文を読む。人が「/gijiroku」と打っても、AIが自分で選んでもよい</span></div>
<div><b>3. 申し送りメモとの分担</b><span>いつも要る事実はメモ、長い手順は手順書</span></div>
</div>
</div>
<p class="cap">私の環境には20本。議事録のほか、スライド作り、レビュー、税金の相談など</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/skills
-->

---

<!-- _class: content-center -->

# 見張り（hooks）は、AIの判断とは関係なく機械で動く

<div class="fig">
<div class="hookflow">
<div class="step">頼む</div>
<div class="hook"><i></i><b>頼んだ直後</b>情報を足す</div>
<div class="step on">考える</div>
<div class="hook stop"><i></i><b>道具を使う直前</b>止められる</div>
<div class="step">道具を使う</div>
<div class="hook"><i></i><b>使った直後</b>点検する</div>
<div class="step">返事</div>
<div class="hook"><i></i><b>返事の直前</b>記録する</div>
</div>
<div class="numbered" style="margin-top:32px">
<div><b>1. 何か</b><span>決めた場面で、小さなプログラム（AIに書かせてもよい）を自動で走らせる仕組み。止めるだけでなく、メモを渡したり記録したりもする</span></div>
<div><b>2. 止め方</b><span>「道具を使う直前」の見張りが「ダメ」と返すと、その道具は使われない</span></div>
</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/hooks
[話すこと] 正式名は UserPromptSubmit / PreToolUse / PostToolUse / Stop。検索用に一度だけ言う
-->

---

<!-- _class: content-center -->

# 見張りが止めた実例。AIが実行しようとした瞬間に「ダメ」と返す

<div class="fig">
<img class="shot" src="assets/shots/hook-deny-crop.png" alt="Claude Codeに.envの中身を表示するよう頼んだ画面。コマンドの実行前に見張りがエラーを返し、秘密ファイルの読み取りが禁止されている">
<div class="numbered three">
<div><b>1. 頼んだこと</b><span>「.env（パスワードなどが入るファイル）の中身を見せて」</span></div>
<div><b>2. AIの動き</b><span>中身を読むコマンドを組み立てて、実行しようとした</span></div>
<div><b>3. 見張りの動き</b><span>実行前に「ダメ」と返し、コマンドは走らなかった</span></div>
</div>
<p class="cap">2026-09-21に私の環境で撮影。AIは自分でも「値は読まない」と気をつけたが、見張りはAIの判断と関係なく止める</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/hooks
[実演2] 可能なら自分の環境で再現して見せる。4分
-->

---

<!-- _class: content-center -->

# 設定ファイル（settings.json）に、許す操作と禁じる操作を書く

<div class="fig">
<div class="scene-grid">
<div class="ticket code">
<div><b>permissions</b><span>allow（許す）、deny（禁じる）、ask（毎回聞く）の3つの表</span></div>
<div><b>hooks</b><span>どの場面でどの見張りを走らせるか</span></div>
<div><b>env</b><span>AIが動くときの細かい設定</span></div>
<div><b>model</b><span>使う頭脳の種類</span></div>
</div>
<div class="numbered">
<div><b>1. 自分用</b><span>~/.claude/settings.json。全プロジェクトに効く</span></div>
<div><b>2. プロジェクト用</b><span>.claude/settings.json。チームで共有する</span></div>
<div><b>3. 私の環境の実数</b><span>許す49件、禁じる21件、毎回聞く19件</span></div>
</div>
</div>
<p class="cap">「禁じる」に書いた操作は、AIがやりたがっても実行されない。ただし4章で見るとおり、書き方に穴があると抜けられる</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/settings
[話すこと] 優先順位は 組織 > コマンド引数 > プロジェクト（local > 共有） > 自分用。学生には「自分用とプロジェクト用がある」で十分
-->

---

<!-- _class: content-center -->

# 確実に守らせたいものほど、下の段へ置く

<div class="fig">
<div class="svgfig">
<svg width="1152" height="360" viewBox="0 0 1152 360" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="384" height="120" fill="#f2f2f2"/>
<text x="24" y="44" class="b">1. お願いする</text>
<text x="24" y="76" class="s">申し送りメモ、日記</text>
<text x="24" y="102" class="s">AIが読んで従う。忘れることもある</text>
<rect x="384" y="120" width="384" height="120" fill="#e6e6e6"/>
<text x="408" y="164" class="b">2. 条件つきで渡す</text>
<text x="408" y="196" class="s">条件つきメモ、手順書</text>
<text x="408" y="222" class="s">要るときだけ読ませる。効き方は1と同じ</text>
<rect x="768" y="240" width="384" height="120" fill="#000071"/>
<text x="792" y="284" class="b w">3. 機械で止める</text>
<text x="792" y="316" class="s w">実行前の見張り、許可リストの「禁じる」</text>
<text x="792" y="342" class="s w">AIの判断と関係なく効く</text>
<path d="M0 120 H384 V240 H768 V360" fill="none" stroke="#0031d8" stroke-width="4"/>
<text x="1140" y="30" text-anchor="end" class="s">下へ行くほど、AIの解釈が入る余地が減る</text>
</svg>
</div>
<p class="cap">口頭注意 → 張り紙 → 鍵をかける、の順。公式も「メモと日記は文脈で、強制ではない。必ず止めたいなら見張りを」と書いている</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory#claudemd-vs-auto-memory
-->

---

<!-- _class: chapter -->
<!-- header: '4. 私の環境' -->

<div class="n">CHAPTER 4</div>

# 私の環境

実物の数と、こう作っている理由

---

# 私の環境の全体像。お願いは短く、止めるものは機械で

<div class="fig">
<div class="layer-stack tight">
<div class="layer">
<span class="layer-no">1</span>
<div><b>お願いする</b><small>「日本語で要点から答える」「秘密は読まない」「保存の確定は頼まれたときだけ」。日記には訂正の記録</small></div>
<div></div>
</div>
<div class="layer">
<span class="layer-no">2</span>
<div><b>条件つきで渡す</b><small>「ファイルの履歴を触るときだけ読むメモ」、手順書「スライド作り」「議事録」</small></div>
<div></div>
</div>
<div class="layer on">
<span class="layer-no">3</span>
<div><b>機械で止める</b><small>「パスワードのファイルを読むコマンドを止める」「終わる前に別のAIの検品を挟む」</small></div>
<div class="logos chips"><span class="ico ico-lg i-claude"></span><span class="ico ico-lg i-codex"></span></div>
</div>
</div>
<p class="cap">実数（2026-09-21）: メモ11行＋共通原則49行、日記87件、条件つきメモ4本、手順書20本、見張り20本、禁じる21件。ClaudeとCodexで同じ設定を使い回す</p>
</div>

<!--
[話すこと] 数は多く見えるが、最初からこうだったわけではない。困ったことが起きるたびに1つずつ足した。
次の4枚で、足すときの考え方を4つ話す
-->

---

<!-- _class: content-center -->

# 考え方1: 3回言ったことは、お願いをやめて見張りにする

<div class="fig">
<div class="incident">
<div><span class="w">1回目</span><b>訂正する</b><span class="d">「本番（実際に人が使う側）の設定ファイルは私が管理するから触らないで」→ AIが日記に残す</span></div>
<div><span class="w">2回目</span><b>それでも触る</b><span class="d">日記やメモは読んでも、解釈が割れることがある。効き方は同じ「お願い」の段</span></div>
<div class="bad"><span class="w">3回目</span><b>見張りにする</b><span class="d">「そのファイルへの書き込みは、どの道具からでも止める」を機械で強制</span></div>
<div><span class="w">おまけ</span><b>穴が見つかる</b><span class="d">今日の撮影中に、別の道具経由で書き換えられた。その日のうちに穴をふさいだ</span></div>
</div>
<div class="rule">お願いは忘れられる。実害が出たことは、機械で止める側へ移す</div>
</div>

<!--
[話すこと] 実例: 本番の設定ファイル（render.yaml）、パスワードのファイル（.env）、作業用の一時フォルダの3つが、
訂正→見張りへ移ったもの。今日の撮影中に「禁じる」の穴（別の道具からの書き換え）が見つかり、見張りを1本足した
-->

---

<!-- _class: content-center -->

# 考え方2: 秘密は「読ませない」。1本の柵では足りないので3重にする

<div class="fig">
<div class="row c3">
<div class="card">
<span class="gi lg g-doc"></span>
<div class="t">読む道具を禁じる</div>
<div class="d">許可リストで、鍵やパスワードのフォルダを「読むの禁止」に</div>
</div>
<div class="card on">
<span class="gi lg g-bolt dark"></span>
<div class="t">コマンド経由も止める</div>
<div class="d">「cat .env」（中身を表示するコマンド）のような経路も見張りが止める</div>
</div>
<div class="card">
<span class="gi lg g-split"></span>
<div class="t">プログラム経由も止める</div>
<div class="d">Pythonなどに読ませる抜け道も見張りが止める</div>
</div>
</div>
<p class="cap">AIは悪気なく「確認のため」に読もうとする。机の上の文章はAI会社のサーバーへ送られ、記録にも残る。だから読む前に止める</p>
</div>

<!--
[話すこと] 実際に一度、道具のAPIキーが会話の記録へ流れたことがあり、コマンド経由の見張りを足した。
その後、プログラム経由（python -c）の抜け道が見つかり、3本目を足した
-->

---

<!-- _class: content-center -->

# 考え方3: AIが「終わりました」と言う前に、見張りで確かめさせる

<div class="fig">
<div class="flow">
<div class="step">AIが作業を終える</div><div class="arw">→</div><div class="step on">見張りが止める</div><div class="arw">→</div><div class="step">別のAIが見直す</div><div class="arw">→</div><div class="step">直してから報告</div>
</div>
<div class="numbered" style="margin-top:32px">
<div><b>1. 見直しを挟む見張り</b><span>プログラムを変えたまま終わろうとしたら、別製品のAIに検品させてから報告させる</span></div>
<div><b>2. 別の案を探す見張り</b><span>新しいアイデアを共有したら、作り始める前に「もっと良い方法はないか」を1回調べさせる</span></div>
<div><b>3. 本当に終わったか確かめる見張り</b><span>保存や送信のあとに、実際の状態を別のコマンドで確認させる</span></div>
</div>
</div>

<!--
[話すこと] 1は今日のスライド作りでも5回発火し、そのたびに事実の誤りが見つかった。
3は、以前「マージ完了」と報告されたのに実際は完了していなかった事故から生まれた
-->

---

<!-- _class: content-center -->

# 考え方4: 毎回読ませる量は減らし、要るときだけ読ませる

<div class="fig">
<div class="pair">
<div class="pair-side">
<b>最初のころ</b>
<span>申し送りメモに全部書く<br>→ 長くなり、関係ない作業でも毎回読む。守られる率も下がる</span>
</div>
<div class="pair-link">→</div>
<div class="pair-side on">
<b>今</b>
<span>メモは11行。手順は手順書へ、条件つきの話は条件つきメモへ<br>→ 頼む前の机は約34k。必要なときだけ増える</span>
</div>
</div>
<div class="rule">机が軽いほど、AIは今の仕事に集中できる。まず10行から始めて、増やしすぎない</div>
</div>

<!--
[話すこと] 共通原則（49行）は別ファイルにして、ClaudeとCodexの両方から同じものを読ませている。
2製品で方針が食い違わないようにするため
-->

---

<!-- _class: content-center -->

# 柵を作る順番。困ったことが起きてから、1段ずつ下げる

<div class="fig">
<div class="closing-path">
<div><span class="gi lg g-chat"></span><b>まず訂正する</b><small>AIが日記に残す。多くはこれで足りる</small></div>
<span class="closing-arrow">→</span>
<div><span class="gi lg g-doc"></span><b>繰り返すならメモに書く</b><small>申し送りメモか、条件つきメモか、手順書</small></div>
<span class="closing-arrow">→</span>
<div class="on"><span class="gi lg g-bolt dark"></span><b>実害が出たら見張りにする</b><small>機械で止め、抜け道が見つかったら足す</small></div>
</div>
<p class="cap">最初から全部作らない。柵が多すぎると、AIも人も動きにくくなる</p>
</div>

<!--
[話すこと] 見張りは「善意の事故」を止める柵で、悪意のある回避を完全に防ぐものではない、と割り切っている
-->

---

<!-- header: 'まとめ' -->

# 今日の言葉を、1枚にまとめる

<div class="fig">
<div class="tablewrap">
<table class="compare glossary">
<colgroup><col style="width:28%"><col style="width:36%"><col style="width:15%"><col style="width:21%"></colgroup>
<thead><tr><th>今日の言い方（正式名）</th><th>一言で</th><th>誰が書く</th><th>いつ効く</th></tr></thead>
<tbody>
<tr><th>机の上（コンテキスト）</th><td>AIが返事のたびに読み込む文章の全部</td><td>製品と人と会話</td><td>毎回</td></tr>
<tr><th>申し送りメモ（CLAUDE.md）</th><td>作業の最初に読まれる指示書</td><td>人</td><td>始めるときと片づけ後</td></tr>
<tr><th>条件つきメモ（rules）</th><td>当てはまるファイルを開いたときだけ読む指示</td><td>人</td><td>その場所を開いたとき</td></tr>
<tr><th>日記（memory）</th><td>AIが自分で残す学び</td><td>AI</td><td>始めるときに目次を読む</td></tr>
<tr><th>手順書（skills）</th><td>必要なときだけ開く手順</td><td>人</td><td>開いたとき</td></tr>
<tr><th>見張り（hooks）</th><td>決めた場面で自動で走る小さなプログラム</td><td>人</td><td>条件に合う場面で自動で</td></tr>
<tr><th>許可リスト（settings.json）</th><td>許す・禁じる・毎回聞く操作の表</td><td>人</td><td>常に</td></tr>
<tr class="on"><th>手綱と柵（ハーネス）</th><td>頭脳以外の全部。上の全部と、事後の検品を含む</td><td>製品と人</td><td>常に</td></tr>
<tr class="on"><th>繰り返し（エージェントループ）</th><td>考える、道具、結果を見る、の繰り返し</td><td>製品</td><td>頼んだあと</td></tr>
<tr class="on"><th>回す仕組み（ループエンジニアリング）</th><td>その繰り返しを外から自動で回す設計</td><td>人</td><td>時刻や出来事で</td></tr>
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
<div><span class="gi lg g-doc"></span><b>申し送りメモを10行書く</b><small>これは何、よく使う操作、守ること</small></div>
<span class="closing-arrow">→</span>
<div><span class="gi lg g-split"></span><b>AIを1回訂正する</b><small>例「返事は日本語で」。日記に残ったか「/memory」で確かめる</small></div>
<span class="closing-arrow">→</span>
<div class="on"><span class="gi lg g-bolt dark"></span><b>「/context」を打ってみる</b><small>自分の机の上に何が載っているか見る</small></div>
</div>
<p class="cap">Claude Codeを入れたパソコンで。入れ方は勉強会のあとに案内する</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/context-window
[話すこと] 見張りを作るのは、困ったことが起きてからでよい（33枚目）
-->
