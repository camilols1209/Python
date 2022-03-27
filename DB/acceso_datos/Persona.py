from log_config import log
class Persona:
    def __init__(self,id_persona=None,nombre=None,apellido=None,email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido =apellido
        self._email = email
        pass
    def __str__(self) -> str:
        return f'''
        ID_PERSONA: {self._id_persona}, Nombre: {self._nombre},
        Apellido:{self._apellido}, Email: {self._email} '''
    @property
    def id_persona(self):
        return self._id_persona
    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido
    @property
    def email(self):
        return self._email

    @id_persona.setter
    def id_persona(self, value):
        self._id_persona = value
        pass
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
        pass
    @apellido.setter
    def pellido(self, value):
        self._apellido = value
        pass
    @email.setter
    def email(self, value):
        self._email = value
        pass
    pass

if __name__ == '__main__':
    persona1=Persona(1,'Juan','Perez','jperez@mail.com')
    log.debug(persona1)