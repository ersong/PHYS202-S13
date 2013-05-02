import numpy as np

def finiteDifference(x,y):
    """takes in x parameter, function y parameter, and approximates the integral using the 2 point finite difference method"""
    dydx=zeros(y.shape,float)#initialize array to 0s
    dydx[1:-1]=(y[2:]-y[:-2])/(x[2:]-x[:-2])#exclude endpoints, the rest of them are [y(x+2)-y(x)]/[x2-x0], makes no (blank)ing sense
    dydx[0]=(y[1]-y[0])/(x[1]-x[0])#first term = slope
    dydx[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])#slope of last term = [y(last)-y(before last]]/[x(last)-x(before)]
    return dydx

def fourPtFiniteDiff(x,y):
    """takes in x parameter, function y parameter, and approximates the integral using the 4 point finite difference method"""
    dydx=zeros(y.shape,float)#initialize dydx array with 0s
    dydx[0]=(y[1]-y[0])/(x[1]-x[0])#first term = slope
    dydx[1]=(y[2]-y[1])/(x[2]-x[1])#2nd term = slope
    dydx[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])#last term= slope
    dydx[-2]=(y[-2]-y[-3])/(x[-2]-x[-3])#term before last term=slope
    dydx[2:-3]=(y[0:-5]-8*y[1:-4]+8*y[3:-2]-y[4:-1])/(12*(x[3:-2]-x[2:-3]))#I never learned the 4pt Formula in Calculus BC, they teach different things
    
    return dydx