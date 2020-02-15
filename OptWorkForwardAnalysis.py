
from XavgCrossOverOpt import XavgCrossOver
from OptUnit import Opt
from test import TstOptform
#Note: This imported method come true using by functional pointer.

#-----------------------------------------------------------------------
# WFAnlyze�@�֐��|�C���^�I�Ȏg�����ŌĂяo��
#-----------------------------------------------------------------------
def WFO(args):
    WFCnt = args[0]
    OOSRate = args[1]
    AnlyPrd = args[2]
    prmOptRg = args[3]  #�ϐ����X�g
    #("2000-01-01","2005-01-01"),yahoo�̃f�[�^�͕\�L�œ����Ă���̂ł��̂����Ή�
    #args������In&OutSmpPrd���v�Z
    InSmpPrd  = [(1/1/2000,1/1/2005),(1/1/2001,1/1/2006),(1/1/2002,1/1/2007),(1/1/2003,1/1/2008),(1/1/2004,1/1/2009)]
    OutSmpPrd = [(1/1/2005,1/1/2006),(1/1/2006,1/1/2007),(1/1/2007,1/1/2008),(1/1/2008,1/1/2009),(1/1/2009,1/1/2010)]

#    reslut=Opt(TstOptform,prmOptRg)#�ʂł���ɍœK��
#   InSmpPrd��prmOptRg�𓝍����čœK�������AOutSmpPrd�p�ϐ��擾
    reslut=Opt(XavgCrossOver,prmOptRg)#�ʂł���ɍœK���@���ԕϐ����Œ�A�p�����[�^�[���R�œ�����

#    print(reslut)
#   ���ꂼ��̊��Ԗ��ɍœK���ɑΉ������ϐ��ƍœK�����ʂ��A���Ă���@return rsltOpt,len(rsltOpt),max,min
#   ���̏ꍇ�͐ݒ���Ԃƕϐ��g�ƌ��ʂ̂݋A���Ă��邪���ꂼ��̌��ʂ���œ������Ȃ���΂Ȃ�Ȃ�
#   �܂������ɕ�����InOutSmp���Ԃ̑g�ݍ��킹���ێ������܂܌v�Z����K�v����B
#   InSmpPrd����1���WFO�̌��ʂ��ȉ��̂悤�Ɋi�[����
#   [[(1/1/2000,1/1/2005):(1/1/2005,1/1/2006),prmOptRg�g�ݍ��킹,����],�ȉ����l]
#   ��L�����ɍŏI���ʂ��v�Z����@WFA�͂���𕡐��񑩂˂銴��
    return args
#-----------------------------------------------------------------------
# WFAnlyze�����܂�
#-----------------------------------------------------------------------

if __name__ == "__main__":
    print("execution from cmd! at ",__name__)
    objcFunc = TstOptform
#    objcFunc = XavgCrossOver
    #prmOptRg[[x1,x2...xi],[y1,y2...yj]...]
    #�œK���񐔎����v�Z�̂���Variable�̐������p��
    prmOptRg = [
                [2,4,8,16,32,64,128,256],
                [2,4,6,8,10],
                [3,9,27,81]
                ]

    WFCnt = [5,10,15,20,25,30,35,40,45,50]
    OOSRate = [0.025,0.05,0.075,0.1,0.125,0.15,0.175,0.2,0.225,0.25,0.275,0.3]
    AnlyPrd = [99999]
#   list�̎w��v�f�܂ł̃��X�g���̐ς�ݐς������X�g����� 0=8 1=8 2=40 3=160
#   idx % (�S���̗v�f��/len(prmOptRg[1]))

#WFA�̂��߂Ƀf�[�^�`���͑����ɑ΂���OOS�̊�����WF�񐔂Ō��߂��ق����ǂ���
#���̌�WFA�p�Ɋ��Ԗ��̃f�[�^�ɕϊ�����K�v������̂ŏ�L�̓��e���ێ�����̂��]�܂����B
#����or���Ԃ�OOS�̊�����WF�񐔂�3���p�����[�^�[�ɂ���H
#OOSrate WFCnt ���Ԃ̓^�v���^�Ō��ʂ����Ԃ��ƂɃZ�b�g�ɂ��ĕۑ�����
#    WFA(objcFunc,prmOptRg,WFCnt, OOSRate, AnlyPrd)

    #�ړI�֐��Ƒg�ݍ��킹�����ϐ��Q�����X�g�̏ꍇ�̍œK��
#    Opt(objcFunc,prmOptRg)

    #�ړI�֐��������Ƒg�ݍ��킹�����ϐ��Q�����X�g�̏ꍇ�̍œK��
    prmOptRg2 = [
        WFCnt,OOSRate,AnlyPrd,[prmOptRg]
    ]
    Opt(WFO,prmOptRg2)
