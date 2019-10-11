
from XavgCrossOverOpt import XavgCrossOver
#Note: This imported method come true using by functional pointer.

def OptUnit(objcFunc,prmOptRg,prmOptRglen):

    #���X�g�^rsltOpt:�ϐ��̐��ɉ����čœK�����ʂ̉񐔂��搔�I�ɑ�����
    #rsltOpt =[ [[x1,y1...],[rslt1,...]], ... ]
    #len(rsltOpt[])==i*j*k...
    #Access to valueList : rsltOpt[opt_cnt][0]
    #Access to resultList: rsltOpt[opt_cnt][1]
    rsltOpt = []

    maxOptCnt = 1

#-----------------------------------------------------------------------
# �œK���v���Z�X�F
# ���͕ϐ��y�A�ɑ΂��œK���A����ꂽ���ʂ̌����y�ю��̕ϐ��g�����肵�ēx�œK��
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#   Case1.��������
#       �񐔂Ə��Ԃ����܂��Ă�̂ŁA����ϐ����܂Ƃ߂ă��X�g�ɂ��ē���
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
        #rslt��tmp3��ǉ�
        rsltOpt.append([tmp3,[]])
#        rsltOpt.append([ tmp3,[objcFunc(tmp3)] ])
    print("rsltOpt=",rsltOpt)

    for opt_cnt in range(len(rsltOpt)):               #�ϐ��̓C���f�b�N�X�w�肵�Ēl��n���ׂ�
#        print("execute opt_cnt=",opt_cnt)
        pass

#-----------------------------------------------------------------------
# �œK���v���Z�X�����܂�
#-----------------------------------------------------------------------



if __name__ == "__main__":
    print("execution from cmd! at ",__name__)
    objcFunc = XavgCrossOver
    #prmOptRg[[x1,x2...xi],[y1,y2...yj]...]
    #�œK���񐔎����v�Z�̂���Variable�̐������p��
    prmOptRg = [
                [2,4,8,16,32,64,128,256],
                [2,4,6,8,10],
                [3,9,27,81]
                ]
    prmOptRglen = [8,5,4]
    #ex: print(prmOptRg[2][3])=81

#   list�̎w��v�f�܂ł̃��X�g���̐ς�ݐς������X�g����� 0=8 1=8 2=40 3=160
#   idx % (�S���̗v�f��/len(prmOptRg[1]))

    OptUnit(objcFunc,prmOptRg,prmOptRglen)