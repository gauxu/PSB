from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import unittest

def func(x, y):
    return x**2 + y**2


#-----------------------------------------------------------------------
# Test用目的関数
#-----------------------------------------------------------------------
def TstOptform(args):
    #print(args)
    tmp=1
    for cnt in range(len(args)):
        if cnt==0:
            tmp+=args[cnt]**(len(args)-cnt)
        if cnt>0:
            tmp-=args[cnt]**(len(args)-cnt)
    return tmp
#-----------------------------------------------------------------------
# Test用目的関数ここまで
#-----------------------------------------------------------------------


class StrategyIF(unittest.TestCase):
    def __init__(self):
        print(super().__init__)
        super().__init__()
        __MyAssertion(self,__init__)
    def RuleMethod(self):
        __MyAssertion(self,RuleMethod)
    def __MyAssertion(self,msg):
        tmp="[MyAsserion] Must Orveride"+ self +"on" + msg + "."
        assert False,tmp
        
    
class Strategy1(StrategyIF):
    def __init__(self):
        print("Strategy1 instance")
    def RuleMethod(self):
        print("override success.")

class Strategy2(StrategyIF):
    def __init__(self):
        print("Strategy2 instance")
    def RuleMethod(self):
        print("override success.")

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == "__main__":
    unittest.main()
    stIF=StrategyIF
    st1=Strategy1()
    st2=Strategy2()


"""
    print("Execution from cmd! at ",__name__)
    func2()

    x = np.arange(-3.0, 3.0, 0.1)
    y = np.arange(-3.0, 3.0, 0.1)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)
    print(x)
    print(y)
    print(X)
    print(Y)
    print(Z)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    ax.plot_wireframe(X, Y, Z)
    plt.show()
"""
