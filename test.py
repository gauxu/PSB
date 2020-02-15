from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def func(x, y):
    return x**2 + y**2


#-----------------------------------------------------------------------
# Test?p?���?I?���??
#-----------------------------------------------------------------------
def TstOptform(args):
    tmp=1
    for cnt in range(len(args)):
        if cnt==0:
            tmp+=args[cnt]**(len(args)-cnt)
        if cnt>0:
            tmp-=args[cnt]**(len(args)-cnt)
    return tmp
#-----------------------------------------------------------------------
# Test?p?���?I?���???���?���?���?���
#-----------------------------------------------------------------------


class MP:
    mp=0

def func1(arg):
    mp1=arg
    mp1.mp=mp1.mp
    mp1.mp=4
#    return arg

def func2():
    mp=MP
    mp.mp=2
    commission=110
    tradeName="Test"
    entryPrice=0
    numShares=100
    myBPV=1000
    cumuProfit=300


    print(mp)
    a=func1(mp)
    print(mp)

if __name__ == "__main__":
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