# エンジニア勉強会 第5回（2026-11-26 / 60分）

「Gitとチーム開発：branch、PR、CI、worktree」。
今回から冒頭の約10分を「前回のおさらいと、その後の変化」にする（2026-11-25、ユーザーの指示）。
おさらいは第4回（パーソナルエージェント、AI社員、AI組織）の要点と、この2週間の4製品の更新、Orca Botsの紹介。
本編は、AIよりエンジニア寄りの内容にするという指示を受けて「Gitとチーム開発」を選んだ（2026-11-25、ユーザーの選択）。
第1回で発展事項として後回しにしたbranchとworktreeの回収になり、Orcaがエージェントごとにworktreeを切る理由にもつながる。

**エンジニア向けに書く**（第4回と同じ）。用語は言い換えず、各ページの上の1行は「要点」にする。章末の問いは入れない。

全31枚（表紙1、目次1、章扉4、本文24、まとめ1）。テーマCSSは第1回の`../theme/deck.css`、部品は第4回の`style:`を引き継ぎ、第5回だけの部品は`style:`の末尾に置く。

## ファイル

| ファイル | 中身 |
|---|---|
| `slides.md` | Marp本体（全31枚）。各ページのコメントに`[話すこと]`と`[Sources]` |
| `content-notes.md` | 構成の判断と事実確認の記録 |
| `demo-script.md` | 2回の実演と時間調整 |
| `build/` | HTML、PDF、PNGの出力先（git管理外） |

## 60分の構成

| 範囲 | 内容 | 時間 |
|---|---|---:|
| 1–2 | 表紙、目次 | 1分 |
| 3–10 | 0. おさらい（4–6が第4回、7が更新、8–9がOrca Bots、10が本編への橋渡し） | 10分 |
| 11–16 | 1. Gitの仕組み（conflictまで） | 10分 |
| 実演1 | ターミナルでbranch、merge、conflictの解消 | 4分 |
| 17 | 1. 続き（取り消し） | 2分 |
| 18–25 | 2. GitHubでのチーム開発（CIまで） | 12分 |
| 実演2 | GitHubのPR画面で、差分、レビュー、CIのチェックを見せる | 3分 |
| 26–30 | 3. AIエージェントとGit | 7分 |
| 31 | まとめ | 2分 |
| 質疑 | | 5分 |

本編51分＋予備4分。
時間が押した場合は、次を口頭の一言に縮める: 3つの場所（13枚目）、mergeの3方式（23枚目）、レビューの観点（22枚目）。

当日のチェックポイント:

| 経過 | 到達点 |
|---|---|
| 0:11 | 11枚目、第1章 |
| 0:21 | 実演1（16枚目のあと） |
| 0:27 | 18枚目、第2章 |
| 0:39 | 実演2（24枚目のあと） |
| 0:42 | 26枚目、第3章 |
| 0:49 | 31枚目、まとめ |
| 0:55 | 質疑へ移る（予備を使い切った場合） |

## ビルド

`vol5/`の中で実行する。2026-11-25時点も、Homebrewの`marp`はNode.js 26で起動しないため、node@24で動かす。

```sh
N=/opt/homebrew/opt/node@24/bin/node
J=/opt/homebrew/lib/node_modules/@marp-team/marp-cli/marp-cli.js

$N $J slides.md -o build/slides.html --theme ../theme/deck.css --html < /dev/null
$N $J slides.md -o build/slides.pdf --theme ../theme/deck.css --html --allow-local-files < /dev/null
$N $J slides.md --images png -o build/png/s.png --theme ../theme/deck.css --html --allow-local-files < /dev/null

# 安全域からのはみ出しを機械で確認する
python3 ../scripts-check-margins.py

# 31枚を一覧表示
ffmpeg -y -pattern_type glob -i 'build/png/s.0*.png' -vf "scale=480:270,tile=4x8" -frames:v 1 build/sheet/contact.png
```

## ターミナルの画面

12、16、27枚目のターミナルは、使い捨てのリポジトリで実行した実出力（2026-11-25、git 2.56.1）。
mainで`config.toml`の色を赤、`feature/color`で緑に変えてmergeした。
27枚目はパスを短く表示し、`fatal`の行の末尾を「…」で切っている。

## ロゴとアイコン

第5回でOrcaを追加した。`stablyai/orca`の`resources/icon.png`（MIT、256px、2026-11-25取得）を`scripts-build-icons.py`で`theme/deck.css`へ埋め込んでいる。
各ロゴは識別のための引用で、権利は各社・各プロジェクトに帰属する。

## デザインの約束

第1回、第3回、第4回の`README.md`の約束を守る。第5回で加えた部品:

- `.terminal-screen.tight`: 行の多い実出力。16pxに詰め、長いハッシュも1行に収める
- `.terminal-screen.yaml`: YAMLの実物。インデントを保つため`white-space: pre`
- `.scene-grid.wide`: ターミナルを広く取り、右に説明を置く
- `code.warn`（赤系）と`code.hl`（黄）: conflictのマーカーと、注目させる行
- branchとmergeは、枝分かれと合流の図で見せる（14、15枚目。2026-11-25、ユーザーの指摘）。branchの実体（ref）は口頭と話者メモで補う
- 見出しは1行に収める。2行になったら文言を短くし、詳しい内容は「要点」へ移す
