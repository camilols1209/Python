from time import sleep


class Producto:
    contador_productos=0
    def __init__(self,nombre,precio) -> None:
        Producto.contador_productos+=1
        self._id_producto=Producto.contador_productos
        self._nombre=nombre
        self._precio=precio
        pass
    @property
    def precio(self):
        return self._precio

    def __str__(self) -> str:
        return f'Id Producto: {self._id_producto}, Nommbre: {self._nombre}, Precio: {self._precio}'
    pass