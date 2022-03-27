class Persona:
    contador_personas=0
    def __init__(self,nombre,edad) -> None:
        #Persona.contador_personas+=1
        self.id_persona=Persona.generar_siguiente_valor()
        self.nombre=nombre
        self.edad=edad
        pass
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas+=1
        return cls.contador_personas
    def __str__(self) -> str:
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'
    pass
persona1=Persona('Juan',28)
print(persona1)
persona2=Persona('Karla',30)
print(persona2)