---
marp: true
theme: deck
paginate: false
size: 16:9
title: エンジニアの基礎：開発プロセス、Web、DB、クラウド、セキュリティ
description: builbaseエンジニア勉強会 第3回（60分）
author: seiji
style: |
  /* 第3回だけで使う部品。共通テーマ theme/deck.css の変数と寸法に合わせる */
  .flow .step small { display: block; margin-top: 8px; font-size: 16px; font-weight: 400; color: var(--gray-700); line-height: 1.45; }
  .flow.sm { gap: 12px; }
  .flow.sm .step { padding: 18px 16px; font-size: 20px; }
  .flow.sm .arw { font-size: 22px; }
  .flow .step.alt { border-color: var(--green); background: #f1f8f4; color: var(--green); }
  /* Marp既定の section table は display:block・width:max-content。表として全幅に伸ばす */
  .compare.full { display: table; width: 100%; }
  .compare.tight th, .compare.tight td { padding: 12px 16px; }
  .compare.tight { font-size: 18px; }
  .compare.tight tbody th { font-size: 19px; }
  .compare code, .plan-paper code, .numbered code { font-family: ui-monospace, Menlo, monospace; font-size: 0.92em; background: var(--gray-50); padding: 1px 6px; border-radius: 4px; }
  .compare td.ok { color: var(--green); font-weight: 700; text-align: center; }
  .compare td.ng { color: var(--red); font-weight: 700; text-align: center; }
  .numbered.three { grid-template-columns: repeat(3, 1fr); margin-top: 24px; }
  .numbered.two { grid-template-columns: 1fr 1fr; column-gap: 40px; }
  .numbered.sm b { font-size: 22px; }
  .numbered.sm span { font-size: 18px; }
  .pair.top { align-items: stretch; }
  .pair.top .pair-side { justify-content: center; min-height: 0; padding: 28px 30px; }
  .pair-side .mono { white-space: pre-wrap; font-family: ui-monospace, Menlo, monospace; font-size: 17px; line-height: 1.6; text-align: left; color: var(--ink); margin-top: 14px; }
  .pair-side ul { text-align: left; margin: 14px 0 0; font-size: 19px; color: var(--gray-700); }
  .pair-side li { margin: 6px 0; }
  .terminal-screen code { font-size: 19px; line-height: 1.6; white-space: pre; }
  .terminal-screen code.output { color: #9de2b9; margin: 0 0 12px 0; }
  .terminal-screen code.dim { color: #b8b8b8; }
  .terminal-screen.full { min-height: 0; padding: 58px 34px 24px; }
  /* 表を2つ並べる（テーブルと外部キー） */
  .dbt-pair { display: grid; grid-template-columns: 0.8fr 1.2fr; gap: 56px; align-items: start; }
  .dbt-title { font-size: 20px; font-weight: 700; color: var(--navy); margin-bottom: 8px; font-family: ui-monospace, Menlo, monospace; }
  .dbt { display: table; width: 100%; border-collapse: collapse; font-size: 18px; font-family: ui-monospace, Menlo, monospace; }
  .dbt th, .dbt td { border: 1px solid var(--gray-200); padding: 8px 12px; text-align: left; }
  .dbt th { background: var(--gray-50); color: var(--gray-700); font-weight: 700; }
  .dbt .pk { color: var(--blue); }
  .dbt .fk { color: var(--green); }
  /* ツール一覧。ロゴ、名前、一言を1行に置く */
  .tool-cols { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; }
  .tool-cols .gl { font-size: 18px; font-weight: 700; color: var(--gray-536); margin-bottom: 6px; }
  .tool-list { display: grid; gap: 0; }
  .tool-list > div { display: grid; grid-template-columns: 44px 190px 1fr; align-items: center; gap: 14px; padding: 13px 0; border-top: 1px solid var(--gray-200); }
  .tool-list .ico { width: 34px; height: 34px; margin: 0; }
  .tool-list .txt { display: inline-flex; align-items: center; justify-content: center; width: 34px; height: 34px; border-radius: 6px; background: var(--gray-100); color: var(--gray-700); font-size: 12px; font-weight: 700; }
  .tool-list b { font-size: 21px; }
  .tool-list span { font-size: 18px; color: var(--gray-700); line-height: 1.45; }
  .tool-list.one > div { grid-template-columns: 44px 220px 1fr; padding: 15px 0; }
  /* アジャイルソフトウェア開発宣言の4つの価値 */
  .values { display: grid; gap: 10px; }
  .values > div { display: grid; grid-template-columns: 1fr 60px 1fr; align-items: center; padding: 14px 24px; background: var(--gray-50); border-radius: 8px; font-size: 22px; }
  .values .l { color: var(--gray-536); text-align: right; }
  .values .a { color: var(--gray-420); text-align: center; font-size: 18px; }
  .values .r { color: var(--navy); font-weight: 700; }
  /* 責任分担の表（オンプレ、IaaS、PaaS、SaaS） */
  .stack { display: grid; grid-template-columns: 170px repeat(4, 1fr); gap: 6px; font-size: 18px; }
  .stack > div { padding: 9px 8px; text-align: center; border-radius: 4px; }
  .stack .h { font-weight: 700; color: var(--ink); font-size: 20px; }
  .stack .lb { text-align: right; color: var(--gray-700); padding-right: 14px; }
  .stack .u { background: var(--blue); color: #ffffff; font-weight: 700; }
  .stack .p { background: var(--gray-100); color: var(--gray-700); }
  .stack .ex { font-size: 16px; color: var(--gray-536); line-height: 1.4; }
  .legend { display: flex; justify-content: center; gap: 28px; margin-top: 16px; font-size: 18px; color: var(--gray-700); }
  .legend i { display: inline-block; width: 18px; height: 18px; border-radius: 3px; vertical-align: -3px; margin-right: 8px; }
  .legend i.u { background: var(--blue); }
  .legend i.p { background: var(--gray-100); border: 1px solid var(--gray-200); }
  /* 構成の段階（小規模→成長後） */
  .stages { display: grid; gap: 22px; }
  .stages > div { display: grid; grid-template-columns: 170px 1fr; align-items: center; gap: 24px; }
  .stages .lbl { font-size: 22px; font-weight: 700; color: var(--navy); }
  .stages .lbl small { display: block; font-size: 16px; font-weight: 400; color: var(--gray-536); }
  .stages .flow { justify-content: start; }
  .stages .step .ico { width: 24px; height: 24px; }
  .chip-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-top: 28px; }
  .chip-row > div { border-top: 5px solid var(--blue); background: var(--gray-50); padding: 14px 18px; }
  .chip-row b { display: block; font-size: 21px; }
  .chip-row span { display: block; margin-top: 4px; font-size: 17px; color: var(--gray-700); line-height: 1.45; }
  /* 横並びの工程は等幅にし、1文字ずつの折り返しを防ぐ */
  .flow.sm, .flow.agenda, .flow.eq { display: flex; justify-content: center; align-items: stretch; }
  .flow.sm .step, .flow.agenda .step, .flow.eq .step { flex: 1 1 0; min-width: 0; display: flex; flex-direction: column; justify-content: center; }
  .flow.sm .arw, .flow.agenda .arw, .flow.eq .arw { flex: none; align-self: center; text-align: center; }
  .stages .flow.sm .step { flex: 0 1 auto; padding: 16px 22px; }
  .flow.agenda .step { font-size: 21px; padding: 22px 12px; word-break: keep-all; }
  /* 各ページ上部の一言。ひとことで（青）とたとえると（緑）。第2回の .analogy と同じ役割 */
  .lead { box-sizing: border-box; flex: none; margin-bottom: 22px; padding: 12px 22px; border-left: 8px solid var(--blue); background: var(--gray-50); font-size: 22px; line-height: 1.5; }
  .lead b { color: var(--blue); margin-right: 14px; }
  .lead.ana { border-left-color: var(--green); background: #f1f8f4; }
  .lead.ana b { color: var(--green); }
  /* 一言を足した枚は、左右比較の枠の最小の高さを詰める */
  section:has(.lead) .pair-side { min-height: 220px; }
  .numbered.summary { gap: 10px; }
  .numbered.summary > div { padding: 8px 0 8px 20px; }
  /* ===== 第3回のレイアウト規則（全ページ共通） =====
     見出し → 一言（.lead）→ 主役の図（残りの高さを使い切る）→ まとめの1行（.rule）の順に置く */
  .fig > .flow.sm, .fig > .flow.eq, .fig > .flow.agenda, .fig > .pair, .fig > .scene-grid, .fig > .plan-layout,
  .fig > .tblwrap, .fig > .stages, .fig > .tool-list, .fig > .tool-cols, .fig > .row, .fig > .stack, .fig > .svgfig,
  .fig > .terminal-screen, .fig > .numbered.summary { flex: 1 1 auto; min-height: 0; }
  .fig > .flow.sm, .fig > .flow.eq, .fig > .flow.agenda { align-items: stretch; }
  .flow.sm .step, .flow.eq .step, .flow.agenda .step { font-size: 25px; padding: 20px 14px; gap: 0; border-radius: 12px; }
  .flow.sm .step small, .flow.eq .step small, .flow.agenda .step small { font-size: 18px; margin-top: 12px; line-height: 1.5; }
  .flow .step i { display: flex; align-items: center; justify-content: center; align-self: center; width: 34px; height: 34px; border-radius: 50%; background: var(--navy); color: #fff; font-style: normal; font-size: 18px; margin-bottom: 14px; }
  .flow .step.on i { background: var(--blue); }
  .flow .step em { align-self: center; margin-top: 10px; padding: 2px 14px; border-radius: 999px; background: var(--blue-50); color: var(--navy); font-style: normal; font-family: ui-monospace, Menlo, monospace; font-size: 16px; font-weight: 700; }
  .flow .step.on em { background: #ffffff; }
  .flow.sm .arw, .flow.eq .arw { font-size: 26px; }
  .fig > .rule { flex: none; margin-top: 24px; }
  .fig > .numbered.three { flex: none; }
  .fig > .chip-row { flex: none; }
  .pair { align-items: stretch; }
  .pair .pair-link { align-self: center; }
  .pair-side, section:has(.lead) .pair-side { min-height: 0; padding: 28px 32px; }
  .pair-side b { font-size: 28px; }
  .pair-side > span { font-size: 21px; }
  .pair-side ul { font-size: 21px; }
  .pair-side li { margin: 10px 0; }
  .pair-side .mono { font-size: 18px; }
  .scene-grid { align-items: stretch; }
  .scene-grid > .numbered { align-content: center; }
  .numbered.sm b { font-size: 25px; }
  .numbered.sm span { font-size: 20px; }
  .terminal-screen code { font-size: 20px; }
  .terminal-screen.full { justify-content: center; }
  .plan-layout { align-items: center; }
  .tblwrap { display: flex; }
  .tblwrap > table { height: 100%; }
  .compare.full { font-size: 21px; }
  .compare.full tbody th { font-size: 22px; }
  .compare.full thead th { font-size: 18px; }
  .compare.tight { font-size: 19px; }
  .compare.tight tbody th { font-size: 20px; }
  .fig > .svgfig { align-items: center; }
  .stack { grid-auto-rows: 1fr; font-size: 20px; }
  .stack > div { display: flex; align-items: center; justify-content: center; }
  .stack .lb { justify-content: flex-end; }
  .stack .ex { font-size: 16px; }
  .tool-list { grid-auto-rows: 1fr; }
  .tool-list b { font-size: 23px; }
  .tool-list span { font-size: 19px; }
  .tool-cols > div { display: flex; flex-direction: column; }
  .tool-cols > div > .tool-list { flex: 1; }
  .chip-row { margin-top: 24px; }
  .chip-row b { font-size: 22px; }
  .numbered.summary { align-content: space-evenly; }
  .numbered.summary b { font-size: 26px; }
  .numbered.summary span { font-size: 21px; }
  .lead { font-size: 22px; margin-bottom: 30px; }
  /* 黒い枠は影の分だけ見た目が上に広がるので、一言の枠との間をさらに空ける */
  .lead + .scene-grid, .lead + .terminal-screen { margin-top: 8px; }
  /* 番号付きの縦の工程。横並びより1行の文字が多く入り、折り返さない */
  .vsteps { display: grid; grid-auto-rows: 1fr; gap: 10px; }
  .fig > .vsteps { flex: 1 1 auto; min-height: 0; }
  .vsteps > div { display: grid; grid-template-columns: 40px 360px 1fr; align-items: center; gap: 22px; padding: 0 26px; border: 1px solid var(--gray-200); border-radius: 10px; }
  .vsteps > div.on { border-color: var(--blue); background: var(--blue-50); }
  .vsteps i { display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 50%; background: var(--navy); color: #fff; font-style: normal; font-weight: 700; font-size: 20px; }
  .vsteps .on i { background: var(--blue); }
  .vsteps b { font-size: 26px; display: flex; align-items: center; gap: 14px; }
  .vsteps .on b { color: var(--navy); }
  .vsteps em { padding: 2px 14px; border-radius: 999px; background: var(--blue-50); color: var(--navy); font-style: normal; font-family: ui-monospace, Menlo, monospace; font-size: 16px; }
  .vsteps .on em { background: #fff; }
  .vsteps span { font-size: 22px; color: var(--gray-700); }
  /* 左右の比較は、見出しと箇条書きを左にそろえ、縦は中央に置く */
  .pair-side, .pair.top .pair-side { align-items: center; text-align: center; justify-content: center; }
  .pair-side > b { text-align: center; }
  .pair-side ul { align-self: center; text-align: left; }
  .pair-side .mono { text-align: left; }
  /* 枠の見出しは上端に帯として置き、上下の余白を等しくする。本文は残りの高さの中央に置く */
  .pair-side, .pair.top .pair-side { justify-content: flex-start; padding: 22px 32px 28px; }
  .pair-side > b { padding: 0 0 22px; margin: 0; }
  .pair-side > b + * { margin-top: auto !important; }
  .pair-side > :last-child { margin-bottom: auto; }
  /* 左右の枠は中身の量にかかわらず同じ幅にする */
  .pair { grid-template-columns: minmax(0, 1fr) 74px minmax(0, 1fr); }
  .pair-side > b { align-self: stretch; padding-bottom: 12px; margin-bottom: 4px; border-bottom: 1px solid var(--gray-200); }
  .pair-side.on > b { border-bottom-color: var(--blue-100); color: var(--navy); }
  .pair-side ul { padding-left: 1.1em; margin: 10px 0 0; color: var(--ink); }
  .pair-side > span { color: var(--gray-700); }
  .pair-side .mono { white-space: pre; align-self: stretch; margin-top: 14px; padding: 14px 18px; border-radius: 8px; background: var(--ink); color: #ffffff; font-size: 17px; line-height: 1.6; }
  .pair-side .logos { align-self: center; }
  .pair-side .code-note { margin-top: 16px; font-size: 19px; font-family: ui-monospace, Menlo, monospace; color: var(--gray-700); }
  .dbt.mini { margin-top: 14px; font-size: 18px; font-family: var(--sans); }
  .dbt.mini th, .dbt.mini td { padding: 6px 12px; }
  .row.c3 .card { min-height: 0; padding: 28px 24px; }
  .row.c3 .card .t { font-size: 27px; margin: 16px 0 10px; }
  .row.c3 .card .d { font-size: 20px; }
  section { text-wrap: pretty; }
  .vsteps > div.ng { border-color: var(--red); background: #fdeeee; }
  .vsteps .ng i { background: var(--red); }
  .vsteps .ng b { color: var(--red); }
  .vsteps .ng em { background: #ffffff; color: var(--red); }
  .fig > .row { align-content: stretch; }
  .vsteps.narrow > div { grid-template-columns: 40px 240px 1fr; }
  .dbt.mini { margin-top: 10px; }
  .dbt.mini th, .dbt.mini td { padding: 4px 12px; }
  section:has(.dbt.mini) .pair-side { padding: 22px 28px; }
  .stages { align-content: space-evenly; }
  .stages .flow.sm { justify-content: flex-start; }
  .stages .flow.sm .step { font-size: 24px; padding: 20px 28px; }
  /* 黒い枠の影が下の安全域にはみ出さないよう、下に影の分だけ空ける */
  .fig > .scene-grid, .fig > .terminal-screen { margin-bottom: 10px; }
  /* 図版（インラインSVG）。文字は本文と同じ書体で描く */
  .svgfig { display: flex; justify-content: center; }
  .svgfig svg { font-family: var(--sans); }
  .svgfig text { font-size: 20px; fill: var(--ink); }
  .svgfig text.b { font-weight: 700; font-size: 21px; }
  .svgfig text.s { font-size: 17px; fill: var(--gray-700); }
  .svgfig text.m { font-family: ui-monospace, Menlo, monospace; font-size: 17px; }
  .svgfig text.w { fill: #ffffff; }
  .svgfig text.navy { fill: var(--navy); }
  .svgfig text.green { fill: var(--green); }
---

<!-- _class: title -->

# エンジニア勉強会

<p>
第3回 エンジニアの基礎：開発プロセス、Web、DB、クラウド、セキュリティ<br>
2026-10-26
</p>

---

<!-- header: 'はじめに' -->

# 今日の内容

<div class="fig">
<div class="lead"><b>ひとことで</b>Webサービスを「どう作り、どう動き、どこに置き、どう守るか」を一周する</div>
<div class="vsteps">
<div><i>1</i><b>開発プロセス</b><span>どの順番で作るか。ウォーターフォールとアジャイル</span></div>
<div><i>2</i><b>Webの仕組み</b><span>URLを開いてから画面が出るまで</span></div>
<div><i>3</i><b>DB</b><span>データのしまい方と、DBの選び方</span></div>
<div><i>4</i><b>クラウド</b><span>どこで動かすか。サービスの選び方</span></div>
<div><i>5</i><b>セキュリティ</b><span>誰に何を許し、どう守るか</span></div>
</div>
<p class="cap">例題は第1回と同じTodoアプリ。実演はブラウザの開発者ツールとSupabaseの2回</p>
</div>

---

<!-- _class: chapter -->
<!-- header: '1. 開発プロセス' -->

<div class="n">CHAPTER 1</div>

# 開発プロセス

何を、どの順番で作るか

---

# ウォーターフォールは、工程を順に完了させて進める

<div class="fig">
<div class="lead ana"><b>たとえると</b>家を建てる。設計図を全部描いて合意してから工事を始め、途中で間取りは変えない</div>
<div class="vsteps">
<div><i>1</i><b>要件定義</b><span>何を作るかを決める</span></div>
<div><i>2</i><b>基本設計</b><span>画面と機能を決める</span></div>
<div><i>3</i><b>詳細設計</b><span>プログラムの中身を決める</span></div>
<div><i>4</i><b>実装</b><span>コードを書く</span></div>
<div><i>5</i><b>テスト</b><span>正しく動くかを確かめる</span></div>
<div><i>6</i><b>リリース</b><span>使い始めてもらう</span></div>
</div>
<div class="rule">各工程の書類（成果物）を確認し、OKが出てから次の工程へ進む</div>
</div>

<!--
[話すこと] 名前は「滝」。水が上から下へ流れて戻らないように、前の工程へ戻ることを原則として想定しない。
だから最初の要件定義の精度が全体を決める。成果物は要件定義書、設計書、ソースコード、テスト結果など
-->

---

# V字モデルでは、作る前に「どう確かめるか」も決めておく

<div class="fig">
<div class="lead"><b>ひとことで</b>左で決めたことを、右で同じ高さのテストが確かめる</div>
<div class="svgfig">
<svg width="1152" height="380" viewBox="0 0 1152 380" xmlns="http://www.w3.org/2000/svg">
<path d="M150 40 L290 140 L430 240 L576 330 L722 240 L862 140 L1002 40" fill="none" stroke="#cccccc" stroke-width="4"/>
<line x1="260" y1="40" x2="892" y2="40" stroke="#949494" stroke-width="2" stroke-dasharray="8 6"/>
<line x1="400" y1="140" x2="752" y2="140" stroke="#949494" stroke-width="2" stroke-dasharray="8 6"/>
<line x1="540" y1="240" x2="612" y2="240" stroke="#949494" stroke-width="2" stroke-dasharray="8 6"/>
<text x="576" y="28" text-anchor="middle" class="s">頼まれた通りのものか</text>
<text x="576" y="128" text-anchor="middle" class="s">部品同士がつながるか</text>
<text x="576" y="226" text-anchor="middle" class="s">部品1つ</text>
<rect x="40" y="10" width="220" height="60" rx="8" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="150" y="48" text-anchor="middle" class="b navy">要件定義</text>
<rect x="180" y="110" width="220" height="60" rx="8" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="290" y="148" text-anchor="middle" class="b navy">基本設計</text>
<rect x="320" y="210" width="220" height="60" rx="8" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="430" y="248" text-anchor="middle" class="b navy">詳細設計</text>
<rect x="466" y="300" width="220" height="60" rx="8" fill="#000071"/>
<text x="576" y="338" text-anchor="middle" class="b w">実装</text>
<rect x="612" y="210" width="220" height="60" rx="8" fill="#f1f8f4" stroke="#197a4b" stroke-width="2"/>
<text x="722" y="248" text-anchor="middle" class="b green">単体テスト</text>
<rect x="752" y="110" width="220" height="60" rx="8" fill="#f1f8f4" stroke="#197a4b" stroke-width="2"/>
<text x="862" y="148" text-anchor="middle" class="b green">結合テスト</text>
<rect x="892" y="10" width="220" height="60" rx="8" fill="#f1f8f4" stroke="#197a4b" stroke-width="2"/>
<text x="1002" y="48" text-anchor="middle" class="b green">システムテスト</text>
</svg>
</div>
</div>

<!--
[Sources]
- IPA「共通フレーム2013」の工程区分を簡略化した
[話すこと] 左は下りながら細かく決めていく設計、右は上りながら確かめていくテスト。
同じ高さの設計とテストが対になる。最後に発注者が受入テストで確かめる
-->

---

# 後の工程で見つかった間違いほど、直す範囲が広がる

<div class="fig">
<div class="lead"><b>ひとことで</b>間違いは、早く見つけるほど安く直せる</div>
<div class="pair top">
<div class="pair-side">
<b>要件定義で見つかる</b>
<ul>
<li>書類の1行を直す</li>
<li>関係者にもう一度確認する</li>
</ul>
</div>
<div class="pair-link">vs</div>
<div class="pair-side on">
<b>テストや公開後に見つかる</b>
<ul>
<li>書類と設計を直す</li>
<li>コードを直し、影響する場所を探す</li>
<li>テストをやり直す</li>
<li>公開後なら、利用者への連絡とデータの修正も</li>
</ul>
</div>
</div>
<div class="rule">ウォーターフォールは、やることが最初に決まっているほど強く、変わるほど弱い</div>
</div>

<!--
[話すこと] 「後の工程ほど修正コストが何十倍」という数字がよく引用されるが、元の研究の条件は限られる。
数字ではなく、直す対象が増えるという構造で理解する
-->

---

# アジャイルは、少しずつ作って見せ、直しながら進める

<div class="fig">
<div class="lead ana"><b>たとえると</b>料理の味見。少し作って味見し、塩を足す。最初にレシピを全部決めない</div>
<div class="vsteps">
<div><i>1</i><b>少し作る</b><span>小さな機能を1つ作る</span></div>
<div><i>2</i><b>見せる</b><span>お客さんに触ってもらう</span></div>
<div><i>3</i><b>直す</b><span>意見をもとに変える</span></div>
<div class="on"><i>4</i><b>繰り返す</b><span>また1に戻って、少し作る</span></div>
</div>
<div class="rule">完璧な計画より、動くものを早く見せて方向を確かめる</div>
</div>

<!--
[Sources]
- https://agilemanifesto.org/iso/ja/manifesto.html
[話すこと] 元になったのはアジャイルソフトウェア開発宣言（2001年）。「計画に従うことよりも変化への対応を」など4つの価値を掲げる。
アジャイルは特定の手法の名前ではなく、この考え方の総称。
具体的なやり方の代表がスクラム（次のページ）
-->

---

# スクラムは、1〜4週間の区切りを繰り返す

<div class="fig">
<div class="lead"><b>ひとことで</b>アジャイルの代表的なやり方。区切りのことをスプリントと呼ぶ</div>
<div class="vsteps">
<div><i>1</i><b>リストを作る<em>バックログ</em></b><span>やりたいことを優先順に並べる</span></div>
<div><i>2</i><b>計画する</b><span>今回の区切りでやる分を選ぶ</span></div>
<div class="on"><i>3</i><b>作る</b><span>毎日15分、進み具合を共有しながら作る</span></div>
<div><i>4</i><b>見せる</b><span>できたものをお客さんに見せる</span></div>
<div><i>5</i><b>振り返る</b><span>進め方を良くして、次の区切りへ</span></div>
</div>
<div class="numbered three">
<div><b>プロダクトオーナー</b><span>何を、どの順で作るかを決める人</span></div>
<div><b>スクラムマスター</b><span>チームが進めやすいように支える人</span></div>
<div><b>開発者</b><span>実際に作る人たち</span></div>
</div>
</div>

<!--
[Sources]
- https://scrumguides.org/scrum-guide.html （スクラムガイド2020。スプリントは1か月以内）
[話すこと] 正式名はスプリントプランニング、デイリースクラム、スプリントレビュー、スプリントレトロスペクティブ。
期間は1か月以内で、1〜2週間にするチームが多い
-->

---

# どちらを選ぶかは、最初に全部決められるかで決まる

<div class="fig">
<div class="lead"><b>ひとことで</b>決まっているならウォーターフォール、作りながら決めるならアジャイル</div>
<div class="tblwrap">
<table class="compare full">
<colgroup><col style="width:18%"><col style="width:41%"><col style="width:41%"></colgroup>
<thead><tr><th>観点</th><th>ウォーターフォール</th><th>アジャイル</th></tr></thead>
<tbody>
<tr><th>やること</th><td>最初に決められる</td><td>作りながら変わる</td></tr>
<tr><th>お金の払い方</th><td>完成品に払う契約（請負）向き</td><td>作業量に払う契約（準委任）向き</td></tr>
<tr><th>向く例</th><td>銀行や役所のシステム、法律の改正対応</td><td>新しいサービス、社内ツール</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[話すこと] 受託開発では契約の形が進め方を縛る。請負は完成の責任を負うので、範囲を先に固めたい。
準委任には成果に対して払う型もあるので、「準委任＝アジャイル」とは限らない
-->

---

# 実際の案件では、前半を固めて後半を短い区切りで回す形もある

<div class="fig">
<div class="lead"><b>ひとことで</b>大枠は先に決め、細かいところは作りながら決める</div>
<div class="flow sm">
<div class="step">要件定義・<br>基本設計<small>範囲と予算を<br>先に決める</small></div>
<div class="arw">→</div>
<div class="step alt">スプリント1<small>作って見せる</small></div>
<div class="arw">→</div>
<div class="step alt">スプリント2<small>直して見せる</small></div>
<div class="arw">→</div>
<div class="step alt">スプリント3<small>仕上げる</small></div>
<div class="arw">→</div>
<div class="step">確認・<br>リリース<small>まとめて<br>確かめる</small></div>
</div>
<div class="rule">手法の名前より、何を先に決め、何を後で変えられるようにするかが大事</div>
</div>

<!--
[話すこと] ハイブリッド型と呼ばれることが多い。前半で範囲と予算を合意し、
実装は短い区切りで回して途中の画面を見せながら細部を詰める
-->

---

<!-- _class: chapter -->
<!-- header: '2. Webの仕組み' -->

<div class="n">CHAPTER 2</div>

# Webの仕組み

URLを開いたとき、裏で何が起きているか

---

# URLを開いてから画面が出るまでに、5つの段階がある

<div class="fig">
<div class="lead"><b>ひとことで</b>住所を調べ、つなぎ、鍵をかけ、頼んで受け取り、画面に描く</div>
<div class="vsteps">
<div><i>1</i><b>住所を調べる<em>DNS</em></b><span>名前を、数字の住所（IPアドレス）に変える</span></div>
<div><i>2</i><b>つなぐ<em>TCP</em></b><span>相手のコンピュータと通信路を作る</span></div>
<div><i>3</i><b>鍵をかける<em>TLS</em></b><span>やりとりを暗号化する</span></div>
<div class="on"><i>4</i><b>頼む・受け取る<em>HTTP</em></b><span>ページの中身をもらう</span></div>
<div><i>5</i><b>描く<em>レンダリング</em></b><span>受け取った中身を画面に表示する</span></div>
</div>
<div class="rule">URLのhttpsの「s」は、3の「鍵をかける」をしている印</div>
</div>

<!--
[話すこと] これは初めてHTTPSのサイトを開くときの一例。2回目以降や新しい方式（HTTP/3）では省かれる段階もある。
example.comのような名前は人間向け。コンピュータは数字の住所（IPアドレス）でしか相手を探せないので、最初に変換する。
1枚のページの中に画像やCSSがあれば、それぞれについて追加で頼む。実演1で見る
-->

---

# ブラウザとサーバーは、「頼む」と「返す」でやりとりする

<div class="fig">
<div class="lead"><b>ひとことで</b>頼むのがリクエスト、返すのがレスポンス。この決まりがHTTP</div>
<div class="scene-grid">
<div class="terminal-screen full">
<div class="terminal-bar">リクエストとレスポンス</div>
<code class="dim">頼む（リクエスト）</code>
<code>GET /api/todos</code>
<code class="output">Host: example.com</code>
<code class="dim">返す（レスポンス）</code>
<code>200 OK</code>
<code class="output">[{"title":"牛乳を買う","done":false}]</code>
</div>
<div class="numbered sm">
<div><b>メソッド（何をしたいか）</b><span>GETは見せて、POSTは作って、DELETEは消して</span></div>
<div><b>ステータスコード（結果）</b><span>200は成功、404は見つからない、500はサーバー側の失敗</span></div>
<div><b>ヘッダ（添え書き）</b><span>データの形式やログイン情報など、本文以外の情報</span></div>
</div>
</div>
</div>

<!--
[Sources]
- https://developer.mozilla.org/ja/docs/Web/HTTP
[話すこと] 更新はPUTやPATCH。ステータスコードは、2xxが成功、3xxがリダイレクトなど、4xxが送った側の誤り、5xxがサーバー側の誤り。
401（ログインしていない）と403（権限がない）は第5章でもう一度出る
-->

---

# HTTPは前のやりとりを覚えないので、Cookieで名乗る

<div class="fig">
<div class="lead"><b>ひとことで</b>ログインすると会員番号（セッションID）をもらい、以後は毎回それを見せる</div>
<div class="svgfig">
<svg width="1152" height="340" viewBox="0 0 1152 340" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10z" fill="#4d4d4d"/></marker></defs>
<rect x="40" y="0" width="160" height="48" rx="8" fill="#000071"/>
<text x="120" y="32" text-anchor="middle" class="b w">ブラウザ</text>
<rect x="680" y="0" width="160" height="48" rx="8" fill="#000071"/>
<text x="760" y="32" text-anchor="middle" class="b w">サーバー</text>
<line x1="120" y1="48" x2="120" y2="330" stroke="#cccccc" stroke-width="3"/>
<line x1="760" y1="48" x2="760" y2="330" stroke="#cccccc" stroke-width="3"/>
<line x1="124" y1="95" x2="752" y2="95" stroke="#4d4d4d" stroke-width="2.5" marker-end="url(#ah)"/>
<text x="440" y="83" text-anchor="middle">① ログインする（メールとパスワード）</text>
<line x1="756" y1="160" x2="128" y2="160" stroke="#4d4d4d" stroke-width="2.5" marker-end="url(#ah)"/>
<text x="440" y="148" text-anchor="middle">② 会員番号abc123をCookieに入れて返す</text>
<line x1="124" y1="225" x2="752" y2="225" stroke="#0031d8" stroke-width="2.5" marker-end="url(#ah)"/>
<text x="440" y="213" text-anchor="middle" style="fill:#0031d8">③ 「Todoを見せて」＋Cookie: abc123</text>
<line x1="756" y1="290" x2="128" y2="290" stroke="#4d4d4d" stroke-width="2.5" marker-end="url(#ah)"/>
<text x="440" y="278" text-anchor="middle">④ その人のTodoだけ返す</text>
<rect x="800" y="110" width="330" height="140" rx="8" fill="#f2f2f2" stroke="#cccccc"/>
<text x="822" y="146" class="b">サーバーのメモ（セッション）</text>
<text x="822" y="184" class="m">abc123 → 佐藤さん</text>
<text x="822" y="220" class="s">③の番号で、誰かを引く</text>
</svg>
</div>
<div class="rule">ブラウザは③から毎回Cookieを付けて送り、サーバーはメモと照らし合わせる</div>
</div>

<!--
[話すこと] HTTP自体が前のやりとりを覚えない性質を、ステートレスと呼ぶ。
Cookieは、サイトごとにブラウザが預かる小さなメモ。
サーバー側に記録を持たず、署名付きの札（JWT）に情報を入れて渡す方式もある。第5章で触れる
-->

---

# APIは、プログラム同士の注文窓口

<div class="fig">
<div class="lead"><b>ひとことで</b>URLで「何を」、メソッドで「どうするか」を伝える。REST型のAPIでよく使う作法</div>
<div class="plan-layout">
<div class="plan-paper">
<div class="plan-paper-title">TodoアプリのAPI</div>
<div><b><code>GET</code></b><span><code>/todos</code> 一覧を見せて</span></div>
<div><b><code>GET</code></b><span><code>/todos/42</code> 42番を見せて</span></div>
<div><b><code>POST</code></b><span><code>/todos</code> 新しく作って</span></div>
<div><b><code>PATCH</code></b><span><code>/todos/42</code> 42番を変えて</span></div>
<div><b><code>DELETE</code></b><span><code>/todos/42</code> 42番を消して</span></div>
</div>
<div class="numbered sm">
<div><b>URLは名詞</b><span>/getTodosではなく/todos</span></div>
<div><b>動詞はメソッド</b><span>同じURLでも、メソッドで意味が変わる</span></div>
<div><b>データはJSON</b><span>プログラムが読みやすい文字の形式</span></div>
</div>
</div>
</div>

<!--
[話すこと] APIはApplication Programming Interfaceの略。画面の裏では、フロントエンドがこの窓口に注文している。
RESTは作法で、厳密な規格ではない
-->

---

# フロントエンド、バックエンド、DBの3つに分けて作る

<div class="fig">
<div class="lead ana"><b>たとえると</b>レストラン。客席が画面、厨房が処理、冷蔵庫がデータ。客は厨房に入れない</div>
<div class="flow eq">
<div class="step">フロントエンド<small>ブラウザに出る画面<br><span class="ico i-nextjs"></span>Next.js、React</small></div>
<div class="arw">⇄<br><small style="font-size:15px">HTTP</small></div>
<div class="step on">バックエンド<small>ログイン確認や計算<br>Node.js、Python、Go</small></div>
<div class="arw">⇄<br><small style="font-size:15px">SQL</small></div>
<div class="step">DB<small>データを保存する<br><span class="ico i-postgresql"></span>PostgreSQL</small></div>
</div>
<div class="rule">ブラウザのコードは誰でも読める。秘密の値と権限の判断はバックエンドへ</div>
</div>

<!--
[話すこと] 役割を分けると、画面だけ、処理だけを別々に変えられる。
SupabaseはDBに加えてAPIとログインをまとめて用意してくれるので、バックエンドの一部を書かずに済む（第4章のBaaS）。
[実演1] ここでブラウザの開発者ツール（Networkタブ）を開き、ページを再読み込みしてリクエストの一覧、ステータス、ヘッダを見せる。2分
-->

---

<!-- _class: chapter -->
<!-- header: '3. DB' -->

<div class="n">CHAPTER 3</div>

# DB

データを壊さず、速く取り出せるようにしまう

---

# RDBは、表同士を番号でつないでデータを持つ

<div class="fig">
<div class="lead ana"><b>たとえると</b>Excelのシート。1行が1件、列が項目。シート同士を番号でつなぐ</div>
<div class="dbt-pair">
<div>
<div class="dbt-title">users（利用者）</div>
<table class="dbt">
<thead><tr><th class="pk">id 🔑</th><th>name</th></tr></thead>
<tbody>
<tr><td class="pk">1</td><td>佐藤</td></tr>
<tr><td class="pk">2</td><td>鈴木</td></tr>
</tbody>
</table>
</div>
<div>
<div class="dbt-title">todos（やること）</div>
<table class="dbt">
<thead><tr><th class="pk">id 🔑</th><th class="fk">user_id →</th><th>title</th></tr></thead>
<tbody>
<tr><td class="pk">10</td><td class="fk">1</td><td>牛乳を買う</td></tr>
<tr><td class="pk">11</td><td class="fk">1</td><td>資料を送る</td></tr>
<tr><td class="pk">12</td><td class="fk">2</td><td>会議の準備</td></tr>
</tbody>
</table>
</div>
</div>
<div class="numbered three">
<div><b>主キー 🔑</b><span>行を1つに決める番号。重複できない</span></div>
<div><b>外部キー →</b><span>別の表の主キーを指す列。存在しない番号は入らない</span></div>
<div><b>制約</b><span>空欄禁止などのルールを、DB自身が守らせる</span></div>
</div>
</div>

<!--
[話すこと] RDBのRはRelational（関係）。Excelとの違いは、大勢が同時に書き込んでも壊れないこと、ルールを守らせられること、大量のデータから速く探せること。
-->

---

# 同じことを2か所に書かない（正規化）

<div class="fig">
<div class="lead"><b>ひとことで</b>1つの情報は1か所にだけ置くと、直すときに漏れない</div>
<div class="pair top">
<div class="pair-side">
<b>分けていない</b>
<table class="dbt mini"><thead><tr><th>title</th><th>名前</th><th>メール</th></tr></thead><tbody><tr><td>牛乳を買う</td><td>佐藤</td><td>sato@…</td></tr><tr><td>資料を送る</td><td>佐藤</td><td>sato@…</td></tr></tbody></table>
<span>メールが変わると全部の行を直す</span>
</div>
<div class="pair-link">→</div>
<div class="pair-side on">
<b>分けた</b>
<table class="dbt mini"><thead><tr><th>users.id</th><th>名前</th><th>メール</th></tr></thead><tbody><tr><td>1</td><td>佐藤</td><td>sato@…</td></tr></tbody></table>
<table class="dbt mini"><thead><tr><th>todos.title</th><th>user_id</th></tr></thead><tbody><tr><td>牛乳を買う</td><td>1</td></tr><tr><td>資料を送る</td><td>1</td></tr></tbody></table>
</div>
</div>
<div class="rule">メールが変わっても、直すのはusersの1行だけ。漏れも食い違いも起きない</div>
</div>

<!--
[話すこと] この作業を正規化と呼ぶ。第1〜第3正規形といった細かい定義より、「同じ事実を2か所に書かない」を覚える。
読む速さのために、あえて重複させること（非正規化）もある
-->

---

# DBへの頼み方の言葉が、SQL

<div class="fig">
<div class="lead"><b>ひとことで</b>「どの表の、どの行を、どうしたいか」を英語に近い文で書く</div>
<div class="terminal-screen full">
<div class="terminal-bar">SQL</div>
<code class="dim">-- 取り出す: 終わっていないTodoを、持ち主の名前と一緒に</code>
<code>SELECT todos.title, users.name FROM todos</code>
<code class="output">  JOIN users ON users.id = todos.user_id WHERE todos.done = false;</code>
<code class="dim">-- 追加する</code>
<code class="output">INSERT INTO todos (user_id, title) VALUES (1, '請求書を出す');</code>
<code class="dim">-- 変える。WHERE（どの行か）を忘れると、全部の行が変わる</code>
<code class="output">UPDATE todos SET done = true WHERE id = 10;</code>
</div>
</div>

<!--
[話すこと] JOINは2つの表を番号でつないで1つの表のように読むこと。
プログラムからDBを扱う道具（ORM。Prisma、Drizzleなど）を使っても、裏で動くのはSQL。読めると調べ物が速い
-->

---

# トランザクションは、途中で失敗したら全部なかったことにする

<div class="fig">
<div class="lead ana"><b>たとえると</b>銀行振込。Aさんから引いたのにBさんに入らない、という状態を作らない</div>
<div class="vsteps">
<div><i>1</i><b>開始する<em>BEGIN</em></b><span>ここから先を、ひとまとまりとして扱う</span></div>
<div><i>2</i><b>Aから引く</b><span>Aさんの残高から1000円引く</span></div>
<div><i>3</i><b>Bに足す</b><span>Bさんの残高に1000円足す</span></div>
<div class="on"><i>4</i><b>成功なら確定<em>COMMIT</em></b><span>2と3を、まとめて確定する</span></div>
<div class="ng"><i>×</i><b>失敗なら取り消し<em>ROLLBACK</em></b><span>4の代わりに、2も3もなかったことにする</span></div>
</div>
<div class="chip-row">
<div><b>全部か無か</b><span>Atomicity</span></div>
<div><b>ルールを守る</b><span>Consistency</span></div>
<div><b>同時でも混ざらない</b><span>Isolation</span></div>
<div><b>確定したら残る</b><span>Durability</span></div>
</div>
</div>

<!--
[話すこと] 下の4つは、RDBが守る性質。頭文字でACIDと呼ぶ。「確定したら残る」は、確定した内容が障害の後も残るという意味。
お金や在庫のように「片方だけ成功」が許されないデータを扱うとき、RDBを選ぶ大きな理由になる
-->

---

# インデックスは、探すのを速くする索引

<div class="fig">
<div class="lead ana"><b>たとえると</b>本の索引。最初から全ページめくらず、索引から目的のページへ飛ぶ</div>
<div class="pair top">
<div class="pair-side">
<b>索引なし</b>
<span>「佐藤さんのTodo」を探すのに、全部の行を上から順に読む。データが増えるほど遅くなる</span>
</div>
<div class="pair-link">→</div>
<div class="pair-side on">
<b>索引あり</b>
<div class="mono">CREATE INDEX todos_user_id_idx<br>  ON todos (user_id);</div>
<span>索引をたどって、該当する行だけを読む</span>
</div>
</div>
<div class="rule">代わりに、データを書き込むたびに索引も書き直すので、書き込みは少し遅くなる</div>
</div>

<!--
[話すこと] だから、検索に使う列にだけ索引を作る。主キーには自動で作られる。
索引が効いているかは、EXPLAIN ANALYZEで確かめられる。実演2で見せる
-->

---

# データの形や量によっては、NoSQLも選ぶ

<div class="fig">
<div class="lead"><b>ひとことで</b>表の形にこだわらない代わりに、大量のデータや形のばらばらなデータに強い</div>
<div class="row c4">
<div class="card">
<div class="t">キーバリュー</div>
<div class="d">名前で値を引く。とても速い<br><br>例: Redis</div>
</div>
<div class="card">
<div class="t">ドキュメント</div>
<div class="d">JSONのような入れ子を丸ごとしまう<br><br>例: MongoDB、Firestore</div>
</div>
<div class="card">
<div class="t">ワイドカラム</div>
<div class="d">書き込みの多いログなどに強い<br><br>例: Cassandra</div>
</div>
<div class="card">
<div class="t">グラフ</div>
<div class="d">人と人のつながりをたどる<br><br>例: Neo4j</div>
</div>
</div>
<div class="rule">RDBの代わりではなく、用途を絞って一緒に使う</div>
</div>

<!--
[話すこと] NoSQLは「Not only SQL」の略。
多くは、表をまたいでつなぐ処理（JOIN）が苦手な代わりに、台数を増やして規模を広げやすい
-->

---

# 主なDBの名前を、まず知っておく

<div class="fig">
<div class="lead"><b>ひとことで</b>新しいWebサービスなら、まずPostgreSQLかMySQLの名前が挙がる</div>
<div class="tool-cols">
<div>
<div class="gl">RDB（表で持つ）</div>
<div class="tool-list">
<div><span class="ico i-postgresql"></span><b>PostgreSQL</b><span>機能が多い無料のDB</span></div>
<div><span class="ico i-mysql"></span><b>MySQL</b><span>Webで広く使われる無料のDB</span></div>
<div><span class="ico i-sqlite"></span><b>SQLite</b><span>ファイル1つで動く。スマホアプリの中など</span></div>
</div>
</div>
<div>
<div class="gl">NoSQL</div>
<div class="tool-list">
<div><span class="ico i-mongodb"></span><b>MongoDB</b><span>ドキュメント型の代表</span></div>
<div><span class="ico i-firebase"></span><b>Firestore</b><span>Googleのドキュメント型。画面へすぐ反映</span></div>
<div><span class="ico i-redis"></span><b>Redis</b><span>メモリ上で動く。一時的な保存に使う</span></div>
</div>
</div>
</div>
</div>

<!--
[話すこと] 企業の古いシステムではSQL ServerやOracle（有料のRDB）も多い。AWSにはDynamoDBというNoSQLがある。
FirestoreやDynamoDBは、そのクラウドの中でしか使えない（第4章のロックイン）
-->

---

# DBの管理は、プロに任せられる（マネージドDB）

<div class="fig">
<div class="lead"><b>ひとことで</b>お金を払って、DBの面倒を見る作業をクラウドの会社に任せる</div>
<div class="pair top">
<div class="pair-side">
<b>自分で面倒を見る</b>
<ul>
<li>サーバーにDBを入れて設定する</li>
<li>データのコピー（バックアップ）を取る</li>
<li>見つかった弱点を直す（更新）</li>
<li>止まったら夜中でも直す</li>
</ul>
</div>
<div class="pair-link">vs</div>
<div class="pair-side on">
<b>マネージドDB</b>
<span>左の作業の多くを代わりにやってくれる</span>
<div class="logos" style="margin-top:18px"><span class="ico ico-lg i-supabase"></span><span class="ico ico-lg i-neon"></span><span class="ico ico-lg i-googlecloud"></span></div>
<span>Supabase、Neon、Cloud SQL、RDS</span>
</div>
</div>
<div class="rule">少人数のチームや個人開発なら、マネージドを選ぶ</div>
</div>

<!--
[話すこと] SupabaseとNeonはPostgreSQLを無料枠から使える。RDS（AWS）とCloud SQL（Google Cloud）は大手クラウドのもの
-->

---

# DBは、「どんなデータか」と「誰が面倒を見るか」で選ぶ

<div class="fig">
<div class="lead"><b>ひとことで</b>上の2行でほぼ決まる。残りは迷ったときの決め手</div>
<div class="tblwrap">
<table class="compare full tight">
<colgroup><col style="width:22%"><col style="width:42%"><col style="width:36%"></colgroup>
<thead><tr><th>観点</th><th>自分に聞くこと</th><th>答えによる選び方</th></tr></thead>
<tbody>
<tr><th>データの形</th><td>表で書けるか。表同士のつながりが多いか</td><td>つながりが多いならRDB</td></tr>
<tr><th>正確さ</th><td>お金や在庫のように、ずれが許されないか</td><td>許されないならRDB</td></tr>
<tr><th>量と速さ</th><td>書き込みがとても多いか。急に増えるか</td><td>多いならNoSQLも検討</td></tr>
<tr><th>管理</th><td>止まったとき、誰が直すか</td><td>専任がいなければマネージド</td></tr>
<tr><th>情報の多さ</th><td>調べて答えが見つかるか。チームが慣れているか</td><td>PostgreSQLとMySQLは情報が多い</td></tr>
<tr><th>費用</th><td>無料枠はあるか。何に対してお金がかかるか</td><td>最初は無料枠のあるものから</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[話すこと] 「流行っているから」「速いと聞いたから」は観点に入れない
-->

---

# 迷ったらPostgreSQL

<div class="fig">
<div class="lead"><b>ひとことで</b>できることが多く、どこでも動き、あとで引っ越しやすい</div>
<div class="row c3">
<div class="card"><span class="ico ico-lg i-postgresql"></span><div class="t">できることが多い</div><div class="d">表のデータも、JSONのような入れ子のデータも扱える</div></div>
<div class="card"><span class="ico ico-lg i-postgresql"></span><div class="t">機能を足せる</div><div class="d">地図の検索、AIの検索（pgvector）などを後から足せる</div></div>
<div class="card on"><span class="ico ico-lg i-postgresql"></span><div class="t">引っ越しやすい</div><div class="d">Supabase、Neon、AWS、Google Cloudのどこでも動く</div></div>
</div>
<div class="rule">スマホの中に保存するならSQLite、一時的な保存ならRedisを一緒に使う</div>
</div>

<!--
[話すこと] SupabaseもPostgreSQLなので、ここまでのSQLと索引の話がそのまま使える。
[実演2] ここでSupabaseを開き、Table Editorでtodosの表、SQL EditorでSELECTとEXPLAIN ANALYZE（索引の有無）を見せる。2分
-->

---

<!-- _class: chapter -->
<!-- header: '4. クラウド' -->

<div class="n">CHAPTER 4</div>

# クラウド

サーバーを買わずに、借りて使う

---

# クラウドは、コンピュータを買わずに借りて使うこと

<div class="fig">
<div class="lead ana"><b>たとえると</b>自家発電と電力会社。発電機を買わずに、使った分だけ電気代を払う</div>
<div class="tblwrap">
<table class="compare full">
<colgroup><col style="width:18%"><col style="width:41%"><col style="width:41%"></colgroup>
<thead><tr><th>観点</th><th>オンプレミス（自分で機械を持つ）</th><th>クラウド（借りる）</th></tr></thead>
<tbody>
<tr><th>始めるお金</th><td>機械と置き場所を先に買う</td><td>ほぼ不要。使った分を後から払う</td></tr>
<tr><th>準備の時間</th><td>注文から設置まで数週間以上</td><td>画面から数分</td></tr>
<tr><th>増やす・減らす</th><td>機械を買い足す、捨てる</td><td>設定を変えるだけ</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[話すこと] 負荷が一定で長く使うなら、自分で持つほうが総額は安いこともある。
クラウドの価値は安さより、すぐ始められて、伸び縮みできること
-->

---

# どこまで任せるかで、IaaS、PaaS、SaaSに分かれる

<div class="fig">
<div class="lead"><b>ひとことで</b>右へ行くほど任せる範囲が広く楽になるが、自由は減る</div>
<div class="stack">
<div></div><div class="h">オンプレ</div><div class="h">IaaS</div><div class="h">PaaS</div><div class="h">SaaS</div>
<div class="lb">アプリ</div><div class="u">自分</div><div class="u">自分</div><div class="u">自分</div><div class="p">会社</div>
<div class="lb">データ</div><div class="u">自分</div><div class="u">自分</div><div class="u">自分</div><div class="u">自分</div>
<div class="lb">OSなど</div><div class="u">自分</div><div class="u">自分</div><div class="p">会社</div><div class="p">会社</div>
<div class="lb">機械・建物</div><div class="u">自分</div><div class="p">会社</div><div class="p">会社</div><div class="p">会社</div>
<div></div><div class="ex">自社のサーバー</div><div class="ex">AWSのEC2<br>（仮想のサーバー）</div><div class="ex">Vercel、Render<br>（コードを置くだけ）</div><div class="ex">Gmail、Slack<br>（使うだけ）</div>
</div>
<p class="cap">Supabaseのように、ログインやDBを丸ごと借りるものはBaaSと呼ぶ</p>
</div>

<!--
[話すこと] IaaSは「場所と機械」、PaaSは「動かす環境」、SaaSは「完成したアプリ」を借りる。
OSはWindowsやLinuxのような土台のソフト。IaaSではOSの更新も自分の仕事。
SaaSでも、データとアカウントの管理は自分の責任（次のページ）
-->

---

# 設定とデータは、どのサービスでも自分で守る

<div class="fig">
<div class="lead ana"><b>たとえると</b>マンション。建物の警備は管理会社、部屋の鍵をかけるのは住人</div>
<div class="pair">
<div class="pair-side">
<b>クラウドの会社</b>
<ul>
<li>データセンター</li>
<li>機械</li>
<li>ネットワーク</li>
</ul>
</div>
<div class="pair-link">＋</div>
<div class="pair-side on">
<b>使う人（自分）</b>
<ul>
<li>アカウントと権限</li>
<li>公開する範囲の設定</li>
<li>データと自分のコード</li>
</ul>
</div>
</div>
<div class="rule">ファイルの置き場を「誰でも見られる」に設定して漏れたら、責任は自分にある</div>
</div>

<!--
[Sources]
- https://aws.amazon.com/compliance/shared-responsibility-model/
[話すこと] これを責任共有モデルと呼ぶ。クラウドの情報漏えいの多くは、会社側への攻撃ではなく使う側の設定ミスで起きる
-->

---

# 小さく始めるなら、手軽なサービスで十分

<div class="fig">
<div class="lead"><b>ひとことで</b>個人開発や試作はここから。AWSなどの大手は必要になってから</div>
<div class="tool-list one">
<div><span class="ico i-vercel"></span><b>Vercel</b><span>画面のサイトを公開する。GitHubに上げると自動で公開される。無料プランは個人の非商用だけ</span></div>
<div><span class="ico i-render"></span><b>Render</b><span>サーバーのプログラムや定期実行を動かす</span></div>
<div><span class="ico i-cloudflare"></span><b>Cloudflare</b><span>世界中の拠点からサイトを速く配る。ドメインの管理も</span></div>
<div><span class="ico i-supabase"></span><b>Supabase</b><span>PostgreSQLに、ログイン機能とファイル置き場が付いたもの</span></div>
<div><span class="ico i-firebase"></span><b>Firebase</b><span>Google製。DB、ログイン、公開、通知がそろう</span></div>
</div>
</div>

<!--
[Sources]
- https://vercel.com/docs/plans/hobby （Hobbyは非商用の個人利用に限る。2026-10-20確認）
[話すこと] 仕事の案件をVercelの無料プランで公開してはいけない。有料のProにする。
大手3社は同じ役割のサービスを別の名前で持っている（例: 仮想サーバーはEC2、Compute Engine、Virtual Machines）。1つで考え方を覚えれば他も読める
-->

---

# クラウドは、「何を動かすか」と「どこまで自分で触るか」で選ぶ

<div class="fig">
<div class="lead"><b>ひとことで</b>DBの選び方と同じく、上の2行でほぼ決まる</div>
<div class="tblwrap">
<table class="compare full tight">
<colgroup><col style="width:22%"><col style="width:42%"><col style="width:36%"></colgroup>
<thead><tr><th>観点</th><th>自分に聞くこと</th><th>答えによる選び方</th></tr></thead>
<tbody>
<tr><th>動かすもの</th><td>画面のサイトか、ずっと動くプログラムか</td><td>画面ならVercel、常に動くならRender</td></tr>
<tr><th>触る範囲</th><td>OSまで自分で設定する必要があるか</td><td>なければPaaS、あればIaaS</td></tr>
<tr><th>費用</th><td>月額固定か、使った分だけか</td><td>使う人が少ないうちは使った分だけが安い</td></tr>
<tr><th>引っ越し</th><td>その会社だけの機能にどこまで頼るか</td><td>共通の技術なら移りやすい</td></tr>
<tr><th>場所</th><td>データを日本に置く必要があるか</td><td>東京・大阪の拠点があるか確かめる</td></tr>
<tr><th>チーム</th><td>会社の決まり、チームの経験</td><td>迷ったら、チームが扱える方</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[話すこと] その会社だけの機能に深く頼り、引っ越せなくなることをロックインと呼ぶ
-->

---

# 最初から大きく作らず、育ったら引っ越せる形にしておく

<div class="fig">
<div class="lead"><b>ひとことで</b>最初は手軽なサービス、利用者が増えたら大手クラウドへ</div>
<div class="stages">
<div>
<div class="lbl">小さいうち<small>試作、社内ツール</small></div>
<div class="flow sm">
<div class="step"><span class="ico i-vercel"></span>Vercel<small>画面とAPI</small></div>
<div class="arw">→</div>
<div class="step"><span class="ico i-supabase"></span>Supabase<small>DB、ログイン、ファイル</small></div>
</div>
</div>
<div>
<div class="lbl">育ったあと<small>利用者と機能が増えた</small></div>
<div class="flow sm">
<div class="step">配信<small>CloudFront</small></div>
<div class="arw">→</div>
<div class="step">プログラム<small>ECS</small></div>
<div class="arw">→</div>
<div class="step">DB<small>RDS（PostgreSQL）</small></div>
<div class="arw">＋</div>
<div class="step">ファイル<small>S3</small></div>
</div>
</div>
</div>
<div class="rule">共通の技術（PostgreSQLなど）で作っておくと、引っ越しの手間を小さくできる</div>
</div>

<!--
[話すこと] 育ったあとの例はAWSで書いた。Google CloudならCloud RunとCloud SQL。
引っ越すのは、費用、性能、細かい権限の設定、会社のルールのどれかが理由になるとき
-->

---

# 使った分だけ払う仕組みは、使いすぎると請求が膨らむ

<div class="fig">
<div class="lead"><b>ひとことで</b>アカウントを作ったら、最初に「予算を超えたら知らせる」設定をする</div>
<div class="pair top">
<div class="pair-side">
<b>起きること</b>
<ul>
<li>プログラムの誤りで、処理が止まらず呼ばれ続ける</li>
<li>漏れたキーで、他人に勝手に使われる</li>
<li>試しに作ったサーバーの消し忘れ</li>
</ul>
</div>
<div class="pair-link">→</div>
<div class="pair-side on">
<b>防ぎ方</b>
<ul>
<li>予算アラートを設定する</li>
<li>上限を決められるサービスは上限を決める</li>
<li>作ったものをコードで管理し、使い終わったら消す（IaC）</li>
</ul>
</div>
</div>
<div class="rule">多くの予算アラートは知らせるだけで、課金は止まらない</div>
</div>

<!--
[話すこと] IaCはInfrastructure as Code。サーバーなどの構成をコードに書いて作る方法（Terraformなど）。画面で手作業で作ると、何を作ったか誰も分からなくなる
-->

---

<!-- _class: chapter -->
<!-- header: '5. セキュリティ' -->

<div class="n">CHAPTER 5</div>

# セキュリティ

誰に、何を許すか

---

# 「誰か」を確かめるのが認証、「何をしてよいか」を決めるのが認可

<div class="fig">
<div class="lead ana"><b>たとえると</b>会社の入口で身分証を見せる（認証）。入館証で入れる部屋が決まる（認可）</div>
<div class="pair">
<div class="pair-side">
<b>認証</b>
<ul>
<li>パスワード</li>
<li>スマホでの確認</li>
<li>Googleでログイン</li>
</ul>
<span class="code-note">失敗したら401（ログインしていない）</span>
</div>
<div class="pair-link">→</div>
<div class="pair-side on">
<b>認可</b>
<ul>
<li>管理者だけ削除できる</li>
<li>自分のTodoだけ見える</li>
</ul>
<span class="code-note">失敗したら403（権限がない）</span>
</div>
</div>
<div class="rule">ログインできた人が、何でもできるわけではない。操作ごとに権限を確かめる</div>
</div>

<!--
[話すこと] 英語ではAuthentication（認証）とAuthorization（認可）。
URLの数字を変えたら他人のデータが見えた、は認可の確かめ漏れ。Webの弱点の1位（OWASP Top 10:2025のA01）。
ログインの状態を持つ方法には、セッション（サーバーがメモを持つ）とJWT（署名付きの札を渡す）がある
-->

---

# パスワードはハッシュで保存し、APIキーはコードに書かない

<div class="fig">
<div class="lead"><b>ひとことで</b>APIキーは家の鍵と同じ。GitHubやSlackに貼らない</div>
<div class="scene-grid">
<div class="terminal-screen full">
<div class="terminal-bar">ターミナル</div>
<code><span class="prompt">$</span> cat .gitignore</code>
<code class="output">.env.local</code>
<code><span class="prompt">$</span> git log --oneline -- .env.local</code>
<code class="output">a1b2c3d 設定ファイルを追加</code>
<code class="dim">↑ 一度コミットすると、消しても履歴に残る</code>
</div>
<div class="numbered sm">
<div><b>パスワード</b><span>ハッシュという、元に戻せない形に変えて保存する</span></div>
<div><b>秘密の文字列</b><span>APIキーは.env.localに書き、Gitに入れない</span></div>
<div><b>漏れたら</b><span>消すより先に、そのキーを無効にして作り直す</span></div>
</div>
</div>
</div>

<!--
[話すこと] ハッシュにはbcryptやArgon2を使う。公開リポジトリに上がったキーは、すぐに自動で集められると考える。
.gitignoreに書くのは、最初のコミットより前。後から書いても、すでに記録したファイルは除外されない
-->

---

# 利用者が入力したものは、そのまま信じない

<div class="fig">
<div class="lead"><b>ひとことで</b>入力欄に「命令」を書かれても、命令として実行しない</div>
<div class="tblwrap">
<table class="compare full">
<colgroup><col style="width:25%"><col style="width:37.5%"><col style="width:37.5%"></colgroup>
<thead><tr><th>攻撃</th><th>何が起きるか</th><th>防ぎ方</th></tr></thead>
<tbody>
<tr><th>SQLインジェクション</th><td>入力した文字がSQLとして動き、データを盗まれる、消される</td><td>入力をSQLの文に直接つなげない（プレースホルダー）</td></tr>
<tr><th>XSS</th><td>入力したプログラムが、他の人のブラウザで動く</td><td>表示時に無害な文字へ変える（文字の表示はReactが自動）</td></tr>
<tr><th>CSRF</th><td>ログイン中の人に、別のサイトから勝手な操作をさせる</td><td>操作ごとの合言葉（CSRFトークン）、Cookieの設定</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[Sources]
- https://top10.owasp.org/2025
- https://top10.owasp.org/2025/A05_2025-Injection/
- https://top10.owasp.org/2025/A01_2025-Broken_Access_Control/
[話すこと] OWASP Top 10:2025では、SQLインジェクションとXSSはA05 Injection、CSRFはA01 Broken Access Controlに含まれる。
ReactでdangerouslySetInnerHTMLを使うと自動の変換が外れる。名前の通り危ない
-->

---

# 権限は必要な分だけ渡し、他人が作った部品も疑う

<div class="fig">
<div class="lead"><b>ひとことで</b>鍵は必要な部屋の分だけ。持ち込む部品は中身を確かめる</div>
<div class="pair top">
<div class="pair-side">
<b>権限は最小に</b>
<span>Supabaseは、行ごとに「誰が読めるか」を決められる（RLS）</span>
<div class="mono">alter table todos<br>  enable row level security;<br>create policy "own todos" on todos<br>  for select using (<br>    (select auth.uid()) = user_id<br>  );</div>
</div>
<div class="pair-link">＋</div>
<div class="pair-side on">
<b>部品（パッケージ）を疑う</b>
<span>npmなどで入れる部品に、悪意あるコードが混ざる攻撃がある</span>
<ul>
<li>使う版を固定する（lockfile）</li>
<li>必要のない部品を入れない</li>
<li>名前の似た偽物に注意する</li>
</ul>
</div>
</div>
</div>

<!--
[Sources]
- https://supabase.com/docs/guides/database/postgres/row-level-security
- https://top10.owasp.org/2025 （A03 Software Supply Chain Failures）
[話すこと] RLSの例は「自分のTodoだけ読める」というルール。user_idには、Supabaseのログイン利用者のID（uuid型）が入る。
SupabaseはブラウザからDBへ直接アクセスできるので、公開スキーマ（public）の表でRLSを無効にすると、APIキーだけで読める状態になりうる。
部品を狙う攻撃を供給網攻撃と呼ぶ。Webの弱点の3位（A03）
-->

---

<!-- header: 'まとめ' -->

# 今日のまとめ

<div class="fig">
<div class="vsteps narrow">
<div><i>1</i><b>開発プロセス</b><span>全部決められるならウォーターフォール、作りながらならアジャイル</span></div>
<div><i>2</i><b>Webの仕組み</b><span>画面、処理、データの3つに分かれ、HTTPで頼んで返す</span></div>
<div><i>3</i><b>DB</b><span>表で持ち、失敗したら全部取り消す。迷ったらPostgreSQL</span></div>
<div><i>4</i><b>クラウド</b><span>どこまで任せるかで選び、最初に予算アラートを設定する</span></div>
<div><i>5</i><b>セキュリティ</b><span>認証と認可を分け、入力を信じず、権限は最小にする</span></div>
</div>
</div>
