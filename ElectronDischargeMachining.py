import math

def find_parameter(E=None, C=None, Vb=None):
    """
    Find the missing parameter in EDM spark energy formula.
    Provide any two of E, C, Vb.
    
    Parameters:
    E (float): Energy in joules
    C (float): Capacitance in farads
    Vb (float): Breakdown voltage in volts
    
    Returns:
    dict: Dictionary with all three values
    """
    if E is None and C is not None and Vb is not None:
        E = 0.5 * C * (Vb ** 2)
    elif C is None and E is not None and Vb is not None:
        C = (2 * E) / (Vb ** 2)
    elif Vb is None and E is not None and C is not None:
        Vb = math.sqrt((2 * E) / C)
    else:
        raise ValueError("Please provide exactly two parameters.")
    
    return {"Energy (J)": E, "Capacitance (F)": C, "Breakdown Voltage (V)": Vb}

print(find_parameter(E=1, Vb=200))
