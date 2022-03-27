try:
    
    archivo = open('prueba.txt','w',encoding='utf-8')
    archivo.write('Agregar información\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
