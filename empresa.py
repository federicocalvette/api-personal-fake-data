import random

def get_empresa():
    lines = open(f'./data_mock/empresas.txt').read().splitlines()
    empresa = random.choice(lines)
    return empresa


def get_empresa_para_mail(empresa_form): 
    empresa = empresa_form.replace(" ", "")
    empresa = empresa.lower()
    return empresa