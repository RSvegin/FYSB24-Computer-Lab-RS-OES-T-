Import Radial_functions.py as Rf 
Import matplotlib as plt

r = linspace(0,20,1000) 
Z = 1
P = Rf.P1s(r,Z)
plt.plot(r,P)
plt.show
