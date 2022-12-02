

class Gran_premio:
    def __init__(self, id=None, nombre=None, distancia=None, num_carreras=None): #clase con los atributos de la tabla
        self._id = id
        self._nombre = nombre
        self._distancia = distancia
        self._num_carreras = num_carreras

    def __str__(self):
        return f'{self._id}, {self._nombre}, {self._distancia}, {self._num_carreras}'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def distancia(self):
        return self._distancia

    @distancia.setter
    def distancia(self, distancia):
        self._distancia = distancia

    @property
    def num_carreras(self):
        return self._num_carreras

    @num_carreras.setter
    def num_carreras(self, num_carreras):
        self._num_carreras = num_carreras

