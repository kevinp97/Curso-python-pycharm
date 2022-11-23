import os
'''
Jerarquia
    Instrumento
        -Nombre
        -Tipo
    Guitarra:
        -Num cuerdas
    Guitarra electrica: hereda de guitarra
        -Potencia
    Piano:
        -Teclas
    Tambor:
        -tamanio

Todos los instrumentos tienen afinar() y tocar()
Decorador log para cuando entre y salga de los metodos siguientes, si lo pongo a nivel de info que se desactive los logs
    -afinar(): Afinar el instrumento de manera aleatoria, se afina bien o mal
    -tocar(): Tocando el instrumento 'nombre' de manera correcta:: si esta afinado
            Si no esta afinado lanzamos una excepcion. TAMBOR TIENE APORREAR

    Clase orquesta:
        -Crear_orquesta(1 guitarra, 1 guitarra_electrica, 1 piano, 1 tambor) --> Metemos todos los instrumentos en una lista
        -Iniciar_concierto() a partir del listado de instrumentos, 1º se afinan todos con su metodo y 2º se ponen a tocar

    Cuando toquemos el tambor, un tambor no se va a tocar, sino que va a tener el metodo de aporrear



'''
from abc import ABC, abstractmethod
import random
import logging as log
from Ejercicios.Excepciones.excepciones_ejer10 import Instrumento_no_afinado_correctamente

log.basicConfig(level=log.INFO,
                format='[%(asctime)s: %(filename)s:%(lineno)s] %(levelname)s:%(message)s',
                datefmt= '%I:%M:%S %p',
                handlers=[log.FileHandler('../logs/ejercicio10.log'),
                          log.StreamHandler()])

def log_orquesta(funcion):

    def mostrar_logs_afinar(*args):
        log.debug(f'Antes de ejecucion  {funcion.__name__}')
        funcion(*args)
        log.debug(f'Después de ejecución {funcion.__name__}\n')
    return mostrar_logs_afinar




class Instrumento(ABC):

    def __init__(self, nombre, tipo):
        self._nombre = nombre #atributos privados
        self._tipo = tipo
        self._afinado = False

    @property    #getter y setter para impedir la modificacion
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def afinado(self):
        return self._afinado

    @afinado.setter
    def afinado(self, afinado):
        self._afinado = afinado


    @abstractmethod
    def afinarInstrumento(self): #click derecho, generate, implement method salen los metodos abstractos para meterlos
        pass

    @abstractmethod
    def tocarInstrumento(self):
        pass

class Guitarra(Instrumento):

    def __init__(self, nombre, tipo, numero_cuerdas):
        Instrumento.__init__(self, nombre, tipo)
        self._numero_cuerdas = numero_cuerdas

    @property
    def numero_cuerdas(self):
        return self._numero_cuerdas

    @numero_cuerdas.setter
    def numero_cuerdas(self, numero_cuerdas):
        self._numero_cuerdas = numero_cuerdas

    @log_orquesta
    def afinarInstrumento(self):
        log.info(f'Se va ha afinar el instrumento: {self.nombre}')
        self.afinado = random.choice([True, False]) #para esto sirve el property y setter
        log.info(f'Se ha afinado el instrumento: {self.nombre}')
        return self.nombre

    def tocarInstrumento(self):
        #log.info(f'Se va a tocar el instrumento: {self.nombre}')
        if self.afinado:
            log.info(f'Se está tocando correctamente el instrumento: {self.nombre}')
        else:
            raise Instrumento_no_afinado_correctamente(f'El instrumento {self.nombre} no está afinado correctamente')

class Guitarra_electrica(Guitarra):

    def __init__(self, nombre, tipo, numero_cuerdas, potencia):
        Guitarra.__init__(self, nombre, tipo, numero_cuerdas)
        self._potencia = potencia

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, potencia):
        self._potencia = potencia

    @log_orquesta
    def afinarInstrumento(self):
        log.info(f'Se va ha afinar el instrumento: {self.nombre}')
        self.afinado = random.choice([True, False])
        log.info(f'Se ha afinado el instrumento: {self.nombre}')
        return self.nombre


    def tocarInstrumento(self):
        #log.debug(f'Se va a tocar el instrumento: {self.nombre}')
        if self.afinado:
            log.info(f'Se está tocando correctamente el instrumento: {self.nombre}')
        else:
            raise Instrumento_no_afinado_correctamente(f'El instrumento {self.nombre} no está afinado correctamente')


class Piano(Instrumento):

    def __init__(self, nombre, tipo, numero_teclas):
        Instrumento.__init__(self, nombre, tipo)
        self._numero_teclas = numero_teclas

    @property
    def numero_teclas(self):
        return self._numero_teclas

    @numero_teclas.setter
    def numero_teclas(self, numero_teclas):
        self._numero_teclas = numero_teclas

    @log_orquesta
    def afinarInstrumento(self):
        log.info(f'Se va ha afinar el instrumento: {self.nombre}')
        self.afinado = random.choice([True, False])
        log.info(f'Se ha afinado el instrumento: {self.nombre}')
        return self.nombre


    def tocarInstrumento(self):
        #log.debug(f'Se va a tocar el instrumento: {self.nombre}')
        if self.afinado:
            log.info(f'Se está tocando correctamente el instrumento: {self.nombre}')
        else:
            raise Instrumento_no_afinado_correctamente(f'El instrumento {self.nombre} no está afinado correctamente')


class Tambor(Instrumento):

    def __init__(self, nombre, tipo, tamanio):
        Instrumento.__init__(self, nombre, tipo)
        self._tamanio = tamanio

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

    @log_orquesta
    def afinarInstrumento(self):
        log.info(f'Se va ha afinar el instrumento: {self.nombre}')
        self.afinado = random.choice([True, False])
        log.info(f'Se ha afinado el instrumento: {self.nombre}\n')
        return self.nombre


    def tocarInstrumento(self):
        #log.debug(f'Se va a tocar el instrumento: {self.nombre}')
        if self.afinado:
            log.info(f'Se está tocando correctamente el instrumento: {self.nombre}\n')
        else:
            raise Instrumento_no_afinado_correctamente(f'El instrumento {self.nombre} no está afinado correctamente\n')

    def aporrear(self):
        if self.afinado:
            log.info(f'Se está aporreando correctamente el instrumento: {self.nombre}\n')
        else:
            raise Instrumento_no_afinado_correctamente(f'El instrumento {self.nombre} no está afinado correctamente\n')


class Orquesta():

    def __init__(self, guitarra, guitarra_electrica, piano, tambor):
        self.guitarra = guitarra
        self.guitarra_electrica = guitarra_electrica
        self.piano = piano
        self.tambor = tambor
        self.instrumentos = []

    def crearOrquesta(self):
        self.instrumentos = [self.guitarra, self.guitarra_electrica, self.piano, self.tambor]

    def iniciarConcierto(self):
        for instrumento in self.instrumentos:
            instrumento.afinarInstrumento()

        try:
            for instrumento in self.instrumentos:
                if isinstance(instrumento, Tambor):
                    instrumento.aporrear()

                else:
                    instrumento.tocarInstrumento()

        except Instrumento_no_afinado_correctamente as inac:
            log.error(inac.message)
            log.info(f'El concierto se detiene porque {instrumento.nombre} no esta afinado')
            self.iniciarConcierto()

        except:
            log.error('Algo pasa en la orquesta')

if __name__ == '__main__':
    guitarra = Guitarra('guitarra','cuerda pulsada', 6)
    guitarra_electrica = Guitarra_electrica('guitarra electrica', 'cuerda pulsada', 6, '20W')
    piano = Piano('piano','cuerda',54)
    tambor = Tambor('tambor', 'percusión', '40cm')

    orquesta = Orquesta(guitarra, guitarra_electrica, piano, tambor)
    orquesta.crearOrquesta()
    orquesta.iniciarConcierto()
