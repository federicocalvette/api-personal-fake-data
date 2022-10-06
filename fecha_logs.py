from datetime import datetime

def get_fecha():
    now = datetime.now()
    day = "%d/%m/%Y %H:%M:%S"
    fecha = now.strftime(day)
    return fecha
