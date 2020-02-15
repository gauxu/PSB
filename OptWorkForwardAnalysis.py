
from XavgCrossOverOpt import XavgCrossOver
from OptUnit import Opt
from test import TstOptform
#Note: This imported method come true using by functional pointer.

#-----------------------------------------------------------------------
# WFAnlyze　関数ポインタ的な使い方で呼び出す
#-----------------------------------------------------------------------
def WFO(args):
    WFCnt = args[0]
    OOSRate = args[1]
    AnlyPrd = args[2]
    prmOptRg = args[3]  #変数リスト
    #("2000-01-01","2005-01-01"),yahooのデータは表記で入ってくるのでそのうち対応
    #argsを元にIn&OutSmpPrdを計算
    InSmpPrd  = [(1/1/2000,1/1/2005),(1/1/2001,1/1/2006),(1/1/2002,1/1/2007),(1/1/2003,1/1/2008),(1/1/2004,1/1/2009)]
    OutSmpPrd = [(1/1/2005,1/1/2006),(1/1/2006,1/1/2007),(1/1/2007,1/1/2008),(1/1/2008,1/1/2009),(1/1/2009,1/1/2010)]

#    reslut=Opt(TstOptform,prmOptRg)#個別でさらに最適化
#   InSmpPrdとprmOptRgを統合して最適化をし、OutSmpPrd用変数取得
    reslut=Opt(XavgCrossOver,prmOptRg)#個別でさらに最適化　期間変数を固定、パラメーター自由で投げる

#    print(reslut)
#   それぞれの期間毎に最適化に対応した変数と最適化結果が帰ってくる　return rsltOpt,len(rsltOpt),max,min
#   この場合は設定期間と変数組と結果のみ帰ってくるがそれぞれの結果を後で統合しなければならない
#   また同時に複数のInOutSmp期間の組み合わせを維持したまま計算する必要ある。
#   InSmpPrdを一1回のWFOの結果を以下のように格納する
#   [[(1/1/2000,1/1/2005):(1/1/2005,1/1/2006),prmOptRg組み合わせ,結果],以下同様]
#   上記を元に最終結果を計算する　WFAはこれを複数回束ねる感じ
    return args
#-----------------------------------------------------------------------
# WFAnlyzeここまで
#-----------------------------------------------------------------------

if __name__ == "__main__":
    print("execution from cmd! at ",__name__)
    objcFunc = TstOptform
#    objcFunc = XavgCrossOver
    #prmOptRg[[x1,x2...xi],[y1,y2...yj]...]
    #最適化回数自動計算のためVariableの数だけ用意
    prmOptRg = [
                [2,4,8,16,32,64,128,256],
                [2,4,6,8,10],
                [3,9,27,81]
                ]

    WFCnt = [5,10,15,20,25,30,35,40,45,50]
    OOSRate = [0.025,0.05,0.075,0.1,0.125,0.15,0.175,0.2,0.225,0.25,0.275,0.3]
    AnlyPrd = [99999]
#   listの指定要素までのリスト数の積を累積したリストを作る 0=8 1=8 2=40 3=160
#   idx % (全部の要素数/len(prmOptRg[1]))

#WFAのためにデータ形式は足数に対するOOSの割合とWF回数で決めたほうが良さげ
#その後WFA用に期間毎のデータに変換する必要があるので上記の内容も保持するのが望ましい。
#足数or期間とOOSの割合とWF回数の3つをパラメーターにする？
#OOSrate WFCnt 期間はタプル型で結果を期間ごとにセットにして保存する
#    WFA(objcFunc,prmOptRg,WFCnt, OOSRate, AnlyPrd)

    #目的関数と組み合わせたい変数群をリストの場合の最適化
#    Opt(objcFunc,prmOptRg)

    #目的関数＆引数と組み合わせたい変数群をリストの場合の最適化
    prmOptRg2 = [
        WFCnt,OOSRate,AnlyPrd,[prmOptRg]
    ]
    Opt(WFO,prmOptRg2)
