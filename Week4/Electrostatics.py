from math import *

def pointPotential(x,y,q,posx,posy):
    """Give charge q in Coulombs, charge location (x,y) in meters, and point of interest (posx, posy) in meters"""
    Vxy=(8.8975517873681764e9)*q/sqrt((x-posx)**2.+(y-posy)**2.)
    return Vxy

def dipolePotential(x,y,q,d,angle):
    """Give charge q in Coulombs, charge location (x,y) in meters, distance d in meters, and angle of rotation, angle"""
    k=8.8975517873681764e9
    a=(d/2.)*cos(angle)
    b=(d/2.)*sin(angle)
    c1=sqrt((x-a)**2.+(y-b)**2.)
    c2=sqrt((x+a)**2.+(y+b)**2.)
    kq=k*q
    Vxy = kq/c1-kq/c2
    return Vxy