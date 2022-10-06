from unicodedata import normalize


def sin_tilde(palabra):
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    palabra_sin_tilde = normalize('NFKC', normalize('NFKD', palabra).translate(trans_tab))
    return palabra_sin_tilde