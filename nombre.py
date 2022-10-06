import random


def get_nombre(codigo_pais, genero_form):
    """_summary_

    Args:
        codigo_pais (String): Pais a usar ES, US, BR
        genero_form (String): Genero para buscar datos de hombre o de mujer en la data mock

    Returns:
        Str: Nombre
    """    
    lines = open(f'./data_mock/{codigo_pais}/nombre_{genero_form}.txt').read().splitlines()
    nombre =random.choice(lines)
    return nombre