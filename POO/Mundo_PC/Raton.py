
from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones=0
    def __init__(self, marca, tipo_entrada) -> None:
        super().__init__(marca, tipo_entrada)
        Raton.contador_ratones+=1
        self._id_raton= Raton.contador_ratones
        pass
    
    def __str__(self) -> str:
        return f'Id: {self._id_raton}, Marca: {self._marca} , Tipo_entrada: {self._tipo_entrada}'
    pass

if __name__=='__main__':
    raton=Raton("HP","USB")
    print(raton)