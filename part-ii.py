import Radial_functions as Rf 
import matplotlib.pyplot as plt
import numpy as np
import radial as rad
import radiallog as radlog
import pandas as pd

#numbers for Na I
Z = 11
N = 11
zeta = Z - N + 1    # = 1 for Na I
a = 0.2683          # lab value

orbitals=[

    (1, 0, "1s"),
    (2, 0, "2s"),
    (2, 1, "2p"),
    (3, 0, "3s"),
    (3, 1, "3p"),
    (3, 2, "3d"),
    (4, 0, "4s"),
    (4, 1, "4p"),
    (4, 2, "4d"),
    (4, 3, "4f"),
    (5, 0, "5s"),
] #which orbitals to compute with n and l and their name (i keep forgetting)



energies=[]
for (n,l, lab) in orbitals:
    E=radlog.radiallog(l=l,n=n,Z=Z,zeta=zeta,a=a, plot=False)
    energies.append(E[2])

data={"orbital":lab,
    "Computed Energies":energies,}
df=pd.DataFrame(data)
print(df)