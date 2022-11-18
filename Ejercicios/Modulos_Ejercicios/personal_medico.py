from Ejercicios.Modulos_Ejercicios.identificacion import Identificacion
import random
import datetime
from Ejercicios.Modulos_Ejercicios.cola import Cola


class Doctor(Identificacion):
    '''
    Clase Doctor que hereda nombre, apellido y dni de la clase Identificacion. Esta clase lo que hace es crear objetos
    de tipo doctor en la que, a parte de los atributos de identifiaccion se le añade una especialidad.
    A parte tiene ciertas funciones como:
        -Atender paciente: Segun por el orden de la sala de espera va atendiendo pacientes
        -Diagnostico: Va diagnosticando ese paciente y decide si ingresarlo o no
        -ingresar paciente: Una vez decidido que se tiene que ingresar, se transforma el paciente en enfermo y lo ingresa
                            en una habitacion, esta tiene tamaño 3, si estan ocupadas, manda al paciente a otro hospital.
        -Fichar entrada/salida: Para fichar que han entrado/salido del hospital.
    '''

    def __init__(self, especialidad, nombre, apellido, dni):
        Identificacion.__init__(self, nombre, apellido, dni)
        self.especialidad = especialidad

    def atender_paciente(self, sala_espera):
        self.sala_espera = sala_espera
        print(f'---- El paciente {self.sala_espera.items[0].nombre} llega a la consulta del doctor {self.nombre}')
        print(f'---- El doctor {self.nombre} está atendiendo a {self.sala_espera.items[0].nombre}')

    def diagnostico(self, sala_espera):
        self.sala_espera = sala_espera
        self.diagnostico_doctor = random.randint(1, 10)
        print(f'---- El doctor {self.nombre} ha diagnosticado a {sala_espera.items[0].nombre}')
        if self.diagnostico_doctor >= 7:
            print(f'---- El {sala_espera.items[0].nombre} está enfermo, hay que ingresarlo')

        else:
            print(f'---- El {sala_espera.items[0].nombre} puede volver a casa')
            print(f'---- El doctor {self.nombre} espera en consulta a su siguiente paciente...')

    def ingresar_paciente(self, sala_espera, enfermo, habitaciones):
        self.sala_espera = sala_espera
        self.enfermo = enfermo
        self.habitaciones = habitaciones
        self.habitaciones.encolar(self.enfermo.nombre)
        if len(self.habitaciones.items) > 3:
            print(f'---- No se pueden ingresar más enfermos, el enfermo {self.sala_espera.items[0].nombre} tiene que acudir a otro hospital con la enfermedad {self.enfermo.enfermedad}')
        else:
            print(f'---- El {self.sala_espera.items[0].nombre} ha sido ingresado por el doctor {self.nombre} por la enfermedad de {self.enfermo.enfermedad}')
            print(f'---- El doctor {self.nombre} espera en consulta a su siguiente paciente...')

    def fichar_entrada(self):
        print(f'El doctor {self.nombre} {self.apellido} con dni {self.dni} ha fichado su entrada con fecha {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year} a las {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}')

    def fichar_salida(self):
        print(f'El doctor {self.nombre} {self.apellido} con dni {self.dni} ha fichado su salida con fecha {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year} a las {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}')

    def __str__(self):
        return f'Nombre:{self.nombre}  Apellido:{self.apellido}  DNI:{self.dni}  Especialidad:{self.especialidad}'


class Enfermero(Identificacion):
    '''
        Clase Enfermero que hereda nombre, apellido y dni de la clase Identificacion. Esta clase lo que hace es crear objetos
        de tipo enfermero en la que, a parte de los atributos de identifiaccion se le añade la planta donde trabaja.
        A parte tiene ciertas funciones como:
            -Atender paciente: Segun por el orden de la sala de espera va atendiendo pacientes y lo deriva a un doctor

            -Fichar entrada/salida: Para fichar que han entrado/salido del hospital.
    '''

    def __init__(self, planta, nombre, apellido, dni):
        Identificacion.__init__(self, nombre, apellido, dni)
        self.planta = planta

    def fichar_entrada(self):
        print(f'El enfermero {self.nombre} {self.apellido} con dni {self.dni} ha fichado su entrada con fecha {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year} a las {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}')

    def fichar_salida(self):
        print(f'El enfermero {self.nombre} {self.apellido} con dni {self.dni} ha fichado su salida con fecha {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year} a las {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}')

    def atender_paciente(self, sala_espera, doctores):
        self.sala_espera = sala_espera
        self.doctores = doctores
        print(f'- El paciente {self.sala_espera.items[0].nombre} llega a la planta {self.planta} donde le espera el enfermero')
        print(f'- El enfermero {self.nombre} atiende a {self.sala_espera.items[0].nombre} que viene con los siguientes sintomas: {self.sala_espera.items[0].sintoma} y lo deriva con el doctor {self.doctores.nombre}')
        print(f'- El enfermero {self.nombre} espera a su siguiente paciente...')

    def __str__(self):
        return f'Nombre:{self.nombre}  Apellido:{self.apellido}  DNI:{self.dni}  Planta asignada:{self.planta}'
