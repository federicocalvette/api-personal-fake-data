import API_coutries.configs as api_config
import requests
import random


PERSONAL_TOKEN = api_config.PERSONAL_TOKEN
USER_EMAIL = api_config.USER_EMAIL


class Localidad():

    def __init__(self, pais):
        self.pais = pais
        self.access_token = get_access_token()
        self.state = get_states(self.access_token, pais)
        self.city = get_cities(self.access_token, self.state)

    def get_json_localidad(self):
        return {
            'Pais': self.pais,
            'Estado': self.state,
            'Ciudad': self.city
        }


def get_access_token():
    payload = {}
    headers = {
        'Accept': 'application/json',
        'api-token': PERSONAL_TOKEN,
        'user-email': USER_EMAIL
    }

    response = requests.request(
        "GET", api_config.URL_GET_ACCESS_TOKEN, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        auth_token = data.get("auth_token", "")
        return auth_token
    else:
        return 'Error obteniendo el auth_token'


def get_states(access_token, pais):

    payload = {}
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.request(
        "GET", api_config.URL_GET_STATES + pais, headers=headers, data=payload)

    #print(response.json())
    if response.status_code == 200:
        data = response.json()
        array_states = []

        for item in data:
            array_states.append(item['state_name'])
        try:
            state = random.choice(array_states)
        except IndexError:
            state = None
        return state

    else:
        return 'Error obteniendo el state'


def get_cities(access_token, state):
    payload = {}
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.request(
        "GET", api_config.URL_GET_CITIES+state, headers=headers, data=payload)

    #print(response.text)
    if response.status_code == 200:
        data = response.json()
        array_cities = []
        for item in data:
            array_cities.append(item['city_name'])

        try:
            city = random.choice(array_cities)
        except IndexError:
            city = None
        return city
    else:
        return 'Error obteniendo la city'
