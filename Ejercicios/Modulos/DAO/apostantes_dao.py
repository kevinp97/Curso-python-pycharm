from basededatos.utils.conexiones import get_mysql_conection
from Ejercicios.Modulos.Obj_tabla.apostantes import Apostantes
import logging as log

log.basicConfig(level=log.INFO,
                format='[%(asctime)s: %(filename)s:%(lineno)s] %(levelname)s:%(message)s',
                datefmt= '%I:%M:%S %p')

class Apostantes_DAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM apostantes ORDER BY id' #declarado con constante privada
    _INSERTAR = 'INSERT INTO apostantes(nombre, saldo) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE apostantes SET nombre=%s, saldo=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM apostantes WHERE id=%s'

    @classmethod #Metodo de clase: es igual que el metodo estatico, pero vamos a poder acceder a traves de objetos. Podemos acceder a todas las variables de clase
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                apostantes = []
                for registro in registros:
                    apostante = Apostantes(registro[0], registro[1], registro[2])
                    apostantes.append(apostante)

                return apostantes

    @classmethod
    def insertar(cls, apostante):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (apostante.nombre, apostante.saldo)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'productos insertada: {apostante}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def actualizar(cls, apostante):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (apostante.nombre, apostante.saldo, apostante.id)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'productos actualizada: {apostante}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def eliminar(cls, apostante):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, apostante.id)
                log.debug(f'Objeto eliminado: {apostante}')
                conexion.commit()
                return cursor.rowcount