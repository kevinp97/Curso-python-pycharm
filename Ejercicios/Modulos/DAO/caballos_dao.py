from basededatos.utils.conexiones import get_mysql_conection
from Ejercicios.Modulos.Obj_tabla.caballos import Caballos
import logging as log

log.basicConfig(level=log.INFO,
                format='[%(asctime)s: %(filename)s:%(lineno)s] %(levelname)s:%(message)s',
                datefmt= '%I:%M:%S %p')

class Caballos_DAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM caballos WHERE id_GP=%s' #declarado con constante privada
    _INSERTAR = 'INSERT INTO caballos(nombre, fecha_nacimiento, velocidad, experiencia, valor_apuesta, id_GP) VALUES(%s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE caballos SET nombre=%s, fecha_nacimiento=%s, velocidad=%s, experiencia=%s, valor_apuesta=%s, id_GP=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM caballos WHERE id=%s'

    @classmethod #Metodo de clase: es igual que el metodo estatico, pero vamos a poder acceder a traves de objetos. Podemos acceder a todas las variables de clase
    def seleccionar(cls, gp):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR,[gp])
                registros = cursor.fetchall()
                caballos = []
                for registro in registros:
                    caballo = Caballos(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
                    caballos.append(caballo)

                return caballos

    @classmethod
    def insertar(cls, caballo):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (caballo.nombre, caballo.fecha_nacimiento, caballo.velocidad, caballo.experiencia, caballo.valor_apuesta, caballo.id_GP)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'productos insertada: {caballo}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def actualizar(cls, caballo):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (caballo.nombre, caballo.fecha_nacimiento, caballo.velocidad, caballo.experiencia, caballo.valor_apuesta, caballo.id_GP, caballo.id)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'productos actualizada: {caballo}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def eliminar(cls, caballo):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, caballo.id)
                log.debug(f'Objeto eliminado: {caballo}')
                conexion.commit()
                return cursor.rowcount