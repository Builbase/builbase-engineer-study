---
marp: true
theme: deck
paginate: false
size: 16:9
title: ターミナルとエディタ / AIを複数体動かす
description: builbaseエンジニア勉強会（60分）
author: seiji
---

<!-- _class: title -->

# エンジニア勉強会

<p>
第1回 ターミナルとエディタ／AIを複数体動かす<br>
2026-08-28 18:00–19:00
</p>

---

<!-- header: 'はじめに' -->
# なぜやるのか

<div class="fig">
<div class="row c2">
<div class="card">
<span class="gi lg g-growth"></span>
<div class="t">スキルを上げる</div>
<div class="d">知識の幅を広げる</div>
</div>
<div class="card on">
<span class="gi lg g-bolt dark"></span>
<div class="t">仕事を速くする</div>
<div class="d">日々のタスクを効率化する</div>
</div>
</div>
</div>

---

# 進め方と、これからの開催

<div class="rows">
<div class="row c2">
<div class="card flat">
<div class="ai navy"><div class="glyph"></div></div>
<div class="t">基本は私が話します</div>
<div class="d">説明しながら進めます</div>
</div>
<div class="card on">
<span class="gi g-chat"></span>
<div class="t">いつでも聞いてください</div>
<div class="d">気になったところは、その場で<br>聞いてもらえると助かります</div>
</div>
</div>
<div class="row c3">
<div class="card flat">
<span class="gi g-calendar"></span>
<div class="t">第2・第4月曜</div>
<div class="d">毎月2回</div>
</div>
<div class="card flat">
<span class="gi g-bolt"></span>
<div class="t">18:00–19:00</div>
<div class="d">1時間</div>
</div>
<div class="card flat">
<span class="gi g-doc"></span>
<div class="t">毎回ちがうテーマ</div>
<div class="d">次回もお待ちしています</div>
</div>
</div>
</div>

---

# 今日の内容

<div class="fig">
<div class="row c2">
<div class="card">
<div class="t">1. ターミナルとエディタ</div>
<div class="d">道具の役割を分けて、使いどころを選ぶ</div>
</div>
<div class="card on">
<div class="t">2. AIを複数体動かす</div>
<div class="d">独立した仕事だけを、安全に並列化する</div>
</div>
</div>
</div>

---

<!-- _class: chapter -->
<!-- header: '1. ターミナルとエディタ' -->

<div class="n">CHAPTER 1</div>

# ターミナルとエディタ

違いは、画面の色ではなく主役にする作業

---

# 道具は3つの層に分けると混ざらない

<div class="fig">
<div class="layer-stack">
<div class="layer">
<span class="layer-no">1</span>
<div><b>エディタ</b><small>コードを読む、直す</small></div>
<div class="logos"><span class="ico ico-lg i-vscode"></span><span class="ico ico-lg i-cursor"></span></div>
</div>
<div class="layer on">
<span class="layer-no">2</span>
<div><b>ターミナル環境</b><small>CLIセッションを表示、整理する</small></div>
<div class="logos"><span class="ico ico-lg i-ghostty"></span><span class="ico ico-lg i-cmux"></span><span class="ico ico-lg i-herdr"></span></div>
</div>
<div class="layer">
<span class="layer-no">3</span>
<div><b>CLIエージェント</b><small>コードを調査、変更、検証する</small></div>
<div class="logos"><span class="ico ico-lg i-claude"></span><span class="ico ico-lg i-codex"></span></div>
</div>
</div>
</div>

<!--
[Sources]
- https://ghostty.org/docs/features
- https://code.visualstudio.com/docs/editing/userinterface
- https://code.claude.com/docs/en/overview
- https://developers.openai.com/codex/cli/
-->

---

# ターミナルは、コマンドの入出力を映す窓

<div class="fig">
<div class="scene-grid">
<div class="terminal-screen">
<div class="terminal-bar">Terminal</div>
<code><span class="prompt">$</span> npm test</code>
<code class="output">✓ 24 tests passed</code>
<code><span class="prompt">$</span> git status</code>
<code class="output">nothing to commit</code>
</div>
<div class="numbered">
<div><b>1. ターミナル</b><span>文字を受け取り、結果を描画する</span></div>
<div><b>2. シェル</b><span>zshやbashがコマンドを解釈する</span></div>
<div><b>3. プログラム</b><span>gitやnpm、AIエージェントが動く</span></div>
</div>
</div>
<p class="cap">黒い画面の中にも、別々の役割がある</p>
</div>

<!--
[Sources]
- MIT Missing Semester, The Shell: https://missing.csail.mit.edu/2020/course-shell/
- Video, 4:12–6:22: https://www.youtube.com/watch?v=Z56Jmr9Z34Q
-->

---

# エディタは、ファイルを読んで書く作業台

<div class="fig">
<div class="scene-grid">
<div class="win three editor-scene">
<div class="bar"><i></i><i></i><i></i><b>Editor</b></div>
<div class="body">
<div class="p"><div class="h">フォルダ</div><div class="ln m"></div><div class="ln s"></div><div class="ln b l"></div><div class="ln s"></div></div>
<div class="p"><div class="h">コード</div><div class="ln l"></div><div class="ln k m"></div><div class="ln s"></div><div class="ln l"></div></div>
<div class="p"><div class="h">診断</div><div class="stat"><i class="wait"></i>1 error</div><div class="stat"><i class="done"></i>Git diff</div></div>
</div>
</div>
<div class="numbered">
<div><b>1. 探す</b><span>フォルダ、検索、定義移動</span></div>
<div><b>2. 直す</b><span>補完や診断を見ながら編集</span></div>
<div><b>3. 確かめる</b><span>差分、Git、デバッグ、テスト</span></div>
</div>
</div>
</div>

<!--
[Sources]
- VS Code beginner video, 2026: https://www.youtube.com/watch?v=f8_uF_IDV50
- https://code.visualstudio.com/docs/editing/getting-started
- https://code.visualstudio.com/docs/editing/userinterface
-->

---

# ターミナルとエディタは同時に使える

<div class="fig">
<div class="pair">
<div class="pair-side">
<div class="logos"><span class="ico ico-lg i-vscode"></span><span class="ico ico-lg i-cursor"></span></div>
<b>エディタの内蔵ターミナル</b>
<span>コードを見ながら、同じシェルとCLIを使う</span>
</div>
<div class="pair-link">⇄</div>
<div class="pair-side on">
<div class="logos"><span class="ico ico-lg i-ghostty"></span><span class="ico ico-lg i-cmux"></span></div>
<b>ターミナルからエディタを開く</b>
<span>CLIを主役にし、必要なときだけコードを見る</span>
</div>
</div>
<div class="rule">選ぶのは道具ではなく、どこに注意を置くか</div>
</div>

<!--
[Sources]
- https://code.visualstudio.com/docs/terminal/basics
- https://ghostty.org/docs/features
-->

---

# VS CodeとCursorは、強みの置き方が違う

<div class="fig">
<table class="compare">
<thead><tr><th></th><th>強み</th><th>注意点</th><th>向いている場面</th></tr></thead>
<tbody>
<tr><th><span class="ico i-vscode"></span>VS Code</th><td>広い拡張機能、Git、デバッグ、内蔵ターミナル</td><td>拡張機能の選定と権限確認が必要</td><td>基礎を学び、チーム標準へ合わせる</td></tr>
<tr class="on"><th><span class="ico i-cursor"></span>Cursor</th><td>VS Code系の操作感にAIと複数エージェントを統合</td><td>料金枠、AIの権限、拡張機能の差を確認</td><td>AI中心で実装し、差分を画面で読む</td></tr>
</tbody>
</table>
<p class="cap">2026年時点では、どちらもエディタ内でAIセッションを扱える</p>
</div>

<!--
[Sources]
- https://code.visualstudio.com/docs/core-editor/overview
- https://code.visualstudio.com/docs/agents/run/agents-window
- https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security
- https://docs.cursor.com/get-started/migrate-from-vs-code
- https://prod.cursor.com/help/ai-features/multi-agent
- https://cursor.com/docs/configuration/worktrees
-->

---

# ターミナル環境は、管理したい規模で選ぶ

<div class="fig">
<table class="compare terminal-tools">
<thead><tr><th></th><th>強み</th><th>注意点</th><th>向いている場面</th></tr></thead>
<tbody>
<tr><th><span class="ico i-ghostty"></span>Ghostty</th><td>軽快な描画、タブ、分割。汎用の土台</td><td>AIの状態管理は別の道具が必要</td><td>少数のCLIセッション</td></tr>
<tr class="on"><th><span class="ico i-cmux"></span>cmux</th><td>縦タブ、分割、通知、ブラウザを一画面へ集約</td><td>macOS限定。仕事の分割は人間が決める</td><td>Macで複数セッションを見渡す</td></tr>
<tr><th><span class="ico i-herdr"></span>Herdr</th><td>セッションを常駐させ、別端末から再接続できる</td><td>サーバーとattach／detachの理解が必要</td><td>長時間のCLI作業へ戻る</td></tr>
</tbody>
</table>
</div>

<!--
[Sources]
- https://ghostty.org/docs/features
- https://github.com/manaflow-ai/cmux
- https://www.youtube.com/watch?v=i-WxO5YUTOs
- https://herdr.dev/
- https://herdr.dev/docs/
-->

---

# Ghosttyは、軽快な汎用ターミナル

<div class="fig">
<div class="terminal-profile">
<div class="terminal-brand">
<span class="terminal-logo i-ghostty"></span>
<b>Ghostty</b>
<span class="terminal-kind">汎用ターミナル</span>
<p class="terminal-fit"><b>向く場面</b><span>普段の開発と、少数のCLIセッション</span></p>
</div>
<div class="terminal-points">
<div class="terminal-point strength">
<h2>強み</h2>
<ul>
<li>GPU描画とネイティブUIで軽快</li>
<li>タブ、分割、複数ウインドウを標準搭載</li>
<li>macOSとLinuxで使える</li>
</ul>
</div>
<div class="terminal-point weakness">
<h2>弱み</h2>
<ul>
<li>Windows版はまだない</li>
<li>AIの入力待ちは、自分でタブや分割を追う</li>
</ul>
</div>
</div>
</div>
</div>

<!--
[Sources]
- https://ghostty.org/docs/features
- https://github.com/ghostty-org/ghostty
- Icon: https://raw.githubusercontent.com/ghostty-org/ghostty/main/images/icons/icon_512.png
- AIセッション管理の注意点は、Ghosttyが汎用ターミナルであることとcmux開発者の利用記述からの推論: https://github.com/manaflow-ai/cmux
-->

---

# cmuxは、複数AIを見渡せる

<div class="fig">
<div class="terminal-profile reverse">
<div class="terminal-brand">
<span class="terminal-logo i-cmux"></span>
<b>cmux</b>
<span class="terminal-kind">AI作業向けターミナル</span>
<p class="terminal-fit"><b>向く場面</b><span>Macで複数のAIセッションを動かす</span></p>
</div>
<div class="terminal-points">
<div class="terminal-point strength">
<h2>強み</h2>
<ul>
<li>縦タブに作業場所、Git、通知を集約</li>
<li>入力待ちを色と通知で見つけやすい</li>
<li>ターミナルとブラウザを並べて操作できる</li>
</ul>
</div>
<div class="terminal-point weakness">
<h2>弱み</h2>
<ul>
<li>macOS専用</li>
<li>誰に何を任せるかは、人が設計する</li>
</ul>
</div>
</div>
</div>
</div>

<!--
[Sources]
- https://cmux.com/
- https://github.com/manaflow-ai/cmux
- https://github.com/manaflow-ai/cmux/blob/main/docs/notifications.md
- Icon: https://cmux.com/brand/app-icon-light.png
-->

---

# Herdrは、長時間の作業へ戻れる

<div class="fig">
<div class="terminal-profile">
<div class="terminal-brand">
<span class="terminal-logo i-herdr"></span>
<b>Herdr</b>
<span class="terminal-kind">常駐型のターミナル管理</span>
<p class="terminal-fit"><b>向く場面</b><span>長時間のAI作業へ、別の端末から戻る</span></p>
</div>
<div class="terminal-points">
<div class="terminal-point strength">
<h2>強み</h2>
<ul>
<li>サーバーが動く間は、切断しても処理が続く</li>
<li>別のターミナルやSSHから再接続できる</li>
<li>working、blocked、idleを見分けられる</li>
</ul>
</div>
<div class="terminal-point weakness">
<h2>弱み</h2>
<ul>
<li>サーバー起動とdetach／reattachを覚える</li>
<li>サーバー再起動では、実行中プロセスは戻らない</li>
<li>未対応AIは、詳細な状態表示や復元に限界がある</li>
</ul>
</div>
</div>
</div>
</div>

<!--
[Sources]
- https://herdr.dev/
- https://herdr.dev/docs/
- https://herdr.dev/docs/session-state/
- https://herdr.dev/docs/agents/
- https://github.com/herdrdev/herdr
- Icon: https://raw.githubusercontent.com/herdrdev/herdr/master/assets/logo.png
-->

---

# Claude CodeとCodexは、ターミナルの中で動く

<div class="fig">
<div class="row c2">
<div class="card">
<div class="logos"><span class="ico ico-lg i-claude"></span><span class="ico ico-lg i-codex"></span></div>
<div class="t">できること</div>
<div class="d">リポジトリを調査し、編集し、<br>コマンドで検証する</div>
</div>
<div class="card on">
<span class="gi lg g-doc dark"></span>
<div class="t">人間が見ること</div>
<div class="d">権限、実行コマンド、差分、<br>テスト結果、残ったリスク</div>
</div>
</div>
<p class="cap">エージェントの停止と、成果物の完成は別</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/overview
- https://developers.openai.com/codex/cli/
-->

---

# cmuxなら、CLIセッションを一画面で追える

<div class="fig">
<div class="win three">
<div class="bar"><i></i><i></i><i></i><span class="ico i-cmux"></span><b>cmux</b></div>
<div class="body" style="height:300px">
<div class="p"><div class="h">セッション</div><div class="stat"><i class="run"></i>プロジェクトA／実行中</div><div class="stat"><i class="wait"></i>プロジェクトB／入力待ち</div><div class="stat"><i class="run"></i>プロジェクトC／実行中</div><div class="stat"><i class="done"></i>プロジェクトD／停止</div></div>
<div class="p dark"><div class="ln d l"></div><div class="ln dg m"></div><div class="ln d s"></div><div class="ln d l"></div><div class="ln dg m"></div></div>
<div class="p"><div class="h">ブラウザ／別ペイン</div><div class="ln m"></div><div class="ln s"></div><div class="ln b l"></div><div class="ln s"></div></div>
</div>
</div>
<p class="cap">通知と一覧は「戻る場所」を教える。成果の正しさは差分とテストで確かめる</p>
</div>

<!--
[Sources]
- https://github.com/manaflow-ai/cmux
- https://www.youtube.com/watch?v=i-WxO5YUTOs
-->

---

# 使い分けは「どこに注意を置くか」で決まる

<div class="fig">
<div class="attention-scale">
<div class="attention-side">
<div class="logos"><span class="ico ico-lg i-vscode"></span><span class="ico ico-lg i-cursor"></span></div>
<b>コードに注意を置く</b><span>読む、直す、デバッグする</span>
</div>
<div class="attention-line"><i></i></div>
<div class="attention-side on">
<div class="logos"><span class="ico ico-lg i-cmux"></span><span class="ico ico-lg i-herdr"></span></div>
<b>セッションに注意を置く</b><span>複数の実行、入力待ち、通知を追う</span>
</div>
</div>
<p class="cap">一方を捨てる必要はない。作業に合わせて主役を入れ替える</p>
</div>

<!--
[Sources]
- https://code.visualstudio.com/docs/agents/run/agents-window
- https://github.com/manaflow-ai/cmux
- https://herdr.dev/docs/
-->

---

<!-- _class: chapter -->
<!-- header: '2. AIを複数体動かす' -->

<div class="n">CHAPTER 2</div>

# AIを複数体動かす

増やす前に、並列化できる仕事かを見極める

---

# 「複数体動かす」には2種類ある

<div class="fig">
<div class="row c2">
<div class="card">
<div class="row c3 ai-row"><div class="ai sm blue"><div class="glyph"></div></div><div class="ai sm blue"><div class="glyph"></div></div><div class="ai sm blue"><div class="glyph"></div></div></div>
<div class="t">A. 違うプロジェクト</div><div class="d">別々の案件を、同時に進める</div>
</div>
<div class="card on">
<div class="row c4 ai-row"><div class="ai sm blue"><div class="glyph"></div></div><div class="ai sm navy"><div class="glyph"></div></div><div class="ai sm gray"><div class="glyph"></div></div><div class="ai sm green"><div class="glyph"></div></div></div>
<div class="t">B. 1つのプロジェクト</div><div class="d">依存しない仕事へ分け、結果を統合する</div>
</div>
</div>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://code.claude.com/docs/en/agent-teams
-->

---

<!-- _header: '2. AIを複数体動かす／A. 違うプロジェクト' -->

# A. 違うプロジェクトは、待ち時間を重ねられる

<div class="fig">
<div class="row c3 project-row">
<div class="proj"><div class="ai blue"><div class="glyph"></div></div><div class="box">プロジェクトA</div></div>
<div class="proj"><div class="ai blue"><div class="glyph"></div></div><div class="box">プロジェクトB</div></div>
<div class="proj"><div class="ai blue"><div class="glyph"></div></div><div class="box">プロジェクトC</div></div>
</div>
<div class="flow compact-flow">
<div class="step on">指示する</div><div class="arw">→</div><div class="step">別の仕事へ移る</div><div class="arw">→</div><div class="step on">通知で戻る</div><div class="arw">→</div><div class="step">差分を確認する</div>
</div>
<p class="cap">特別な分散処理ではない。人間が複数の待ち時間を管理している</p>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/long-running-work
- https://code.visualstudio.com/docs/agents/run/agents-window
-->

---

<!-- _header: '2. AIを複数体動かす／A. 違うプロジェクト' -->

# 「止まった」と「終わった」を分けて見る

<div class="fig">
<div class="row c3 state-row">
<div class="card flat"><div class="status-dot run"></div><div class="t">実行中</div><div class="d">まだ手を出さず、別の仕事へ</div></div>
<div class="card on"><div class="status-dot wait"></div><div class="t">入力待ち</div><div class="d">承認、質問、追加情報を返す</div></div>
<div class="card"><div class="status-dot done"></div><div class="t">停止</div><div class="d">差分とテストを見て、完成か判断</div></div>
</div>
<div class="rule">通知は注意を戻す仕組み。品質を保証する仕組みではない</div>
</div>

<!--
[Sources]
- https://github.com/manaflow-ai/cmux
- https://herdr.dev/docs/
- https://learn.chatgpt.com/docs/long-running-work
-->

---

<!-- _class: chapter -->
<!-- header: '2. AIを複数体動かす／B. 1つのプロジェクト' -->

<div class="n">CHAPTER 2／本命</div>

# B. 1つのプロジェクトを4つの担当に分ける

4体を一斉に動かす前に、役割を決める

---

<!-- _header: '2. AIを複数体動かす／B. 1つのプロジェクト' -->

# コードを書く前に、全員が読む設計メモを作る

<div class="fig">
<div class="plan-layout">
<div class="plan-paper">
<div class="plan-paper-title">Todoアプリの設計メモ</div>
<div><b>画面</b><span>一覧、追加、完了ボタン</span></div>
<div><b>機能</b><span>Todoを追加して、完了にできる</span></div>
<div><b>データ</b><span>タイトルと完了状態を保存する</span></div>
<div><b>完成</b><span>追加と完了切り替えが動く</span></div>
</div>
<div class="plan-voice">
<div class="ai navy"><div class="glyph"></div></div>
<p>いきなり<br>「全部作って」<br>とは頼まない</p>
</div>
</div>
<p class="cap">全員が同じ設計メモを読んでから、担当を渡す</p>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/long-running-work
- https://learn.chatgpt.com/docs/features
- https://code.claude.com/docs/en/agent-teams
-->

---

<!-- _header: '2. AIを複数体動かす／B. 1つのプロジェクト' -->

# Todoアプリを4つの担当に分ける

<div class="fig">
<div class="role-cast">
<div class="role-person">
<span class="role-number">1</span>
<div class="ai blue"><div class="glyph"></div></div>
<b>UI担当</b><span>画面を作る</span>
</div>
<div class="role-person">
<span class="role-number">2</span>
<div class="ai navy"><div class="glyph"></div></div>
<b>バックエンド担当</b><span>機能とAPIを作る</span>
</div>
<div class="role-person">
<span class="role-number">3</span>
<div class="ai gray"><div class="glyph"></div></div>
<b>DB担当</b><span>データを保存する</span>
</div>
<div class="role-person review">
<span class="role-number">4</span>
<div class="ai green"><div class="glyph"></div></div>
<b>レビュー担当</b><span>3つを合わせて確認する</span>
</div>
</div>
<div class="rule">4体を使う最初のコツは、役割を混ぜないこと</div>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://code.claude.com/docs/en/agent-teams
-->

---

<!-- _header: '2. AIを複数体動かす／B. 1つのプロジェクト' -->

# 待たなくてよい3担当だけ、同時に進める

<div class="fig">
<div class="parallel-board">
<div class="parallel-left">
<div class="parallel-source">共通の設計メモ</div>
<div class="parallel-down">↓</div>
<div class="parallel-runs">
<div><span>1</span><b>UI担当</b><small>仮のデータで画面</small></div>
<div><span>2</span><b>バックエンド担当</b><small>機能とAPI</small></div>
<div><span>3</span><b>DB担当</b><small>保存の仕組み</small></div>
</div>
</div>
<div class="parallel-next">→<small>3つが<br>終わったら</small></div>
<div class="parallel-review">
<div class="ai green"><div class="glyph"></div></div>
<b>4. レビュー担当</b>
<span>最後に3つを合わせる</span>
</div>
</div>
<div class="rule">同じファイルを触る作業は、同時に進めない</div>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://code.claude.com/docs/en/agent-teams
- https://docs.github.com/en/copilot/concepts/agents/copilot-cli/fleet
-->

---

<!-- _header: '2. AIを複数体動かす／B. 1つのプロジェクト' -->

# 「担当」だけでなく、ゴールまで決める

<div class="fig">
<div class="outcome-list">
<div><span class="outcome-no">1</span><b>UI担当</b><p>Todo一覧と追加フォーム</p><small>仮のデータで画面を確認</small></div>
<div><span class="outcome-no">2</span><b>バックエンド担当</b><p>追加、取得、更新の機能</p><small>APIのテストまで実行</small></div>
<div><span class="outcome-no">3</span><b>DB担当</b><p>Todoの保存と読み出し</p><small>データが残ることを確認</small></div>
</div>
<p class="cap">「バックエンドをお願い」だけでは、どこで終わるか分からない</p>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/long-running-work
- https://www.anthropic.com/engineering/multi-agent-research-system
-->

---

<!-- _header: '2. AIを複数体動かす／B. 1つのプロジェクト' -->

# AIへの指示は、4行で書く

<div class="fig">
<div class="prompt-layout">
<div class="prompt-person">
<div class="ai blue"><div class="glyph"></div></div>
<b>UI担当へ</b>
</div>
<div class="prompt-arrow">→</div>
<div class="prompt-paper">
<div><b>やること</b><span>Todo一覧画面を作る</span></div>
<div><b>触る場所</b><span>画面のフォルダ</span></div>
<div><b>触らない場所</b><span>APIとDBのフォルダ</span></div>
<div><b>終わりの条件</b><span>画面表示とテストが通る</span></div>
</div>
</div>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/long-running-work
- https://www.anthropic.com/engineering/multi-agent-research-system
-->

---

<!-- _header: '2. AIを複数体動かす／B. 1つのプロジェクト' -->

# 同じファイルは、2体で触らない

<div class="fig">
<div class="scene-grid conflict-layout">
<div class="conflict-scene">
<div class="conflict-person"><div class="ai blue"><div class="glyph"></div></div><b>UI担当</b></div>
<div class="conflict-file"><strong>×</strong><b>Todo.tsx</b><span>2体が同時に編集</span></div>
<div class="conflict-person"><div class="ai navy"><div class="glyph"></div></div><b>バックエンド担当</b></div>
</div>
<div class="numbered">
<div><b>1. 場所を分ける</b><span>UI、API、DBの担当を分ける</span></div>
<div><b>2. 重なるなら待つ</b><span>先に一方を終わらせる</span></div>
<div><b>3. 小さければ1体</b><span>無理に並列にしない</span></div>
</div>
</div>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://learn.chatgpt.com/docs/environments/git-worktrees
- https://code.claude.com/docs/en/worktrees
-->

---

<!-- _header: '2. AIを複数体動かす／B. 1つのプロジェクト' -->

# レビュー担当は、3人の完成を待つ

<div class="fig">
<div class="review-merge">
<div class="review-inputs">
<div><span class="review-dot blue"></span><b>UI</b><small>画面</small></div>
<div><span class="review-dot navy"></span><b>バックエンド</b><small>機能とAPI</small></div>
<div><span class="review-dot gray"></span><b>DB</b><small>保存</small></div>
</div>
<div class="review-arrow">→</div>
<div class="review-person">
<div class="ai green"><div class="glyph"></div></div>
<b>レビュー担当</b><span>3つをつなげて動かす</span>
</div>
<div class="review-arrow">→</div>
<div class="review-checks">
<div>画面から操作できる</div>
<div>データを保存できる</div>
<div>全体テストが通る</div>
</div>
</div>
<div class="rule">別のAIが「大丈夫」と言っても、最後は人が確認する</div>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://code.claude.com/docs/en/agent-teams
- https://www.anthropic.com/engineering/multi-agent-research-system
-->

---

<!-- _header: '2. AIを複数体動かす／B. 1つのプロジェクト' -->

# うまくいかないときは、3か所を確認する

<div class="fig">
<div class="mistake-list">
<div><span>1</span><b>同じファイルを直した</b><i>→</i><strong>担当場所を分ける</strong></div>
<div><span>2</span><b>UIとAPIの形が違った</b><i>→</i><strong>設計メモをそろえる</strong></div>
<div><span>3</span><b>レビューを早く始めた</b><i>→</i><strong>3担当の完成を待つ</strong></div>
</div>
<div class="rule">迷ったら、同時に動かす数を減らす</div>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/long-running-work
- https://learn.chatgpt.com/docs/environments/git-worktrees
- https://www.anthropic.com/engineering/multi-agent-research-system
-->

---

# 今日から試す3つ

<div class="fig">
<div class="closing-path">
<div><span class="gi lg g-split"></span><b>役割を分ける</b><small>UI、機能、DB、レビュー</small></div>
<span class="closing-arrow">→</span>
<div><span class="gi lg g-doc"></span><b>担当を文章で渡す</b><small>やること、場所、終わり</small></div>
<span class="closing-arrow">→</span>
<div class="on"><span class="gi lg g-bolt dark"></span><b>人が動かして確認する</b><small>AIの報告だけで終わらせない</small></div>
</div>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://learn.chatgpt.com/docs/long-running-work
- https://learn.chatgpt.com/docs/environments/git-worktrees
-->
