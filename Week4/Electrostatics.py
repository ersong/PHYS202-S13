import numpy as np

def pointPotential(x,y,q,posx,posy):
    """Give charge q in Coulombs, charge location (x,y) in meters, and point of interest (posx, posy) in meters"""
    Vxy=(8.8975517873681764e9)*q/np.sqrt((x-posx)**2.+(y-posy)**2.)
    return Vxy

def dipolePotential(x,y,q,d,angle):
    """Give charge q in Coulombs, charge location (x,y) in meters, distance d in meters, and angle of rotation, angle"""
    k=8.8975517873681764e9
    a=(d/2.)*np.cos(angle)
    b=(d/2.)*np.sin(angle)
    c1=np.sqrt((x-a)**2.+(y-b)**2.)
    c2=np.sqrt((x+a)**2.+(y+b)**2.)
    kq=k*q
    Vxy = kq/c1-kq/c2
    return Vxy

def pointField(x,y,q,Xq,Yq):
    """Takes array (x,y), charge q, and position Xq,Yq, and returns tuple (Ex,Ey)"""
    k=8.98e9
    E1=k*q*(x-Xq)/((x-Xq)**2+(y-Yq)**2)**.5
    E2=k*q*(y-Yq)/((x-Xq)**2+(y-Yq)**2)**.5
    Ex=sum(E1)
    Ey=sum(E2)
    return (Ex,Ey)