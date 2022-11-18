from Ejercicios.Modulos_Ejercicios.identificacion import Identificacion
import random
from Ejercicios.Modulos_Ejercicios.cola import Cola
from Ejercicios.Modulos_Ejercicios.personal_medico import Doctor, Enfermero
from Ejercicios.Modulos_Ejercicios.pacientes import Paciente,Enfermo
import datetime
import time

def inicializacion_datos():
    '''
        Inicializacion de los datos
    '''
    # Datos pacientes
    nombres_pacientes = Cola()

    # Cola pacientes
    sala_espera = Cola()

    # Habitaciones
    habitaciones = Cola()

    # Doctores
    doctor_1 = Doctor('Pediatria', 'Doctor1_nombre', 'Doctor1_apellido', 'Doctor1_dni')
    doctor_2 = Doctor('Cardiologia', 'Doctor2_nombre', 'Doctor2_apellido', 'Doctor2_dni')

    # Enfermeros
    enfermero_1 = Enfermero('Primera', 'Enfermero1_nombre', 'Enfermero2_apellido', 'Enfermero1_dni')
    enfermero_2 = Enfermero('Tercera', 'Enfermero2_nombre', 'Enfermero2_apellido', 'Enfermero2_dni')

    # Pacientes
    lista_enfermedades = ['Tos constante', 'Amigdalitis', 'Pierna rota', 'Dolor de cabeza', 'Alergia', 'Asma',
                          'Bronquitis', 'Colico nefritico', 'Conjuntivitis', 'Faringitis']
    lista_sintomas = ['Mocos', 'Tos', 'Dolor de barriga', 'Fiebre', 'Pereza', 'Dolor de cabeza', 'Dolor musular',
                      'Problema respiratorio', 'Vision borrosa']
    paciente_1 = Paciente(random.choices(lista_sintomas, k=random.randint(1, 3)), 'Paciente1_nombre',
                          'Paciente1_apellido', 'Paciente1_dni')
    paciente_2 = Paciente(random.choices(lista_sintomas, k=random.randint(1, 3)), 'Paciente2_nombre',
                          'Paciente2_apellido', 'Paciente2_dni')
    paciente_3 = Paciente(random.choices(lista_sintomas, k=random.randint(1, 3)), 'Paciente3_nombre',
                          'Paciente3_apellido', 'Paciente3_dni')
    paciente_4 = Paciente(random.choices(lista_sintomas, k=random.randint(1, 3)), 'Paciente4_nombre',
                          'Paciente4_apellido', 'Paciente4_dni')

    doctores = [doctor_1, doctor_2]
    enfermeros = [enfermero_1, enfermero_2]
    pacientes = [paciente_1, paciente_2, paciente_3, paciente_4]

    return doctores, enfermeros, pacientes, sala_espera, nombres_pacientes, habitaciones, lista_enfermedades


if __name__ == '__main__':

    doctores, enfermeros, pacientes, sala_espera, nombres_pacientes, habitaciones, lista_enfermedades = inicializacion_datos()
    ''' Transcurso de las acciones'''
    print(f'***************************** \n ***************************** '
          f'\nFecha {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year} '
          f'a las {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}'
          f'\n ***************************** \n *****************************\n')

    time.sleep(2)
    # Entran los doctores y enfermeros a trabajar
    for doctor in doctores:
        doctor.fichar_entrada()
    print('\n')
    time.sleep(1)
    for enfermero in enfermeros:
        enfermero.fichar_entrada()
    print('\n')

    # Van llegando los pacientes y se van poniendo a la cola
    for paciente in pacientes:
        sala_espera.encolar(paciente)
        nombres_pacientes.encolar(paciente.nombre)# guardamos los nombres de los pacientes para mostrar una lista simulando la cola
        print(f'El paciente {paciente.nombre} se va poniendo a la cola')
        time.sleep(1)

    print(f'La sala de espera está compuesta por: {nombres_pacientes.items} \n')

    # Los enfermeros van atendiento a los pacientes por orden
    while sala_espera.es_vacia() == False:

        for personal in range(0, len(enfermeros)):
            enfermeros[personal].atender_paciente(sala_espera,doctores[personal])
            doctores[personal].atender_paciente(sala_espera)
            doctores[personal].diagnostico(sala_espera)
            if doctores[personal].diagnostico_doctor >= 7:
                enfermo = Enfermo(random.choice(lista_enfermedades), sala_espera.items[0].nombre,
                                  sala_espera.items[0].apellido, sala_espera.items[0].dni)
                doctores[personal].ingresar_paciente(sala_espera,enfermo,habitaciones)
            sala_espera.desencolar()  # desencolamos la sala de espera, eliminando el elemento [0]
            print('\n')
            time.sleep(2)

        print('\n')

    # Salen de trabajar los doctores y enfermeros
    for doctor in doctores:
        doctor.fichar_salida()
    print('\n')
    time.sleep(1)
    for enfermero in enfermeros:
        enfermero.fichar_salida()
    print('\n')