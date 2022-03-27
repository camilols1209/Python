def mi_funcion(nombre, apellido):
    #mi función
    print('saludos desde mi función')
    print(f'Nombre: {nombre}, Apellido: {apellido}')

#mi_funcion('Juan','Perez')

def sumar(a:int=0,b:int =0)->int:
    print(f' valor de A = {a}  \n  valor de B = {b}')
    return a+b

#print(sumar(2))

def listarNombre(*nombres): #parametros de n elementos
    for nombre in nombres:
        print (nombre)

#listarNombre('Juan','Karla','Maria')

#keywords arguments =kwargs

def listaTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}:{valor}')

listaTerminos(alex='bobo',camila='mongola')