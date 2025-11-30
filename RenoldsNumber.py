def RenoldsNumber(density,flowvelocity,dia,dynamicviscosity):
   """ Reynolds number: Laminar versus turbulent flow
        Re=r*V*D/h
         r = density of liquid, V = mean 
        flow velocity, D = tube diameter, 
        h = dynamic viscosity of liquid"""
    re=0
    re=density*flowvelocity*dia
    re=re/dynamicviscosity
    return re

def FlowType(re):
   """Reynolds number tells about the flow type,
       either Laminar or turbulent flow """
    if re<2000:
        print("LaminarFlow",re)
    elif re in range(2001,4000):
        print("TurbulentFlow",re)
    elif re>4000:
        print("TurbulentFlow",re)


density=float(input())
flowvelocity=float(input())
dia=float(input())
dynamicviscosity=float(input())
RenoldsNumber(density,flowvelocity,dia,dynamicviscosity)

recal=RenoldsNumber(density,flowvelocity,dia,dynamicviscosity)
FlowType(recal)
