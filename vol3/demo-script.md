# 実演デモ台本（第3回）

60分の中で2回入れる。各2分。

## 共通の準備

- [ ] ブラウザの文字を拡大し、DevToolsのフォントも大きくする
- [ ] 通知、メール、チャットのプレビューを切る
- [ ] 実演がうまくいかない場合に備え、各実演のスクリーンショットを用意する

## 実演1: DevToolsのNetworkタブ

挿入位置は17枚目（3つに分けて作る）のあと。

見せたいことは、1回の表示の裏で多数のリクエストが飛び、それぞれにメソッド、ステータス、ヘッダがあること。

### 手順

1. 公開されている任意のサイトを開き、DevToolsのNetworkタブを開いて再読み込みする
2. 一覧の件数と、HTML、CSS、JS、画像の種類を指す
3. 先頭のHTMLのリクエストを開き、Headersでメソッド、ステータスコード、Content-Typeを見せる
4. Timingで、DNS、接続（TCP）、TLS、待ち時間を指し、13枚目の5段階と対応させる
5. Fetch/XHRで絞り、JSONを返すAPIのレスポンスを見せる（あれば）

### 注意

- ログイン済みのサイトを映すと、CookieやAuthorizationヘッダが映る。ログインしていないサイトか、シークレットウィンドウで行う

## 実演2: Supabaseで表とインデックスを見る

挿入位置は29枚目（迷ったらPostgreSQL）のあと。

見せたいことは、表がそのまま見えることと、インデックスの有無で実行計画が変わること。

### 準備

- [ ] 勉強会専用のSupabaseプロジェクトを新しく作る。業務や本番のプロジェクトは使わない
- [ ] `users`と`todos`を作り、実行計画の差が出るよう`todos`に数万行を入れておく（勉強会専用のプロジェクト内だけ）
- [ ] 前日に、インデックスの有無でSeq ScanとIndex Scanが切り替わることを確かめる

### 手順

1. Table Editorで`todos`を開き、列と外部キー（`user_id`）を見せる
2. SQL Editorで`explain analyze select * from todos where user_id = 1;`を実行し、Seq Scanと実行時間を見せる
3. `create index todos_user_id_idx on todos (user_id);`を実行する
4. 同じEXPLAIN ANALYZEを再実行し、Index Scan（またはBitmap Index Scan）と実行時間の差を見せる

### 注意

- 行数が少ないと、インデックスがあってもSeq Scanが選ばれる。準備の段階で行数を確かめる
- 画面にAPIキーや接続文字列を出さない（Project SettingsのAPIの画面は開かない）
