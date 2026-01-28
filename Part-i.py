import Radial_functions as Rf 
import matplotlib.pyplot as plt
import numpy as np
import radial as ra

#For question two
r = np.linspace(0,20,10000) 
Z = 1


P = Rf.P1s(r,Z)
P3s = Rf.P3s(r,Z)
P3p = Rf.P3p(r,Z)
P3d = Rf.P3d(r,Z)

"""
plt.plot(r,P)
plt.plot(r,P3s)
plt.plot(r,P3p)
plt.plot(r,P3d)
plt.legend(["P","P3s","P3p","P3d"])
plt.show
plt.savefig('Q2-Pplots.png')
"""

def V(r,l):
    return -(Z/r) + (l*(l+1))/(2*r**2)

Vs = V(r,0)
Vp = V(r,1)
Vd = V(r,2)

r = np.clip(r, 0.1,8)
Vs = np.clip(Vs, -3, 0.5)
Vp = np.clip(Vp, -3, 0.5)
Vd = np.clip(Vd, -3, 0.5)
"""
plt.plot(r, Vs)
plt.plot(r,Vp)
plt.plot(r,Vd)
plt.legend(["Vs","Vp","Vd"])
plt.savefig('Q2-Potentials')
"""
l = 0
n = 1
Z = 1

r,P,E = ra.radial(l,n,Z)

import radiallog as rl
r,P,E = rl.radiallog(l,n,Z)
