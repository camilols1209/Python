from Usuario import Usuario
from Log import log
from CursorPool import CursorPool
class UsuarioDao:
    _SELECIONAR="SELECT * FROM usuario ORDER BY id_usuario"
    _INSERTAR="INSERT INTO usuario(username, password) VALUES (%s, %s)"
    _ACTUALIZAR="UPDATE usuario SET username=%s, password=%s, WHERE id_usuario=%s"
    _ELIMINAR="DELETE FROM usuario WHERE id_usuario=%s"
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECIONAR)
            registros=cursor.fetchall()
            usuarios=list()

            for reg in registros:
                usuario=Usuario(reg.id_usuario,reg.username,reg.password)
                usuarios.append(usuario)
            return usuarios
    @classmethod
    def insertar(cls,usuario):
        with CursorPool() as cursor:
            data=(usuario.username,usuario.password)
            cursor.execute(cls._INSERTAR,data)
            log.debug(f'Usuario insertado: {usuario}\n')
            return cursor.rowcount
    @classmethod
    def actualizar(cls,usuario):
        with CursorPool() as cursor:
            data=(usuario.username,usuario.password,usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR,data)
            log.debug(f'Usuario Actualizado: {usuario}\n')
            return cursor.rowcount
    @classmethod
    def eliminar(cls,usuario):
        with CursorPool() as cursor:
            data=(usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR,data)
            log.debug(f'Usuario Eliminado : {usuario}\n')
            return cursor.rowcount
    pass