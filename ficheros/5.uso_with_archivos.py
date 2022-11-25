#De manera automática abre y cierra el archivo no hace falta try catch
with open('prueba.txt','r', encoding='utf8') as archivo: #mucho mas comodo que usando try y catch
    print(archivo.read())
    #Ejecuta __enter__ y __exit__
