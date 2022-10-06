import radar
from datetime import datetime, date

def get_fecha_nacimiento():
    now = datetime.now()

    ano_mayor_de_edad = int(now.strftime('%Y')) - 18
    ano_mayor_edad_promedio = int(now.strftime('%Y')) - 65

    mes = now.strftime('%m')
    dia = now.strftime('%d')


    date_start = f'{str(ano_mayor_edad_promedio)}-{mes}-{dia}'

    date_end = f'{str(ano_mayor_de_edad)}-{mes}-{dia}'


    # Generate random datetime (parsing dates from str values)
    fecha_nacimiento = radar.random_datetime(start=date_start, stop=date_end)

    return str(fecha_nacimiento)


def get_edad(fecha):

    born = fecha.split('-') #born[0] >> year , born[1] >> month , born[2] >> day

    today = date.today() 
    return today.year - int(born[0]) - ((today.month, today.day) < (int(born[1]), int(born[2])))



def get_info_nacimiento():
    fecha_nacimiento = get_fecha_nacimiento()
    edad = get_edad(fecha_nacimiento)
    
    response  = {
        'fecha_nacimiento': fecha_nacimiento,
        'edad': edad
    }
    
    return response 