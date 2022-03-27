from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden

teclado1= Teclado('HP','USB')
raton1=Raton('HP','Bluetooth')
monitor1=Monitor('HP',22)
computador1=Computadora('HP',monitor1,teclado1,raton1)
print(computador1)


teclado2= Teclado('LG','USB')
raton2=Raton('LG','Bluetooth')
monitor2=Monitor('LG',22)
computador2=Computadora('LG',monitor2,teclado2,raton2)
print(computador2)
orden1= Orden([computador1,computador2])

print(orden1)

teclado3= Teclado('ASUS','USB')
raton3=Raton('ASUS','Bluetooth')
monitor3=Monitor('ASUS',33)
computador3=Computadora('ASUS',monitor3,teclado3,raton3)
print(computador3)

orden1.agregar_computadora(computador3)
print(orden1)