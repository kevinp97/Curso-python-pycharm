'''
                                CARRERA DE CABALLOS
Crear 3 tablas y cargarla con la información de los ficheros.
Tabla gran_premio: id: Primary key
 nombre:
 distancia:
 num_carreras: 4 carreras, por lo que los apostantes podran apostar 4 veces


Tabla caballos: id:
 nombre:
 fecha_nacimiento: Si es más viejo, menos corre
 velocidad: [1-80]
 experiencia: Importante, porque si gana una carrera tiene experiencia para poder ganar la siguiente [1-100]
 valor_apuesta: Si un apostante apuesta por un caballo, ganara x por lo apostado, esta casilla es la cuota [1-10]
 id_GP: Referencia al id de la tabla carrera

'''

'''
Tabla apostantes:id:
 nombre:
 saldo: Incrementa o decrementa segun gane o apuesta

Lógica del ejercicio: Por cada gran premio, se van a tener que ejecutar el numero de carreras indicada, si el gran premio
tiene 4 carreras, se van a ejecutar 4 carreras y habran 4 apuestas.
Por cada carrera, se tiene que poner a correr a los caballos apuntados a dicha carrera, es decir, en la tabla de caballos
pueden haber 8 caballos, y hay 2 gran premio, cuando lance el GP1 solo los caballos que tengan el id_GP 1 la correran.
Para ello una clase caballo, que simule la carrera. Hay que simular que cuando el caballo corre, avanza una serie de metros
primero avanza el primer caballo y avanzará x metros, asi el segundo, etc. Se repite hasta que un caballo gane. Para ver
como avanza el caballo hay que tener en cuenta velocidad, experiencia y fecha de nacimiento, ya que cada vez que un caballo
corre, avanza con (velocidad+experiencia-edad+num_aleatorio(1-50)), gana el caballo que una vez llegado a la distancia
más valor tenga. Si en la tirada final el caballo 1 llega a 510m y el 3 a 520, gana el caballo 3. NO PUEDE HABER EMPATE
se hace correr una vuelta más para decidir el desempate

Apostantes: Cada apostante con salgo >0 Preguntar cuanto quieren apostar y a que caballo
ID_caballo Nombre Cuota hay que mostrarle eso al apostante para que decida
Una vez los apostantes haya hecho sus apuestas, se empieza la carrera

Al terminar la carrera, los apostantes que hayan acertado se les incrementa el saldo de su cuenta con la cantidad apostada
multiplicado por el valor de la apuesta y a todos los caballos cuando terminan, se le incrementa la experiencia en 1 y el
caballo que haya ganado se le incrementa en 5

Mostrar resumen de cada apostante con su saldo.
'''
'''
Para cada gran premio(Para cada carrera(1. Leer datos tablas    2. Logica hipodromo     3. Actualizar datos))
'''
from Ejercicios.Modulos.DAO.apostantes_dao import Apostantes_DAO
from Ejercicios.Modulos.DAO.caballos_dao import Caballos_DAO
from Ejercicios.Modulos.DAO.gran_premio_dao import Gran_premio_DAO
from Ejercicios.Modulos.Obj_tabla.gran_premio import Gran_premio
from Ejercicios.Modulos.Obj_tabla.caballos import Caballos
from Ejercicios.Modulos.Obj_tabla.apostantes import Apostantes
import logging as log
from datetime import datetime
import random


log.basicConfig(level=log.DEBUG,
                format='[%(asctime)s: %(filename)s:%(lineno)s] %(levelname)s:%(message)s',
                datefmt= '%I:%M:%S %p')



class Seleccion_caballos():

    def __init__(self, caballos_dao, id_gp):
        self.caballos_dao = caballos_dao
        self.caballos_carrera = []
        self.id_gp = id_gp


    def datos_carrera(self):
        self.caballos = self.caballos_dao.seleccionar(self.id_gp)
        for caballo in self.caballos:
            self.caballos_carrera.append(caballo)
        log.info(f'Los caballos participantes son los siguiente:')
        for n_caballo in self.caballos_carrera:
            anios_caballo = datetime.now().year - n_caballo.fecha_nacimiento.year
            meses_caballo = datetime.now().month - n_caballo.fecha_nacimiento.month
            log.info(f'Nombre: {n_caballo.nombre}  Edad:{anios_caballo} años y {meses_caballo} meses  Velocidad:{n_caballo.velocidad} km/h  Experiencia:{n_caballo.experiencia}  Cuota:{n_caballo.valor_apuesta} ')

        return self.caballos_carrera

class Seleccion_apostantes():

    def __init__(self, apostantes_dao, caballos_carrera):
        self.apostantes_dao = apostantes_dao
        self.caballos_carrera = caballos_carrera
        self.lista_apostantes = []
        self.libro_apuestas_caballo = {}
        self.libro_apuestas_dinero = {}

    def datos_apostantes(self):
        log.info('Los apostantes se acercan al mostrador y facilitan sus datos')
        self.apostantes = self.apostantes_dao.seleccionar()
        for apostante in self.apostantes:
            log.info(f'Datos apostante: {apostante.nombre} {apostante.saldo}€')
            if apostante.saldo <= 0:
                log.info(f'El {apostante.nombre} no tiene dinero para apostar')
            else:
                self.lista_apostantes.append(apostante)
        log.info('Los apostantes que pueden apostar son los siguientes:')
        for apostante_con_dinero in self.lista_apostantes:
            log.info(f' Datos apostante: {apostante_con_dinero.nombre} {apostante_con_dinero.saldo}€')

    def apuesta_a_caballo(self):
        for apostante in self.lista_apostantes:
                cantidad_apuesta = random.randint(1,apostante.saldo)
                eleccion_caballo = random.choice(self.caballos_carrera)
                ganancias_limpias = (cantidad_apuesta*eleccion_caballo.valor_apuesta) - cantidad_apuesta

                log.info(
                    f'{apostante.nombre} elige que apuesta {cantidad_apuesta}€ por el {eleccion_caballo.nombre} a cuota {eleccion_caballo.valor_apuesta}. Posibles ganancias de {ganancias_limpias}€')
                self.libro_apuestas_dinero[apostante.nombre] = cantidad_apuesta
                self.libro_apuestas_caballo[apostante.nombre] = eleccion_caballo.nombre
        log.info(f'El libro de apuestas para la carrera es el siguiente {self.libro_apuestas_dinero}')
        return self.libro_apuestas_caballo, self.libro_apuestas_dinero


class Hipodromo:
    def __init__(self, gran_premio_dao, ):
        self.gran_premio_dao = gran_premio_dao
        self.gran_premio = self.gran_premio_dao.seleccionar()


    def cantidad_grandes_premios(self):
        n_grandes_premios = len(self.gran_premio)
        log.info(f'Hay un total de {n_grandes_premios} grandes premios')

    def gran_premios(self):
        for gp in self.gran_premio:
            self.id_gp = gp.id
            self.distancia = gp.distancia
            log.info(f'Hay {gp.num_carreras} carreras de {gp.distancia} metros, empieza el {gp.nombre}')

            for carrera in range(0, gp.num_carreras):
                log.info('**************** EMPIEZA LA CARRERA ****************')
                self.caballos_carrera = Seleccion_caballos(Caballos_DAO, self.id_gp).datos_carrera() #seleccionamos los caballos participantes
                seleccion_apostantes = Seleccion_apostantes(Apostantes_DAO, self.caballos_carrera)
                seleccion_apostantes.datos_apostantes() #datos apostantes
                seleccion_apostantes.apuesta_a_caballo() #apuesta a caballo
                # Se realiza la carrera de caballos
                log.info(f'Los caballos se posicionan en el puesto de salida')
                log.info('\n ******************************************************************\n')
                self.carrera_caballo()
                self.caballo_ganador_carrera()


    def carrera_caballo(self):
        self.carrera_de_caballos = {}
        self.llegada_meta = False
        for caballo in self.caballos_carrera:
            self.carrera_de_caballos[caballo.nombre] = 0
        log.info('**************** EMPIEZA LA CARRERA ****************')
        while self.llegada_meta == False:
            for caballo in self.caballos_carrera:
                metros_avanzados = self.carrera_de_caballos[caballo.nombre]
                anios_caballo = datetime.now().year - caballo.fecha_nacimiento.year
                desplazamiento = caballo.velocidad + caballo.experiencia - anios_caballo + random.randint(1, 50)
                self.carrera_de_caballos[caballo.nombre] = metros_avanzados + desplazamiento
                if self.carrera_de_caballos[caballo.nombre] >= self.distancia:
                    self.llegada_meta = True
            log.info(f'CARRERA EN DIRECTO: {self.carrera_de_caballos}')

    def caballo_ganador_carrera(self):
        self.ganador = 0
        self.empate = False
        self.caballo_ganador = ''

        for caballo in self.carrera_de_caballos:
            if self.carrera_de_caballos[caballo] > self.ganador:
                self.caballo_ganador = caballo
                self.ganador = self.carrera_de_caballos[caballo]

            elif self.carrera_de_caballos[caballo] == self.ganador:
                self.empate = True
        log.info(f'El caballo ganar ha sido {self.caballo_ganador}')




if __name__ == '__main__':

    hipodromo = Hipodromo(Gran_premio_DAO)
    hipodromo.cantidad_grandes_premios()
    hipodromo.gran_premios()



    # grandes_premios = Gran_premio_DAO()
    # gran_premio = grandes_premios.seleccionar()
    # n_grandes_premios = len(gran_premio)
    # log.info(f'Hay un total de {n_grandes_premios}')
    # for gp in gran_premio:
    #     id_gp = gp.id
    #     nombre_gp = gp.nombre
    #     distancia = gp.distancia
    #     num_carreras = gp.num_carreras
    #     log.info(f'Hay {num_carreras} carreras de {distancia} metros, empieza el {nombre_gp}')
    #
    #     for carrera in range(0,num_carreras):
    #
    #
    #         # seleccionamos los caballos participantes en la carrera ya actualizados
    #         seleccion_caballos = Caballos_DAO()
    #         caballos = seleccion_caballos.seleccionar(id_gp)
    #         caballos_carrera = []
    #         for caballo in caballos:
    #             caballos_carrera.append(caballo)
    #         log.info(f'La carrera número {carrera + 1} está a punto de comenzar')
    #         log.info(f'Los caballos participantes son los siguiente:')
    #         for n_caballo in caballos_carrera:
    #             anios_caballo = datetime.now().year - n_caballo.fecha_nacimiento.year
    #             meses_caballo = datetime.now().month - n_caballo.fecha_nacimiento.month
    #             log.info(f'Nombre: {n_caballo.nombre}  Edad:{anios_caballo} años y {meses_caballo} meses  Velocidad:{n_caballo.velocidad} km/h  Experiencia:{n_caballo.experiencia}  Cuota:{n_caballo.valor_apuesta} ')
    #         log.info('\n')
    #         log.info('APUESTAS')
    #         #Seleccionamos los datos de todos los apostantes
    #         seleccion_apostantes = Apostantes_DAO()
    #         apostantes = seleccion_apostantes.seleccionar()
    #         lista_apostantes = []
    #         log.info('Los apostantes se acercan al mostrador y facilitan sus datos')
    #         for apostante in apostantes:
    #             log.info(f'Datos apostante: {apostante.nombre} {apostante.saldo}€')
    #             if apostante.saldo <= 0:
    #                 log.info(f'El {apostante.nombre} no tiene dinero para apostar')
    #             else:
    #                 lista_apostantes.append(apostante)
    #
    #         log.info('Los apostantes que pueden apostar son los siguientes:')
    #         for apostante_con_dinero in lista_apostantes:
    #             log.info(f' Datos apostante: {apostante_con_dinero.nombre} {apostante_con_dinero.saldo}€')
    #
    #
    #         #Se realiza la apuesta por el caballo
    #         libro_apuestas_caballo = {}
    #         libro_apuestas_dinero = {}
    #         for apostante in lista_apostantes:
    #             cantidad_apuesta = random.randint(1,apostante.saldo)
    #             eleccion_caballo = random.choice(caballos_carrera)
    #
    #             ganancias_limpias = (cantidad_apuesta*eleccion_caballo.valor_apuesta) - cantidad_apuesta
    #
    #             log.info(f'{apostante.nombre} elige que apuesta {cantidad_apuesta}€ por el {eleccion_caballo.nombre} a cuota {eleccion_caballo.valor_apuesta}. Posibles ganancias de {ganancias_limpias}€')
    #             libro_apuestas_dinero[apostante.nombre] = cantidad_apuesta
    #             libro_apuestas_caballo[apostante.nombre] = eleccion_caballo.nombre
    #         log.info(f'El libro de apuestas para la carrera es el siguiente {libro_apuestas_dinero}')
    #
    #
    #         #Se realiza la carrera de caballos
    #         log.info(f'Los caballos se posicionan en el puesto de salida')
    #         carrera_de_caballos = {}
    #         for caballo in caballos_carrera:
    #             carrera_de_caballos[caballo.nombre] = 0
    #
    #         log.info(f'Los caballos se posicionan en parrilla de salida: {carrera_de_caballos}')
    #         llegada_meta = False
    #         log.info('**************** EMPIEZA LA CARRERA ****************')
    #         while llegada_meta == False:
    #             for caballo in caballos_carrera:
    #                 metros_avanzados = carrera_de_caballos[caballo.nombre]
    #                 anios_caballo = datetime.now().year - caballo.fecha_nacimiento.year
    #                 desplazamiento = caballo.velocidad + caballo.experiencia - anios_caballo + random.randint(1,50)
    #                 carrera_de_caballos[caballo.nombre] = metros_avanzados + desplazamiento
    #                 if carrera_de_caballos[caballo.nombre] >= distancia:
    #                     llegada_meta = True
    #             log.info(f'CARRERA EN DIRECTO: {carrera_de_caballos}')
    #         ganador = 0
    #         empate = False
    #         caballo_ganador = ''
    #         for caballo in carrera_de_caballos:
    #             if carrera_de_caballos[caballo] > ganador:
    #                 caballo_ganador = caballo
    #                 ganador = carrera_de_caballos[caballo]
    #
    #             elif carrera_de_caballos[caballo] == ganador:
    #                 empate = True
    #         log.info(f'El caballo ganar ha sido {caballo_ganador}')
    #
    #         #Comprobación de las apuestas
    #         log.info(libro_apuestas_caballo)
    #         log.info(libro_apuestas_dinero)
    #
    #         apostantes_ganadores = []
    #         apostantes_perdedores = []
    #         for apostante_caballo in libro_apuestas_caballo:
    #             if caballo_ganador == libro_apuestas_caballo[apostante_caballo]:
    #                 apostantes_ganadores.append(apostante_caballo)
    #             else:
    #                 apostantes_perdedores.append(apostante_caballo)
    #
    #         log.info(f'Han ganado los siguientes apostantes: {apostantes_ganadores}')
    #         log.info(f'Han perdido los siguientes apostantes: {apostantes_perdedores}')
    #
    #         #Actualizacion de los datos de los apostantes
    #         lista_apostantes_id = []
    #         for apostante in lista_apostantes:
    #             lista_apostantes_id.append(apostante.id)
    #         log.info(lista_apostantes_id)
    #         seleccion_apostantes.actualizar(tuple(lista_apostantes_id))
    #
    #         #Actualizacion de los datos de los caballos
    #
    #
    #
    #
    #         log.info('--------------------------------------------------------------------------')
    #
    #         log.info('\n')