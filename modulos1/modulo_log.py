import logging as log
'''
En desarrollo se usa muchisimo los logs para tener toda la informacion porsible, cuando se llega a produccion, los unicos 
logs que se dejan son los de error.
En la libreria log hay distintos niveles, de más estricto a más permisivo.
 -Nivel trace: algunos lenguajes 
 -Nivel debug: Las trazas son de más bajo nivel: Estoy entrando en el metodo con los siguientes atributos, etc... Mucha informacion. (DESARROLLO)
 -Nivel info: Las trazas que metemos son más interesantes, como saber el elemento de control 
 -Nivel warning: Son trazas de avisos que es por si vemos que el funcionamiento de una parte no es normal y sigue funcionando (Nivel por defecto de python)
 -Nivel error: Cuando capturemos una excepcion
 -Nivel critical: algunos lenguajes
 
La gracia de esto, es que si ponemos el nivel debug, apareceran todos los logs de abajo de debug, con debug incluido. 
Si cambiamos a nivel info, aparecen de info para abajo, por lo que debug desapareceria.
Más info: https://docs.python.org/3/howto/logging.html
'''
#Para cambiar el nivel del log
log.basicConfig(level=log.DEBUG,
                format='[%(asctime)s: %(filename)s:%(lineno)s] %(levelname)s:%(message)s',
                datefmt= '%I:%M:%S %p',
                handlers=[log.FileHandler('../logs/curso_python.log'),
                          log.StreamHandler()]) #que muestre el nombre del fichero, numero linea, nombre del log y el mensaje, formato fecha y le decimos que guarde logs en esa ruta

log.error('Esto es un log de prueba de error')
log.debug('Esto es un log de prueba de debug')