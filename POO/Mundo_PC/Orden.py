class Orden:
    contador_ordenes=0
    def __init__(self, computadoras) -> None:
        Orden.contador_ordenes+=1
        self._id_orden=Orden.contador_ordenes
        self._computadoras=computadoras    
        pass
    def agregar_computadora(self,computadora):
        self._computadoras.append(computadora)
        pass
    def __str__(self) -> str:
        computadoras_str=''
        for computadora in self._computadoras:
            computadoras_str+= computadora.__str__()
        return f'''
Orden: {self._id_orden}
    Computadoras: {computadoras_str}       
        
        '''



    pass