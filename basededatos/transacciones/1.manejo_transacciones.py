from basededatos.utils.conexiones import get_mysql_conection
from datetime import datetime
try:
    conexion = get_mysql_conection()

    cursor = conexion.cursor()
    #conexion.autocommit = True solo funciona si la base de datos tiene activada el autocommit
    '''
    SHOW VARIABLES WHERE Variable_name='autocommit';

    '''
    sentencia = 'INSERT INTO productos(nombre, precio, fecha_registro) VALUES(%s, %s, %s)'
    valores = ('Producto', 12313, datetime.now())
    cursor.execute(sentencia, valores)
    
    sentencia = 'UPDATE productos SET nombre=%s, precio=%s, fecha_registro=%s WHERE id=%s'
    valores = ('Producto1234', 21313,datetime.now(), 2)
    cursor.execute(sentencia, valores)

    conexion.commit() #no se ejecuta el commit hasta que no se ha ejecutado la transaccion de forma correcta
    print('Termina la transacción')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo rollback: {e}')

finally:
    conexion.cursor().close()
    conexion.close()

