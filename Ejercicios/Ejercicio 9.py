'''
                                EJERCICIO 9
    TemperatureException --> Exception
    TooHotTemperatureException --> TemperatureException
    TooColdTemperatureException --> TemperatureException

    TazaCafe:
        -Temperature:
        -Tipo_cafe

    Cliente:
        -Nombre
        -TomarTazaCafe(TazaCafe)


    Camarero:
        -Nombre
        -Servirtazacafe()--> Crear objeto TazaCafe donde la temperatura va a ser aleatoria entre (0-100) se le puede preguntar el tipo de cafe al cliente


    Bar:
        -Camarero:Sirve taza de cafe
        -Cliente:Toma taza de cafe

    Crear jerarquia de excepciones que heredan de exception y las otras 2 de temperatura exception
    En el bar la gente se van a enterar si se ha quemado la lengua o le ha parecido frio, una pista:
    Si cuando el cliente se toma la taza de cafe la temperatura es mayor de 80, en el bar la gente se van a enterar que
    el cliente se ha quemado la lengua. Y si esta a menos de 20, el cliente va a protestar por que el cafe esta frio

'''
import random
import logging as log

log.basicConfig(level=log.DEBUG,
                format='[%(asctime)s: %(filename)s:%(lineno)s] %(levelname)s:%(message)s',
                datefmt= '%I:%M:%S %p',
                handlers=[log.FileHandler('../logs/ejercicio9.log'),
                          log.StreamHandler()])

from Ejercicios.Excepciones.excepciones_ejer9 import TemperatureException,TooColdTemperatureException,TooHotTemperatureException

class TazaCafe():
    def __init__(self, temperatura, tipo_cafe):
        self.temperatura = temperatura
        self.tipo_cafe = tipo_cafe
        log.info(f'Temperatura de cafe: {self.temperatura}; tipo de cafe: {self.tipo_cafe}')


class Cliente():
    def __init__(self, nombre, cafe):
        self.nombre = nombre
        self.cafe = cafe

    def tomarTazaCafe(self):
        if self.cafe.temperatura >= 80:
            raise TooHotTemperatureException(f'El cliente se ha quemado la lengua')


        elif self.cafe.temperatura <= 20:
            raise TooColdTemperatureException(f'El cliente está protestando porque se le ha quemado la lengua')



class Camarero():
    def __init__(self,nombre, cafe):
        self.nombre = nombre
        self.cafe = cafe

    def servirTazaCafe(self):
        log.info(f'{self.nombre} sirve el cafe a {self.cafe.temperatura}°')

class Bar():
    def __init__(self, cliente, camarero, cafe):
        self.cliente = cliente
        self.camarero = camarero
        self.cafe = cafe
    def cliente_entra_al_bar(self):
        log.info(f'El cliente {self.cliente.nombre} entra al bar y se sienta en una mesa')

    def camarero_atiende_al_cliente(self):
        log.info(f'El camarero {self.camarero.nombre} atiende al cliente {self.cliente.nombre}')

    def cliente_pide_cafe(self):

        log.info(f'El cliente le pide un {self.cafe.tipo_cafe}')

    def camarero_trae_cafe(self):
        self.camarero.servirTazaCafe()
        try:
            self.cliente.tomarTazaCafe()
        except TooHotTemperatureException as thte:
            log.error(thte.message)
        except TooColdTemperatureException as tcte:
            log.error(tcte.message)
            log.error('El camarero le calienta más el café')
        except:
            log.info('Al cliente le pasa algo')
        else:
            log.info('El cliente se ha tomado el cafe')

if __name__ == '__main__':
    lista_cafe = ['cafe con leche', 'cortado', 'descafeinado', 'bombon']
    taza_de_cafe = TazaCafe(random.randint(0,100), random.choice(lista_cafe))
    cliente = Cliente('Cliente', taza_de_cafe)
    camarero = Camarero('Camarero', taza_de_cafe)
    bar = Bar(cliente, camarero, taza_de_cafe)
    bar.cliente_entra_al_bar()
    bar.camarero_atiende_al_cliente()
    bar.cliente_pide_cafe()
    bar.camarero_trae_cafe()


