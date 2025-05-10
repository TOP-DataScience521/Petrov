def orth_triangle(
    *, 
    cathetus1: float = None, 
    cathetus2: float = None, 
    hypotenuse: float = None
) -> float | None:
    
    data_input = [cathetus1, cathetus2, hypotenuse]
    variables = [i for i in data_input if i != None]
    
    if len(variables) == 2:
        if hypotenuse == None:
            return (cathetus1**2+cathetus2**2)**0.5
        elif cathetus1 == None and hypotenuse >= cathetus2:
            return (hypotenuse**2-cathetus2**2)**0.5
        elif cathetus2 == None and hypotenuse >= cathetus1:
            return (hypotenuse**2-cathetus1**2)**0.5
        else:
            return None
    else: 
        return None
             
# >>> orth_triangle(cathetus1=6, cathetus2=10)
# 11.661903789690601
# >>> orth_triangle(hypotenuse=10, cathetus2=6)
# 8.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None