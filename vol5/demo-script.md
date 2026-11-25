# 実演デモ台本（第5回）

60分の中で2回入れる。実演1は4分、実演2は3分。どちらも未リハーサル（2026-11-25時点）。前日か当日の朝に1回通して、所要時間をここへ書く。

## 共通の準備

- [ ] ターミナルとブラウザの文字を拡大する（ターミナルは24pt程度）
- [ ] 通知、メール、チャットのプレビューを切る
- [ ] 映る画面から、顧客名、個人のリポジトリ名、アカウント名を外す。実演用のリポジトリとアカウントを使う
- [ ] うまくいかない場合は、12、14、16枚目の実出力の画面で説明を続ける

## 実演1: branch、merge、conflictの解消

挿入位置は16枚目（conflict）のあと。

見せたいことは、branchを切ってもファイルがコピーされないこと、両方が同じ行を変えるとconflictになり、人が直してcommitするまでGitが止まること。

### 準備

- [ ] 空のフォルダを用意する（例: `/tmp/git-demo`）。実案件のリポジトリでやらない

### 手順

```sh
git init -b main app && cd app
printf 'title = "Todo"\ncolor = "blue"\n' > config.toml
git add . && git commit -m "設定ファイルを追加"

git switch -c feature/color
sed -i '' 's/blue/green/' config.toml
git commit -am "色を緑に変える"
cat .git/refs/heads/feature/color   # branchは1行のファイル

git switch main
sed -i '' 's/blue/red/' config.toml
git commit -am "色を赤に変える"
git log --oneline --graph --all     # 枝分かれを見せる

git merge feature/color             # CONFLICT
cat config.toml                     # マーカーを見せる
# エディタでcolor = "green"の1行にする
git add config.toml && git commit --no-edit
git log --oneline --graph --all     # 親が2つのmerge commit
```

### 注意

- `sed -i ''`はmacOSの書き方。Linuxなら`sed -i`
- 解消をエディタで見せる時間が無ければ、`git merge --abort`で戻して次へ進む

## 実演2: GitHubのPR画面

挿入位置は24枚目（CI）のあと。

見せたいことは、PRが差分、説明、レビュー、チェックの結果を1か所にまとめていること（21〜24枚目の内容）。

### 準備

- [ ] 実演用の公開リポジトリに、24枚目と同じ`.github/workflows/ci.yml`を置く
- [ ] 前日に、テストが通るPRと、テストが落ちるPRを1本ずつ作っておく（CIの実行を待たずに済む）
- [ ] mainにrulesetを設定し、PRとチェックの成功を必須にしておく

### 手順

1. テストが落ちるPRを開き、Checksの赤いバツと、mergeボタンが押せないことを見せる（25枚目の予告）
2. Files changedで差分を見せ、1行にコメントを付ける
3. テストが通るPRを開き、緑のチェックと「Squash and merge」の選択肢を見せる（mergeはしない）

### 注意

- GitHub FreeのPrivateリポジトリではrulesetが効かない。公開リポジトリか、有料プランのOrganizationで用意する
