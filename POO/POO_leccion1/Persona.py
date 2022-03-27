class Persona :
   
    def __init__(self,nombre, apellido, edad,*args,**kwargs):
        self._nombre=nombre
        self._apellido=apellido
        self._edad=edad
        self.args=args
        self.kwargs=kwargs
        pass
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter #decoradores
    def  nombre(self,nombre):
        self._nombre=nombre
    
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter #decoradores
    def  apellido(self,apellido):
        self._apellido=apellido
    @property
    def edad(self):
        return self._edad

    @edad.setter #decoradores
    def  edad(self,edad):
        self._edad=edad
    def mostraDetalle(self):
        print(f'Persona:{self.nombre} {self.apellido} {self.edad} {self.args} {self.kwargs}')
        pass
    def __del__(self):
        print(f'Persona Eliminada:{self.nombre} {self.apellido} {self.edad} {self.args} {self.kwargs}')
        pass

    pass
if __name__=='__main__':
    persona1= Persona('Alex','lopez',19,1,2,34,1,'2321',pito='tilin')
    persona2= Persona('Camila','lopez',24)
    persona2.nombre='cc'
    print(persona2.nombre)
    print(__name__)