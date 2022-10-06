import random

ID_PAIS = {
    'ES': [
        {
            "id": 11,
            "Country": "Argentina"
        },
        {
            "id": 44,
            "Country": "Chile"
        },
        {
            "id": 48,
            "Country": "Colombia"
        },
        {
            "id": 64,
            "Country": "Ecuador"
        },
        {
            "id": 142,
            "Country": "Mexico"
        },
        {
            "id": 170,
            "Country": "Panama"
        },
        {
            "id": 173,
            "Country": "Peru"
        },
        {
            "id": 207,
            "Country": "Spain"
        },
        {
            "id": 235,
            "Country": "Uruguay"
        }
    ],
    'BR': [
        {
            "id": 31,
            "Country": "Brazil"
        }
    ],
    'US': [
        {
            "id": 233,
            "Country": "United States"
        }
    ]
}

def get_id_pais(codigo_pais):
    json_pais = random.choice(list(ID_PAIS[codigo_pais]))
    return json_pais
