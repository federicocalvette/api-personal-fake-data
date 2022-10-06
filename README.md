#API Personal Fake Data


##Environment
###Run activate env: 
`source ./env/bin/activate`

###Run deactivate env: 
`deactivate`


##API with uvicorn
Run:
`python -m uvicorn main:app --reload`


###Request
`curl --location --request GET 'http://localhost:8000/fake-personal-data'`

###Response
```
{
    "Nombre": "Lourdes",
    "Apellidos": {
        "Apellido_Paterno": "Gutiérrez",
        "Apellido_Materno": "Castro"
    },
    "Edad": 39,
    "Fecha_nacimiento": "1982-11-27",
    "Genero": "mujer",
    "Localidad": {
        "Pais": "Uruguay",
        "Estado": "Durazno",
        "Ciudad": "Durazno"
    },
    "Trabajo": {
        "Empresa": "Birideez",
        "Mail": "l-gutierrez8@hotmail.com",
        "Puesto": "Senior Manager IT"
    }
}
```