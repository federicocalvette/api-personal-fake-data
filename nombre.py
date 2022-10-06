import random


def get_nombre(codigo_pais, genero_form):
    lines = open(f'./data_mock/{codigo_pais}/nombre_{genero_form}.txt').read().splitlines()
    nombre =random.choice(lines)
    return nombre