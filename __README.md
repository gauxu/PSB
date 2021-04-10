## PSB(Python System Backtester)
### 1.About feature
#### 1.1 spec of main feature(主要機能)
+ 戦略portfolioの多様性を確認  
+ WFOで各戦略の継続的最適化  
#### 1.2 spec of sub feature(仕様列挙)
+ 検証可能なTimeFrame:Minimum(M1)-Maximum(Y1)  
+ 各処理が順不同にでも適切に動くようにする。 管理オブジェクト(DB)を渡す。
#### 1.3 update of adding feature at letest
日々の作業ログはGitに残るのでVer.upの仕様として説明が欲しいものを列挙。  
+ <strong>Ver0.0.0</strong>  
全般データはTester管理オブジェクトに集約し各処理に参照渡しをする。  
各処理が順不同にでも適切に動くようにする。 管理オブジェクト渡しで実現できるか。  
デメリットは管理オブジェクトへの強烈な依存性の発生  
#### 1.4 specifications(仕様詳細)
仕様列挙では冗長なものや詳細的なもの
+ 検証対象マーケットgroupListはDBに保管し必要なときに参照。  
検証対象ItemObjの中に売買ItemListと比較参照ItemListを作る  
+ 一度の検証ループで全てのチャートリストとそれに属するマーケットを見る  
それぞれのチャートのタイムフレームと無条件ループ内でイベントコールで処理  
対象マーケットの最低検証時間軸に応じてカウントを進めていく  
+ NOTE:各マーケットの時間足がそれ以上だとしても管理Objに設定された最低検証時間軸を基準に動かす
+ マルチタイムフレーム分析は可能→GILはグリーンスレッドなので早くはない。
+ プログレスバーなどで同時並行処理の作業状況可視化  

#### 1.5 Todo in this project.
[210407]1_PSBをOneMax問題対応  
[200819]_最適化アルゴリズム実装←インターフェイス実装←Deapに関する調査  
[210410]3_PSB_LM.xmind -> plantuml移行  

***
#### At below is unorgnized.
Move to spec them nessesaly of orgnizing at later.

[190902]@gauxu
+ SystemTester.pyを熟読
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
