import random

LISTA_GENEROS = ['mujer', 'hombre']


def get_genero():
    return random.choice(list(LISTA_GENEROS))
