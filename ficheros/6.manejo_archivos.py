class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):#Heredado de la clase object
        print('Obtenemos el recurso'.center(50,'-')) #center es para reservar 50 caracteres y los completa con guiones
        self.nombre = open(self.nombre, 'r', encoding='utf-8') #abre fichero que estamos manejando
        return self.nombre #devuelve el nombre porque este metodo tiene que devolver

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print('Cerramos el recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close()

if __name__ == '__main__':
    with ManejoArchivos('prueba.txt') as archivo:
        print(archivo.read())