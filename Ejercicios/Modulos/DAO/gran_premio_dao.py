from basededatos.utils.conexiones import get_mysql_conection
from Ejercicios.Modulos.Obj_tabla.gran_premio import Gran_premio
import logging as log


log.basicConfig(level=log.DEBUG,
                format='[%(asctime)s: %(filename)s:%(lineno)s] %(levelname)s:%(message)s',
                datefmt= '%I:%M:%S %p')

class Gran_premio_DAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM gran_premio ORDER BY id' #declarado con constante privada
    _INSERTAR = 'INSERT INTO gran_premio(nombre, distancia, num_carreras) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE gran_premio SET nombre=%s, distancia=%s, num_carreras=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM gran_premio WHERE id=%s'

    @classmethod #Metodo de clase: es igual que el metodo estatico, pero vamos a poder acceder a traves de objetos. Podemos acceder a todas las variables de clase
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                grandes_premios = []
                for registro in registros:
                    gran_premio = Gran_premio(registro[0], registro[1], registro[2], registro[3])
                    grandes_premios.append(gran_premio)

                return grandes_premios

    @classmethod
    def insertar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (gran_premio.nombre, gran_premio.distancia, gran_premio.num_carreras)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'productos insertada: {gran_premio}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def actualizar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (gran_premio.nombre, gran_premio.distancia, gran_premio.num_carreras, gran_premio.id)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'productos actualizada: {gran_premio}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def eliminar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, gran_premio.id)
                log.debug(f'Objeto eliminado: {gran_premio}')
                conexion.commit()
                return cursor.rowcount