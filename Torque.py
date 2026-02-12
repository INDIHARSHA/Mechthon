# Max Torque for a shaft is given below
# Tmax=16T/pi*d3
import numpy as np
Tmax=0
dia =float(input("Enter the diameter :"))
T=float(input("Enter the resisting torque :"))
Tmax=(16*T)/(np.pi*dia*dia*dia)
print(Tmax)
