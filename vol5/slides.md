---
marp: true
theme: deck
paginate: false
size: 16:9
title: Gitとチーム開発：branch、PR、CI、worktree
description: builbaseエンジニア勉強会 第5回（60分）
author: seiji
style: |
  /* 第3回・第4回の部品をそのまま引き継ぐ（第5回の部品は末尾）。共通テーマ theme/deck.css の変数と寸法に合わせる */
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
  /* ===== 第5回だけで使う部品 ===== */
  /* ターミナルの出力の中で、conflictのマーカーや注目させたい行の色を変える */
  .terminal-screen code.warn { color: #ffb4a8; }
  .terminal-screen code.hl { color: #ffe08a; }
  .terminal-screen code.dim2 { color: #b8b8b8; margin: 0 0 16px 18px; }
  /* 横長のターミナルと右の説明を並べる */
  .scene-grid.wide { grid-template-columns: 1.35fr 1fr; gap: 40px; }
  .terminal-screen.yaml code { font-size: 17px; line-height: 1.34; white-space: pre; }
  .terminal-screen.yaml { padding-top: 54px; padding-bottom: 18px; }
  /* PDFでは影が灰色の四角で描かれ、下のまとめの1行に被る。第5回は影を付けず、まとめとの間を空ける */
  .terminal-screen { box-shadow: none; }
  .fig > .scene-grid { margin-bottom: 0; }
  .fig > .scene-grid + .rule { margin-top: 32px; }
  /* 右の説明の高さがターミナルを押し下げないよう、項目の上下を詰める */
  .scene-grid.wide .numbered { gap: 12px; }
  .scene-grid.wide .numbered > div { padding: 6px 0 6px 20px; }
  .scene-grid.wide .terminal-screen { min-height: 0; }
  /* 行の多い実出力。文字と行間を詰め、長いハッシュも1行に収める */
  .terminal-screen.tight { padding: 54px 26px 18px; }
  .terminal-screen.tight code { font-size: 16px; line-height: 1.38; white-space: pre; }
  .terminal-screen.tight code.output { margin-bottom: 4px; }
---

<!-- _class: title -->

# エンジニア勉強会

<p>
第5回 Gitとチーム開発：branch、PR、CI、worktree<br>
2026-11-26
</p>

---

<!-- header: 'はじめに' -->

# 今日の内容

<div class="fig">
<div class="lead"><b>要点</b>前回のおさらいのあと、AIエージェントの並列開発を支えているGitとGitHubの仕組みを見る</div>
<div class="vsteps">
<div><i>0</i><b>おさらい</b><span>第4回の要点と、この2週間の変化。Orca Bots</span></div>
<div><i>1</i><b>Gitの仕組み</b><span>commit、branch、merge、conflict、取り消し</span></div>
<div><i>2</i><b>GitHubでのチーム開発</b><span>GitHub flow、PR、レビュー、CI、branch保護</span></div>
<div><i>3</i><b>AIエージェントとGit</b><span>worktreeで並列に動かし、PRで統合する</span></div>
</div>
<p class="cap">製品の情報は2026-11-25時点。料金や提供地域は変わりやすいので、使う前に公式ページで確かめる</p>
</div>

<!--
[話すこと] 今回から、冒頭の10分で前回のおさらいと、その後の変化を話す。
本編はAIではなくエンジニアリングの話。ただし最後に、AIエージェントを並列に動かすときにGitがどう効くかへ戻ってくる
-->

---

<!-- _class: chapter -->
<!-- header: '0. おさらい' -->

<div class="n">CHAPTER 0</div>

# おさらいと、この2週間の変化

第4回：パーソナルエージェント、AI社員、AI組織

---

# 前回は、起動の仕方と仕える相手で4つに分けた

<div class="fig">
<div class="lead"><b>要点</b>指示で動くか、常駐して先回りするか。個人に仕えるか、組織の業務に仕えるか</div>
<div class="map">
<div></div><div class="h">個人</div><div class="h">組織の業務</div>
<div class="h">指示で起動</div>
<div class="c"><b>AIエージェント</b><span>Claude Code、Codex</span></div>
<div class="c"><b>AI社員、AI組織</b><span>ワークフロー、マルチエージェントを自前で組む</span></div>
<div class="h">常駐、先回り</div>
<div class="c on"><b>パーソナルエージェント</b><span>Muse、Duet、dots</span></div>
<div class="c"><b>チーム型の常駐エージェント</b><span>Grok Bot、会社向けの専門dots</span></div>
</div>
<p class="cap">第4回5枚目の地図。今日のOrca Botsは、この地図の左上と右下の間に入る</p>
</div>

<!--
[話すこと] 前回の全体の地図。左上が普段使っているClaude CodeやCodex。左下が前回の主役のパーソナルエージェント。
右上が会社が自前で組むAI社員とAI組織。右下は、製品の側が業務に入ってきた領域
-->

---

# パーソナルエージェントは、常駐し、取り消せない操作の前で止まる

<div class="fig">
<div class="lead"><b>要点</b>利用者ごとのクラウド環境で動き続け、受信やイベントを見て自分で起動する</div>
<div class="row c3">
<div class="card"><div class="ai navy"><div class="glyph"></div></div><div class="t">常駐</div><div class="d">利用者ごとの専用VMで<br>目標と記憶を持ち続ける</div></div>
<div class="card"><div class="ai blue"><div class="glyph"></div></div><div class="t">先回り</div><div class="d">メールや予定を見て<br>やることを自分で見つける</div></div>
<div class="card"><div class="ai green"><div class="glyph"></div></div><div class="t">承認</div><div class="d">送信、支払い、署名、削除の前で<br>人の許可を待つ</div></div>
</div>
<div class="rule">日本で使えるのはMuseとdots。料金は月額より使用量の上限で比べる</div>
</div>

<!--
[Sources]
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
- https://claude.com/resources/articles/claude-duet
[話すこと] 普通のAIエージェントとの違いは、起動の主体と寿命。
Claude Codeは人が頼んだタスクが終われば止まる。パーソナルエージェントは常駐して自分で仕事を見つける
-->

---

# AI社員は1つの業務に配属し、AI組織は分担とまとめ役を置く

<div class="fig">
<div class="lead"><b>要点</b>手順が決まっていればワークフローで足りる。AI組織にするのは、並列に分けられる仕事だけ</div>
<div class="vsteps">
<div><i>1</i><b>AI社員</b><span>役割、ナレッジ、ツールの権限を固定した単一エージェント</span></div>
<div><i>2</i><b>AI組織</b><span>オーケストレーターがタスクを分け、ワーカーへ配って統合する</span></div>
<div><i>3</i><b>組み方</b><span>ノーコード、ワークフロー基盤、エージェントフレームワーク</span></div>
<div class="ng"><i>!</i><b>費用</b><span>マルチエージェントはチャットの約15倍のトークンを使った</span></div>
</div>
</div>

<!--
[Sources]
- https://www.anthropic.com/engineering/building-effective-agents
- https://www.anthropic.com/engineering/multi-agent-research-system （約4倍と約15倍）
[話すこと] 最も単純な構成から始め、必要になったときだけ複雑にする（Anthropic）。
同じ記事は、多くのコーディングは並列化できる部分が少ないとも書いている。今日の第3章でこの話に戻る
-->

---

# この2週間で、提供地域と機能が広がった

<div class="fig">
<div class="lead"><b>要点</b>Grok Botが正式版になってチームで使えるようになり、Museは英語圏へ広がった。Duetは変化なし</div>
<div class="tl">
<div><span class="d">11月11日</span><span class="ico i-grokbot"></span><b>Grok Bot</b><span class="co">1.0</span><span class="ds">正式版。Slack・Teams、会議に参加</span></div>
<div><span class="d">11月13日</span><span class="ico i-chatgpt"></span><b>dots</b><span class="co">米国のPro</span><span class="ds">承認すると代わりに支払う</span></div>
<div><span class="d">11月17日</span><span class="ico i-muse"></span><b>Muse</b><span class="co">豪州、英国</span><span class="ds">提供地域を追加（英国は24日）</span></div>
<div><span class="d">変化なし</span><span class="ico i-duet"></span><b>Duet</b><span class="co">米国のみ</span><span class="ds">順番待ちのプレビューのまま</span></div>
</div>
<div class="rule">日本の料金と提供範囲は、11月10日から変わっていない（公式発表の範囲）</div>
</div>

<!--
[Sources]
- https://x.ai/news/grok-bot-1-0 （2026-11-11。Team Bots、Slack・Teams、会議、確認してから実行する操作）
- https://docs.x.ai/grok-bot/team-bots （TeamかEnterpriseのプラン。管理者が1つのアカウントを全員に使わせる共有コネクタ）
- https://help.openai.com/en/articles/6825453-chatgpt-release-notes （11/13 ChatGPT Walletでの購入。Pro、18歳以上、米国のカード。11/19 Health連携とdot専用タブ）
- https://openai.com/index/introducing-dots/ （11/3追記。GPT-6.1 Terraを併用）
- https://about.fb.com/news/2026/11/muse-is-now-available-in-australia/ （2026-11-17）
- https://about.fb.com/news/2026/11/introducing-muse-in-the-uk-a-personal-ai-agent-you-control/ （2026-11-24）
- https://claude.com/resources/articles/claude-duet （10/23の注記以降、変更なし）
[話すこと] Grok Botはベータの表記が消えた。会議に参加してチャットで発言できる（Team、Enterprise、Ultraなど）。
dotsは11/3からGPT-6.1 Terraも使う。Plusの一部で試験中という報道（Engadget）はあるが、公式はまだ「Proで提供」。
Museは11/5に音声とアバター、11/6にspaces（自分専用の画面）を追加している（第4回の前日まで）
-->

---

# Orca Botsは、開発環境の中に置くbot

<div class="fig">
<div class="lead"><b>要点</b>ADEのOrcaが11月19日にベータで出した。Slackやissueで頼むと、テスト済みのPRが返ってくる</div>
<div class="profile">
<div class="pf-head"><span class="ico i-orca"></span><b>Orca Bots</b><span>Stably AI</span><span>2026-11-19 ベータ</span></div>
<dl class="pf">
<div><dt>Orca本体</dt><dd>Claude Code、Codexなどを、worktreeごとに並列で動かすIDE<small>（無料、MIT）</small></dd></div>
<div><dt>依頼の窓口</dt><dd>Slack、GitHub、Linear、Gmail、webhook、スケジュール</dd></div>
<div><dt>動く場所</dt><dd>自分のマシンのフォルダ。常に動かすならMac miniなどをつなぐ</dd></div>
<div><dt>作業の形</dt><dd>専用のworktreeでClaude CodeやCodexが作業し、PRを返す</dd></div>
<div><dt>人の出番</dt><dd>判断や承認が要るものは「Needs you」にたまる</dd></div>
</dl>
</div>
</div>

<!--
[Sources]
- https://github.com/stablyai/orca/releases/tag/v1.4.265 （2026-11-19 "Introducing Orca Bots (Beta)"）
- https://orca.dev/bots （"Ask a bot in Slack, Linear, or GitHub to fix a bug, and come back to a tested pull request." / "It reports first and acts once you say so"。料金のFAQ）
- https://orca.dev/docs/bots （"A bot lives in a folder on one computer"。Needs you、Waiting。テンプレート24種類）
- https://orca.dev/docs/bots/security （Orca Cloudを通るのはSlack、GitHub、Linear、webhookだけ。権限モード、Who can ask）
- https://orca.dev/docs/model/worktrees （"Every Orca worktree is a real git worktree"）
- https://orca.dev/docs/agents/supported （対応するCLIエージェント41件）
- https://github.com/stablyai/orca （MIT。macOS、Windows、Linux。2026-11-25に確認）
- アイコンはstablyai/orcaのresources/icon.png
[話すこと] ADEはAgent Development Environment。エディタの代わりにエージェントを中心に置いた開発環境で、第1回で紹介したcmuxも同じ仲間。
Botには名前、目的、記憶（ただのMarkdownファイル）があり、定期の見回りもできる。
11/21のv1.4.269から、group roomでBotが返信の中で別のBotを@名前で呼ぶと、そのBotが続きを引き取る。
Slack、GitHub、Linearからの依頼はOrca Cloudが中継する。手元から外向きにつなぐのでポートは開けない。マシンが寝ている間は動かず、依頼は最大1日待つ。
注意点：Botの権限モードは既定でFull access。頼める人は既定で本人だけ。「下書きにとどめる」などの一部のルールはモデルへの指示で、保証ではないと公式が書いている
-->

---

# パーソナルエージェントとの違いは、どこで、誰の契約で動くか

<div class="fig">
<div class="lead"><b>要点</b>各社のクラウドVMで動く製品ではなく、自分のマシンで、自分のエージェントを動かす</div>
<div class="tblwrap">
<table class="compare full prod">
<colgroup><col style="width:18%"><col style="width:41%"><col style="width:41%"></colgroup>
<thead><tr><th></th><th>パーソナルエージェント<br><small>Muse、dots、Duet、Grok Bot</small></th><th><span class="ico i-orca"></span>Orca Bots</th></tr></thead>
<tbody>
<tr class="on"><th>動く場所</th><td>各社のクラウドの専用VMに常駐</td><td>自分のマシン。寝ている間は止まる</td></tr>
<tr><th>モデルと料金</th><td>製品の月額に含まれる</td><td>自分のClaude Code、Codexの契約。上乗せなし</td></tr>
<tr><th>仕事</th><td>メール、予定、購入、業務アプリ</td><td>バグ修正、PRのレビュー、CIの失敗</td></tr>
<tr><th>成果物</th><td>送信、予約、要約</td><td>worktreeの差分とPR</td></tr>
<tr><th>承認</th><td>送信や支払いの前</td><td>判断が要る場面と、PRのレビュー</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[Sources]
- https://orca.dev/bots （"Orca is free and MIT open source. Bots use your existing Claude Code or Codex plan (or API key) with zero markup from us."）
- https://orca.dev/docs/bots
- 第4回の各社の発表（Muse、dots、Duet、Grok Bot）
[話すこと] 第4回の地図では、指示で動くAIエージェント（左上）を、SlackやGitHubから頼めて、見回りもするようにしたもの。
成果物がPRになるので、最終的な確認はGitHubのレビューとCIに乗る。ここから今日の本編につながる
-->

---

# Orcaは、エージェント1つにworktreeを1つ割り当てる

<div class="fig">
<div class="lead"><b>要点</b>同じフォルダで2つのエージェントを動かすと、互いの変更を上書きする。分けているのはGitの機能</div>
<div class="svgfig">
<svg width="1152" height="330" viewBox="0 0 1152 330" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a10" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#666666"/></marker></defs>
<rect x="20" y="115" width="220" height="100" rx="12" fill="#000071"/>
<text x="130" y="158" text-anchor="middle" class="b w">リポジトリ</text>
<text x="130" y="188" text-anchor="middle" class="m w">.git</text>
<line x1="242" y1="150" x2="420" y2="62" stroke="#666666" stroke-width="3" marker-end="url(#a10)"/>
<line x1="242" y1="165" x2="420" y2="165" stroke="#666666" stroke-width="3" marker-end="url(#a10)"/>
<line x1="242" y1="180" x2="420" y2="268" stroke="#666666" stroke-width="3" marker-end="url(#a10)"/>
<rect x="424" y="24" width="330" height="76" rx="10" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="589" y="58" text-anchor="middle" class="b navy">worktree 1</text>
<text x="589" y="84" text-anchor="middle" class="m">feature/login</text>
<rect x="424" y="127" width="330" height="76" rx="10" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="589" y="161" text-anchor="middle" class="b navy">worktree 2</text>
<text x="589" y="187" text-anchor="middle" class="m">feature/api</text>
<rect x="424" y="230" width="330" height="76" rx="10" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="589" y="264" text-anchor="middle" class="b navy">worktree 3</text>
<text x="589" y="290" text-anchor="middle" class="m">fix/typo</text>
<line x1="756" y1="62" x2="836" y2="62" stroke="#666666" stroke-width="3" marker-end="url(#a10)"/>
<line x1="756" y1="165" x2="836" y2="165" stroke="#666666" stroke-width="3" marker-end="url(#a10)"/>
<line x1="756" y1="268" x2="836" y2="268" stroke="#666666" stroke-width="3" marker-end="url(#a10)"/>
<rect x="840" y="24" width="290" height="76" rx="10" fill="#ffffff" stroke="#949494" stroke-width="2"/>
<text x="985" y="70" text-anchor="middle" class="b">Claude Code</text>
<rect x="840" y="127" width="290" height="76" rx="10" fill="#ffffff" stroke="#949494" stroke-width="2"/>
<text x="985" y="173" text-anchor="middle" class="b">Codex</text>
<rect x="840" y="230" width="290" height="76" rx="10" fill="#ffffff" stroke="#949494" stroke-width="2"/>
<text x="985" y="276" text-anchor="middle" class="b">Gemini CLI</text>
</svg>
</div>
<div class="rule">worktree、branch、PRが何をしているかを知ると、AIエージェントの並列開発の限界も見える</div>
</div>

<!--
[Sources]
- https://orca.dev/ （各エージェントを別々のgit worktreeで並列に動かす）
- https://git-scm.com/docs/git-worktree
[話すこと] 第1回で「branchやworktreeは発展事項」と後回しにした話を、今日まとめて回収する。
ここからはAIの話を離れて、Gitそのものの仕組みに入る
-->

---

<!-- _class: chapter -->
<!-- header: '1. Gitの仕組み' -->

<div class="n">CHAPTER 1</div>

# Gitの仕組み

commit、branch、merge、conflict、取り消し

---

# commitは、全ファイルのスナップショットと親へのポインタ

<div class="fig">
<div class="lead"><b>要点</b>Gitは差分ではなく、その時点のファイル全体（tree）を記録し、1つ前のcommitを親として指す</div>
<div class="scene-grid wide">
<div class="terminal-screen tight">
<div class="terminal-bar"><span>commitの中身</span><div class="mock-tools"><span class="ico i-git"></span></div></div>
<code><span class="prompt">$</span> git cat-file -p HEAD</code>
<code class="hl">tree c6410c2e1ea652c71022f100c1a0132c0eadf753</code>
<code class="hl">parent 163016b4adf5bcd2c7a321a44e83ef513590e733</code>
<code class="output" style="margin-bottom:0">author demo &lt;demo@example.com&gt; 1795575375 +0900</code>
<code class="output">committer demo &lt;demo@example.com&gt; 1795575375 +0900</code>
<code class="output">色を赤に変える</code>
</div>
<div class="numbered">
<div><b>tree</b><span>この時点の全ファイルとフォルダ</span></div>
<div><b>parent</b><span>1つ前のcommit。mergeなら2つ</span></div>
<div><b>author、message</b><span>誰が、いつ、何のために</span></div>
</div>
</div>
<div class="rule">IDは中身のハッシュ。履歴を1つ書き換えると、それ以降のcommitのIDが全部変わる</div>
</div>

<!--
[Sources]
- https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F （"Snapshots, Not Differences"）
- https://git-scm.com/book/en/v2/Git-Internals-Git-Objects （commit、tree、blobのオブジェクト）
- 画面は2026-11-25に使い捨てのリポジトリで実行した実出力（git 2.56.1）
[話すこと] 変わっていないファイルは、前のcommitと同じblobを指すだけなので、毎回コピーしているわけではない。
parentをたどると履歴になる。IDが中身から決まるので、rebaseやamendで書き換えると別のcommitになる。第2章のforce pushの話につながる
-->

---

# 変更は、作業ツリー、ステージ、リポジトリの順に入る

<div class="fig">
<div class="lead"><b>要点</b>addで「次のcommitに入れるもの」を選び、commitで記録する。選ぶ段階があるので、1つのcommitを1つの目的にできる</div>
<div class="flow eq">
<div class="step"><i>1</i>作業ツリー<small>いま編集しているファイル</small><em>git status</em></div>
<div class="arw">→</div>
<div class="step on"><i>2</i>ステージ（index）<small>次のcommitに入れる変更</small><em>git add</em></div>
<div class="arw">→</div>
<div class="step"><i>3</i>リポジトリ<small>記録されたcommitの履歴</small><em>git commit</em></div>
</div>
<div class="rule">「バグ修正」と「ついでの整形」は別々にaddして、別々のcommitにする</div>
</div>

<!--
[Sources]
- https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F （"The Three States"）
[話すこと] git add -pでファイルの一部だけをステージに入れられる。
commitを目的ごとに分けておくと、レビューしやすく、あとで1つだけ取り消せる
-->

---

# branchは、履歴を枝分かれさせて作業を分ける

<div class="fig">
<div class="lead"><b>要点</b>mainから枝を出して作業すれば、mainに影響しない。実体は枝の先端を指す名札（ref）</div>
<div class="scene-grid wide">
<div class="svgfig">
<svg width="620" height="300" viewBox="0 0 620 300" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="200" x2="420" y2="200" stroke="#000071" stroke-width="5"/>
<path d="M170 200 Q230 110 330 110 L480 110" fill="none" stroke="#0031d8" stroke-width="5"/>
<circle cx="60" cy="200" r="22" fill="#ffffff" stroke="#000071" stroke-width="4"/><text x="60" y="207" text-anchor="middle" class="s">A</text>
<circle cx="170" cy="200" r="22" fill="#ffffff" stroke="#000071" stroke-width="4"/><text x="170" y="207" text-anchor="middle" class="s">B</text>
<circle cx="390" cy="200" r="22" fill="#ffffff" stroke="#000071" stroke-width="4"/><text x="390" y="207" text-anchor="middle" class="s">E</text>
<circle cx="330" cy="110" r="22" fill="#e8f1fe" stroke="#0031d8" stroke-width="4"/><text x="330" y="117" text-anchor="middle" class="s">C</text>
<circle cx="480" cy="110" r="22" fill="#e8f1fe" stroke="#0031d8" stroke-width="4"/><text x="480" y="117" text-anchor="middle" class="s">D</text>
<rect x="340" y="240" width="100" height="36" rx="18" fill="#000071"/><text x="390" y="265" text-anchor="middle" class="m w">main</text>
<rect x="400" y="30" width="160" height="36" rx="18" fill="#0031d8"/><text x="480" y="55" text-anchor="middle" class="m w">feature/login</text>
<text x="390" y="55" text-anchor="end" class="b">HEAD →</text>
<text x="170" y="250" text-anchor="middle" class="s">ここから枝分かれ</text>
</svg>
</div>
<div class="numbered">
<div><b>枝分かれ</b><span>同じcommitから、別々に積んでいける</span></div>
<div><b>名札（ref）</b><span>枝の先端のcommitを指す。commitすると先へ進む</span></div>
<div><b>HEAD</b><span>いま居る枝を指す</span></div>
</div>
</div>
<div class="rule">git switch -c feature/loginで、今のcommitから枝を出して移る</div>
</div>

<!--
[Sources]
- https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell （"A branch in Git is simply a lightweight movable pointer to one of these commits."）
- https://git-scm.com/book/en/v2/Git-Internals-Git-References
[話すこと] 名札の中身は、.git/refs/heads/mainのようなファイルに書かれたcommitのID（2026-11-25の実測で、cat .git/refs/heads/main → 7453c8b…、cat .git/HEAD → ref: refs/heads/main）。
git gcのあとはpacked-refsという1つのファイルにまとめられ、個別のファイルが無いこともあるが、考え方は同じ。
branchを作ってもファイルはコピーされない。名札が1枚増えるだけなので、気軽に切ってよい。
git checkoutは役割が多すぎたので、branchの移動はgit switch、ファイルを戻すのはgit restoreに分かれた
-->

---

# mergeは、分かれた枝を1本に合流させる

<div class="fig">
<div class="lead"><b>要点</b>mainが伸びていなければ名札を進めるだけ。両方が伸びていれば、合流点のcommitを作る</div>
<div class="svgfig">
<svg width="1152" height="350" viewBox="0 0 1152 350" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a15" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#666666"/></marker></defs>
<text x="280" y="30" text-anchor="middle" class="b">fast-forward（mainが伸びていない）</text>
<line x1="60" y1="220" x2="200" y2="220" stroke="#000071" stroke-width="5"/>
<path d="M200 220 Q250 140 320 140 L460 140" fill="none" stroke="#0031d8" stroke-width="5"/>
<circle cx="80" cy="220" r="22" fill="#ffffff" stroke="#000071" stroke-width="4"/><text x="80" y="227" text-anchor="middle" class="s">A</text>
<circle cx="200" cy="220" r="22" fill="#ffffff" stroke="#000071" stroke-width="4"/><text x="200" y="227" text-anchor="middle" class="s">B</text>
<circle cx="320" cy="140" r="22" fill="#e8f1fe" stroke="#0031d8" stroke-width="4"/><text x="320" y="147" text-anchor="middle" class="s">C</text>
<circle cx="460" cy="140" r="22" fill="#e8f1fe" stroke="#0031d8" stroke-width="4"/><text x="460" y="147" text-anchor="middle" class="s">D</text>
<text x="390" y="112" text-anchor="middle" class="s">featureの枝</text>
<rect x="150" y="260" width="100" height="36" rx="18" fill="#f2f2f2"/><text x="200" y="285" text-anchor="middle" class="m">main</text>
<rect x="410" y="180" width="100" height="36" rx="18" fill="#000071"/><text x="460" y="205" text-anchor="middle" class="m w">main</text>
<path d="M252 278 Q360 280 408 206" fill="none" stroke="#666666" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#a15)"/>
<text x="280" y="330" text-anchor="middle" class="s">新しいcommitは作らず、mainの名札がDへ移る</text>
<line x1="576" y1="20" x2="576" y2="330" stroke="#cccccc" stroke-width="2"/>
<text x="870" y="30" text-anchor="middle" class="b">3-way merge（両方が伸びた）</text>
<line x1="630" y1="220" x2="1080" y2="220" stroke="#000071" stroke-width="5"/>
<path d="M760 220 Q810 140 880 140 L960 140 Q1040 140 1080 205" fill="none" stroke="#0031d8" stroke-width="5"/>
<circle cx="650" cy="220" r="22" fill="#ffffff" stroke="#000071" stroke-width="4"/><text x="650" y="227" text-anchor="middle" class="s">A</text>
<circle cx="760" cy="220" r="22" fill="#ffffff" stroke="#000071" stroke-width="4"/><text x="760" y="227" text-anchor="middle" class="s">B</text>
<circle cx="920" cy="220" r="22" fill="#ffffff" stroke="#000071" stroke-width="4"/><text x="920" y="227" text-anchor="middle" class="s">E</text>
<circle cx="900" cy="140" r="22" fill="#e8f1fe" stroke="#0031d8" stroke-width="4"/><text x="900" y="147" text-anchor="middle" class="s">C</text>
<circle cx="1084" cy="220" r="25" fill="#000071" stroke="#000071" stroke-width="4"/><text x="1084" y="227" text-anchor="middle" class="s w">M</text>
<text x="960" y="112" text-anchor="middle" class="s">featureの枝</text>
<text x="840" y="258" text-anchor="middle" class="s">mainの枝</text>
<rect x="1034" y="260" width="100" height="36" rx="18" fill="#000071"/><text x="1084" y="285" text-anchor="middle" class="m w">main</text>
<text x="870" y="330" text-anchor="middle" class="s">分かれ目B、mainのE、featureのCを比べ、合流点Mを作る</text>
</svg>
</div>
</div>

<!--
[Sources]
- https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging （fast-forwardと、共通の祖先を使う3-way merge）
[話すこと] 合流点Mは親を2つ持つmerge commit。3-wayの「3」は、分かれ目（共通の祖先）と両方の先端の3つ。
片方だけが変えた行はそちらを採り、両方が同じ行を違う内容に変えたときだけ人に聞く。それが次のconflict
-->

---

# 同じ行を両方のbranchが違う内容に変えると、conflictになる

<div class="fig">
<div class="lead"><b>要点</b>Gitはどちらが正しいか判断せず、人が直してcommitするまで止まる。やめるならgit merge --abort</div>
<div class="scene-grid wide">
<div class="terminal-screen tight">
<div class="terminal-bar"><span>mainにfeature/colorをmerge</span><div class="mock-tools"><span class="ico i-git"></span></div></div>
<code><span class="prompt">$</span> git merge feature/color</code>
<code class="warn" style="margin-left:18px">CONFLICT (content): Merge conflict in config.toml</code>
<code><span class="prompt">$</span> cat config.toml</code>
<code class="output" style="margin-bottom:0">title = "Todo"</code>
<code class="warn" style="margin-left:18px">&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD</code>
<code class="output" style="margin-bottom:0">color = "red"</code>
<code class="warn" style="margin-left:18px">=======</code>
<code class="output" style="margin-bottom:0">color = "green"</code>
<code class="warn" style="margin-left:18px">&gt;&gt;&gt;&gt;&gt;&gt;&gt; feature/color</code>
</div>
<div class="numbered">
<div><b>1. 直す</b><span>マーカーを消し、正しい1つにする</span></div>
<div><b>2. git add</b><span>解決したことをGitに伝える</span></div>
<div><b>3. git commit</b><span>merge commitを作る</span></div>
</div>
</div>
</div>

<!--
[Sources]
- https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging （Basic Merge Conflicts）
- 画面は2026-11-25の実出力。mainで色を赤、feature/colorで緑に変えてmergeした
[話すこと] HEADの側が今いるbranch（main）、下が取り込もうとしたbranch。
直し方は機械的には決まらない。赤と緑のどちらが仕様として正しいかは、変更した2人に聞かないと分からない。
→ ここで実演1
-->

---

# 共有したcommitは、revertで打ち消す。resetで消さない

<div class="fig">
<div class="lead"><b>要点</b>pushしたあとに履歴を消すと、ほかの人の手元と食い違う。打ち消すcommitを足して直す</div>
<div class="tblwrap">
<table class="compare full">
<colgroup><col style="width:24%"><col style="width:46%"><col style="width:30%"></colgroup>
<thead><tr><th>コマンド</th><th>すること</th><th>push済みのcommitに</th></tr></thead>
<tbody>
<tr><th><code>git restore</code></th><td>作業ツリーの変更を捨てる</td><td>関係しない</td></tr>
<tr class="on"><th><code>git revert</code></th><td>逆向きの変更を新しいcommitとして足す</td><td class="ok">使える</td></tr>
<tr><th><code>git reset</code></th><td>branchの名札を前のcommitへ戻す</td><td class="ng">使わない</td></tr>
<tr><th><code>git push --force</code></th><td>リモートの履歴を手元の履歴で上書きする</td><td class="ng">使わない</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[Sources]
- https://git-scm.com/docs/git-revert
- https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified
- https://git-scm.com/book/en/v2/Git-Branching-Rebasing （"Do not rebase commits that exist outside your repository and that people may have based work on."）
[話すこと] resetは、まだpushしていない自分だけの履歴を整えるときには便利。
どうしても自分のbranchを書き換えて上書きするなら、--force-with-leaseにする。リモートが自分の知っている状態のときだけ上書きする
-->

---

<!-- _class: chapter -->
<!-- header: '2. GitHubでのチーム開発' -->

<div class="n">CHAPTER 2</div>

# GitHubでのチーム開発

GitHub flow、PR、レビュー、CI、branch保護

---

# 手元とGitHubのリポジトリは、pushとfetchで同期する

<div class="fig">
<div class="lead"><b>要点</b>GitHubのリポジトリも手元と同じGitのリポジトリ。全員がそこへpushし、そこからfetchする</div>
<div class="svgfig">
<svg width="1152" height="320" viewBox="0 0 1152 320" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a19" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#666666"/></marker></defs>
<rect x="416" y="20" width="320" height="110" rx="14" fill="#000071"/>
<text x="576" y="66" text-anchor="middle" class="b w">GitHub（origin）</text>
<text x="576" y="98" text-anchor="middle" class="m w">main, feature/login</text>
<rect x="60" y="200" width="320" height="100" rx="12" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="220" y="242" text-anchor="middle" class="b navy">自分の手元</text>
<text x="220" y="272" text-anchor="middle" class="m">git cloneで作る</text>
<rect x="772" y="200" width="320" height="100" rx="12" fill="#e8f1fe" stroke="#0031d8" stroke-width="2"/>
<text x="932" y="242" text-anchor="middle" class="b navy">同僚の手元</text>
<text x="932" y="272" text-anchor="middle" class="m">git cloneで作る</text>
<line x1="270" y1="196" x2="430" y2="134" stroke="#666666" stroke-width="3" marker-end="url(#a19)"/>
<line x1="410" y1="120" x2="210" y2="196" stroke="#666666" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#a19)"/>
<text x="280" y="140" text-anchor="middle" class="m">fetch</text>
<text x="410" y="186" text-anchor="middle" class="m">push</text>
<line x1="882" y1="196" x2="722" y2="134" stroke="#666666" stroke-width="3" marker-end="url(#a19)"/>
<line x1="742" y1="120" x2="942" y2="196" stroke="#666666" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#a19)"/>
<text x="872" y="140" text-anchor="middle" class="m">fetch</text>
<text x="742" y="186" text-anchor="middle" class="m">push</text>
</svg>
</div>
<div class="rule">git pullは、fetchしてから統合する。分岐していて統合方法が未設定なら止まる</div>
</div>

<!--
[Sources]
- https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes
- https://git-scm.com/docs/git-pull
[話すこと] fetchは手元のorigin/mainなどを更新するだけで、作業中のファイルは変えない。
git 2.56.1で両方が進んだ状態でpullすると、"Need to specify how to reconcile divergent branches."で止まった（2026-11-25に実測。pull.rebaseもpull.ffも未設定の状態）。git config pull.rebase falseならmerge、trueならrebaseになる。
迷ったらfetchしてから差分を見て、自分でmergeかrebaseする
-->

---

# GitHub flowは、mainを常にデプロイできる状態に保つ

<div class="fig">
<div class="lead"><b>要点</b>変更はすべて短命のbranchで行い、PRでレビューを受けてからmainに入れる。CIもここで回す</div>
<div class="vsteps">
<div><i>1</i><b>branchを作る</b><span>mainから、目的が1つのbranchを切る</span></div>
<div><i>2</i><b>commitしてpush</b><span>小さく分けてcommitし、こまめにpushする</span></div>
<div class="on"><i>3</i><b>PRを開く</b><span>何を、なぜ変えたかを書き、レビューを頼む</span></div>
<div class="on"><i>4</i><b>レビューとCI</b><span>指摘を直し、テストが通るまでcommitを足す</span></div>
<div><i>5</i><b>mergeしてデプロイ</b><span>mainへmergeし、branchを消す</span></div>
</div>
</div>

<!--
[Sources]
- https://docs.github.com/en/get-started/using-github/github-flow
[話すこと] 第3回のアジャイルの「少しずつ作って見せる」を、コードの単位でやっている。
branchが長生きするほど、mainとのずれが大きくなってconflictが増える。数日で閉じるのが目安
-->

---

# PRは小さく保つ。説明には、何を、なぜ、どう確かめたかを書く

<div class="fig">
<div class="lead"><b>要点</b>レビューする人は、差分と説明しか見られない。大きいPRほど見落としが増える</div>
<div class="pair top">
<div class="pair-side">
<b>説明に書く3つ</b>
<ul>
<li>何を変えたか</li>
<li>なぜ変えたか（issueへのリンク）</li>
<li>どう確かめたか（テスト、画面）</li>
</ul>
</div>
<div class="pair-link">+</div>
<div class="pair-side on">
<b>小さく保つ</b>
<ul>
<li>1つのPRに目的は1つ</li>
<li>約100行なら妥当、1000行は大きすぎ</li>
<li>整形や改名は別のPRに分ける</li>
</ul>
</div>
</div>
<div class="rule">AIエージェントに作らせたPRも同じ。説明が無い、大きすぎるPRは差し戻す</div>
</div>

<!--
[Sources]
- https://google.github.io/eng-practices/review/developer/small-cls.html （"100 lines is usually a reasonable size for a CL, and 1000 lines is usually too large"。CLはPRに当たる）
- https://google.github.io/eng-practices/review/developer/cl-descriptions.html
[話すこと] 行数はGoogleのガイドの目安で、ルールではない。自動生成のファイルや、ファイルの移動は別に考える。
「どう確かめたか」が書けないPRは、まだ出す段階ではない
-->

---

# レビューは、設計、動作、複雑さ、テストから見る

<div class="fig">
<div class="lead"><b>要点</b>スタイルの指摘は機械（formatter、linter）に任せ、人は機械が見られないところを見る</div>
<div class="vsteps">
<div class="on"><i>1</i><b>設計</b><span>この変更はここにあるべきか。全体と合っているか</span></div>
<div class="on"><i>2</i><b>動作</b><span>利用者にとって正しく動くか。境界の値、並行処理</span></div>
<div class="on"><i>3</i><b>複雑さ</b><span>読んですぐ分かるか。今要らない汎用化をしていないか</span></div>
<div class="on"><i>4</i><b>テスト</b><span>壊れたときに落ちるテストか</span></div>
<div><i>5</i><b>名前、コメント、スタイル</b><span>名前は意図を表しているか。コメントは「なぜ」を書いているか</span></div>
</div>
</div>

<!--
[Sources]
- https://google.github.io/eng-practices/review/reviewer/looking-for.html （Design、Functionality、Complexity、Tests、Naming、Comments、Style、Documentation）
[話すこと] 完璧なコードを求めるのではなく、mainのコードの健全さを上げているかで判断する（同じガイドの基準）。
指摘には、必須の指摘と、好みの提案（Nit:）を区別して書く
-->

---

# PRのmergeには、3つの方式がある

<div class="fig">
<div class="lead"><b>要点</b>mainの履歴をどう残したいかで選ぶ。リポジトリの設定で、使える方式を絞れる</div>
<div class="tblwrap">
<table class="compare full">
<colgroup><col style="width:24%"><col style="width:40%"><col style="width:36%"></colgroup>
<thead><tr><th>方式</th><th>mainに残るもの</th><th>向いている場面</th></tr></thead>
<tbody>
<tr><th>Create a merge commit</th><td>branchのcommit全部と、merge commit</td><td>branchの経緯を残したい</td></tr>
<tr class="on"><th>Squash and merge</th><td>PR全体を1つにまとめたcommit</td><td>1つのPRを1つの変更として扱う</td></tr>
<tr><th>Rebase and merge</th><td>branchのcommitを、mainの先に付け直したもの</td><td>merge commitの無い一直線の履歴</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[Sources]
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges
[話すこと] squashすると、PRの中の細かいcommitは消えてmainがきれいになる。revertもPR単位で1回で済む。
ただしsquashとrebaseは新しいcommitを作るので、mergeしたbranchの上で作業を続けるとconflictしやすい。mergeしたbranchは消して、mainから切り直す
-->

---

# CIは、PRごとに同じテストを自動で回す

<div class="fig">
<div class="lead"><b>要点</b>GitHub Actionsは、リポジトリに置いたYAMLの手順を、PRが更新されるたびにクラウドで実行する</div>
<div class="scene-grid wide">
<div class="terminal-screen yaml">
<div class="terminal-bar"><span>.github/workflows/ci.yml</span><div class="mock-tools"><span class="ico i-github"></span></div></div>
<code>name: CI</code>
<code>on: pull_request</code>
<code>jobs:</code>
<code>  test:</code>
<code>    runs-on: ubuntu-latest</code>
<code>    steps:</code>
<code>      - uses: actions/checkout@v7</code>
<code>      - uses: actions/setup-node@v7</code>
<code>        with: { node-version: 24 }</code>
<code class="hl">      - run: npm ci</code>
<code class="hl">      - run: npm test</code>
</div>
<div class="numbered">
<div><b>on</b><span>いつ動くか。PRの作成と更新</span></div>
<div><b>runs-on</b><span>どの環境で動くか</span></div>
<div><b>steps</b><span>取得、準備、テストを順に実行</span></div>
</div>
</div>
</div>

<!--
[Sources]
- https://docs.github.com/en/actions/writing-workflows/quickstart
- https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions
- https://github.com/actions/checkout/releases （v7.0.1、2026-07-20）、https://github.com/actions/setup-node/releases （v7.1.0、2026-10-08）。2026-11-25に確認
[話すこと] 「自分の手元では動いた」を、毎回まっさらな環境で確かめ直すのがCI。
npm installではなくnpm ciを使うと、package-lock.jsonどおりの版を入れるので、毎回同じ依存で試せる。
結果はPRの画面に緑のチェックか赤いバツで出る。
→ ここで実演2
-->

---

# mainへの入口を、レビューとCIの通過に絞る

<div class="fig">
<div class="lead"><b>要点</b>mainへの直接pushを止め、承認とCIの成功をmergeの条件にする。設定はbranch保護（ruleset）</div>
<div class="vsteps">
<div class="on"><i>1</i><b>PRを必須にする</b><span>mainへ直接pushできなくなる</span></div>
<div class="on"><i>2</i><b>承認を必須にする</b><span>1人以上がApproveするまでmergeできない</span></div>
<div class="on"><i>3</i><b>チェックを必須にする</b><span>CIが成功するまでmergeできない</span></div>
<div class="ng"><i>!</i><b>force pushを禁止する</b><span>mainの履歴を上書きできなくする</span></div>
</div>
<p class="cap">非公開リポジトリでは、プランによって使えない機能がある</p>
</div>

<!--
[Sources]
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
[話すこと] GitHub FreeのPrivateリポジトリでは、protected branchとrulesetが使えない（公開リポジトリと、有料プランなら使える）。
ルールをサーバー側に置くと、人もAIエージェントも同じように止まる。ただし管理者を対象外にする設定や、bypassを許す設定があるので、対象と例外を確かめる。第3章の最後でこの話に戻る
-->

---

<!-- _class: chapter -->
<!-- header: '3. AIエージェントとGit' -->

<div class="n">CHAPTER 3</div>

# AIエージェントとGit

worktreeで並列に動かし、PRで統合する

---

# worktreeは、1つのリポジトリから作業フォルダを複数作る

<div class="fig">
<div class="lead"><b>要点</b>commitとbranchは共有し、作業ツリー、HEAD、indexはフォルダごとに持つ。cloneし直すより軽い</div>
<div class="scene-grid wide">
<div class="terminal-screen tight">
<div class="terminal-bar"><span>worktreeを足す</span><div class="mock-tools"><span class="ico i-git"></span></div></div>
<code><span class="prompt">$</span> git worktree add -b feature/api ../app-api</code>
<code><span class="prompt">$</span> git worktree list</code>
<code class="output" style="margin-bottom:0">app        7453c8b [main]</code>
<code class="output" style="margin-bottom:0">app-api    7453c8b [feature/api]</code>
<code class="output">app-color  1526837 [feature/color]</code>
<code><span class="prompt">$</span> git worktree add ../dup main</code>
<code class="warn" style="margin-left:18px">fatal: 'main' is already used by worktree at …</code>
</div>
<div class="numbered">
<div><b>フォルダ</b><span>branchごとに別。互いのファイルを上書きしない</span></div>
<div><b>履歴</b><span>commitとbranchを共有。すぐ見える</span></div>
<div><b>制約</b><span>同じbranchは2か所で開けない</span></div>
</div>
</div>
</div>

<!--
[Sources]
- https://git-scm.com/docs/git-worktree
- 画面は2026-11-25の実出力。パスを短く表示している
[話すこと] 片付けはgit worktree remove ../app-api。
同じbranchを2か所で開けないのは通常の動作で（--forceで例外的に開けるが使わない）、片方のcommitでもう片方の作業ツリーと名札がずれるのを防ぐため。
node_modulesや.envのような、Git管理外のファイルはworktreeごとに用意が要る。ADEはここを自動でやってくれることが多い
-->

---

# エージェント1つに、worktree、branch、PRを1つずつ

<div class="fig">
<div class="lead"><b>要点</b>並列に作業するのはworktreeの中まで。統合はPRとCIを通し、人がレビューしてmergeする</div>
<div class="flow eq">
<div class="step"><i>1</i>タスクを分ける<small>互いに待たず、同じファイルを触らない単位</small></div>
<div class="arw">→</div>
<div class="step"><i>2</i>worktreeで並列<small>1エージェントに1つのworktreeとbranch</small></div>
<div class="arw">→</div>
<div class="step on"><i>3</i>PRとCI<small>テストが通ったPRだけをレビューに回す</small></div>
<div class="arw">→</div>
<div class="step"><i>4</i>人がmerge<small>1つずつmergeし、残りをmainに追従させる</small></div>
</div>
<div class="rule">Orca、cmux、Claude Codeのsubagentなど、道具が変わってもこの形は同じ</div>
</div>

<!--
[Sources]
- https://orca.dev/
- https://git-scm.com/docs/git-worktree
- https://docs.github.com/en/get-started/using-github/github-flow
[話すこと] 第1回の「UI、バックエンド、DB、レビューの担当を先に決める」を、Gitの仕組みに落とすとこうなる。
1つmergeしたら、残りのbranchはmainを取り込んでからCIを回し直す
-->

---

# worktreeで分けても、同じ行を触ればconflictする

<div class="fig">
<div class="lead"><b>要点</b>worktreeは作業場所を分けるだけ。並列に動かせるかは、道具ではなくタスクの分け方で決まる</div>
<div class="pair top">
<div class="pair-side">
<b>並列にしてよい</b>
<ul>
<li>画面とAPIのように、触るファイルが分かれている</li>
<li>互いの結果を待たない</li>
<li>それぞれ単独でテストできる</li>
</ul>
</div>
<div class="pair-link">vs</div>
<div class="pair-side on">
<b>順番にやる</b>
<ul>
<li>同じファイルや設定を変える</li>
<li>DBのスキーマ変更に、ほかが依存する</li>
<li>全員が同じ文脈を知っている必要がある</li>
</ul>
</div>
</div>
<div class="rule">前回の「多くのコーディングは並列化できる部分が少ない」は、ここで効いてくる</div>
</div>

<!--
[Sources]
- https://www.anthropic.com/engineering/multi-agent-research-system
[話すこと] 右側の作業を並列に投げると、conflictの解消やずれの手直しで、並列にした分以上の時間がかかる。
スキーマ変更のような土台の変更を先にmergeしてから、その上で並列に分けるのが定石
-->

---

# 危ないGit操作は、hookとbranch保護の2か所で止める

<div class="fig">
<div class="lead"><b>要点</b>エージェントへの指示文に書くだけでは破られる。手元ではhookが止め、GitHubではbranch保護が止める</div>
<div class="tblwrap">
<table class="compare full">
<colgroup><col style="width:34%"><col style="width:33%"><col style="width:33%"></colgroup>
<thead><tr><th>止めたい操作</th><th>手元（PreToolUse hook）</th><th>GitHub（branch保護）</th></tr></thead>
<tbody>
<tr><th>mainへ直接pushしない</th><td class="ok">止める</td><td class="ok">止める</td></tr>
<tr><th>force pushしない</th><td class="ok">止める</td><td class="ok">止める</td></tr>
<tr><th>テストが通ってからmerge</th><td>完了前に実行させる</td><td class="ok">必須チェック</td></tr>
<tr><th>秘密のファイルをcommitしない</th><td class="ok">止める</td><td>push後では遅い</td></tr>
</tbody>
</table>
</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/hooks （PreToolUse）
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
- https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection （push protection）
[話すこと] 第2回の「確実に守らせたいものほど、下の段へ置く」をGitに当てはめた表。
hookは手元のエージェントには効くが、別のマシンや人の操作には効かない。サーバー側のbranch保護は、どのマシンからのpushにも効く（管理者やbypassの例外設定は確かめる）。
秘密はpushした時点で漏れたものとして扱うので、手元で止める。GitHubのpush protectionも、既知の形式のトークンを含むpushを止められる
-->

---

<!-- header: 'まとめ' -->

# 今日のまとめ

<div class="fig">
<div class="vsteps">
<div><i>0</i><b>おさらい</b><span>Grok Botは正式版に。Orca Botsは自分のマシンでエージェントを動かす</span></div>
<div><i>1</i><b>Gitの仕組み</b><span>commitはスナップショット。branchで枝分かれし、mergeで合流する</span></div>
<div><i>2</i><b>GitHubでのチーム開発</b><span>小さなPR、レビュー、CI。mainへの入口をbranch保護で絞る</span></div>
<div><i>3</i><b>AIエージェントとGit</b><span>1エージェント1worktree。並列にできるかはタスクの分け方で決まる</span></div>
</div>
</div>

<!--
[話すこと] 今日から試すなら、手元のリポジトリでgit worktree addを1回やってみる。
自分のリポジトリにCIを1本置き、mainを保護する
-->
