from test import TstOptform
#Note: This imported method come true using by functional pointer.

class RsltOptPrm:
    AbstracVal = list()#[0]に相当 1層目は空で2層目から変数ペアとしてこのクラスが入る
    EbdymntVal = list()#[1~n]に相当 要素はこのクラス　最終層では空にするor結果のObj?(これ以上具体性を高められない)
    #EbdymntValは順序不同に具体的な変数組を生成しリストにする(NOTE:Setは重複禁止だから使えなそう)
    #(順位付けや同列選択は抽出時に考慮し選択する？
    #その中からどのように変数を運用するかというだけの話である

    #処理毎のルーチンを関数ポインタとして渡す

def Opt(objcFunc,prmOptRg):

    #リスト型rsltOpt:変数の数に応じて最適化結果の回数が乗数的に増える
    #rsltOpt =[ [InSmp1,[valuepair1],OutSmp1,[outSmpRslt1]],[ [[x1,y1...],[rslt1,...]], ... ],
    #           [InSmp2,[valuepair2],OutSmp2,[outSmpRslt2]],[ [[x1,y1...],[rslt1,...]], ... ] ]
    #Access to valueList in period1 : rsltOpt[0][1][opt_cnt][0]
    #Access to resultList in period2: rsltOpt[1][1][opt_cnt][1]
    #Access to best valueList in period2 : rsltOpt[1][0][1]
    #Access to best resultList in period3: rsltOpt[2][0][3]
    #OOSとWFCntを考慮してもう一階層抽象化
    rsltOpt = []
    prmOptRglen = [len(prmOptRg[i]) for i in range(len(prmOptRg))]
    maxOptCnt = 1

#-----------------------------------------------------------------------
# 最適化プロセス：
# 入力変数ペアに対し最適化、得られた結果の検討及び次の変数組を決定し再度最適化
#-----------------------------------------------------------------------

#関数で切り分けるほうが望ましい その際に最適化方法の選択をする(※基本は総当たり)
#最適化部分のエンジンを切り分ける　変数リストと目的関数を引数とする別モジュールへ
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
        for i in range(len(prmOptRg)):#総当たり分に対応した引数組のリストを生成しtmp3に格納
            tmp2 = divmod( tmp1, prmOptRglen[i] )
            tmp1=tmp2[0]
            tmp3.append(prmOptRg[i][tmp2[1]])
        #rsltにtmp3を元に計算して帰ってきた結果とtmp3の引数組リストをセットにしてリストに追加
        rsltOpt.append([ tmp3,[objcFunc(tmp3)] ])#目的関数を関数ポインタ的にやる
        if opt_cnt == 0:
            max[0]=rsltOpt[opt_cnt][0]
            max[1][0]=rsltOpt[opt_cnt][1][0]
            min[0]=rsltOpt[opt_cnt][0]
            min[1][0]=rsltOpt[opt_cnt][1][0]
        if rsltOpt[opt_cnt][1][0]>max[1][0]:
            max[0]=rsltOpt[opt_cnt][0]
            max[1][0]=rsltOpt[opt_cnt][1][0]
        if rsltOpt[opt_cnt][1][0]<min[1][0]:
            min[0]=rsltOpt[opt_cnt][0]
            min[1][0]=rsltOpt[opt_cnt][1][0]


#    print("rsltOpt=",rsltOpt)
#    print("rsltOptlen=",len(rsltOpt))
#    print("max=",max)
#    print("min=",min)

    return rsltOpt,len(rsltOpt),max,min

#-----------------------------------------------------------------------
# 最適化プロセスここまで
#-----------------------------------------------------------------------



if __name__ == "__main__":
    print("execution from cmd! at ",__name__)
    objcFunc = TstOptform
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

    #目的関数＆引数と組み合わせたい変数群をリストの場合の最適化
    result=Opt(objcFunc,prmOptRg)
    for i in range(len(result)):
        print(result[i])
