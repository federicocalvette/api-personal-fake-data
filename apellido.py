import random


def get_apellido(codigo_pais):
    """
    get_apellido es una funcion para obtener apellidos random 

    Args:
        codigo_pais (str): Es el codigo que se usa para saber la lengua del apellido, ej: ESpañol USa BRasil

    """
    lines = open(f'./data_mock/{codigo_pais}/apellido.txt').read().splitlines()
    apellido =random.choice(lines)
    return apellido