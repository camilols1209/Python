# ABC= Abstract Base Class
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto) -> None:
        if self._validar_valor(ancho):
            self.__ancho=ancho
        else:
            self.__ancho=0

        if self._validar_valor(alto):
            self.__alto=alto
        else:
            self.__alto=0
        pass

    @property
    def alto(self):
        return self.__alto
    
    @property
    def ancho(self):
        return self.__ancho


    @alto.setter #decoradores
    def  alto(self,alto):
        if self._validar_valor(alto):
            self.__alto=alto
        else:
            print(f'El valor ingresado {alto} es Erroneo')
    @ancho.setter #decoradores
    def  ancho(self,ancho):
        if self._validar_valor(ancho):
            self.__ancho=ancho
        else:
            print(f'El valor ingresado {ancho} es Erroneo')
        pass

    @abstractmethod
    def area(self):
        pass
    def _validar_valor(self,valor):
        return True if 0 <valor <10 else False

    def __str__(self) -> str:
        return f' FiguraGeometrica: [ ALto:{self.__alto}, Ancho:{self.__ancho} ]'
        
    pass