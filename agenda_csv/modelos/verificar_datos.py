import re

regex_email = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
regex_phone = r'^[0-9]{9}$'


class Validacion:
    
    def __init__(self):
        pass

    def validar_nombre(self, nombre):
        if len(nombre) < 3 or len(nombre) > 50:
            raise ValueError(f'El nombre debe tener como minimo 3 caracteres y un maximo de 50 caracteres, tamaño actual: {len(nombre)}.')
        return True

    def validar_email(self, email):
        if not re.search(regex_email, email):
            raise ValueError('El formato del email no es valido.')
        return True

    def validar_telefono(self, telefono):
        if not re.search(regex_phone, telefono):
            raise ValueError('El formato del telefono no es valido, debe ser un número de 9 cifras sin guiones ni puntos.')
        return True