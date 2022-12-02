import logging as log
from Ejercicios.Modulos.Obj_tabla.gran_premio import Gran_premio
from Ejercicios.Modulos.Obj_tabla.caballos import Caballos
from Ejercicios.Modulos.Obj_tabla.apostantes import Apostantes
from Ejercicios.Modulos.DAO.gran_premio_dao import Gran_premio_DAO
from Ejercicios.Modulos.DAO.caballos_dao import Caballos_DAO
from Ejercicios.Modulos.DAO.apostantes_dao import Apostantes_DAO
from basededatos.utils.conexiones import get_mysql_conection

log.basicConfig(level=log.DEBUG,
                format='[%(asctime)s: %(filename)s:%(lineno)s] %(levelname)s:%(message)s',
                datefmt= '%I:%M:%S %p')

class Lectura_fichero():


    def __init__(self, fichero):
        self.fichero = fichero

    def lectura_gp(self):
        for linea in self.fichero:
            datos= linea.split('|')
            gp = Gran_premio(nombre=datos[0], distancia=datos[1], num_carreras=datos[2])
            log.info(gp)
            gp_dao = Gran_premio_DAO()
            gp_dao.insertar(gp)

    def lectura_caballos(self):
        for linea in self.fichero:
            datos = linea.split('|')
            caballo = Caballos(nombre=datos[0], fecha_nacimiento=datos[1], velocidad=datos[2], experiencia=datos[3], valor_apuesta=datos[4], id_GP=datos[5])
            log.info(caballo)
            caballo_dao = Caballos_DAO()
            caballo_dao.insertar(caballo)

    def lectura_apostantes(self):
        for linea in self.fichero:
            datos = linea.split('|')
            apostante = Apostantes(nombre=datos[0], saldo=datos[1])
            log.info(apostante)
            apostante_dao = Apostantes_DAO()
            apostante_dao.insertar(apostante)


if __name__ == '__main__':

    # with open('C:\\Users\\kevin\\PycharmProjects\\Formacion\\Ejercicios\\ficheros\\grandes_premios.txt',
    #           'r',
    #           encoding='utf8') as archivo:
    #     grandes_premios = archivo
    #     gp = Lectura_fichero(grandes_premios)
    #     gp.lectura_gp()

    # with open('C:\\Users\\kevin\\PycharmProjects\\Formacion\\Ejercicios\\ficheros\\caballos.txt',
    #           'r',
    #           encoding='utf8') as archivo:
    #     caballos = archivo
    #     caballo = Lectura_fichero(caballos)
    #     caballo.lectura_caballos()
    #
    # with open('C:\\Users\\kevin\\PycharmProjects\\Formacion\\Ejercicios\\ficheros\\apostantes.txt',
    #           'r',
    #           encoding='utf8') as archivo:
    #     apostantes = archivo
    #     apostante = Lectura_fichero(apostantes)
    #     apostante.lectura_apostantes()





