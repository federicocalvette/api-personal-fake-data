import random


def get_apellido(codigo_pais):
    lines = open(f'./data_mock/{codigo_pais}/apellido.txt').read().splitlines()
    apellido =random.choice(lines)
    return apellido