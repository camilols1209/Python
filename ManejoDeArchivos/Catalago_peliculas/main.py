from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas
opcion=None
text="""
Opciones:
1. Agregar Pelicula.
2. Listar Peliculas.
3. Eliminar archivo.
4. salir

Escribe tu Opción (1-4) : """

while opcion!=4:
    try:
        opcion= int(input(text))
        if opcion==1:
            nombre_pelicula=input('Proporciona el nombre de la pelicula: ')
            pelicula=Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_pelicula(pelicula)
        elif opcion==2:
            CatalogoPeliculas.listar_peliculas()
        elif opcion==3:
            CatalogoPeliculas.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrió un error {e}')
        opcion=None
   
else:
    print('Salimos del programa')
    pass