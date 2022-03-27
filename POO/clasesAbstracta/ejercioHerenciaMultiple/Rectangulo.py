from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica,Color):
    def __init__(self, alto,ancho,color) -> None:
        FiguraGeometrica.__init__(self,alto, ancho)
        Color.__init__(self,color)
        pass
    def area(self):
        return self.alto* self.ancho
        
    def __str__(self) -> str:
        return f'Rectangulo:[ Base: {self.ancho}, Altura: {self.alto} ] {super().__str__()} Color: {self.color}'
    pass