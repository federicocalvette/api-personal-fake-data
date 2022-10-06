import fecha_logs


FILE_PATH_OK = './logs/logs_ok.txt'
FILE_PATH_ERRORS = './logs/logs_errors.txt'
FILE_PATH_EXCEPTIONS = './logs/logs_exceptions.txt'



def loguear_ok(nombre_form, apellido_form, mail_form, id_pais, nombre_pais, empresa_form, puesto_form,user_agent):
    fecha = fecha_logs.get_fecha()
    with open(FILE_PATH_OK, 'a') as file:
        file.write(f"{fecha} | {nombre_form}, {apellido_form}, {mail_form}, {id_pais}, {nombre_pais}, {empresa_form}, {puesto_form} | {user_agent}")
        file.write("\n")

def loguear_error(status_code_resp, nombre_form, apellido_form, mail_form, id_pais, nombre_pais, empresa_form, puesto_form,user_agent):
    fecha = fecha_logs.get_fecha()
    with open(FILE_PATH_ERRORS, 'a') as file:
        file.write(f"{fecha} | {status_code_resp} | {nombre_form}, {apellido_form}, {mail_form}, {id_pais}, {nombre_pais}, {empresa_form}, {puesto_form} | {user_agent}")
        file.write("\n")

def loguear_exception(err):
    fecha = fecha_logs.get_fecha()
    with open(FILE_PATH_EXCEPTIONS, 'a') as file:
        file.write(f"{fecha} | {err}")
        file.write("\n")