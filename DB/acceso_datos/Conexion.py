from const import*
from log_config import log
import sys
import psycopg2 
class Conexion:
    _DATABASE= DB_DATABASE
    _USER= DB_USER
    _PASSWORD= DB_PASSWORD
    _PORT= DB_PORT
    _HOST= DB_HOST
    _conexion=None
    _cursor=None
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion=psycopg2.connect(host=cls._HOST,port=cls._PORT,user=cls._USER,password=cls._PASSWORD,database=cls._DATABASE)
                log.debug(f'Conexion Exitosa {cls._conexion} \n')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio un error al obtener la conexion: {e}\n')
                sys.exit()
        else:
            return cls._conexion
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor =cls.obtenerConexion().cursor()
                log.debug(f"Cursor Creado {cls._cursor} \n")
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el Cursor: {e}\n')
                sys.exit()
        else:
            return cls._cursor
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()