from const import*
from log_config import log
import sys
from psycopg2 import pool
class Conexion2:
    _DATABASE= DB_DATABASE
    _USER= DB_USER
    _PASSWORD= DB_PASSWORD
    _PORT= DB_PORT
    _HOST= DB_HOST
    _MIN_CON=1
    _MAX_CON=5
    _pool=None
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool =pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,host=cls._HOST,port=cls._PORT,user=cls._USER,password=cls._PASSWORD,database=cls._DATABASE)
                log.debug(f'Creación del pool exitosa {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool :{e}')
                sys.exit()
        else:
            return cls._pool
        
    @classmethod
    def obtenerConexion(cls):
        conexion= cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del Pool:{conexion} \n')
        return conexion
    @classmethod
    def liberatorConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al Pool: {conexion} \n')
        pass
    
    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
    pass
    
    
if __name__ == '__main__':
    pass