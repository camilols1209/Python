import re


class FiguraGeometrica:
    def __init__(self,ancho,alto) -> None:
        self.__ancho=ancho
        self.__alto=alto
        pass

    @property
    def alto(self):
        return self.__alto
    
    @property
    def ancho(self):
        return self.__ancho


    @alto.setter #decoradores
    def  alto(self,alto):
        self.__alto=alto

    @ancho.setter #decoradores
    def  ancho(self,ancho):
        self.__ancho=ancho

    def __str__(self) -> str:
        return f' FiguraGeometrica: [ ALto:{self.__alto}, Ancho:{self.__ancho} ]'
        
    pass