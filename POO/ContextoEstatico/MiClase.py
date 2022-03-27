class MiClase:
    variables_clase= 'Valor variable'
    def __init__(self, variable_instancia) -> None:
        self.variable_instancia=variable_instancia
        pass
    #metodo estatico
    @staticmethod
    def metodo_estatico():
        print(MiClase.variables_clase)
        pass
    @classmethod
    def metodo_clase(cls):
        
        print(cls.variables_clase)
        pass
clase_1=MiClase('variable objeto 1')
clase_2= MiClase('varible objeto 2')
#clase_1.variables_clase='dd'
MiClase.variables_clase='hello'
print(clase_1.variables_clase,clase_2.variables_clase)
MiClase.metodo_estatico()
MiClase.metodo_clase()