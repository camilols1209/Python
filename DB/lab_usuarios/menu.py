
from Log import log
from UsuarioDao import UsuarioDao
from Usuario import Usuario
while True:
    print(
'''Opciones: 
1. Listar Usuarios
2. Agregar Usuarios
3. Actualizar Usuarios
4. Eliminar Usuarios
5. Salir''')
    opcion= int(input('Escribe tu opcion (1-5):'))
    if opcion ==1:
        usuarios= UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion ==2:
        usernameVar= input('Escribe el Username')
        passwordVar= input('Escribe la Password')
        usuario=Usuario(username=usernameVar,password=passwordVar)
        usuarios_insertados=UsuarioDao.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion==3:
        id= input('Escribe el ID del usuario a modificar: ')


    else:
        log.info('Salimos de la Aplicación')
        break
    pass