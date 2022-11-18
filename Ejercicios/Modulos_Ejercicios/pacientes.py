from Ejercicios.Modulos_Ejercicios.identificacion import Identificacion


class Paciente(Identificacion):
    '''
    Clase paciente que hereda nombre, apellido y dni de la clase Identificacion. Esta clase lo que hace es crear objetos
    de tipo paciente en la que, a parte de los atributos de identifiaccion, se le añade uno o varios sintomas
    '''
    def __init__(self, sintoma, nombre, apellido, dni):
        Identificacion.__init__(self, nombre, apellido, dni)
        self.sintoma = sintoma

    def __str__(self):
        return f'Nombre:{self.nombre}  Apellido:{self.apellido}  DNI:{self.dni}  Sintoma:{self.sintoma}'


class Enfermo(Identificacion):
    '''
        Clase paciente que hereda nombre, apellido y dni de la clase Identificacion. Esta clase lo que hace es crear objetos
        de tipo enfermo en la que, a parte de los atributos de identifiaccion, se le añade una enfermedad
        '''
    def __init__(self, enfermedad, nombre, apellido, dni):
        Identificacion.__init__(self, nombre, apellido, dni)
        self.enfermedad = enfermedad

    def __str__(self):
        return f'Nombre:{self.nombre}  Apellido:{self.apellido}  DNI:{self.dni}  Enfermedad:{self.sintoma}'