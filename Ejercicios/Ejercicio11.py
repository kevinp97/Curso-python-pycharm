'''
Con la informacion del fichero se tiene que hacer lo siguiente:
    - Generar objetos necesarios para generar
    - Leer ficheros
    - Guardar en objetos
    - Generar archivos con los datos de los alumnos de cada colegio
Recgoer info y guardarla en objetos y una vez metida, nos aseguramos que es lo mismo y generar archivos con el nombre
del colegio con los datos de los alumnos de cada colegio.
El fichero de escritura tiene que estar generado como el de entrada, separado con | y asignaturas con ;
'''

from abc import ABC, abstractmethod
import random
import logging as log

log.basicConfig(level=log.DEBUG,
                format='[%(asctime)s: %(filename)s:%(lineno)s] %(levelname)s:%(message)s',
                datefmt= '%I:%M:%S %p',
                handlers=[log.FileHandler('../logs/ejercicio11.log'),
                          log.StreamHandler()])




COLEGIO = 0
NOMBRE_ALUMNO = 1
APELLIDOS_ALUMNO = 2
DNI_ALUMNO = 3
ASIGNATURAS_ALUMNO = 4
SEPARADOR = "|"

class Alumno():
    '''
    Se le pasa al constructor el fichero y el nombre del colegio para poder separar y crear un archivo para cada colegio
    con los alumnos correspondientes
        - Extraer alumnos: Recorre las lineas del fichero y guarda todas las lineas que compartan el nombre con el
                            colegio que se le pasa al constructor
        -Guardar alumno: Coge todas esas lineas, se hace un slice hasta el primer pipe y se guarda el restante de la linea
                        en un nuevo archivo que tiene el nombre del colegio, se usar append para no sobreescribir
    '''

    class Alumno:
        def __init__(self, nombre, apellidos, dni, asignaturas):
            self._nombre = nombre
            self._apellidos = apellidos
            self._dni = dni
            self._asignaturas = asignaturas

        @property
        def nombre(self):
            return self._nombre

        @nombre.setter
        def nombre(self, nombre):
            self._nombre = nombre

        @property
        def apellidos(self):
            return self._apellidos

        @apellidos.setter
        def apellidos(self, apellidos):
            self._apellidos = apellidos

        @property
        def dni(self):
            return self._dni

        @dni.setter
        def dni(self, dni):
            self._dni = dni

        @property
        def asignaturas(self):
            return self._asignaturas

        @asignaturas.setter
        def asignaturas(self, asignaturas):
            self._asignaturas = asignaturas

        def addAsignatura(self, asignatura):
            self.asignaturas.append(asignatura)

        def __str__(self):
            return f"{self.nombre}|{self.apellidos}|{self.dni}|" + ";".join(self.asignaturas)

if __name__ == '__main__':
    colegios = {}
    with open('alumnos-colegio.txt', 'r', encoding='utf8') as archivo:
        #datos = archivo.readlines()
        for linea in archivo:
            # print(linea)
            log.debug(linea)
            datos = linea.split(SEPARADOR)
            log.debug(datos)
            nombre_colegio = datos[COLEGIO]
            alumno = Alumno(datos[NOMBRE_ALUMNO], datos[APELLIDOS_ALUMNO], datos[DNI_ALUMNO],
                            datos[ASIGNATURAS_ALUMNO].split(';'))
            log.debug("Asignaturas:", alumno.asignaturas)
            if not nombre_colegio in colegios:
                colegios[nombre_colegio] = [alumno]
            else:
                colegios[nombre_colegio].append(alumno)
            # colegios[colegio.nombre] += [alumno]
            # colegios.update(colegios)
            # colegios[colegio.nombre].append(alumno)

        for colegio, alumnos in colegios.items():
            log.debug(colegio)
            archivo_escritura = open(f'{colegio}.txt', "w", encoding="UTF-8")
            for alumno in alumnos:
                log.debug(alumno.asignaturas)
                archivo_escritura.write(str(alumno))






