import os
class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'
    
    @classmethod
    def agregar_pelicula(cls,pelicula):
        with open(cls.ruta_archivo,'a',encoding='utf-8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
        pass
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo,'r',encoding='utf-8') as archivo:
            print('Catalogo de peliculas'.center(50,'-'))
            print(archivo.read())
        pass
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo Eliminiando: {cls.ruta_archivo}')
        pass
    pass