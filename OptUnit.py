
from XavgCrossOverOpt import XavgCrossOver
#Note: This imported method come true using by functional pointer.

def OptUnit(objcFunc,prmOptRg,prmOptRglen):

    #リスト型rsltOpt:変数の数に応じて最適化結果の回数が乗数的に増える
    #rsltOpt =[ [[x1,y1...],[rslt1,...]], ... ]
    #len(rsltOpt[])==i*j*k...
    #Access to valueList : rsltOpt[opt_cnt][0]
    #Access to resultList: rsltOpt[opt_cnt][1]
    rsltOpt = []

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

    for opt_cnt in range(maxOptCnt):
        tmp1 = opt_cnt
        tmp2 = tuple()
        tmp3 = list()
        for i in range(len(prmOptRg)):
            tmp2 = divmod( tmp1, prmOptRglen[i] )
            tmp1=tmp2[0]
            tmp3.append(prmOptRg[i][tmp2[1]])
        #rsltにtmp3を追加
        rsltOpt.append([tmp3,[]])
#        rsltOpt.append([ tmp3,[objcFunc(tmp3)] ])
    print("rsltOpt=",rsltOpt)

    for opt_cnt in range(len(rsltOpt)):               #変数はインデックス指定して値を渡すべし
#        print("execute opt_cnt=",opt_cnt)
        pass

#-----------------------------------------------------------------------
# 最適化プロセスここまで
#-----------------------------------------------------------------------



if __name__ == "__main__":
    print("execution from cmd! at ",__name__)
    objcFunc = XavgCrossOver
    #prmOptRg[[x1,x2...xi],[y1,y2...yj]...]
    #最適化回数自動計算のためVariableの数だけ用意
    prmOptRg = [
                [2,4,8,16,32,64,128,256],
                [2,4,6,8,10],
                [3,9,27,81]
                ]
    prmOptRglen = [8,5,4]
    #ex: print(prmOptRg[2][3])=81

#   listの指定要素までのリスト数の積を累積したリストを作る 0=8 1=8 2=40 3=160
#   idx % (全部の要素数/len(prmOptRg[1]))

    OptUnit(objcFunc,prmOptRg,prmOptRglen)