from Persona import Persona

print('Creación objetos'.center(50,'-'))
perosna1=Persona('Alex','Lopez',23)
perosna1.mostraDetalle()
print('Eliminar objetos'.center(50,'-'))
del perosna1
print(__name__)