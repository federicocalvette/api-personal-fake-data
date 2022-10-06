import genero
import lenguaje
import pais
import nombre
import apellido
import puesto
import mail
import empresa
from API_coutries import main as main_localidad
import edad

class Persona():
    
    
    def __init__(self):
        """
        Description of __init__: contructor de la clase Persona

        Args:
            self (undefined):

        """
                

        # Genero para nombre.
        self.genero_form = genero.get_genero()

        # Codigo de país para saber que origen debe tener el nombre.
        self.codigo_pais = lenguaje.get_lenguaje()

        # Info del país seleccionado.
        self.nombre_pais = pais.get_pais(self.codigo_pais)

        # Localidad
        self.json_localidad = main_localidad.get_json_localidad(self.nombre_pais)

        # Nombre.
        self.nombre_form = nombre.get_nombre(self.codigo_pais, self.genero_form)

        # Apellido.
        self.apellido_form = apellido.get_apellido(self.codigo_pais)
        self.apellido_form_2 = apellido.get_apellido(self.codigo_pais)

        # Puesto de trabajo.
        self.puesto_form = puesto.get_puesto()

        # Empresa
        self.empresa_form = empresa.get_empresa()

        # Empresa mail
        self.empresa_mail = empresa.get_empresa_para_mail(self.empresa_form)
        #print('Empresa para el dominio del mail: '+empresa_mail)

        # Mail
        self.mail_form = mail.get_random_mail(self.nombre_form, self.apellido_form, self.empresa_mail)

        # Edad y fecha nacimiento
        info_nacimiento = edad.get_info_nacimiento()
        self.edad_form = info_nacimiento.get('edad')
        self.fecha_nacimiento = info_nacimiento.get('fecha_nacimiento')

    def get_fake_person(self):
        """Generador de la respuesta 

        Returns:
            json: json con la info de la persona fake
        """        
    
        response = {
            'Nombre': self.nombre_form,
            'Apellidos': {
                'Apellido_Paterno': self.apellido_form,
                'Apellido_Materno': self.apellido_form_2
            },
            'Edad': self.edad_form,
            'Fecha_nacimiento': self.fecha_nacimiento,
            'Genero': self.genero_form,
            'Localidad': self.json_localidad,
            'Trabajo': {
                'Empresa': self.empresa_form,
                'Mail': self.mail_form,
                'Puesto': self.puesto_form
            }
        }

        return response
