from Producto import Producto


class Orden:
    contador_ordenes=0
    def __init__(self,productos) -> None:
        Orden.contador_ordenes+=1
        self._id_orden= Orden.contador_ordenes
        self._productos=list(productos)

        pass
    def agregar_producto(self,producto):
        self._productos.append(producto)
        pass
    def calcular_total(self):
        total=0
        for producto in self._productos:
            total+= producto.precio
        return total
    def __str__(self) -> str:
        producto_str=''
        for producto in self._productos:
            producto_str+= '\n'+producto.__str__()
            pass
        return f'Orden:{self._id_orden}\nProductos: {producto_str}'
    pass
if __name__=='__main__':
    producto1=Producto('Mesa',1000)
    producto2=Producto('Silla',250)
    productos=[producto1,producto2]
    orden=Orden(productos)
    print(orden)