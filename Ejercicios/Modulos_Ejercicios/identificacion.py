class Identificacion():
    ''' Este objeto es el padre del resto del hospital y lo que hace es crear un objeto con los datos de nombre
    apellido y dni de las personas'''
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
