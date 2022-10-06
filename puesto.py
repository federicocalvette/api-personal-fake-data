import random

def get_puesto():
    """Funcion para obtener puesto de trabajo mock random

    Returns:
        string: puesto mock
    """    
    lines = open(f'./data_mock/puesto.txt').read().splitlines()
    puesto = random.choice(lines)
    return puesto