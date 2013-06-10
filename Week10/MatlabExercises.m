%Exercise 1
%(a) Create a script file in Matlab with the following lines of code:
clear all; close all;
%%
% Enter the measured data points by hand
x = [-10 -9 -8 -7 -6 -5 -4 -3 0];
y = [2.65 2.10 1.90 1.40 1.00 0.80 0.60 0.30 0.00];
ey = [0.1 0.1 0.1 0.1 0.05 0.05 0.05 0.05 0.2];
% Plot the data with error bars
figure(1)
errorbar(x,y,ey,'b.')
% Don’t forget the labels
xlabel('x (mm)')
ylabel('y (mm)')
axis equal
%%
hold on
%%
% Do something in a second figure window.
%figure(5)
plot(x,x.^2)
hold off
%%
%b) Hope the function is accessible
WeightedFit(x,y,ey)
%%
%c)

%%
%d)
fun = @(a,b,c,x) -sqrt(a^2-(x-b).^2)+c;
% Find a starting point for the parameters a, b, and c.
guess = fun(15,0,15,x); % fun(a,b,c,x)
plot(x,guess,'r:')
% fit the data
fittedmodel = fit(x',y',fun,'StartPoint',[15 0 15]);
% plot the result
plot(fittedmodel,'r-');
%%
%e)
% fit the data using the uncertainties as weights
w = ey.^-2;
weightedfitted = fit(x',y',fun,'StartPoint',[15 0 15],'Weights',w');
% plot the result
plot(weightedfit,'r-');
%%
%Exercise 2
%(a) If you need to load data into Matlab from a file, rather than typing it in by hand, you can use the importdata()
%command. Create a new script file to analyze the radioactive decay data from Tuesday. Add these lines to your script to do
%load the data and plot it:
hold on
experiment = importdata('radioactivedecay.dat');
t = experiment.data(:,1);
N = experiment.data(:,2);
figure(42)
plot(t,N,'.b')
hold off
%(If you get errors, add a % to the front of the comment lines in the data file.)
%%
%(b) Now use Matlab's fitting tools to fit this data (i.e. don't linearize it and apply your own linear least squares fit, use the builtin
%function from Matlab we just learned about).
cftool( t, N );
%%
%(c) Print out the resulting fit parameters and plot the data with the fitted line on it. Add a legend to your plot.
%Hint: help legend
hold on
help legend
figure(3)
plot(t,N,'.b')
cftool( t, N );
hold off