import random
from random import randrange
import sacar_tilde

LISTA_MAIL_DOMINIO_GENERICO = ['gmail.com','hotmail.com', 'yahoo.com', 'outlook.com']
LISTA_MAIL_DOMINIO_EMPRESA = ['.com', '.net', '.io', '.es', '.org', '.tech']
LISTA_CARACTER_DIV = ['.', '_', '-']


correo_tipo = random.randrange(15)


def get_random_mail(nombre, apellido, empresa):
    """get_random_mail: Funcion para generar el mail 

    Args:
        nombre (str): Nombre para crear el mail
        apellido (str): Apellido para crear el mail
        empresa (str): Empresa para crear el dominio del mail
    """
    
    nombre = sacar_tilde.sin_tilde(nombre)
    apellido = sacar_tilde.sin_tilde(apellido)

    if correo_tipo == 0:
        # fcalvette@gmail.com
        return(nombre[0].lower() + apellido.lower() + "@" + empresa.lower() + random.choice(LISTA_MAIL_DOMINIO_EMPRESA))

    elif correo_tipo == 1:
        # fcalvette@empresa.com
        return(nombre[0].lower() + apellido.lower() + "@" +
               random.choice(LISTA_MAIL_DOMINIO_GENERICO))

    elif correo_tipo == 2:
        # fc@empresa.com
        return(nombre[0].lower() + apellido[0].lower() + "@" +
               empresa.lower() + random.choice(LISTA_MAIL_DOMINIO_EMPRESA))

    elif correo_tipo == 3:
        # federicoc@empresa.com
        return(nombre.lower() + apellido[0].lower() + "@" +
               empresa.lower() + random.choice(LISTA_MAIL_DOMINIO_EMPRESA))

    elif correo_tipo == 4:
        # fcalvette1@gmail.com
        return(nombre[0].lower() + apellido.lower() + str(randrange(10)) + "@" + random.choice(LISTA_MAIL_DOMINIO_GENERICO))

    elif correo_tipo == 5:
        # fcalvette12@gmail.com
        return(nombre[0].lower() + apellido.lower() + str(randrange(10)) + str(randrange(10)) + "@" + random.choice(LISTA_MAIL_DOMINIO_GENERICO))

    elif correo_tipo == 6:
        # fcalvette123@gmail.com
        return(nombre[0].lower() + apellido.lower() + str(randrange(10)) + str(randrange(10)) + str(randrange(10)) + "@" + random.choice(LISTA_MAIL_DOMINIO_GENERICO))

    elif correo_tipo == 7:
        # fcalvette1234@gmail.com
        return(nombre[0].lower() + apellido.lower() + str(randrange(10)) + str(randrange(10)) + str(randrange(10)) + str(randrange(10)) + "@" + random.choice(LISTA_MAIL_DOMINIO_GENERICO))

    elif correo_tipo == 8:
        # f_calvette@gmail.com
        return(nombre[0].lower() + random.choice(LISTA_CARACTER_DIV) + apellido.lower() + "@" + random.choice(LISTA_MAIL_DOMINIO_GENERICO))

    elif correo_tipo == 9:
        # f_calvette1@gmail.com
        return(nombre[0].lower() + random.choice(LISTA_CARACTER_DIV) + apellido.lower() + str(randrange(10)) + "@" + random.choice(LISTA_MAIL_DOMINIO_GENERICO))

    elif correo_tipo == 10:
        # f_calvette12@gmail.com
        return(nombre[0].lower() + random.choice(LISTA_CARACTER_DIV) + apellido.lower() + str(randrange(10)) + str(randrange(10)) + "@" + random.choice(LISTA_MAIL_DOMINIO_GENERICO))

    elif correo_tipo == 11:
        # federico_calvette1@gmail.com
        return(nombre.lower() + random.choice(LISTA_CARACTER_DIV) + apellido.lower() + str(randrange(10)) + "@" + random.choice(LISTA_MAIL_DOMINIO_GENERICO))

    elif correo_tipo == 12:
        # federico_calvette12@gmail.com
        return(nombre.lower() + random.choice(LISTA_CARACTER_DIV) + apellido.lower() + str(randrange(10)) + str(randrange(10)) + "@" + random.choice(LISTA_MAIL_DOMINIO_GENERICO))

    elif correo_tipo == 13:
        # federico_c1@gmail.com
        return(nombre.lower() + random.choice(LISTA_CARACTER_DIV) + apellido[0].lower() + str(randrange(10)) + "@" + random.choice(LISTA_MAIL_DOMINIO_GENERICO))

    elif correo_tipo == 14:
        # federico_c12@gmail.com
        return(nombre.lower() + random.choice(LISTA_CARACTER_DIV) + apellido[0].lower() + str(randrange(10)) + str(randrange(10)) + "@" + random.choice(LISTA_MAIL_DOMINIO_GENERICO))

    else:
        # fcalvette@gmail.com
        return(nombre[0].lower() + apellido.lower() + "@" + empresa.lower() + random.choice(LISTA_MAIL_DOMINIO_EMPRESA))
