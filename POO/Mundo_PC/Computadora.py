from Raton import Raton
from Monitor import Monitor
from Teclado import Teclado

class Computadora:
    contador_computadoras=0
    def __init__(self, nombre, monitor, teclado, raton) -> None:
        Computadora.contador_computadoras+=1
        self._id_computadora=Computadora.contador_computadoras
        self._nombre=nombre
        self._monitor=monitor
        self._teclado=teclado
        self._raton=raton 
        pass
    def __str__(self) -> str:
        return f'''
{self._nombre}: {self._id_computadora}
Monitor: {self._monitor}
Teclado: {self._teclado}
Ratón:{self._raton}
        '''
    pass
if __name__=='__main__':
    teclado1= Teclado('HP','USB')
    raton1=Raton('HP','Bluetooth')
    monitor1=Monitor('HP',22)
    computador1=Computadora('HP',monitor1,teclado1,raton1)
    print(teclado1)
    print(raton1)
    print(monitor1)
    print(computador1)