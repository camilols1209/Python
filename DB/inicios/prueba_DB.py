import psycopg2
from const import *

# connection with postgres
connection=psycopg2.connect(host=DB_HOST,user=DB_USER,password=DB_PASSWORD,port=DB_PORT,database=DB_DATABASE)

try:
    with connection:
        with connection.cursor() as cursor:
            query='SELECT * FROM persona WHERE id_persona IN %s'
            id=((1,2),)
            cursor.execute(query,id)
            data=cursor.fetchall()
            print(data)
except Exception as e:
    print(f'Ocurrio un ERROR{e}')
finally:
    connection.close()
