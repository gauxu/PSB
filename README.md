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
デメリットは管理オブジェクトへの強烈な依存性の発生(散り散りになるよりマシ)  

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
+ 検証手段の整理と確認のためMMの検証項目を追加・整理  
戦略分散化のための考えの整理  
[210411]1_Rp_AnalyzeItem作成 jupytorNotebookとmdは相性良  
[210411]2_Rp_SystemTesterの解析・理解 主要オブジェクトのmemo整理  
[210412]2_ReservedWords.mdに変数・予約語概要記述 PlantUMLで整理検討  
[210407]3_PSBをOneMax問題対応  
[200819]3_Deapに関する調査 最適化ライブラリ関連のインターフェイス理解・実装  
[210411]3_Rp_PSBのロードマップ "PSB_LM" をplantumlで作成・整理  
[210410]3_PSB_LM.xmind -> plantuml移行  
[210411]3_PSBのフォルダ整理  

***
#### 0.0 Etc…(At below is unorgnized.)
Move to spec them nessesaly of orgnizing at later.  
##### 0.0.1 todo
[210411]1_Strategy(サヤ取り):米国自動車株の相関性調査  
[210411]3_GitHubのissueが使えるか研究  
[210411]3_GitHubのOrgnize研究  

##### 0.0.2 issue
[190804]@gauxu:外部でコメントされていた「#exitPrice = list()」から#を削除  

内部スコープでglobalで宣言されていたexitPriceがglobal未定義Errorのため  
globalでデータ受渡しをしていたが、上手く情報の集約管理できなかったと思われる  