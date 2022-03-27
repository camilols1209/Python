from Conexion import Conexion
from Persona import Persona
from log_config import log
from CursorPool import CursorPool
class PersonaDao:
    '''
    DAO (Data Access Object)
    CRUD (Create Read Update Delete)
    '''
    _SELECIONAR="SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR="INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
    _ACTUALIZAR="UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
    _ELIMINAR="DELETE FROM persona WHERE id_persona=%s"
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECIONAR)
            registros=cursor.fetchall()
            personas=list()
            for registro in registros:
                persona=Persona(registro[0],registro[1],registro[2])
                personas.append(persona)
            pass
            return personas
    @classmethod
    def insertar(cls,persona):
        
        with CursorPool() as cursor:
            
            valores=(persona.nombre,persona.apellido,persona.email)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Persona a insertada: {persona}\n')
            return cursor.rowcount

    @classmethod
    def actualizar(cls,persona):
         with CursorPool() as cursor:
                valores=(persona.nombre,persona.apellido,persona.email,persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug(f'Persona actualizada: {persona}\n')
                return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
        with CursorPool() as cursor:
            
            valores=(persona.id_persona,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug(f'Persona eliminada: {persona}\n')
            return cursor.rowcount
        
    pass
if __name__=='__main__':
    
    #actualizar personas
    """  persona = Persona(nombre='Camila',apellido='Lopez',email='jlopez@mail.com',id_persona=8)
    actualizar_personas = PersonaDao.actualizar(persona)
    log.debug(f'Personas Actulizadas: {actualizar_personas}')

    #eliminar personas 
    personas_eliminadas=PersonaDao.eliminar(persona)
    log.debug(f'Personas Eliminadas: {personas_eliminadas}') """
    #crear personas
    #persona = Persona(nombre='Jesus',apellido='Lopez',email='jlopez@mail.com')
    #persona_insertada=PersonaDao.insertar(persona)
    #log.debug(f'personas Insertadas:{persona_insertada}')
    #seleccionar personas
    personas=PersonaDao().seleccionar()
    for persona in personas:
        log.debug(f'{persona}\n')