import random

LISTA_GENEROS = ['mujer', 'hombre']


def get_genero():
    """Funcion para obtener un genero random, H o M

    Returns:
        String: Genero
    """    
    return random.choice(list(LISTA_GENEROS))
