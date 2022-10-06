import random

LISTA_LENGUAJE = ['ES','BR', 'ES', 'ES', 'US']


def get_lenguaje():
    """Funcion para obtener la lengua / idioma de los datos

    Returns:
        string: Idioma / lengua
    """    
    return random.choice(list(LISTA_LENGUAJE))
