from utils.conexiones import get_mysql_conection

try:
    conexion = get_mysql_conection() #para coger la conexion
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM productos'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')