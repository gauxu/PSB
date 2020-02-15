#/////////////////////////////////////////////////////////////////////////////////
#System Tester.py - programmed by George Pruitt
#Feel free to distribute and improve upon
#Version 1.4
#/////////////////////////////////////////////////////////////////////////////////

#--------------------------------------------------------------------------------
#Import Section - inlcude functions, classes, variabels
#from external modules
#--------------------------------------------------------------------------------
import csv
import tkinter as tk
import os.path
from getData import getData
from dataLists import myDate,myTime,myOpen,myHigh,myLow,myClose
from tradeClass import tradeInfo    #トレード記録のフォーマット管理と利益計算用クラス
from equityDataClass import equityClass
from trade import trade
from systemMarket import systemMarketClass
from portfolio import portfolioClass
from indicators import highest,lowest,rsiClass,stochClass,sAverage,bollingerBands
from indicators import xAverage
from systemAnalytics import calcSystemResults
from tkinter.filedialog import askopenfilenames

from OptUnit import Opt,RsltOptPrm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#--------------------------------------------------------------------------------
  #End of Import Section
#--------------------------------------------------------------------------------
class systemTesterClass(object):
    SysName = "Noname"
    def __init__(self):
        self.mp=[0]
        self.tradeName='None'
        self.numShares=0
        self.cumuProfit=0

        self.marketPosition,self.listOfTrades,self.trueRanges,self.ranges = ([] for i in range(4))
        self.entryPrice,self.entryQuant,self.exitQuant = ([] for i in range(3))#マーケット毎に再初期化？
        self.exitPrice = list()
        self.currentPrice = 0
        self.totComms = 0
        self.barsSinceEntry = 0
        self.numRuns = 0

#        self.myBPV = 0
#        self.myComName
#        self.myMinMove
        self.allowPyr = 0
        self.curShares = 0

        self.commission = 100 # deducted on a round turn basis
        self.numBarsToGoBack = 1000 # number of bars from the end of data
        self.rampUp = 100 # need this minimum of bars to calculate indicators 最低必要バー数

    def initmrkt(self):  #マーケット毎再初期化？　マーケット処理下のループにて再初期化されるリスト等
        self.listOfTrades[:] = []
        self.marketPosition[:] = []
        self.entryPrice[:] = []
        self.entryQuant[:] = []
        self.exitQuant[:] = []
        self.trueRanges[:] = []

#ポジクローズの価格や日時、名前、枚数などのデータをもとにtradeクラスを処理
# ret：利益とtradeクラスと枚数
def exitPos(dClass,myExitPrice,myExitDate,tempName,myCurShares):
#        global mp_r,commission_r
#        global tradeName,entryPrice,entryQuant_r,exitPrice,numShares,myBPV_r,cumuProfit_w
    if dClass.mp < 0:
        trades = tradeInfo('liqShort',myExitDate,tempName,myExitPrice,myCurShares,0)
        profit = trades.calcTradeProfit('liqShort',dClass.mp,dClass.entryPrice,myExitPrice,dClass.entryQuant,myCurShares) * dClass.myBPV
        profit = profit - myCurShares * dClass.commission
        trades.tradeProfit = profit
        dClass.cumuProfit += profit
        trades.cumuProfit = dClass.cumuProfit
        myClose
    if dClass.mp > 0:
        trades = tradeInfo('liqLong',myExitDate,tempName,myExitPrice,myCurShares,0)
        profit = trades.calcTradeProfit('liqLong',dClass.mp,dClass.entryPrice,myExitPrice,dClass.entryQuant,myCurShares) * dClass.myBPV
        profit = profit - myCurShares * dClass.commission
        trades.tradeProfit = profit
        dClass.cumuProfit += profit
        trades.cumuProfit = dClass.cumuProfit
    curShares = 0
    for remShares in range(0,len(dClass.entryQuant)):
        curShares += dClass.entryQuant[remShares]
    return (profit,trades,curShares)

    

#--------------------------------------------------------------------------------
  #Helper Functions local to this module
#--------------------------------------------------------------------------------
def getDataAtribs(dClass):
    return(dClass.bigPtVal,dClass.symbol,dClass.minMove)
def getDataLists(dClass):
    return(dClass.date,dClass.open,dClass.high,dClass.low,dClass.close)
def roundToNearestTick(price,upOrDown,tickValue):
    temp1 = price - int(price)
    temp2 = int(temp1 / tickValue)
    temp3 = temp1 -(tickValue*temp2)
    if upOrDown == 1:
        temp4 = tickValue - temp3
        temp5 = temp1 + temp4
    if upOrDown == -1:
        temp4 = temp1 - temp3
        temp5 = temp4
    return(int(price) + temp5)

def calcTodaysOTE(mp,myClose,entryPrice,entryQuant,myBPV):
    todaysOTE = 0
    for entries in range(0,len(entryPrice)):
        if mp >= 1:
            todaysOTE += (myClose - entryPrice[entries])*myBPV*entryQuant[entries]
        if mp <= -1:
            todaysOTE += (entryPrice[entries] - myClose)*myBPV*entryQuant[entries]
    return(todaysOTE)

#--------------------------------------------------------------------------------
  #End of functions
#--------------------------------------------------------------------------------
class DCL():
    dataClassList = getData()       #複数のマーケットのデータをクラスオブジェクトにしてリスト化
    @staticmethod
    def OutputDate():
        print("各対象マーケットの検証期間")
        for i in range(len(DCL.dataClassList)):
            print(DCL.dataClassList[i].symbol,"-[",DCL.dataClassList[i].date[0],DCL.dataClassList[i].date[-1],"]")


#---------------------------------------------------------------------------------
  #Lists and variables are defined and initialized here
#---------------------------------------------------------------------------------
def XavgCrossOver(args):
#    print(args)    #引数チェック用
    val_01=args[0]
    val_02=args[1]
    BgnPrd = args[2][0]
    EndPrd = args[2][1]
    print(BgnPrd,EndPrd)
    #リセットは特に無し初期化のみ　最重要リスト　equityDataListは現在のところ未使用
    #最適化を繰り替えす際は全てのマーケットに対して何回も実行するため初期化
#    dataClassList,systemMarketList,equityDataList = ([] for i in range(3))
    systemMarketList,equityDataList = ([] for i in range(2))

    #マーケット毎に再初期化？
    STC = systemTesterClass()
#   マーケット処理下のループにて再初期化される場合のリスト
#   STC.initmrkt()
    alist, blist, clist, dlist, elist = ([] for i in range(5))#作業用バッファ？
#---------------------------------------------------------------------------------
  #End of Lists and Variables
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
  #Get the raw data and its associated attributes [pointvalue,symbol,tickvalue]
  #Read a csv file that has at least D,O,H,L,C - V and OpInt are optional
  #Set up a portfolio of multiple markets
#---------------------------------------------------------------------------------

    #dataClassList = getData()       #複数のマーケットのデータをクラスオブジェクトにしてリスト化
    numMarkets = len(DCL.dataClassList) #処理対象のマーケット数
    portfolio = portfolioClass()    #ポートフォリオ統合用クラスのインスタンス

#---------------------------------------------------------------------------------
  #SET COMMISSION, NUMBER OF BARS TO BACK TEST, AND RAMP UP FOR INDICATORS
#---------------------------------------------------------------------------------

    myXavg = 0

#////////  DO NOT CHANGE BELOW /////////////////////////////////////////////////
    for marketCnt in range(0,numMarkets):
        #マーケットを変える度に初期化
        STC.initmrkt()
        STC.myBPV,STC.myComName,STC.myMinMove = getDataAtribs(DCL.dataClassList[marketCnt])
        myDate,myOpen,myHigh,myLow,myClose = getDataLists(DCL.dataClassList[marketCnt])
        for i in range(0,len(myDate)):
            STC.marketPosition.append(0)
            STC.ranges.append(myHigh[i] - myLow[i])
            if i == 0:
                STC.trueRanges.append(STC.ranges[i])
            if i > 0:
                STC.trueRanges.append(max(myClose[i-1],myHigh[i]) - min(myClose[i-1],myLow[i]))
        systemMarket = systemMarketClass()#NOTE:systemMarketはportforlioクラスから出したい場合ローカルにすべき
        equity = equityClass()
        equItm = 0
        totProfit =0
        maxPositionL = 0
        maxPositionS = 0
        cumuProfit = 0
        curShares = 0
        numShares = 0
        STC.marketPosition.append(0)
        if len(myDate) < STC.numBarsToGoBack: STC.numBarsToGoBack = len(myDate)
        if STC.numBarsToGoBack < STC.rampUp: break

#////////  DO NOT CHANGE ABOVE /////////////////////////////////////////////////

#---------------------------------------------------------------------------------
#Instantiate Indicator Classes
#---------------------------------------------------------------------------------
        rsiStudy = rsiClass()
        stochStudy = stochClass()
#---------------------------------------------------------------------------------
        for i in range(len(myDate) - STC.numBarsToGoBack,len(myDate)):
            equItm += 1
            tempDate = myDate[i]
            todaysCTE = todaysOTE = todaysEquity = 0
            STC.marketPosition[i] = STC.marketPosition[i-1]
            STC.mp = STC.marketPosition[i]
            buyLevel,shortLevel,exitLevel = bollingerBands(myDate,myClose,60,2,i,1)
            buyLevel = roundToNearestTick(buyLevel,1,STC.myMinMove)
            shortLevel = roundToNearestTick(shortLevel,-1,STC.myMinMove)
    #        print(tempDate," avg ",exitLevel," ",buyLevel - exitLevel)
            atrVal = sAverage(STC.trueRanges,10,i,0)
    #        rsiVal = rsiStudy.calcRsi(myClose,10,i,0)
            myXavg = xAverage(myClose,myXavg,val_01,i,0)
            stopAmt = val_02/STC.myBPV
    #        print(myDate[i]," myXavg ",myXavg," close ",myClose[i])
    #        fastKVal,fastDVal,slowDVal = stochStudy.calcStochastic(3,9,9,myHigh,myLow,myClose,i,1)

    #        if (mp > 0 and maxPositionL < 3) : maxPositionL = mp
    #        if (mp < 0 and maxPositionS < 3) : maxPositionS = mp


 #Long Entry Logic
            if ((STC.mp == 0 and myDate[i]>=BgnPrd and myDate[i]<=EndPrd) or STC.mp == -1)  and myClose[i] >= myXavg:
                profit = 0
                price = myClose[i]
                if STC.mp <= -1:
                    profit,trades,curShares = exitPos(STC,price,myDate[i],"RevShrtLiq",curShares)
                    STC.listOfTrades.append(trades)
                    STC.mp = 0
                    todaysCTE = profit
                tradeName = "Xavg Buy"
                STC.mp += 1
                STC.marketPosition[i] = STC.mp
                numShares = 1
                STC.entryPrice.append(price)
                STC.entryQuant.append(numShares)
                curShares = curShares + numShares
                trades = tradeInfo('buy',myDate[i],tradeName,STC.entryPrice[-1],numShares,1)
                barsSinceEntry = 1
                totProfit += profit
                STC.listOfTrades.append(trades)
 #Long Exit - Loss
            if STC.mp >= 1 and myLow[i] < STC.entryPrice[-1] - stopAmt and barsSinceEntry > 1:
                price = min(myOpen[i],STC.entryPrice[-1] - stopAmt)
                tradeName = "L-MMLoss"
                exitDate =myDate[i]
                numShares = curShares
                STC.exitQuant.append(numShares)
                profit,trades,curShares = exitPos(STC,price,myDate[i],tradeName,numShares)
                if curShares == 0 : STC.mp = STC.marketPosition[i] = 0
                totProfit += profit
                todaysCTE = profit
                STC.listOfTrades.append(trades)
                maxPositionL = maxPositionL - 1
 # Long Exit - Time Based
            if STC.mp >= 1 and myClose[i] < STC.entryPrice[-1] and barsSinceEntry >= 10:
                price = myClose[i]
                tradeName = "L-BollExit"
                numShares = curShares
                STC.exitQuant.append(numShares)
                profit,trades,curShares = exitPos(STC,price,myDate[i],tradeName,numShares)
                if curShares == 0 : STC.mp = STC.marketPosition[i] = 0
                totProfit += profit
                todaysCTE = profit
                STC.listOfTrades.append(trades)
                maxPositionL = maxPositionL -1
# Short Logic
            if ((STC.mp == 0 and myDate[i]>=BgnPrd and myDate[i]<=EndPrd) or STC.mp == 1)  and myClose[i] <= myXavg:
                profit = 0
                price = myClose[i]
                if STC.mp >= 1:
                    profit,trades,curShares = exitPos(STC,price,myDate[i],"RevLongLiq",curShares)
                    todaysCTE = profit
                    STC.listOfTrades.append(trades)
                    STC.mp = 0
                STC.mp -= 1
                tradeName = "Xavg Short"
                STC.marketPosition[i] = STC.mp
                STC.entryPrice.append(price)
                numShares = 1
                STC.entryQuant.append(numShares)
                curShares = curShares + numShares
                trades = tradeInfo('sell',myDate[i],tradeName,STC.entryPrice[-1],numShares,1)
                barsSinceEntry = 1
                totProfit += profit
                STC.listOfTrades.append(trades)
# Short Exit Loss

            if STC.mp <= -1 and myHigh[i] >= STC.entryPrice[-1] + stopAmt and barsSinceEntry > 1:
                price = max(myOpen[i],STC.entryPrice[-1] + stopAmt)
                tradeName = "S-MMLoss"
                exitDate = myDate[i]
                numShares = curShares
                STC.exitQuant.append(numShares)
                profit,trades,curShares = exitPos(STC,price,myDate[i],tradeName,numShares)
                if curShares == 0 : STC.mp = STC.marketPosition[i] = 0
                totProfit += profit
                todaysCTE = profit
                STC.listOfTrades.append(trades)
                maxPositionS = maxPositionS -1
# Short Exit Profit
            if STC.mp <= -1 and myClose[i] > STC.entryPrice[-1]  and barsSinceEntry >= 10:
                price = myClose[i]
                tradeName = "S-TimeExi"
                exitDate =myDate[i]
                numShares = curShares
                STC.exitQuant.append(numShares)
                profit,trades,curShares = exitPos(STC,price,myDate[i],tradeName,numShares)
                if curShares == 0 : STC.mp = STC.marketPosition[i] = 0
                totProfit += profit
                todaysCTE = profit
                STC.listOfTrades.append(trades)
                maxPositionS = maxPositionS - 1

 ###########  DO NOT CHANGE BELOW ################################################################
            if STC.mp == 0 :
                todaysOTE = 0
                curShares = 0
                STC.entryPrice[:] = []
                maxPositionL = 0
                maxPositionS = 0
            if STC.mp != 0 :
                barsSinceEntry = barsSinceEntry + 1
                todaysOTE = calcTodaysOTE(STC.mp,myClose[i],STC.entryPrice,STC.entryQuant,STC.myBPV)
            todaysEquity = todaysOTE + totProfit
            equity.setEquityInfo(myDate[i],equItm,todaysCTE,todaysOTE)
        if STC.mp >= 1:
            price = myClose[i]
            tradeName = "L-EOD"
            exitDate =myDate[i]
            numShares = curShares
            STC.exitQuant.append(numShares)
            profit,trades,curShares = exitPos(STC,price,myDate[i],tradeName,numShares)
            STC.listOfTrades.append(trades)
        if STC.mp <= -1:
            price = myClose[i]
            tradeName = "S-EOD"
            exitDate =myDate[i]
            numShares = curShares
            STC.exitQuant.append(numShares)
            profit,trades,curShares = exitPos(STC,price,myDate[i],tradeName,numShares)
            STC.listOfTrades.append(trades)
        systemMarket.setSysMarkInfo("XavgCross",STC.myComName,STC.listOfTrades,equity)
        systemMarketList.append(systemMarket)
        STC.numRuns = STC.numRuns + 1

    portfolio.setPortfolioInfo("PortfolioTest",systemMarketList)

    calcSystemResults(systemMarketList)

#   戻り値は数値比較するため、オブジェクト返しは禁止 (ex. return portfolio) is ignore!
#    return portfolio.outputGrades() #結果を変えたいなら引数に指定することで変更
    #return portfolio.outputGrades() #結果を変えたいなら引数に指定することで変更
    print(args)    #引数チェック用
    print(portfolio.portEquityVal[-1])
    return portfolio.portEquityVal[-1]


if __name__ == "__main__":
    print("Execution from cmd! at ",__name__)
    objcFunc = XavgCrossOver
    #prmOptRg[[x1,x2...xi],[y1,y2...yj]...]
    #最適化回数自動計算のためVariableの数だけ用意
    prmOptRg = [
                [17,20,25,30,36,43,50,60,75,90,107,128,154,185,220,265,320],    #step *1.2
                [1000,1200,1450,1730,2050,2480,3000,3600,4300,5150,6200,7500,8900,10000],  #step *1.5
                [(20070101,20151231)]
                ]
    prmOptRg2 = [[6,8,10,12,14,16,18,20],[0.5,0.6,0.7,0.8],[5000,6000,7000,8000,9000],
                    [
                    [17,20,25,30,36,43,50,60,75,90,107,128,154,185,220,265,320],    #step *1.2
                    [1000,1200,1450,1730,2050,2480,3000,3600,4300,5150,6200,7500,8900,10000]  #step *1.5
                    ]
                ]

    resultOptprm = [[], #1段階上位の最適化による抽象化変数があればそれを設定(通常インデックス0用の空リスト)
                    [[10,0.6,5000], #日付の一段階上位の抽象化変数をインデックス0で参照、具体的な変数は1以降のインデックスで参照
                                    #インデックスによる分類を優先、結果による分類は別に後でやる方が良さそう
                        [[20070101,20081231,20090101,20091231],[[],[17,1200],[17,1450]]],
                        [[20080101,20091231,20100101,20101231],[[],[17,1200],[17,1450]]],
                        #...
                        [[20120101,20131231,20140101,20141231],[[],[17,1200],[17,1450]]]
                    ],
                    [[20,0.8,7000],
                        [[20070101,2008131,20090101,20091231],[[17,1200],[17,1450]]],
                        [[20080101,2009131,20100101,20101231],[[17,1200],[17,1450]]],
                        #...
                        [[20120101,20131231,20140101,20141231],[[17,1200],[17,1450]]]
                    ]
                   ]

    print(resultOptprm[1])
    print(resultOptprm[1][0])#周期の一般化変数(ソート未)
    print(resultOptprm[2][0])#周期の一般化変数(ソート未)
    print(resultOptprm[1][1])
    print(resultOptprm[1][2])
    print(resultOptprm[1][3])
    print(resultOptprm[1][1][0])
    print(resultOptprm[1][1][1][0])#抽象化概念等あれば(公比数列の一般式の決定変数等)
    print(resultOptprm[1][1][1][1])
    print(resultOptprm[1][1][1][2])
    print(resultOptprm[2][1])
    print(resultOptprm[2][2])
    print(resultOptprm[2][3])


#   listの指定要素までのリスト数の積を累積したリストを作る 0=8 1=8 2=40 3=160
#   idx % (全部の要素数/len(prmOptRg[1]))


#    WFA(objcFunc,prmOptRg,WFCnt, OOSRate, AnlyPrd)

    #目的関数と組み合わせたい変数群をリストの場合の最適化
#    Opt(objcFunc,prmOptRg)

    #目的関数＆引数と組み合わせたい変数群をリストの場合の最適化
    #result=Opt(XavgCrossOver,prmOptRg)

    #DCL.OutputDate()

    x = np.array(prmOptRg[0])
    y = np.array(prmOptRg[1])
    X, Y = np.meshgrid(x, y)
    Z = X*Y*0
#    for i in range(len(result)):
#        print(result[i])

        #result[i][0][0]#val1
        #result[i][0][1]#val2
        #result[i][0][2][0]#bgprd
        #result[i][0][2][1]#edprd
        #result[i][1][0]#rslt1
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    ax.plot_wireframe(X, Y, Z)
    plt.show()

