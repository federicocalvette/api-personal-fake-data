import radar
from datetime import datetime, date

def get_fecha_nacimiento():
    """ Funcion para generar fecha de nacimiento random """
    now = datetime.now()

    ano_mayor_de_edad = int(now.strftime('%Y')) - 18
    ano_mayor_edad_promedio = int(now.strftime('%Y')) - 60

    mes = now.strftime('%m')
    dia = now.strftime('%d')


    date_start = f'{str(ano_mayor_edad_promedio)}-{mes}-{dia}'

    date_end = f'{str(ano_mayor_de_edad)}-{mes}-{dia}'


    # Generate random datetime (parsing dates from str values)
    fecha_nacimiento = radar.random_datetime(start=date_start, stop=date_end)

    return str(fecha_nacimiento)


def get_edad(fecha_gen):
    """
    Description of get_edad: Funcion para calcular la edad en funcion de la fecha de nacimiento

    Args:
        fecha_gen (date): Fecha de nacimiento 

    """
    try:
        fecha = fecha_gen.split(' ')
        born = fecha[0].split('-') #born[0] >> year , born[1] >> month , born[2] >> day

        today = date.today() 
        return today.year - int(born[0]) - ((today.month, today.day) < (int(born[1]), int(born[2])))
    except ValueError:
        return 'null'


def get_info_nacimiento():
    """ Funcion para pedir la info de fecha nacimiento y edad """
    fecha_nacimiento = get_fecha_nacimiento()
    edad = get_edad(fecha_nacimiento)
    
    response  = {
        'fecha_nacimiento': fecha_nacimiento,
        'edad': edad
    }
    
    return response 