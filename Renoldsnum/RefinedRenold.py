def ReynoldsNumber(density=None, flowvelocity=None, dia=None, dynamicviscosity=None, re=None):
    """Compute Reynolds number or solve any missing variable."""
    
    # Calculate Re
    if re is None and None not in (density, flowvelocity, dia, dynamicviscosity):
        return (density * dia * flowvelocity) / dynamicviscosity

    # Solve density
    if density is None and None not in (re, flowvelocity, dia, dynamicviscosity):
        return (dynamicviscosity * re) / (dia * flowvelocity)

    # Solve velocity
    if flowvelocity is None and None not in (re, density, dia, dynamicviscosity):
        return (dynamicviscosity * re) / (dia * density)

    # Solve viscosity
    if dynamicviscosity is None and None not in (density, flowvelocity, dia, re):
        return (density * dia * flowvelocity) / re

    return None


def FlowType(re):
    """Classify flow type based on Reynolds number."""
    if re < 2000:
        print("Laminar Flow:", re)
    elif 2000 <= re <= 4000:
        print("Transitional Flow:", re)
    else:
        print("Turbulent Flow:", re)


def getinput():
    density = input("Density: ")
    flowvelocity = input("Velocity: ")
    dia = input("Diameter: ")
    dynamicviscosity = input("Viscosity: ")
    re = input("Reynolds Number: ")

    density = float(density) if density else None
    flowvelocity = float(flowvelocity) if flowvelocity else None
    dia = float(dia) if dia else None
    dynamicviscosity = float(dynamicviscosity) if dynamicviscosity else None
    re = float(re) if re else None

    result = ReynoldsNumber(density, flowvelocity, dia, dynamicviscosity, re)

    print("\nCalculated value:", result)

    if re is None:  # if Re was not provided, result IS Re
        FlowType(result)
    else:
        FlowType(re)


getinput()
