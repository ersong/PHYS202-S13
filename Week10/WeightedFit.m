function [slope,intercept,slerr,interr] = WeightedFit(x,y,z)
%Take in arrays representing (x,y) values for a set of linearly varying data, error z, and perform a weighted linear least squares regression. Return the resulting slope and intercept parameters of the best fit line with their uncertainties.
%   Detailed explanation goes here
%retval =
n=size(x);
    xp=0;%<x>
    for i =1:n,
        xp+=x[i]
    
    xp/=n;
    yp=0;%<y>
    for i =1:n,
        yp+=y[i]
    
    yp=float(yp/n);
    xp2=0;%<x^2>
    
    for i =1:n,
        xp2+=(x[i])^2
    
    xp2=float(xp2/n);
    xy=0;%<xy>
    
    for i =1:n,
        xy+=x[i]*y[i]
    
    xy=float(xy/n);
    slope=(xy-xp*yp)/(xp2-xp^2.);
    intercept=(xp2*yp-xp*xy)/(xp2-xp^2.);
    delta=zeros(shape(x));
    
    for i =1:n,
        delta[i]=y[i]-(slope*x[i]+intercept)
    %print delta
    
    delta2=0;
    for i =1:n,
        %print delta2
        delta2+=delta[i]^2
    
    delta2 = float(delta2/n);
    slerr =float((1/(n-2))*(delta2/(xp2-xp^2.)))^.5;
    interr =float((1/(n-2))*(delta2*xp2/(xp2-xp^2.)))^.5;

end

