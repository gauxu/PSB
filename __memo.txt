■PSB_projectMemo
・Lib及びimportモジュール名
SystemTester.py     #各サンプルのテストモジュールの元になっている
getData.py          #株価や基本データを纏めて読み込む→データベースから
dataLists.py        #myDate,myTime,myOpen,myHigh,myLow,myClose
tradeClass.py       #tradeInfo
equityDataClass.py  #equityClass
trade.py            #trade
systemMarket.py     #systemMarketClass
portfolio.py        #portfolioClass
systemAnalytics.py  #calcSystemResults

marketDataClass.py
tradeModule.py

masterDateList
※NOTE:その他予約語等 → __ReserveWords.txt  …Ref

・デバッグコンソールには処理の途中経過と_Compositeの内容が出力

・出力ファイルmemo
_Composite  #全Mrkt毎結果と合算月間リターン推移
_Summary    #銘柄ごとの成績と月間推移
_Trades     #各銘柄ごとのトレード記録
_StrtTrdDD  #トレードを開始してからの任意のすべてに対するMDD調査
_MonteCarlo #モンテカルロシミュレーション結果

・GAライブラリ関連用語
creator.FitnessMax:適応度クラス
creator.Individual:個体クラス　適応度クラスを属性として持つ
toolbox.attr_bool:遺伝子を生成する関数
toolbox.individual:個体を生成する関数
toolbox.population:個体集団を生成する関数
toolbox.evaluate:評価関数
toolbox.mate:交差を実行する関数
toolbox.mutate:変異を実行する関数
toolbox.select:次世代の個体を選択する関数
