try:
    archivo = open('prueba.txt', 'w', encoding='UTF-8')
    archivo.write('Agregamos información al archivo probando probando\n')
    archivo.write('Adiós, bye\n')
except Exception as e:
    print(e)
finally:
    archivo.close() #HAY QUE CERRAR SIEMPRE EL ARCHIVO