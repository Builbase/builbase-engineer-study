---
marp: true
theme: deck
paginate: false
size: 16:9
title: パーソナルエージェントとAI組織：Muse、dots、Duet、Grok Botの設計と使い分け
description: builbaseエンジニア勉強会 第4回（60分）
author: seiji
style: |
  /* 第3回の部品をそのまま引き継ぐ（第4回の部品は末尾）。共通テーマ theme/deck.css の変数と寸法に合わせる */
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
  /* 考えてみよう（各章の最後の問い）。答えはコメントの[答え] */
  .lead.q { border-left-color: #b45309; background: #fdf6ec; }
  .lead.q b { color: #b45309; }
  .stack .h { flex-direction: column; line-height: 1.3; }
  .stack + .cap { margin-top: 20px; }
  .stack .h small { font-size: 14px; font-weight: 400; color: var(--gray-700); }
  .card .opt { align-self: center; display: flex; align-items: center; justify-content: center; width: 52px; height: 52px; border-radius: 50%; background: var(--navy); color: #fff; font-size: 26px; font-weight: 700; }
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
  /* ===== 第4回だけで使う部品 ===== */
  /* 発表の年表。1社1行で、日付、アイコン、名前、会社、ひとことを横に並べる */
  .tl { display: grid; grid-auto-rows: 1fr; align-content: stretch; }
  .fig > .tl { flex: 1 1 auto; min-height: 0; }
  .tl > div { display: grid; grid-template-columns: 120px 60px 160px 250px minmax(0,1fr); align-items: center; gap: 20px; border-top: 1px solid var(--gray-200); padding: 0 8px; }
  .tl > div:last-child { border-bottom: 1px solid var(--gray-200); }
  .tl .d { font-size: 22px; font-weight: 700; color: var(--navy); }
  .tl .ico { width: 56px; height: 56px; margin: 0; border-radius: 13px; box-shadow: 0 0 0 1px var(--gray-200); }
  .tl b { font-size: 27px; white-space: nowrap; }
  .tl .co { font-size: 19px; color: var(--gray-536); white-space: nowrap; }
  .tl .ds { font-size: 22px; color: var(--ink); white-space: nowrap; }
  /* 製品の紹介。左にアイコンと名前、右に項目の一覧 */
  .profile { display: grid; grid-template-columns: 230px 1fr; gap: 44px; align-items: center; }
  .fig > .profile { flex: 1 1 auto; min-height: 0; }
  .pf-head { display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center; }
  .pf-head .ico { width: 150px; height: 150px; margin: 0 0 8px; border-radius: 34px; box-shadow: 0 0 0 1px var(--gray-200); }
  .pf-head b { font-size: 34px; line-height: 1.2; }
  .pf-head span { font-size: 19px; color: var(--gray-536); line-height: 1.4; white-space: nowrap; }
  .pf-head b + span { margin-top: 4px; }
  .pf-head span + span { margin-top: -8px; }
  .pf { display: grid; grid-auto-rows: 1fr; margin: 0; align-self: stretch; }
  .pf > div { display: grid; grid-template-columns: 150px 1fr; align-items: center; gap: 22px; border-top: 1px solid var(--gray-200); }
  .pf > div:last-child { border-bottom: 1px solid var(--gray-200); }
  .pf dt { font-size: 20px; font-weight: 700; font-style: normal; color: var(--navy); }
  .pf dd { margin: 0; font-size: 21px; line-height: 1.45; color: var(--ink); }
  .pf dd small { font-size: 17px; color: var(--gray-536); }
  /* 比較表の見出しにアイコンを置く */
  .compare thead th .ico { width: 30px; height: 30px; border-radius: 7px; vertical-align: -9px; margin-right: 8px; box-shadow: 0 0 0 1px var(--gray-200); }
  .compare.prod thead th { font-size: 19px; color: var(--ink); }
  .compare.prod td { font-size: 19px; color: var(--ink); }
  .compare.prod tbody th { font-size: 20px; color: var(--navy); }
  .compare.prod th, .compare.prod td { padding: 14px 14px; }
  /* 4象限の地図。横軸は用事の種類、縦軸は誰のために動くか。文字はすべて横書きで1行に収める */
  .quad { display: grid; grid-template-columns: 96px 1fr 1fr; grid-template-rows: minmax(0,1fr) minmax(0,1fr) 36px; gap: 10px; }
  .fig > .quad { flex: 1 1 auto; min-height: 0; }
  .quad .cell { border: 1px solid var(--gray-200); border-radius: 12px; background: var(--gray-50); display: flex; flex-direction: column; justify-content: center; align-items: flex-start; gap: 18px; padding: 12px 40px; }
  .quad .cell.empty { background: #ffffff; border-style: dashed; color: var(--gray-536); font-size: 19px; align-items: center; }
  .quad .p { display: flex; flex-direction: row; align-items: center; gap: 18px; }
  .quad .p .ico { width: 68px; height: 68px; margin: 0; border-radius: 13px; box-shadow: 0 0 0 1px var(--gray-200); flex: none; }
  .quad .p b { display: block; font-size: 27px; line-height: 1.3; white-space: nowrap; }
  .quad .p span { display: block; font-size: 20px; color: var(--gray-700); line-height: 1.4; white-space: nowrap; }
  .quad .ax { display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 700; color: var(--gray-700); white-space: nowrap; }
  /* 3者の比較で、列見出しに人型やアイコンを置く */
  .who { display: inline-flex; align-items: center; gap: 10px; }
  .who .ai .glyph { width: 34px; height: 34px; }
  .who .ai { gap: 0; }
  /* ツール一覧の行の中に、ロゴを2つ並べる */
  .tool-list .dual { display: flex; gap: 6px; }
  .tool-list .dual { gap: 10px; }
  .tool-list .dual .ico { width: 42px; height: 42px; }
  .tool-list.wide > div { grid-template-columns: 110px 380px 1fr; }
  /* 連携できるアプリの数。アイコン、名前、数、補足を1行に並べる */
  .tool-list.cnt > div { grid-template-columns: 44px 150px 260px 1fr; }
  .tool-list .n { font-size: 30px; font-weight: 700; color: var(--navy); white-space: nowrap; }
  .tool-list .n small { font-size: 18px; font-weight: 400; color: var(--gray-536); margin-left: 4px; }
  .compare thead th .ico.pair2 { margin-right: 2px; }
  .tool-list .ico.app { border-radius: 8px; box-shadow: 0 0 0 1px var(--gray-200); }
  /* 言葉の地図。起動の主体（行）と対象の範囲（列） */
  .map { display: grid; grid-template-columns: 150px minmax(0,1fr) minmax(0,1fr); grid-template-rows: 44px minmax(0,1fr) minmax(0,1fr); gap: 10px; }
  .fig > .map { flex: 1 1 auto; min-height: 0; }
  .map .h { display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 700; color: var(--gray-700); white-space: nowrap; }
  .map .c { border: 1px solid var(--gray-200); border-radius: 12px; background: var(--gray-50); display: flex; flex-direction: column; justify-content: center; padding: 14px 28px; gap: 6px; }
  .map .c.on { border-color: var(--blue); background: var(--blue-50); }
  .map .c b { font-size: 27px; white-space: nowrap; }
  .map .c.on b { color: var(--navy); }
  .map .c span { font-size: 19px; color: var(--gray-700); }
---

<!-- _class: title -->

# エンジニア勉強会

<p>
第4回 パーソナルエージェントとAI組織：Muse、dots、Duet、Grok Botの設計と使い分け<br>
2026-11-11
</p>

---

<!-- header: 'はじめに' -->

# 今日の内容

<div class="fig">
<div class="lead"><b>要点</b>2026年8〜10月に出た常駐型エージェント4製品を比べ、自前のAI社員・AI組織と使い分ける</div>
<div class="vsteps">
<div><i>1</i><b>パーソナルエージェント</b><span>普通のAIエージェントとの違い。実行環境、起動、承認</span></div>
<div><i>2</i><b>4製品の比較</b><span>モデル、チャネル、連携数、提供地域、料金</span></div>
<div><i>3</i><b>AI社員とAI組織の作り方</b><span>単一エージェント、ワークフロー、マルチエージェント</span></div>
<div><i>4</i><b>使い分け</b><span>契約するか、自前で組むか</span></div>
</div>
<p class="cap">製品の情報は2026-11-10時点。料金や提供地域は変わりやすいので、使う前に公式ページで確かめる</p>
</div>

<!--
[話すこと] 第2回で扱ったエージェントの仕組み（モデル、ツール、ループ、ハーネス）を前提にする。
今日はその上に乗った完成品と、会社が自前で組んできた構成の比較
-->

---

<!-- _class: chapter -->
<!-- header: '1. パーソナルエージェントの設計' -->

<div class="n">CHAPTER 1</div>

# パーソナルエージェントの設計

頼まれて動くエージェントから、常駐して先回りするエージェントへ

---

# 3か月で、大手4社が常駐型のエージェントを出した

<div class="fig">
<div class="lead"><b>要点</b>どれもクラウド上の専用環境に常駐して先回りし、取り消せない操作の前で承認を待つ</div>
<div class="tl">
<div><span class="d">8月11日</span><span class="ico i-grokbot"></span><b>Grok Bot</b><span class="co">xAI</span><span class="ds">チームに複数置くエージェント</span></div>
<div><span class="d">9月8日</span><span class="ico i-muse"></span><b>Muse</b><span class="co">Meta</span><span class="ds">一般向け。生活の用事の代行</span></div>
<div><span class="d">9月29日</span><span class="ico i-chatgpt"></span><b>dots</b><span class="co">OpenAI（ChatGPT内）</span><span class="ds">目標を持たせて常時進める</span></div>
<div><span class="d">10月21日</span><span class="ico i-duet"></span><b>Duet</b><span class="co">Anthropic</span><span class="ds">業務アプリの監視（米国のみ）</span></div>
</div>
<div class="rule">総称として「パーソナルエージェント」と呼ばれている</div>
</div>

<!--
[Sources]
- https://x.ai/news/introducing-grok-bot （Grok Bot。2026-08-11、ベータ）
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ （Muse。2026-09-08）
- https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/ （dots。2026-09-29のDevDay）
- https://claude.com/resources/articles/claude-duet （Claude Duet。2026-10-21、研究プレビュー）
- アイコンは各社のApp Storeの公式アプリアイコン。dotsは単独のアプリが無いのでChatGPTのアイコン
[話すこと] Duetの正式名はClaude Duet。dotsは小文字が正式。
-->

---

# 言葉は、起動の仕方と仕える相手で整理できる

<div class="fig">
<div class="lead"><b>要点</b>指示やトリガーで動くか、常駐して先回りするか。個人に仕えるか、組織の業務に仕えるか</div>
<div class="map">
<div></div><div class="h">個人</div><div class="h">組織の業務</div>
<div class="h">指示で起動</div>
<div class="c"><b>AIエージェント</b><span>Claude Code、Codex</span></div>
<div class="c"><b>AI社員、AI組織</b><span>ワークフロー、マルチエージェントを自前で組む</span></div>
<div class="h">常駐、先回り</div>
<div class="c on"><b>パーソナルエージェント</b><span>Muse、Duet、dots</span></div>
<div class="c"><b>チーム型の常駐エージェント</b><span>Grok Bot、会社向けの専門dots（試験中）</span></div>
</div>
<p class="cap">下の段の2つが、今日の4製品（パーソナルエージェント）。右下はAI社員の役割に入ってきた領域で、第4章で扱う</p>
</div>

<!--
[話すこと] 今日の話はこの1枚の上で進める。第1章と第2章が左下、第3章が右上、第4章で右下と全体に戻る。
AI社員とAI組織は業界の正式な用語ではなく、業務に配属するAIの呼び名
-->

---

# 普通のAIエージェントとの違いは、起動と寿命にある

<div class="fig">
<div class="lead"><b>要点</b>先回りは4製品に共通する前提。違いは起動の主体と、動き続ける長さ</div>
<div class="tblwrap">
<table class="compare full prod">
<colgroup><col style="width:18%"><col style="width:41%"><col style="width:41%"></colgroup>
<thead><tr><th></th><th><span class="ico i-claude pair2"></span><span class="ico i-codex"></span>AIエージェント<br><small>Claude Code、Codexなど</small></th><th>パーソナルエージェント<br><small>Muse、dots、Duet、Grok Bot</small></th></tr></thead>
<tbody>
<tr class="on"><th>起動</th><td>プロンプト、またはスケジュール</td><td>受信やイベントを見て、自分で起動</td></tr>
<tr><th>寿命</th><td>タスクの単位。終われば止まる</td><td>常駐し、目標と記憶を持ち続ける</td></tr>
<tr><th>実行環境</th><td>手元のPC、または一時的なサンドボックス</td><td>利用者ごとのクラウド環境（常駐）</td></tr>
<tr><th>権限</th><td>リポジトリとターミナル</td><td>メール、カレンダー、決済などのOAuth</td></tr>
<tr><th>出力</th><td>差分、PR、ターミナルへの出力</td><td>通知、毎朝の要約、承認の依頼</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[Sources]
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ （"proactively helps with people's goals and suggests ideas" / "it can make suggestions unprompted"）
- https://www.aljazeera.com/economy/2026/9/30/openai-launches-dots-personal-ai-assistant-built-to-handle-everything （"sometimes before you even think to ask"）
- https://claude.com/resources/articles/claude-duet （"Claude Duet comes to you first"）
- https://x.ai/news/introducing-grok-bot （"Over time they become more proactive, picking up work before you need to ask"）
[話すこと] Claude CodeやCodexにも、定期実行や長時間のタスクはある。それでも、何をやるかは人が決めて渡す。
パーソナルエージェントは、受信箱や予定を見て、やることを自分で見つける。
Grok Botは、使ううちに先回りが増えると説明している
-->

---

# 各社の発表から共通部分を抜き出すと、こういう構成になる

<div class="fig">
<div class="lead"><b>要点</b>利用者ごとのクラウド環境で、ループ、記憶、スケジューラが動き、外への操作は承認を通る</div>
<div class="svgfig">
<svg width="1152" height="380" viewBox="0 0 1152 380" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="ah2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#666666"/></marker></defs>
<rect x="6" y="150" width="128" height="64" rx="10" fill="#ffffff" stroke="#949494" stroke-width="2"/>
<text x="70" y="189" text-anchor="middle" class="b">利用者</text>
<line x1="136" y1="172" x2="186" y2="172" stroke="#666666" stroke-width="3" marker-end="url(#ah2)"/>
<line x1="186" y1="194" x2="138" y2="194" stroke="#666666" stroke-width="3" marker-end="url(#ah2)"/>
<rect x="190" y="132" width="180" height="100" rx="10" fill="#ffffff" stroke="#949494" stroke-width="2"/>
<text x="280" y="172" text-anchor="middle" class="b">チャネル</text>
<text x="280" y="198" text-anchor="middle" class="s">アプリ、Slack</text>
<text x="280" y="220" text-anchor="middle" class="s">WhatsApp</text>
<line x1="372" y1="182" x2="412" y2="182" stroke="#666666" stroke-width="3" marker-end="url(#ah2)"/>
<rect x="416" y="6" width="438" height="368" rx="14" fill="#f2f2f2" stroke="#cccccc" stroke-width="2"/>
<text x="635" y="36" text-anchor="middle" class="b">利用者ごとのクラウド環境（常駐）</text>
<rect x="440" y="54" width="390" height="76" rx="10" fill="#000071"/>
<text x="635" y="88" text-anchor="middle" class="b w">エージェントループ</text>
<text x="635" y="114" text-anchor="middle" class="s w">モデル、ツール呼び出し、計画</text>
<rect x="440" y="146" width="185" height="76" rx="10" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="532" y="180" text-anchor="middle" class="b navy">長期の記憶</text>
<text x="532" y="206" text-anchor="middle" class="s">好み、目標、経緯</text>
<rect x="645" y="146" width="185" height="76" rx="10" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="737" y="180" text-anchor="middle" class="b navy">スケジューラ</text>
<text x="737" y="206" text-anchor="middle" class="s">定期の見回り</text>
<rect x="440" y="238" width="390" height="112" rx="10" fill="#fdeeee" stroke="#ec0000" stroke-width="2"/>
<text x="635" y="276" text-anchor="middle" class="b">承認ゲート</text>
<text x="635" y="304" text-anchor="middle" class="s">読み取り、下書きは自動</text>
<text x="635" y="330" text-anchor="middle" class="s">送信、支払い、削除は既定で人が許可</text>
<line x1="832" y1="270" x2="884" y2="190" stroke="#666666" stroke-width="3" marker-end="url(#ah2)"/>
<line x1="832" y1="306" x2="884" y2="306" stroke="#666666" stroke-width="3" marker-end="url(#ah2)"/>
<rect x="888" y="140" width="258" height="96" rx="10" fill="#ffffff" stroke="#949494" stroke-width="2"/>
<text x="1017" y="180" text-anchor="middle" class="b">コネクタ</text>
<text x="1017" y="208" text-anchor="middle" class="s">OAuth、MCP</text>
<rect x="888" y="258" width="258" height="96" rx="10" fill="#ffffff" stroke="#949494" stroke-width="2"/>
<text x="1017" y="298" text-anchor="middle" class="b">ブラウザ操作</text>
<text x="1017" y="326" text-anchor="middle" class="s">連携の無いサイト</text>
<text x="1017" y="110" text-anchor="middle" class="s">外部サービスへ</text>
</svg>
</div>
</div>

<!--
[Sources]
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ （Muse Secure VM。"a dedicated secure computer with its own browser"。Sentinelが外向きの通信を検査）
- https://www.macrumors.com/2026/10/21/anthropic-claude-duet/ （Duetは専用のVMとブラウザ。数時間ごとに確認）
- https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/ （dotsは専用のクラウドPCとブラウザ）
- https://x.ai/news/introducing-grok-bot （"including platforms with no clean API or MCP"）
[話すこと] 各社の発表から共通部分を抜き出した図で、どこか1社の公式の構成図ではない。
MuseとDuetは、パスワードやトークンをエージェントに見せない設計だと明言している。
Grok Botは構成の詳細を公表していない（専用のコンピュータを持つことまで）。MuseとDuetはVMと明言している。
dotsは操作ごとに許可、承認、禁止の規則を設定できるので、承認の範囲は利用者が変えられる
-->

---

# 承認の境界は、取り消せるかどうかで引かれている

<div class="fig">
<div class="lead"><b>要点</b>読み取りと下書きは自動で進め、外部に副作用が出る操作の前で止める</div>
<div class="pair top">
<div class="pair-side">
<b>自動で進める</b>
<ul>
<li>メールやカレンダーの読み取り</li>
<li>調査、比較</li>
<li>返信や資料の下書き</li>
</ul>
</div>
<div class="pair-link">→</div>
<div class="pair-side on">
<b>承認を待つ</b>
<ul>
<li>メッセージの送信</li>
<li>支払い、購入</li>
<li>書類への署名</li>
<li>ファイルの削除</li>
</ul>
</div>
</div>
<div class="rule">Duetは、証券の売買と口座間の送金を、承認があっても実行しない</div>
</div>

<!--
[Sources]
- https://claude.com/resources/articles/claude-duet （送信、支払い、署名、削除の前に承認を待つ。証券の売買と口座間の送金はブロック）
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ （メールの送信や購入の前に確認。Sentinelが許可したものだけが外へ出る）
[話すこと] 右の4つはDuetの公式の一覧。止まる範囲は製品ごとに違う。
Duetは、メッセージごとに専用の分類器と安全用のシステムプロンプトで検査している（MacRumors）。
dotsは、操作ごとに許可、承認が必要、禁止のルールを利用者が決められると報じられている
-->

---

<!-- _class: chapter -->
<!-- header: '2. 4製品の比較' -->

<div class="n">CHAPTER 2</div>

# 4製品の比較

モデル、チャネル、連携数、提供地域、料金

---

# Museは、一般向けに生活の用事を代行する

<div class="fig">
<div class="lead"><b>要点</b>日本で使え、4製品で唯一の無料枠がある。外向きの通信は別のエージェントが検査する</div>
<div class="profile">
<div class="pf-head"><span class="ico i-muse"></span><b>Muse</b><span>Meta</span><span>2026-09-08</span></div>
<dl class="pf">
<div><dt>主な用途</dt><dd>メール送信、旅行の予約、購入、請求の見直し</dd></div>
<div><dt>モデル</dt><dd>Muse Spark</dd></div>
<div><dt>チャネル</dt><dd>iOS、Android、Web（muse.ai）<br><small>米国ではWhatsAppからも使える</small></dd></div>
<div><dt>提供と料金</dt><dd>日本は10月23日から。無料（週の上限あり）<br><small>有料はパワー月2,799円、マキシマム月13,990円</small></dd></div>
<div><dt>安全設計</dt><dd>Sentinelが許可した通信だけが外へ出る</dd></div>
</dl>
</div>
</div>

<!--
[Sources]
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ （Muse Spark、Muse Secure VM、Sentinel、学習のオプトアウト）
- https://pc.watch.impress.co.jp/docs/news/2150743.html （日本は2026-10-23から。パワー月2,799円で毎週5億Museトークン、マキシマム月1万3,990円で毎週30億Museトークン）
[話すこと] Sentinelは同じVMで動く別のエージェントで、Museがネットへ出すものを全部確認する。
会話を学習に使わせない設定（オプトアウト）がある。広告には使わないと発表している。
VM全体を利用者だけが持つ鍵で暗号化する「Muse Confidential VM」を年内に出す予定。
日本では、高度な音声モード、アバター、Muse専用のメールアドレスは後日案内
-->

---

# dotsは、目標を持たせて常時進めさせる

<div class="fig">
<div class="lead"><b>要点</b>ChatGPTの上位プランに付く。Slackから話しかけられ、会社向けには役割を固定したdotsを試験中</div>
<div class="profile">
<div class="pf-head"><span class="ico i-chatgpt"></span><b>dots</b><span>OpenAI</span><span>2026-09-29</span></div>
<dl class="pf">
<div><dt>主な用途</dt><dd>継続するタスク<br><small>例：利用者の声を監視し、不具合を直す</small></dd></div>
<div><dt>モデル</dt><dd>GPT-6 Astra（発表時）</dd></div>
<div><dt>チャネル</dt><dd>ChatGPT、Codex<br><small>Slack、Teamsからも話しかけられる</small></dd></div>
<div><dt>提供と料金</dt><dd>ChatGPT Pro（月100ドル〜）かBusiness Premium<br><small>1人1体から。日本でも使える</small></dd></div>
<div><dt>安全設計</dt><dd>不在時は読み取り専用にできる</dd></div>
</dl>
</div>
</div>

<!--
[Sources]
- https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/ （GPT-6 Astra。Pro、Business Premium。ChatGPTかCodexから起動。Slack、Teams。専門のdots。Agent 365との連携）
- https://www.aljazeera.com/economy/2026/9/30/openai-launches-dots-personal-ai-assistant-built-to-handle-everything （「読み取り専用」モード。不在時にブラウザやPCを操作させない）
- 日本で使えることは発表者が確認済み（2026-11-10）。円の価格は第三者の整理（smartscope.blog、ai.zenken.co.jpなど）
[話すこと] モデルは発表時のGPT-6 Astra。10月26日に、Astraと同等の性能で1/10の単価のGPT-6.1 TerraがChatGPTとCodexに追加された（https://9to5mac.com/2026/10/26/openai-upgrades-chatgpt-and-codex-with-new-gpt-6-1-terra-model/）。dotsが使うモデルが変わったかは、公式の説明が見つからなかった。
日本ではPro 100が月16,800円から。Business Premiumは1人月19,250円（年払いなら15,250円、税別）。Plusでは使えない。
会社向けの専門のdotsは、それぞれに認証情報とツールを持たせ、Microsoftと組んでAgent 365の管理機能につなぐ
-->

---

# Duetは、業務アプリを監視して先に声をかける

<div class="fig">
<div class="lead"><b>要点</b>専門職と小さな会社の経営者向け。今は米国のみで、日本では使えない</div>
<div class="profile">
<div class="pf-head"><span class="ico i-duet"></span><b>Duet</b><span>Anthropic</span><span>2026-10-21</span></div>
<dl class="pf">
<div><dt>主な用途</dt><dd>未払い請求の催促、給与計算の準備、ECサイトの運営</dd></div>
<div><dt>モデル</dt><dd>Claude Opus 5.5</dd></div>
<div><dt>チャネル</dt><dd>iOS、Android、claude.ai</dd></div>
<div><dt>提供と料金</dt><dd>米国のPro、Max、Ultraに追加料金なし<br><small>順番待ち。利用枠はClaudeのほかの機能と共有</small></dd></div>
<div><dt>安全設計</dt><dd>メッセージごとに分類器で検査する</dd></div>
</dl>
</div>
</div>

<!--
[Sources]
- https://claude.com/resources/articles/claude-duet （"starting with US Pro, Max, and Ultra subscribers"。"designed it around Claude Opus 5.5"。QuickBooks、Stripe、Gusto、Shopifyの例。裏での確認も利用枠に数える）
- https://www.macrumors.com/2026/10/21/anthropic-claude-duet/ （毎朝の要約、数時間ごとの確認、専用の分類器と安全用のシステムプロンプト）
[話すこと] Anthropic自身が、スレッドを読み違えたり急ぎ具合を見誤ったりすることがあると書いている。
チケットの予約のような個人の用事は苦手。ブラウザの画面はまだ利用者に見せられない
-->

---

# Grok Botは、チームに複数置いて業務を任せる

<div class="fig">
<div class="lead"><b>要点</b>個人の秘書ではなく、チームのメンバーとして置く設計。APIの無いツールも画面操作で使う</div>
<div class="profile">
<div class="pf-head"><span class="ico i-grokbot"></span><b>Grok Bot</b><span>xAI</span><span>2026-08-11</span></div>
<dl class="pf">
<div><dt>主な用途</dt><dd>営業メール、マーケティング、事務、バグ修正<br><small>例：CRMの更新、請求書の処理</small></dd></div>
<div><dt>モデル</dt><dd>非公表</dd></div>
<div><dt>チャネル</dt><dd>デスクトップアプリ、iOS<br><small>チームのグループチャットに参加する</small></dd></div>
<div><dt>提供と料金</dt><dd>X SubscriptionのPremium（月30ドル）以上<br><small>日本でも契約できる。WebならPremiumは月5,280円</small></dd></div>
<div><dt>安全設計</dt><dd>判断が要るときだけ人を呼ぶ</dd></div>
</dl>
</div>
</div>

<!--
[Sources]
- https://x.ai/news/introducing-grok-bot （"Grok Bot is your team of always-on agents"。営業、マーケティング、事務、バグ修正の例。使用量はGrokやCursorの枠と別）
- https://x.ai/news/x-subscription （2026-10-12。Free、Plus月8ドル、Premium月30ドル、Super月100ドル、Ultra月200ドル）
- https://docs.x.ai/x-subscription/grok-bot （"Grok Bot is included on Premium, Super, and Ultra plans"。Plusは対象外。使用量はGrok、Cursorと共有の週の枠）
- https://www.gamebusiness.jp/article/2026/10/14/28307.html （日本でも新プランを契約できる。Web版でPlus月1,280円、Premium月5,280円、Super月17,800円、Ultra月34,800円。iOSはWebより高い）
[話すこと] 発表時はSuperGrokとCursorの上位プランの利用者向けだった。10月にX Subscriptionへまとめられた。
ベータ版。Enterpriseは順番待ち
-->

---

# 並べると、日本で使えないのはDuetだけ

<div class="fig">
<div class="lead"><b>要点</b>モデルは各社の最上位。差が出るのは提供地域、料金の入口、連携の数</div>
<div class="tblwrap">
<table class="compare full prod">
<colgroup><col style="width:14%"><col style="width:21.5%"><col style="width:21.5%"><col style="width:21.5%"><col style="width:21.5%"></colgroup>
<thead><tr><th></th><th><span class="ico i-muse"></span>Muse</th><th><span class="ico i-chatgpt"></span>dots</th><th><span class="ico i-duet"></span>Duet</th><th><span class="ico i-grokbot"></span>Grok Bot</th></tr></thead>
<tbody>
<tr><th>対象</th><td>一般</td><td>個人と会社</td><td>専門職、小さな会社</td><td>チーム</td></tr>
<tr><th>モデル</th><td>Muse Spark</td><td>GPT-6 Astra（発表時）</td><td>Opus 5.5</td><td>非公表</td></tr>
<tr class="on"><th>日本</th><td>使える</td><td>使える</td><td>使えない</td><td>使える</td></tr>
<tr><th>料金の入口</th><td>無料</td><td>月100ドル〜</td><td>月20ドル〜</td><td>月30ドル〜</td></tr>
<tr><th>連携の数</th><td>数十</td><td>4,000以上</td><td>6,000以上</td><td>非公表</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[Sources]
- 前の4枚と次の1枚と同じ
- https://claude.com/pricing （Claude Proは月20ドル）
[話すこと] 料金の入口は、そのエージェントを使える一番安いプラン。上位プランほど動かせる量が増える。
dotsのBusiness Premiumは2席以上の契約
-->

---

# 連携できるアプリの数は、桁が違う

<div class="fig">
<div class="lead"><b>要点</b>数より、使うアプリに対応しているか。連携の無いサイトは、どれもブラウザ操作で補う</div>
<div class="tool-list cnt">
<div><span class="ico app i-muse"></span><b>Muse</b><span class="n">数十<small>総数は非公表</small></span><span>小さな会社向けに15を追加。カスタムコネクタも足せる</span></div>
<div><span class="ico app i-chatgpt"></span><b>dots</b><span class="n">4,000以上</span><span>ChatGPTに接続したアプリを使う</span></div>
<div><span class="ico app i-duet"></span><b>Duet</b><span class="n">6,000以上</span><span>Claudeのマーケットプレイスのコネクタとプラグインの合計</span></div>
<div><span class="ico app i-grokbot"></span><b>Grok Bot</b><span class="n">非公表</span><span>APIもMCPも無いツールに、画面操作でログインする</span></div>
</div>
</div>

<!--
[Sources]
- https://about.fb.com/news/2026/09/introducing-muse-small-business/ （2026-09-29。15の連携を名指し、"can also connect to dozens of tools"、"custom connectors"）
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ （"a dedicated secure computer with its own browser"）
- https://theprint.in/theprint-essential/openais-chatgpt-dots-can-connect-to-4000-apps-how-will-it-work/3057880/ （OpenAIの発表の「4,000以上のアプリ」。公式ページは403で読めなかった）
- https://claude.com/resources/articles/claude-duet （"Claude Duet can use the over 6,000 connectors and plugins"）
- https://x.ai/news/introducing-grok-bot （"including platforms with no clean API or MCP"。数は書かれていない）
[話すこと] Museの総数は公式に無い。第三者がアプリ内で数えた値は54（2026-10-07、metamuseai.site）。
dotsとDuetの数はマーケット全体の合計。1つずつの品質や、自分のアカウントで使える権限は別
-->

---

# 用途とチームの規模で、4製品の位置が分かれる

<div class="fig">
<div class="lead"><b>要点</b>任せたいタスクがどの枠に入るかで、候補を絞る</div>
<div class="quad">
<div class="ax">チーム</div>
<div class="cell empty">生活の用事をチームで任せる製品は、まだ少ない</div>
<div class="cell"><div class="p"><span class="ico i-grokbot"></span><div><b>Grok Bot</b><span>チームに複数置く</span></div></div><div class="p"><span class="ico i-chatgpt"></span><div><b>dots</b><span>会社向けの専門dots（試験中）</span></div></div></div>
<div class="ax">個人</div>
<div class="cell"><div class="p"><span class="ico i-muse"></span><div><b>Muse</b><span>予約、購入、請求の見直し</span></div></div></div>
<div class="cell"><div class="p"><span class="ico i-duet"></span><div><b>Duet</b><span>受信箱と請求の監視</span></div></div><div class="p"><span class="ico i-chatgpt"></span><div><b>dots</b><span>継続タスクを1人1体</span></div></div></div>
<div></div>
<div class="ax">生活の用事</div>
<div class="ax">仕事</div>
</div>
</div>

<!--
[話すこと] 位置は各社の発表で強調している用途から置いた。どの製品も、反対側の用途ができないわけではない。
dotsは1人1体から始まり、会社で役割を持たせる方向にも広げている。だから2か所に置いた
-->

---

# 月額より、使用量の上限を見る

<div class="fig">
<div class="lead"><b>要点</b>常駐型は裏でもモデルを呼ぶので、使用量の上限が先に尽きることがある</div>
<div class="tool-list one">
<div><span class="ico app i-muse"></span><b>Muse</b><span>無料にも有料にも、週ごとのトークンの上限がある</span></div>
<div><span class="ico app i-chatgpt"></span><b>dots</b><span>最初は1人1体まで</span></div>
<div><span class="ico app i-duet"></span><b>Duet</b><span>Claudeの利用枠を共有。定期の見回りも枠を使う</span></div>
<div><span class="ico app i-grokbot"></span><b>Grok Bot</b><span>Bot用の使用量は、ほかのGrokの利用と別枠</span></div>
</div>
<div class="rule">試すときは、小さなタスクを1つ任せ、1週間の消費量を見る</div>
</div>

<!--
[Sources]
- https://pc.watch.impress.co.jp/docs/news/2150743.html （Museトークンの週の枠）
- https://claude.com/resources/articles/claude-duet （"Background checks count toward your usage limits"）
- https://x.ai/news/introducing-grok-bot （"Grok Bot comes with its own usage, separate from your Grok and Cursor plans"）
- https://www.axios.com/2026/09/29/openai-dots-ai-assistant-devday （one dot per user to start）
-->

---

# 選ぶときは、4つの条件を順に当てる

<div class="fig">
<div class="lead"><b>要点</b>提供地域、用途、規模、既存の環境の順に絞る</div>
<div class="vsteps">
<div><i>1</i><b>日本で使えるか</b><span>Duetはまだ米国だけ</span></div>
<div><i>2</i><b>生活の用事か、仕事か</b><span>生活ならMuseから</span></div>
<div><i>3</i><b>個人か、チームか</b><span>チームならGrok Bot、会社ならdots</span></div>
<div><i>4</i><b>既存の契約と連携先</b><span>ChatGPTならdots、ClaudeならDuet、XならGrok Bot</span></div>
</div>
<div class="rule">会社のアカウントをつなぐ前に、社外のAIにデータを渡してよいかを確かめる</div>
</div>

<!--
[話すこと] 4つ目は、記憶や連携をそのまま引き継げるかの話。既に使っているサービスのほうが初期設定が少ない
-->

---

<!-- _class: chapter -->
<!-- header: '3. AI社員とAI組織の作り方' -->

<div class="n">CHAPTER 3</div>

# AI社員とAI組織の作り方

会社がこれまで自前で組んできた構成

---

# AI社員は、役割と権限を固定した単一エージェント

<div class="fig">
<div class="lead"><b>要点</b>1つの業務に配属する。システムプロンプト、ナレッジ、ツールの権限の3つで決まる</div>
<div class="row c3">
<div class="card"><div class="ai blue"><div class="glyph"></div></div><div class="t">システムプロンプト</div><div class="d">役割と手順<br>例：問い合わせの一次対応</div></div>
<div class="card"><div class="ai navy"><div class="glyph"></div></div><div class="t">ナレッジ</div><div class="d">参照する資料（RAG）<br>例：回答例、FAQ</div></div>
<div class="card"><div class="ai green"><div class="glyph"></div></div><div class="t">ツールと権限</div><div class="d">触ってよい範囲<br>例：CRMは読み取りのみ</div></div>
</div>
<div class="rule">誰が担当しても同じ手順と品質で回ることが目的</div>
</div>

<!--
[話すこと] 「AI社員」は正式な技術用語ではない。業務ごとに役割を固定したエージェントやワークフローの呼び名。
例は、問い合わせの一次対応、日報のまとめ、提案書の下書き
-->

---

# AI組織は、オーケストレーターがワーカーにタスクを配る

<div class="fig">
<div class="lead"><b>要点</b>orchestrator-workers構成。ワーカーが並列に動き、オーケストレーターが統合する</div>
<div class="svgfig">
<svg width="1152" height="360" viewBox="0 0 1152 360" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#666666"/></marker></defs>
<rect x="20" y="146" width="190" height="68" rx="10" fill="#ffffff" stroke="#949494" stroke-width="2"/>
<text x="115" y="188" text-anchor="middle" class="b">依頼</text>
<line x1="212" y1="166" x2="340" y2="166" stroke="#666666" stroke-width="3" marker-end="url(#ah)"/>
<line x1="340" y1="196" x2="214" y2="196" stroke="#666666" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#ah)"/>
<text x="276" y="152" text-anchor="middle" class="s">タスク</text>
<text x="276" y="226" text-anchor="middle" class="s">統合した結果</text>
<rect x="344" y="128" width="260" height="104" rx="12" fill="#000071"/>
<text x="474" y="174" text-anchor="middle" class="b w">オーケストレーター</text>
<text x="474" y="204" text-anchor="middle" class="s w">分解、割り当て、統合</text>
<line x1="606" y1="160" x2="790" y2="62" stroke="#666666" stroke-width="3" marker-end="url(#ah)"/>
<line x1="606" y1="180" x2="790" y2="180" stroke="#666666" stroke-width="3" marker-end="url(#ah)"/>
<line x1="606" y1="200" x2="790" y2="298" stroke="#666666" stroke-width="3" marker-end="url(#ah)"/>
<rect x="794" y="24" width="330" height="76" rx="10" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="959" y="58" text-anchor="middle" class="b navy">調査ワーカー</text>
<text x="959" y="84" text-anchor="middle" class="s">検索、情報収集</text>
<rect x="794" y="142" width="330" height="76" rx="10" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="959" y="176" text-anchor="middle" class="b navy">作成ワーカー</text>
<text x="959" y="202" text-anchor="middle" class="s">文書、コードの生成</text>
<rect x="794" y="260" width="330" height="76" rx="10" fill="#f1f8f4" stroke="#197a4b" stroke-width="2"/>
<text x="959" y="294" text-anchor="middle" class="b green">評価ワーカー</text>
<text x="959" y="320" text-anchor="middle" class="s">検証して差し戻す</text>
</svg>
</div>
<div class="rule">1つのコンテキストに収まらないタスクを、分割して並列に進める</div>
</div>

<!--
[Sources]
- https://www.anthropic.com/engineering/multi-agent-research-system （"a lead agent coordinates the process while delegating to specialized subagents that operate in parallel"）
[話すこと] ワーカーはサブエージェントとも呼ぶ。中身は同じモデルで、システムプロンプトと渡すツールを変えて役割を分けることが多い。
ワーカーの分け方はタスク次第。調査、作成、評価はよくある例
-->

---

# 組み方は、大きく3通り

<div class="fig">
<div class="lead"><b>要点</b>上から順に導入は軽く、制御の自由度は低い</div>
<div class="tool-list wide">
<div><span class="dual"><span class="ico app i-chatgpt"></span><span class="ico i-claude"></span></span><b>ノーコードのエージェント</b><span>ChatGPTのGPTs、ClaudeのProjects。指示とナレッジを登録する</span></div>
<div><span class="dual"><span class="ico i-n8n"></span><span class="ico i-dify"></span></span><b>ワークフロー基盤</b><span>n8n、Dify、Zapier、Make。トリガーとノードをつなぎ、途中にLLMを挟む</span></div>
<div><span class="dual"><span class="ico i-crewai"></span><span class="ico i-langgraph"></span></span><b>エージェントフレームワーク</b><span>CrewAI、LangGraph。役割、状態、受け渡しをコードで定義する</span></div>
</div>
<div class="rule">AI社員は上の2つ、AI組織は3つ目で組むことが多い</div>
</div>

<!--
[Sources]
- https://docs.crewai.com/en/concepts/agents （role、goal、backstoryでエージェントを定義する）
- ロゴはsimple-icons 16.28.0（n8n、Dify、CrewAI、LangGraph、Claude）とApp StoreのChatGPTアイコン
[話すこと] CrewAIは役割（role）、目標（goal）、背景（backstory）を持つエージェントの集まりとして書く。
LangGraphはエージェントの状態遷移をグラフとして書く。
どれで組んでも、AI社員とAI組織のどちらも作れる。目安として聞いてほしい
-->

---

# 制御フローをコードが決めるか、LLMが決めるか

<div class="fig">
<div class="lead"><b>要点</b>どちらもLLMを使う。違いは、処理の順序がコードで決まっているか、LLMがその場で決めるか</div>
<div class="pair top">
<div class="pair-side">
<b>ワークフロー</b>
<ul>
<li>制御フローはコードで固定</li>
<li>毎回同じ順で動く</li>
<li>結果と費用を予測しやすい</li>
</ul>
</div>
<div class="pair-link">vs</div>
<div class="pair-side on">
<b>エージェント</b>
<ul>
<li>制御フローはLLMが決める</li>
<li>状況に合わせてツールを選ぶ</li>
<li>想定外に強いが、結果と費用がぶれる</li>
</ul>
</div>
</div>
<div class="rule">最も単純な構成から始め、必要になったときだけ複雑にする</div>
</div>

<!--
[Sources]
- https://www.anthropic.com/engineering/building-effective-agents （"Workflows are systems where LLMs and tools are orchestrated through predefined code paths." / "Agents ... dynamically direct their own processes and tool usage" / "finding the simplest solution possible, and only increasing complexity when needed"）
[話すこと] AI社員の多くは、中身はワークフロー。パーソナルエージェントはエージェント側。何を頼まれるか事前に決められないため
-->

---

# よく使われる構成は、5つのパターンの組み合わせ

<div class="fig">
<div class="lead"><b>要点</b>AnthropicのBuilding effective agentsが整理した5つ。AI組織の多くは4と5</div>
<div class="vsteps">
<div><i>1</i><b>Prompt chaining</b><span>前の出力を次の入力にして、順に処理する</span></div>
<div><i>2</i><b>Routing</b><span>入力を分類し、専用の処理へ振り分ける</span></div>
<div><i>3</i><b>Parallelization</b><span>独立した部分の並列処理か、同じ処理の多数決</span></div>
<div class="on"><i>4</i><b>Orchestrator-workers</b><span>中心のLLMがタスクを分解し、ワーカーへ配る</span></div>
<div class="on"><i>5</i><b>Evaluator-optimizer</b><span>生成と評価を分け、合格するまで繰り返す</span></div>
</div>
</div>

<!--
[Sources]
- https://www.anthropic.com/engineering/building-effective-agents （"Prompt chaining" "Routing" "Parallelization" "Orchestrator-workers" "Evaluator-optimizer"）
[話すこと] 1〜3はワークフロー寄り、4はエージェント寄り。5は「作る係とチェック係」の組で、小さく始めても効果が出やすい
-->

---

# マルチエージェントは、チャットの約15倍のトークンを使った

<div class="fig">
<div class="lead"><b>要点</b>Anthropicの調査タスクでの実測値。並列化で広く調べられる代わりに、費用が増える</div>
<div class="svgfig">
<svg width="1152" height="300" viewBox="0 0 1152 300" xmlns="http://www.w3.org/2000/svg">
<text x="250" y="62" text-anchor="end" class="b">チャット</text>
<rect x="270" y="30" width="58" height="48" rx="4" fill="#949494"/>
<text x="344" y="62" class="b">1</text>
<text x="250" y="152" text-anchor="end" class="b">単一エージェント</text>
<rect x="270" y="120" width="232" height="48" rx="4" fill="#0031d8"/>
<text x="518" y="152" class="b">約4倍</text>
<text x="250" y="242" text-anchor="end" class="b">マルチエージェント</text>
<rect x="270" y="210" width="770" height="48" rx="4" fill="#000071"/>
<text x="1056" y="242" class="b">約15倍</text>
</svg>
</div>
<div class="rule">全員が同じコンテキストを要るタスクは、分けても速くならない</div>
</div>

<!--
[Sources]
- https://www.anthropic.com/engineering/multi-agent-research-system （"agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats"）
[話すこと] 調査タスクでの数字。タスクの種類で変わる。
同じ記事は、多くのコーディングは本当に並列化できる部分が少なく、マルチエージェントに向かないと書いている
-->

---

<!-- _class: chapter -->
<!-- header: '4. 使い分け' -->

<div class="n">CHAPTER 4</div>

# 使い分け

契約するか、自前で組むか

---

# 3つは、誰のために働き、誰が作るかで分かれる

<div class="fig">
<div class="lead"><b>要点</b>パーソナルエージェントは個人に仕える既製品。AI社員とAI組織は業務に仕える自前の構成</div>
<div class="tblwrap">
<table class="compare full prod">
<colgroup><col style="width:16%"><col style="width:28%"><col style="width:28%"><col style="width:28%"></colgroup>
<thead><tr><th></th><th>パーソナルエージェント</th><th>AI社員</th><th>AI組織</th></tr></thead>
<tbody>
<tr class="on"><th>仕える相手</th><td>個人</td><td>1つの業務</td><td>大きな業務</td></tr>
<tr><th>作り方</th><td>製品を契約する</td><td>役割と手順を設定する</td><td>分担と受け渡しを設計する</td></tr>
<tr><th>制御</th><td>エージェント</td><td>ワークフローが多い</td><td>オーケストレーター</td></tr>
<tr><th>権限</th><td>本人のアカウント</td><td>業務用のアカウント</td><td>ワーカーごとに最小限</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[話すこと] 権限の違いが一番大きい。パーソナルエージェントは本人のメールや決済に触れる。
AI社員やAI組織は、会社が業務用のアカウントと、ワーカーごとの最小権限を決めて渡す（第3回の「権限は最小に」と同じ）
-->

---

# 境目は近づいている。製品の側がチームに入ってきた

<div class="fig">
<div class="lead"><b>要点</b>これまで自前で組んでいた「業務に配属するエージェント」を、契約して置けるようになり始めた</div>
<div class="tool-list one">
<div><span class="ico app i-chatgpt"></span><b>dots</b><span>会社向けに、役割、認証情報、ツールを個別に持つ専門のdotsを試験中</span></div>
<div><span class="ico app i-grokbot"></span><b>Grok Bot</b><span>チームで複数のBotを持ち、営業や事務を任せる</span></div>
<div><span class="ico app i-duet"></span><b>Duet</b><span>小さな会社の経営者の、請求や給与の業務を監視する</span></div>
</div>
<div class="rule">「AI社員を組むか、エージェントを契約するか」が新しい選択肢になった</div>
</div>

<!--
[Sources]
- https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/ （"specialist dots"。将来は複数のdotsがチームで働く構想）
- https://x.ai/news/introducing-grok-bot
- https://claude.com/resources/articles/claude-duet
[話すこと] 社内独自の手順や社内システムへの接続が要るなら、自前のAI社員のほうが向く。
既製品は、社外のAIにデータを渡してよいかを先に確かめる
-->

---

# タスクの形で、使うものを決める

<div class="fig">
<div class="lead"><b>要点</b>個人の用事か、手順の決まった業務か、分割できる大きな業務か</div>
<div class="vsteps">
<div><i>1</i><b>個人の用事を片づけたい</b><span>パーソナルエージェント</span></div>
<div><i>2</i><b>手順の決まった業務</b><span>ワークフローか、単一エージェントのAI社員</span></div>
<div><i>3</i><b>並列に分割できる業務</b><span>マルチエージェントのAI組織</span></div>
<div class="ng"><i>!</i><b>外部への送信、支払い、削除</b><span>どれを使っても、人の承認を挟む</span></div>
</div>
</div>

<!--
[話すこと] 上から順に、費用と運用の手間が増える。下へ進むのは、上で足りないと分かってから。
4つ目は使い分けではなく、全部に共通する約束
-->

---

<!-- header: 'まとめ' -->

# 今日のまとめ

<div class="fig">
<div class="vsteps">
<div><i>1</i><b>パーソナルエージェント</b><span>クラウドに常駐して先回りし、外部への操作は承認を待つ</span></div>
<div><i>2</i><b>4製品</b><span>日本で使えないのはDuetだけ。料金は使用量の上限で比べる</span></div>
<div><i>3</i><b>AI社員とAI組織</b><span>手順が決まればワークフロー、分割できればマルチエージェント</span></div>
<div><i>4</i><b>使い分け</b><span>個人の用事は契約、業務は自前で組む。外部への操作は人が承認</span></div>
</div>
</div>
