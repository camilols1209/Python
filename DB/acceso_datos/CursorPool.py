from log_config import log
from Conexion2 import Conexion2
class CursorPool:
    def __init__(self):
        self._conexion=None
        self._cursor=None
        pass
    def __enter__(self):
        log.debug(f'Inicio del metodo whit __enter__ \n')
        self._conexion= Conexion2.obtenerConexion()
        self._cursor= self._conexion.cursor()
        return self._cursor
    def __exit__(self, exc_type, exc_value, trace):
        log.debug(f'Se Ejecuta el metodo __exit__')
        if exc_type:
            self._conexion.rollback()
            log.error(f'Ocurrio un error se hace rollback: {exc_value} {exc_type} {trace}')
        else:
            self._conexion.commit()
            log.debug(f'Commit de la transacción')
        self._cursor.close()
        Conexion2.liberatorConexion(self._conexion)
        pass
    pass

if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug(f'Dentro del with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())