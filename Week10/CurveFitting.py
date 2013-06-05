from numpy import *

def LinearLeastSquaresFit(x,y):
    """Take in arrays representing (x,y) values for a set of linearly varying data and perform a linear least squares regression. Return the resulting slope and intercept parameters of the best fit line with their uncertainties."""
    if len(x)!=len(y):
        return "array sizes incompatible"
    n=len(x)
    xp=0#<x>
    for i in range(0,n):
        xp+=x[i]
    xp=float(xp/n)
    yp=0#<y>
    for i in range(0,n):
        yp+=y[i]
    yp=float(yp/n)
    xp2=0#<x^2>
    for i in range(0,n):
        xp2+=(x[i])**2
    xp2=float(xp2/n)
    xy=0#<xy>
    for i in range(0,n):
        xy+=x[i]*y[i]
    xy=float(xy/n)
    slope=(xy-xp*yp)/(xp2-xp**2.)
    intercept=(xp2*yp-xp*xy)/(xp2-xp**2.)
    delta=zeros(shape(x))
    for i in range(0,n):
        delta[i]=y[i]-(slope*x[i]+intercept)
    #print delta
    delta2=0
    for i in range(0,n):
        #print delta2
        delta2+=delta[i]**2
    delta2=float(delta2/n)
    slerr =float((1/(n-2))*(delta2/(xp2-xp**2.)))**.5
    interr =float((1/(n-2))*(delta2*xp2/(xp2-xp**2.)))**.5
    return slope,intercept,slerr,interr

def WeightedLinearLeastSquaresFit(x,y,z):
    """Take in arrays representing (x,y) values for a set of linearly varying data and perform a weighted linear least squares regression. Return the resulting slope and intercept parameters of the best fit line with their uncertainties."""
    if len(x)!=len(y):
        return "array sizes incompatible"
    n=len(x)
    #print "unc y",z
    w=zeros(shape(x))
    for i in range(0,n):
        w[i]=float(1/z[i]**2)
    #print "w",w
    a=0
    for i in range(0,n):
        a+=w[i]
    b=0
    for i in range(0,n):
        b+=w[i]*x[i]*y[i]
    c=0
    for i in range(0,n):
        c+=w[i]*x[i]
    d=0
    for i in range(0,n):
        d+=w[i]*y[i]
    e=0
    for i in range(0,n):
        e+=w[i]*y[i]*y[i]
    f=0
    for i in range(0,n):
        f+=w[i]*x[i]*x[i]
    slope=float(a*b-c*d)/(a*f-c**2)
    intercept=float(f*d-c*e)/(a*f-c**2)
    slerr=float(a/(a*f-c**2))**.5
    interr=float(f/(a*f-c**2))**.5
    return slope,intercept,slerr,interr