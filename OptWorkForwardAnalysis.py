
from XavgCrossOverOpt import XavgCrossOver
#Note: This imported method come true using by functional pointer.

def OptWFA(objcFunc,prmOptRg,InSmpPrd,OutSmpPrd):

    #リスト型rsltOpt:変数の数に応じて最適化結果の回数が乗数的に増える
    #rsltOpt =[ [InSmp1,[valuepair1],OutSmp1,[outSmpRslt1]],[ [[x1,y1...],[rslt1,...]], ... ],
    #           [InSmp2,[valuepair2],OutSmp2,[outSmpRslt2]],[ [[x1,y1...],[rslt1,...]], ... ] ]
    #Access to valueList in period1 : rsltOpt[0][1][opt_cnt][0]
    #Access to resultList in period2: rsltOpt[1][1][opt_cnt][1]
    #Access to best valueList in period2 : rsltOpt[1][0][1]
    #Access to best resultList in period3: rsltOpt[2][0][3]
    rsltOpt = []
    prmOptRglen = [len(prmOptRg[i]) for i in range(len(prmOptRg))]
    maxOptCnt = 1

#-----------------------------------------------------------------------
# 最適化プロセス：
# 入力変数ペアに対し最適化、得られた結果の検討及び次の変数組を決定し再度最適化
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#   Case1.総当たり
#       回数と順番が決まってるので、決定変数をまとめてリストにして入力
#-----------------------------------------------------------------------

    for i in range(len(prmOptRg)):
        maxOptCnt *= len(prmOptRg[i])

    max = [[],[-99999999999]]
    min = [[],[99999999999]]
    for opt_cnt in range(maxOptCnt):
        tmp1 = opt_cnt
        tmp2 = tuple()
        tmp3 = list()
        for i in range(len(prmOptRg)):
            tmp2 = divmod( tmp1, prmOptRglen[i] )
            tmp1=tmp2[0]
            tmp3.append(prmOptRg[i][tmp2[1]])
        #rsltにtmp3を追加
#        rsltOpt.append([tmp3,[]])
        rsltOpt.append([ tmp3,[objcFunc(tmp3)] ])
        if rsltOpt[opt_cnt][1][0]>max[1][0]:
            max[0]=rsltOpt[opt_cnt][0]
            max[1][0]=rsltOpt[opt_cnt][1][0]
        if rsltOpt[opt_cnt][1][0]<min[1][0]:
            min[0]=rsltOpt[opt_cnt][0]
            min[1][0]=rsltOpt[opt_cnt][1][0]
    print("rsltOpt=",rsltOpt)
    print("max=",max)
    print("min=",min)


    for opt_cnt in range(len(rsltOpt)):               #変数はインデックス指定して値を渡すべし
#        print("execute opt_cnt=",opt_cnt)
        pass

#-----------------------------------------------------------------------
# 最適化プロセスここまで
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# 目的関数
#-----------------------------------------------------------------------
def optform(args):
    tmp=1
    for cnt in range(len(args)):
        if cnt==0:
            tmp+=args[cnt]**(len(args)-cnt)
        if cnt>0:
            tmp-=args[cnt]**(len(args)-cnt)
    return tmp
#-----------------------------------------------------------------------
# 目的関数ここまで
#-----------------------------------------------------------------------

if __name__ == "__main__":
    print("execution from cmd! at ",__name__)
    objcFunc = optform
#    objcFunc = XavgCrossOver
    #prmOptRg[[x1,x2...xi],[y1,y2...yj]...]
    #最適化回数自動計算のためVariableの数だけ用意
    prmOptRg = [
                [2,4,8,16,32,64,128,256],
                [2,4,6,8,10],
                [3,9,27,81]
                ]

    #("2000-01-01","2005-01-01"),yahooのデータは表記で入ってくるのでそのうち対応
    InSmpPrd  = [(1/1/2000,1/1/2005),(1/1/2001,1/1/2006),(1/1/2002,1/1/2007),(1/1/2003,1/1/2008),(1/1/2004,1/1/2009)]
    OutSmpPrd = [(1/1/2005,1/1/2006),(1/1/2006,1/1/2007),(1/1/2007,1/1/2008),(1/1/2008,1/1/2009),(1/1/2009,1/1/2010)]

#   listの指定要素までのリスト数の積を累積したリストを作る 0=8 1=8 2=40 3=160
#   idx % (全部の要素数/len(prmOptRg[1]))

#WFAのためにデータ形式は足数に対するOOSの割合とWF回数で決めたほうが良さげ
#その後WFA用に期間毎のデータに変換する必要があるので上記の内容も保持するのが望ましい。
#足数or期間とOOSの割合とWF回数の3つをパラメーターにする？
    OptWFA(objcFunc,prmOptRg,InSmpPrd,OutSmpPrd)