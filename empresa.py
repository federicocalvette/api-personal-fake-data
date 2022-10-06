import random

def get_empresa():
    """ Description of get_empresa: función para obtener una empresa random de la lista con empresas mock """
    lines = open(f'./data_mock/empresas.txt').read().splitlines()
    empresa = random.choice(lines)
    return empresa


def get_empresa_para_mail(empresa_form): 
    """Funcion para depurar el nombre de la empresa y usarlo como dominio en el mail 

    Args:
        empresa_form (string): Nombre de la empresa

    Returns:
        string: Nombre empresa depurado 
    """    
    empresa = empresa_form.replace(" ", "")
    empresa = empresa.lower()
    return empresa