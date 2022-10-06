import random

ES = ["Argentina","Chile","Colombia","Ecuador","Mexico","Panama","Peru","Spain","Uruguay"]
BR = ["Brazil"]
US = ["United States"]

def get_pais(codigo_pais):
    """_summary_

    Args:
        codigo_pais (string): Lengua para pais

    Returns:
        string: Pais a usar
    """    
    if codigo_pais == 'ES':
        pais = random.choice(list(ES))
    elif codigo_pais == 'BR':
        pais = random.choice(list(BR))
    else:
        pais = random.choice(list(US))
    return pais

