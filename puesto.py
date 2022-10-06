import random

def get_puesto():
    lines = open(f'./data_mock/puesto.txt').read().splitlines()
    puesto = random.choice(lines)
    return puesto