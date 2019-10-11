
from XavgCrossOverOpt import XavgCrossOver
#Note: This imported method come true using by functional pointer.

def OptWFA(objcFunc,prmOptRg,InSmpPrd,OutSmpPrd):

    #���X�g�^rsltOpt:�ϐ��̐��ɉ����čœK�����ʂ̉񐔂��搔�I�ɑ�����
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
# �œK���v���Z�X�F
# ���͕ϐ��y�A�ɑ΂��œK���A����ꂽ���ʂ̌����y�ю��̕ϐ��g�����肵�ēx�œK��
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#   Case1.��������
#       �񐔂Ə��Ԃ����܂��Ă�̂ŁA����ϐ����܂Ƃ߂ă��X�g�ɂ��ē���
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
        #rslt��tmp3��ǉ�
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


    for opt_cnt in range(len(rsltOpt)):               #�ϐ��̓C���f�b�N�X�w�肵�Ēl��n���ׂ�
#        print("execute opt_cnt=",opt_cnt)
        pass

#-----------------------------------------------------------------------
# �œK���v���Z�X�����܂�
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# �ړI�֐�
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
# �ړI�֐������܂�
#-----------------------------------------------------------------------

if __name__ == "__main__":
    print("execution from cmd! at ",__name__)
    objcFunc = optform
#    objcFunc = XavgCrossOver
    #prmOptRg[[x1,x2...xi],[y1,y2...yj]...]
    #�œK���񐔎����v�Z�̂���Variable�̐������p��
    prmOptRg = [
                [2,4,8,16,32,64,128,256],
                [2,4,6,8,10],
                [3,9,27,81]
                ]

    #("2000-01-01","2005-01-01"),yahoo�̃f�[�^�͕\�L�œ����Ă���̂ł��̂����Ή�
    InSmpPrd  = [(1/1/2000,1/1/2005),(1/1/2001,1/1/2006),(1/1/2002,1/1/2007),(1/1/2003,1/1/2008),(1/1/2004,1/1/2009)]
    OutSmpPrd = [(1/1/2005,1/1/2006),(1/1/2006,1/1/2007),(1/1/2007,1/1/2008),(1/1/2008,1/1/2009),(1/1/2009,1/1/2010)]

#   list�̎w��v�f�܂ł̃��X�g���̐ς�ݐς������X�g����� 0=8 1=8 2=40 3=160
#   idx % (�S���̗v�f��/len(prmOptRg[1]))

#WFA�̂��߂Ƀf�[�^�`���͑����ɑ΂���OOS�̊�����WF�񐔂Ō��߂��ق����ǂ���
#���̌�WFA�p�Ɋ��Ԗ��̃f�[�^�ɕϊ�����K�v������̂ŏ�L�̓��e���ێ�����̂��]�܂����B
#����or���Ԃ�OOS�̊�����WF�񐔂�3���p�����[�^�[�ɂ���H
    OptWFA(objcFunc,prmOptRg,InSmpPrd,OutSmpPrd)