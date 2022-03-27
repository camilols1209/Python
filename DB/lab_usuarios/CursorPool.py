from Log import log
from Conexion import Conexion
class CursorPool:
    def __init__(self):
        self._conn=None
        self._cursor=None
        pass
    def __enter__(self):
        log.debug(f'Inicio del metodo whit __enter__ \n')
        self._conn= Conexion.obtenerConexion()
        self._cursor= self._conn.cursor()
        return self._cursor
    def __exit__(self, exc_type, exc_value, trace):
        log.debug(f'Se Ejecuta el metodo __exit__')
        if exc_type:
            self._conn.rollback()
            log.error(f'Ocurrio un error se hace rollback: {exc_value} {exc_type} {trace}')
        else:
            self._conn.commit()
            log.debug(f'Commit de la transacción')
        self._cursor.close()
        Conexion.liberatorConexion(self._conn)
        pass
    pass

if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug(f'Dentro del with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())