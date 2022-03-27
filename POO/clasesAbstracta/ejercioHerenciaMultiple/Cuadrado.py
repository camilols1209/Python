from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self, lado,color) -> None:
        FiguraGeometrica.__init__(self,lado, lado)
        Color.__init__(self,color)
        pass
    def area(self):
        return self.alto* self.ancho

    def __str__(self) -> str:
        return f'Cuadrado:[ Lado: {self.alto} ] {super().__str__()} Color: {self.color}'
    pass