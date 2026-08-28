---
marp: true
theme: deck
paginate: false
size: 16:9
title: ターミナルとエディタ / 複数のAIエージェントを動かす
description: builbaseエンジニア勉強会（60分）
author: seiji
---

<!-- _class: title -->

# エンジニア勉強会

<p>
第1回 ターミナルとエディタ／複数のAIエージェントを動かす<br>
2026-08-28 18:00–19:00
</p>

---

<!-- header: 'はじめに' -->
# この勉強会で持ち帰ること

<div class="fig">
<div class="row c2">
<div class="card">
<span class="gi lg g-growth"></span>
<div class="t">道具を役割で選ぶ</div>
<div class="d">名前ではなく、何をする道具かで考える</div>
</div>
<div class="card on">
<span class="gi lg g-bolt dark"></span>
<div class="t">AIの待ち時間を使う</div>
<div class="d">処理中に、別の独立した仕事へ移る</div>
</div>
</div>
</div>

---

# 今日の内容

<div class="fig">
<div class="row c2">
<div class="card">
<div class="t">1. 開発の道具を役割で考える</div>
<div class="d">エディタ、ターミナル、CLIエージェント</div>
</div>
<div class="card on">
<div class="t">2. 複数のAIエージェントを動かす</div>
<div class="d">独立した仕事だけを、同時に進める</div>
</div>
</div>
</div>

---

<!-- _class: chapter -->
<!-- header: '1. 開発の道具を3つの役割で考える' -->

<div class="n">CHAPTER 1</div>

# 開発の道具を3つの役割で考える

エディタ、ターミナル、CLIエージェントは役割が違う

---

# 3つの役割を分けて考える

<div class="fig">
<div class="layer-stack">
<div class="layer">
<span class="layer-no">1</span>
<div><b>エディタ</b><small>コードを読む、直す</small></div>
<div class="logos chips"><span class="ico ico-lg i-vscode"></span><span class="ico ico-lg i-cursor"></span></div>
</div>
<div class="layer on">
<span class="layer-no">2</span>
<div><b>ターミナル</b><small>文字の入力と出力を表示する</small></div>
<div class="logos chips"><span class="ico ico-lg i-macterminal"></span><span class="ico ico-lg i-winterminal"></span><span class="ico ico-lg i-ghostty"></span></div>
</div>
<div class="layer">
<span class="layer-no">3</span>
<div><b>CLIエージェント</b><small>指示を受け、調査、編集、確認を進める</small></div>
<div class="logos chips"><span class="ico ico-lg i-claude"></span><span class="ico ico-lg i-codex"></span></div>
</div>
</div>
</div>

<!--
[Sources]
- https://ghostty.org/docs/features
- https://code.visualstudio.com/docs/editing/userinterface
- https://code.claude.com/docs/en/overview
- https://developers.openai.com/codex/cli/
- https://code.visualstudio.com/docs/agents/run/agents-window
- https://docs.cursor.com/get-started/migrate-from-vs-code
- https://prod.cursor.com/help/ai-features/multi-agent

[話すこと] VS CodeとCursorの違いは口頭で補う。2026年時点ではどちらもエディタ内で
AIセッションを扱える。VS Codeは拡張とGitまわりが厚く、CursorはAIと
複数エージェントが最初から入っている。表にすると読ませてしまうのでスライドには出さない
-->

---

# ① エディタは、ファイルを読んで書く作業台

<div class="fig">
<div class="scene-grid">
<div class="win three editor-scene">
<div class="bar"><i></i><i></i><i></i><b>エディタ</b><div class="mock-tools"><span class="ico i-vscode"></span><span class="ico i-cursor"></span></div></div>
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

# ② ターミナルは、コマンドの入出力を映す窓

<div class="fig">
<div class="scene-grid">
<div class="terminal-screen">
<div class="terminal-bar"><span>ターミナル</span><div class="mock-tools"><span class="ico i-ghostty"></span><span class="ico i-cmux"></span></div></div>
<code><span class="prompt">$</span> npm test</code>
<code class="output">✓ 24 tests passed</code>
<code><span class="prompt">$</span> git status</code>
<code class="output">nothing to commit</code>
</div>
<div class="numbered">
<div><b>1. ターミナル</b><span>入力を受け取り、出力を表示する</span></div>
<div><b>2. シェル</b><span>zshやbashがコマンドを解釈する</span></div>
<div><b>3. プログラム</b><span>gitやnpm、AIエージェントが動く</span></div>
</div>
</div>
<p class="cap">同じ画面の中で、ターミナル、シェル、プログラムが連携する</p>
</div>

<!--
[Sources]
- MIT Missing Semester, The Shell: https://missing.csail.mit.edu/2020/course-shell/
- Video, 4:12–6:22: https://www.youtube.com/watch?v=Z56Jmr9Z34Q
-->

---

# ③ CLIエージェントは、調査、編集、確認を進める

<div class="fig">
<div class="scene-grid">
<div class="terminal-screen">
<div class="terminal-bar"><span>CLIエージェント</span><div class="mock-tools"><span class="ico i-claude"></span><span class="ico i-codex"></span></div></div>
<code><span class="prompt">&gt;</span> ログイン画面のバグを直して</code>
<code class="output">Read  src/Login.tsx</code>
<code class="output">Edit  src/Login.tsx</code>
<code class="output">Run   npm test  → 24 passed</code>
<code class="output">差分を確認してください</code>
</div>
<div class="numbered">
<div><b>1. 調べる</b><span>どのファイルが関係するかを自分で探す</span></div>
<div><b>2. 直す</b><span>ファイルを書き換える</span></div>
<div><b>3. 確かめる</b><span>コマンドを実行して結果を見る</span></div>
</div>
</div>
<p class="cap">人が確認するのは、権限、実行コマンド、差分、テスト結果。処理の停止と作業の完了は別</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/overview
- https://developers.openai.com/codex/cli/
-->
---

# エディタとターミナルは併用できる

<div class="fig">
<div class="pair">
<div class="pair-side">
<div class="logos chips"><span class="ico ico-lg i-vscode"></span><span class="ico ico-lg i-cursor"></span></div>
<b>エディタの内蔵ターミナル</b>
<span>コードを見ながら、シェルやCLIツールを使う</span>
</div>
<div class="pair-link">⇄</div>
<div class="pair-side on">
<div class="logos chips"><span class="ico ico-lg i-ghostty"></span><span class="ico ico-lg i-cmux"></span></div>
<b>ターミナルからエディタを開く</b>
<span>コマンド操作を中心にし、必要なときにコードを見る</span>
</div>
</div>
<div class="rule">一方を捨てず、作業に合わせて主役を入れ替える</div>
</div>

<!--
[Sources]
- https://code.visualstudio.com/docs/terminal/basics
- https://ghostty.org/docs/features
-->

---

<!-- _class: header-offset -->

# VS CodeとCursorは、強みの置き方が違う

<div class="fig">
<table class="compare">
<thead><tr><th></th><th>強み</th><th>確認したい点</th><th>向いている場面</th></tr></thead>
<tbody>
<tr><th><span class="ico i-vscode"></span>VS Code</th><td>拡張機能、Git、デバッグ、リモート開発が充実</td><td>AI体験は拡張機能、設定、利用プランで変わる</td><td>基礎を学び、チームの環境へ合わせる</td></tr>
<tr class="on"><th><span class="ico i-cursor"></span>Cursor</th><td>コード理解、複数箇所の編集、エージェント操作へ入りやすい</td><td>AI機能の利用枠と、製品固有の操作を確認する</td><td>AIを中心に実装し、差分を画面で読む</td></tr>
</tbody>
</table>
<p class="cap">どちらもAIエージェントを扱える。AI以外の開発機能とチームの環境も含めて選ぶ</p>
</div>

<!--
[Sources]
- https://code.visualstudio.com/docs/core-editor/overview
- https://code.visualstudio.com/docs/agents/run/agents-window
- https://code.visualstudio.com/docs/remote/remote-overview
- https://docs.cursor.com/get-started/migrate-from-vs-code
- https://cursor.com/docs/agent/overview
-->

---

# ターミナル環境は、困りごとに合わせて選ぶ

<div class="fig">
<table class="compare terminal-tools">
<thead><tr><th></th><th>強み</th><th>確認したい点</th><th>向いている場面</th></tr></thead>
<tbody>
<tr><th><span class="ico i-ghostty"></span>Ghostty</th><td>軽快な描画、タブ、分割。普段使いの土台</td><td>AIの状態一覧は持たない</td><td>少数のCLIセッション</td></tr>
<tr class="on"><th><span class="ico i-cmux"></span>cmux</th><td>作業場所、Git、通知、ブラウザを一画面へ集約</td><td>macOS専用。仕事の分け方は人が決める</td><td>複数のセッションを見渡す</td></tr>
<tr><th><span class="ico i-herdr"></span>Herdr</th><td>セッションを維持し、別の端末から再接続できる</td><td>サーバーとdetach／reattachを覚える</td><td>長時間のCLI作業へ戻る</td></tr>
</tbody>
</table>
</div>

<!--
[Sources]
- https://ghostty.org/docs/features
- https://github.com/manaflow-ai/cmux
- https://cmux.com/
- https://herdr.dev/
- https://herdr.dev/docs/
-->

---

<!-- _class: header-title-offset -->

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
<li>Windows版はまだ提供されていない</li>
<li>AIの入力待ちは、タブや分割から自分で追う</li>
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
-->

---

# cmuxは、複数の作業を見渡しやすい

<div class="fig">
<div class="terminal-profile reverse">
<div class="terminal-brand">
<span class="terminal-logo i-cmux"></span>
<b>cmux</b>
<span class="terminal-kind">複数作業向けターミナル</span>
<p class="terminal-fit"><b>向く場面</b><span>Macで複数のAIセッションを動かす</span></p>
</div>
<div class="terminal-points">
<div class="terminal-point strength">
<h2>強み</h2>
<ul>
<li>作業場所、Git、通知をサイドバーに集約</li>
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

<!-- _class: header-offset -->

# Herdrは、長時間の作業へ戻りやすい

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
<li>対応するAIでは、作業状態を確認できる</li>
</ul>
</div>
<div class="terminal-point weakness">
<h2>弱み</h2>
<ul>
<li>サーバー起動とdetach／reattachを覚える</li>
<li>サーバー再起動では、実行中の処理は戻らない</li>
<li>状態表示や再開方法は、AIごとに異なる</li>
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
- Icon: https://raw.githubusercontent.com/herdrdev/herdr/master/assets/logo.png
-->

---

# CLIエージェントが進め、人が完成を判断する

<div class="fig">
<div class="row c2">
<div class="card">
<div class="logos"><span class="ico ico-lg i-claude"></span><span class="ico ico-lg i-codex"></span></div>
<div class="t">AIエージェントが進めること</div>
<div class="d">リポジトリを調べ、ファイルを編集し、<br>コマンドで検証する</div>
</div>
<div class="card on">
<span class="gi lg g-doc dark"></span>
<div class="t">人が判断すること</div>
<div class="d">権限、実行コマンド、差分、<br>テスト結果、残ったリスク</div>
</div>
</div>
<p class="cap">AIエージェントの処理が終わっても、成果物が完成したとは限らない</p>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/overview
- https://developers.openai.com/codex/cli/
-->

---

<!-- _header: '' -->

<div class="inline-header">1. 開発の道具を3つの役割で考える</div>

# cmuxでは、確認が必要な場所を一覧できる

<div class="fig">
<div class="win three">
<div class="bar"><i></i><i></i><i></i><span class="ico i-cmux"></span><b>cmux</b></div>
<div class="body" style="height:300px">
<div class="p"><div class="h">セッション</div><div class="stat"><i class="run"></i>プロジェクトA／実行中</div><div class="stat"><i class="wait"></i>プロジェクトB／入力待ち</div><div class="stat"><i class="run"></i>プロジェクトC／実行中</div><div class="stat"><i class="done"></i>プロジェクトD／処理終了</div></div>
<div class="p dark"><div class="ln d l"></div><div class="ln dg m"></div><div class="ln d s"></div><div class="ln d l"></div><div class="ln dg m"></div></div>
<div class="p"><div class="h">ブラウザ／別ペイン</div><div class="ln m"></div><div class="ln s"></div><div class="ln b l"></div><div class="ln s"></div></div>
</div>
</div>
<p class="cap">通知と一覧は、戻る場所を教える。変更内容の正しさは、差分とテスト結果で確認する</p>
</div>

<!--
[Sources]
- https://github.com/manaflow-ai/cmux
- https://github.com/manaflow-ai/cmux/blob/main/docs/notifications.md
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
<p class="cap">一方を捨てる必要はない。作業に合わせて、主役にする画面を入れ替える</p>
</div>

<!--
[Sources]
- https://code.visualstudio.com/docs/agents/run/agents-window
- https://github.com/manaflow-ai/cmux
- https://herdr.dev/docs/
-->

---

<!-- _class: chapter -->
<!-- header: '2. 複数のAIエージェントを動かす' -->

<div class="n">CHAPTER 2</div>

# 複数のAIエージェントを動かす

同時に動かす前に、仕事を分けられるか確かめる

---

# この勉強会では、2つの進め方を扱う

<div class="fig">
<div class="row c2">
<div class="card">
<div class="row c3 ai-row"><div class="ai sm blue"><div class="glyph"></div></div><div class="ai sm blue"><div class="glyph"></div></div><div class="ai sm blue"><div class="glyph"></div></div></div>
<div class="t">A. 違うプロジェクト</div><div class="d">別々の案件を並行して進める</div>
</div>
<div class="card on">
<div class="row c4 ai-row"><div class="ai sm blue"><div class="glyph"></div></div><div class="ai sm navy"><div class="glyph"></div></div><div class="ai sm gray"><div class="glyph"></div></div><div class="ai sm green"><div class="glyph"></div></div></div>
<div class="t">B. 1つのプロジェクト</div><div class="d">独立した仕事へ分け、結果を統合する</div>
</div>
</div>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://code.claude.com/docs/en/agent-teams
-->

---

<!-- _header: '' -->

<!-- _class: content-center manual-header-slide -->

<div class="inline-header">2. 複数のAIエージェントを動かす／A. 違うプロジェクト</div>

# A. 別のプロジェクトなら、処理中に別の仕事へ移れる

<div class="fig">
<div class="row c3 project-row">
<div class="proj"><div class="ai blue"><div class="glyph"></div></div><div class="box">プロジェクトA</div></div>
<div class="proj"><div class="ai blue"><div class="glyph"></div></div><div class="box">プロジェクトB</div></div>
<div class="proj"><div class="ai blue"><div class="glyph"></div></div><div class="box">プロジェクトC</div></div>
</div>
<div class="flow compact-flow">
<div class="step on">指示する</div><div class="arw">→</div><div class="step">別の仕事へ移る</div><div class="arw">→</div><div class="step on">通知で戻る</div><div class="arw">→</div><div class="step">差分を確認する</div>
</div>
<p class="cap">AIエージェントが処理している間に、人は別の案件を確認する</p>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/long-running-work
- https://code.visualstudio.com/docs/agents/run/agents-window
-->

---
<!-- _header: '' -->

<!-- _class: kagi content-center manual-header-slide -->

<div class="inline-header">2. 複数のAIエージェントを動かす／A. 違うプロジェクト</div>

# 「処理の終了」と「作業の完了」は別

<div class="fig">
<div class="row c3 state-row">
<div class="card flat"><div class="status-dot run"></div><div class="t">実行中</div><div class="d">まだ手を出さず、別の仕事へ</div></div>
<div class="card on"><div class="status-dot wait"></div><div class="t">入力待ち</div><div class="d">承認、質問、追加情報を返す</div></div>
<div class="card"><div class="status-dot done"></div><div class="t">処理終了</div><div class="d">差分とテスト結果を見て、完了か判断</div></div>
</div>
<div class="rule">通知は確認のきっかけ。品質を保証するものではない</div>
</div>

<!--
[Sources]
- https://github.com/manaflow-ai/cmux
- https://herdr.dev/docs/
- https://learn.chatgpt.com/docs/long-running-work
-->

---

<!-- _class: chapter -->
<!-- header: '2. 複数のAIエージェントを動かす／B. 1つのプロジェクト' -->

<div class="n">CHAPTER 2／実践</div>

# B. Todoアプリを4つの役割に分ける

複数のエージェントへ渡す前に、担当範囲を決める

---

<!-- _header: '' -->

<!-- _class: content-center manual-header-slide -->

<div class="inline-header">2. 複数のAIエージェントを動かす／B. 1つのプロジェクト</div>

# コードを書く前に、共有する設計メモを作る

<div class="fig">
<div class="plan-layout">
<div class="plan-paper">
<div class="plan-paper-title">Todoアプリの設計メモ</div>
<div><b>画面</b><span>一覧、追加、完了ボタン</span></div>
<div><b>機能</b><span>Todoを追加して、完了にできる</span></div>
<div><b>受け渡し</b><span>Todoの項目とAPIの形</span></div>
<div><b>完成</b><span>追加と完了切り替えが動く</span></div>
</div>
<div class="plan-voice">
<div class="ai navy"><div class="glyph"></div></div>
<p>いきなり<br>「全部作って」<br>とは頼まない</p>
</div>
</div>
<p class="cap">各担当が同じ前提を確認してから、作業を分ける</p>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/long-running-work
- https://learn.chatgpt.com/docs/features
- https://code.claude.com/docs/en/agent-teams
-->

---

<!-- _header: '2. 複数のAIエージェントを動かす／B. 1つのプロジェクト' -->

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
<b>レビュー担当</b><span>できた成果から確認する</span>
</div>
</div>
<div class="rule">役割と担当範囲を先に決める</div>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://code.claude.com/docs/en/agent-teams
-->

---

<!-- _header: '2. 複数のAIエージェントを動かす／B. 1つのプロジェクト' -->

# 境界が決まった仕事だけ、並行して進める

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
<div class="parallel-next">→<small>できたものを<br>その都度渡す</small></div>
<div class="parallel-review">
<div class="ai green"><div class="glyph"></div></div>
<b>4. レビュー担当</b>
<span>届いた成果から確認し、最後に組み合わせる</span>
<div class="review-checks">
<div>変更内容を確認する</div>
<div>ズレを担当へ返す</div>
<div>最後に全体を動かす</div>
</div>
</div>
</div>
<div class="rule">APIとデータ形式を先にそろえる。同じファイルを変更する作業は並行しない</div>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://code.claude.com/docs/en/agent-teams
- https://docs.github.com/en/copilot/concepts/agents/copilot-cli/fleet
-->

---

<!-- _header: '2. 複数のAIエージェントを動かす／B. 1つのプロジェクト' -->

# 担当ごとに、完了条件まで決める

<div class="fig">
<div class="outcome-list">
<div><span class="outcome-no">1</span><b>UI担当</b><p>Todo一覧と追加フォーム</p><small>仮のデータで画面を確認</small></div>
<div><span class="outcome-no">2</span><b>バックエンド担当</b><p>追加、取得、更新の機能</p><small>APIのテストまで実行</small></div>
<div><span class="outcome-no">3</span><b>DB担当</b><p>Todoの保存と読み出し</p><small>データが残ることを確認</small></div>
</div>
<p class="cap">「バックエンドをお願い」だけでは、作業範囲も完了条件も決まらない</p>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/long-running-work
- https://www.anthropic.com/engineering/multi-agent-research-system
-->

---

<!-- _header: '2. 複数のAIエージェントを動かす／B. 1つのプロジェクト' -->

# 最初の指示は、4項目をそろえる

<div class="fig">
<div class="terminal-screen paste">
<div class="terminal-bar">Claude Code（UI担当）</div>
<code><span class="prompt">&gt;</span> <span class="k">やること</span>Todoの一覧画面と、追加フォームを作る</code>
<code class="cont"><span class="k">変更する場所</span>src/components/ の中</code>
<code class="cont"><span class="k">変更しない場所</span>src/api/とsrc/db/</code>
<code class="cont"><span class="k">完了条件</span>npm run devで画面が出て、npm testが通る</code>
</div>
<p class="cap">4項目を明記すると、作業範囲と完了条件の解釈をそろえやすい</p>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/long-running-work
- https://www.anthropic.com/engineering/multi-agent-research-system
-->

---

<!-- _header: '2. 複数のAIエージェントを動かす／B. 1つのプロジェクト' -->

# 同じファイルの同時編集は、統合でぶつかる

<div class="fig">
<div class="incident">
<div><span class="w">先に</span><b>UI担当</b><span class="d">Todo.tsxに追加フォームを書く</span></div>
<div><span class="w">同時に</span><b>バックエンド担当</b><span class="d">同じTodo.tsxに保存処理を書く</span></div>
<div class="bad"><span class="w">統合時</span><b>競合</b><span class="d">両方の変更を、そのまま重ねられない</span></div>
<div><span class="w">テスト</span><b>見逃し</b><span class="d">画面のテストがなければ、不足に気づけない</span></div>
<div class="bad"><span class="w">確認</span><b>差分</b><span class="d">両方の変更が残っているかを見る</span></div>
</div>
<div class="rule">テストだけでなく差分も見る。担当範囲は作業前に分ける</div>
</div>

<!--
[Sources]
- https://code.claude.com/docs/en/worktrees
- https://learn.chatgpt.com/docs/environments/git-worktrees
-->

---

<!-- _header: '' -->

<!-- _class: content-center manual-header-slide -->

<div class="inline-header">2. 複数のAIエージェントを動かす／B. 1つのプロジェクト</div>

# 同じファイルの同時編集は避ける

<div class="fig">
<div class="scene-grid conflict-layout">
<div class="conflict-scene">
<div class="conflict-person"><div class="ai blue"><div class="glyph"></div></div><b>UI担当</b></div>
<div class="conflict-file"><strong>×</strong><b>Todo.tsx</b><span>2つの担当が同時に編集</span></div>
<div class="conflict-person"><div class="ai navy"><div class="glyph"></div></div><b>バックエンド担当</b></div>
</div>
<div class="numbered">
<div><b>1. 場所を分ける</b><span>UI、API、DBの担当を分ける</span></div>
<div><b>2. 重なるなら待つ</b><span>先に一方を終わらせる</span></div>
<div><b>3. 小さければ1つにまとめる</b><span>無理に並行しない</span></div>
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

# 今日から試す3つ

<div class="fig">
<div class="closing-path">
<div><span class="gi lg g-split"></span><b>役割と範囲を分ける</b><small>UI、API、DB、レビュー</small></div>
<span class="closing-arrow">→</span>
<div><span class="gi lg g-doc"></span><b>指示を4項目で渡す</b><small>やること、変更範囲、完了条件</small></div>
<span class="closing-arrow">→</span>
<div class="on"><span class="gi lg g-bolt dark"></span><b>人が差分と動作を確認</b><small>AIエージェントの報告だけで終わらせない</small></div>
</div>
</div>

<!--
[Sources]
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://learn.chatgpt.com/docs/long-running-work
- https://learn.chatgpt.com/docs/environments/git-worktrees
-->
