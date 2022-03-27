class Persona:
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad
        pass
    def __str__(self) -> str:
        return f'Persona: [Nombre:{self.nombre}, Edad: {self.edad}]'
        pass
    pass

class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo) -> None:
        super().__init__(nombre,edad)
        self.sueldo=sueldo
        pass
    def __str__(self) -> str:
        return f'Empleado: [Sueldo:{self.sueldo}] {super().__str__()}'
    pass
"""
empleado1=Empleado('Juan',28,10000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)"""