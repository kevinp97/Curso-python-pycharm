from utils.conexiones import get_mysql_conection

try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM productos WHERE id IN %s' #todos los productos con id que se encuentren en una lista
            # llaves_primarias = ((1,2,3),)
            entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
            #para acceder al nombre por ejemplo
            # for registro in registros:
            #     print(registro[1])


except Exception as e:
    print(f'Ocurrió un error: {e}')
