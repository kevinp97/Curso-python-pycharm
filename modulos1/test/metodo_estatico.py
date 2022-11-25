'''
El metodo estatico se usa para poder acceder a la parte de la memoria dinamica y poder cambiar variables sin necesidad
de crear una funcion y crear un objeto para poder cambiarla
'''

class Prueba:
    variable1 = 'hola'

    def __init__(self):
        self.variable2 = 'hola2'

    def metodo1(self): #creando un objeto
        self.variable2 = 'hola2_mod'
        variable1 = 'hola2'

    @staticmethod
    def metodo_estatico(): #sin crear objeto, y todos los objetos que hereden de esta clase ya variable1 coge el siguiente valor-
        Prueba.variable1 = 'hola_estatico'

print(Prueba.variable1)
Prueba.metodo_estatico()
print(Prueba.variable1)