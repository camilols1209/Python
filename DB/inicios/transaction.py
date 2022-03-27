import psycopg2
from const import *

# connection with postgres
connection=psycopg2.connect(host=DB_HOST,user=DB_USER,password=DB_PASSWORD,port=DB_PORT,database=DB_DATABASE)

try:
    connection.autocommit = False

    cursor= connection.cursor()

    query= 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=1'
    values=('Maria_2','Esparza_2','mesperanza@mail.com_2')
    cursor.execute(query,values)

    query= 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    values=('Martha','Esparza','maesperanza@mail.com')
    cursor.execute(query,values)
    connection.commit()
    print('Termina la transacción')
except Exception as e:
    connection.rollback()
    print(f'Ocurrio un ERROR{e}')
finally:
    connection.close()
