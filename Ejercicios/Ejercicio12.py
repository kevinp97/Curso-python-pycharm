'''
Crear tabla persona con el campo: nombre, apellido, email
con campo id que era la primary key
-Insertar 3 personas con valores que se introduciran manualmente
-Hacer consultas:
    -Obtener solo los nombres de las personas de todas las que hay
    -Sacar toda la informacion de las personas que tengan un email terminado en gmail.com
    -Actualizar a las personas que no tengan un email de gmail: Ejemplo: blablabla@correo.es -> blablabla@gmail.com
'''

from basededatos.utils.conexiones import get_mysql_conection
from datetime import datetime
import logging as log

log.basicConfig(level=log.INFO,
                format='[%(asctime)s: %(filename)s:%(lineno)s] %(levelname)s:%(message)s',
                datefmt= '%I:%M:%S %p',
                handlers=[log.FileHandler('../logs/ejercicio10.log'),
                          log.StreamHandler()])
try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            #AÑADIR 3 PERSONAS A LA TABLA
            # sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)' #El ID es autoincremental, por lo que no hace falta pasarlo
            # valores = (
            #     ('Nombre1', 'Apellido1', 'NombreApellido1@mail.com'),
            #     ('Nombre2', 'Apellido2', 'NombreApellido2@gmail.com'),
            #     ('Nombre3', 'Apellido3', 'NombreApellido3@org.es')
            # )
            # cursor.executemany(sentencia, valores) #esta funcion es para ejecutar varias sentencias
            # registros_insertados = cursor.rowcount
            # print(f'Registros Insertados: {registros_insertados}')


            # #CONSULTA 1
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for registro in registros:
                log.info(registro[1])

            #CONSULTA 2
            # lista_id = []
            sentencia = 'SELECT * FROM persona WHERE email LIKE %s'
            new_value = "%gmail.com"
            cursor.execute(sentencia,[new_value])
            registros = cursor.fetchall()
            log.info(registros)



            # # #CONSULTA 3
            new_value = '%gmail.com'
            to_change = '@gmail.com'
            sentencia = "UPDATE `persona` " \
                            "SET `email` = CONCAT(left(`persona`.`email`, locate('@', `persona`.`email`) - 1), %s) " \
                            "WHERE `persona`.`email` NOT LIKE %s"
            cursor.execute(sentencia, (to_change, new_value))
            conexion.commit()
            registros_actualizados = cursor.rowcount
            conexion.commit() #para que se efectue el insertar
except Exception as e:
    print(f'Ocurrió un error: {e}')