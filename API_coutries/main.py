from API_coutries.localidad import Localidad


def get_json_localidad(pais):
    localidad = Localidad(pais)
    json_localidad = localidad.get_json_localidad()
    return json_localidad