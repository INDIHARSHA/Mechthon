def Shrinkageallowance(tm,lnth,mtemp,rtemp):
    """used to calculate Shrinkage allowance of all materials to assist efficient
       casting, if you are unaware of thermal properties of materialtry to access the
       csv Thermal expansion file, the problem takes the following argumets 
       tm=Thermalexpansion of material
       lnth=length of casting material
       mtemp=temperature of molten metal
       rtemp=temperature of room temperature
    """
    sh=0
    sh=tm*lnth*(mtemp-rtemp)
    return sh
import pandas as pd
df=pd.read_csv("Thermalexpansion.csv")

tm=float(input())
lnth=float(input())
mtemp=float(input())
rtemp=float(input())
Shrinkageallowance(tm,lnth,mtemp,rtemp)
