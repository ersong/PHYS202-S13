import numpy as np

def fourPtFiniteDiff(x,y):
    if x.shape != y.shape:
        print "error: array mismatch"
        return NaN
    dydx = zeros(y.shape,float)
    dydx[0] = (y[1] - y[0]) / (x[1] - x[0])
    dydx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
    dydx[-2] = (y[-1] - y[-3]) / (2*(x[-1] - x[-2]))
    dydx[1] = (y[2] - y[0]) / (2*(x[-1] - x[-2]))

    for i, m in enumerate(y[2:-2]):
        i+=2
        dydx[i] = (y[i-2]-8*y[i-1]+8*y[i+1]-y[i+2])/(12*(x[i+1]-x[i]))
    
    return dydx

def finiteDifference(x,y):
    dy=diff(y)#y(n+1)-y(n)
    #help(diff)
    dx=diff(x)
    dydx=dy/dx
    return dydx