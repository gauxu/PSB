## PSB(Python System Backtester)
### About feature
#### spec of main feature(主要機能)
+ 戦略portfolioの多様性を確認  
+ WFOで各戦略の継続的最適化  
#### spec of sub feature(仕様列挙)
+ 検証可能なTimeFrame:Minimum(M1)-Maximum(Y1)  
#### update of adding feature at letest
日々の作業ログはGitに残るのでVer.upの仕様として説明が欲しいものを列挙。  
+ <strong>Ver0.0.0</strong>  
Tester管理オブジェクトを各種検証Objに参照渡しをすることで共通データを共有させる。IFをシンプル化(実行関数オブジェクト送り)して、ラッピングを繰り返す等
しかし管理オブジェクトへの強烈な依存性発生  
検証対象マーケットObjをリストにする  
検証対象ItemObjの中に売買ItemListと比較参照ItemListを作る  
一度の検証ループで全てのチャートリストとそれに属するマーケットを見る  
それぞれのチャートのタイムフレームと無条件ループ内でイベントコールで処理  
対象マーケットの最低検証時間軸に応じてカウントを進めていく  
NOTE:各マーケットの時間足がそれ以上だとしても管理Objに設定された最低検証時間軸を基準に動かす

#### Todo in this project.
[210407]1_PSBをOneMax問題対応

[190822]_毎日確認/_GrobalMemo PSB_LM.xmind→plantUMLでやりたい
[190822]_1日1回必ずコミット&Gitやメモ等の整理でも良い
[200825]_設計が大事(段取り8割)　UML頑張る

[200819]_最適化アルゴリズム実装←インターフェイス実装←Deapに関する調査
[190822]_出力や調査結果を見やすく可視化←jupytorで記録としてまとめる

[210405]_マルチタイムフレーム分析は可能→グリーンスレッド○  
[210405]_プログレスバーなどで同時並行処理がしたい→Web系GUI実践

[200906]_時間管理術をコンテンツにして発信集計アプリがなければ自作
[200903]_Qiitaでplantuml使用上のコツとかまとめてみる
[200903]_Qiitaで自分用Gitの使い方をまとめてみる
[200903]_スキルシートを作る　知見概念の有無レベル等
[200903]_机・椅子キーボード周りの開発環境についてのメモ
[200903]_Githubにて自分のTodoの公開

***
#### At below is unorgnized.
Move to spec them nessesaly of orgnizing at later.

[190902]@gauxu
+ SystemTester.pyを熟読
MMの検証手段整理しつつ各種最適化された検証手続きをするための方法を探る
ポイントを抑えた変数や関数のメモをMMに記述
+ 検証手段の整理と確認のためMMの検証項目を追加・整理
戦略分散化のための考えの整理
+ #AnalyzeIdea#を3つ作成

[190828]@gauxu
+ GAでOneMax問題を解けるようにした　(deap導入)
サンプルプログラムGA.pyの実行にて確認。
※VSCの実行環境では仮想環境の選択はできるが、
ターミナルで直接venvの変更は無理なことが分かった。
・jupyterNotebookのマークアップ領域に改行コードを追加
マークアップ領域ではhtmlの改行コードで書くこと

[190824]@gauxu
米国自動車株比較の良いサンプルコードがあったので
それを参考にViewRsltMod内にJupyterプロジェクト作成

[190823]@gauxu
鞘取りのロジックと調査作業の段取りの概要を固めTodoに入れてみた

190822@gauxu
MMをプロジェクトと同じ名前でロードマップ「PSB_LM」作成
__Todoや各項目を設定したドキュメントファイルの設定

20190821@gauxu
PSBリモートリポジトリに__ReservedWords.txt追加
__memoにルール手順に変更　具体的な更新手順記述
リモートリポジトリの出力結果ファイルを完全削除

20190810@gauxu
PSBリモートリポジトリに__issue.txt追加

20190809@gauxu
GithubにOrgnize作成し、GauxuアカウントでPSBプロジェクトをコミットした。

20190804@gauxu
#内部スコープでglobalで宣言されてたexitPriceがglobal未定義警告出現、外部でコメントされていた「#exitPrice = list()」から#を削除。
