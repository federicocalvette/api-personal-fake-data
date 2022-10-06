from unicodedata import normalize


def sin_tilde(palabra):
    """Funcion aux para sacar tildes de los nombres/apellidos

    Args:
        palabra (string): Palabra con tilde a sacar

    Returns:
        string: palabra sin tilde
    """    
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    palabra_sin_tilde = normalize('NFKC', normalize('NFKD', palabra).translate(trans_tab))
    return palabra_sin_tilde