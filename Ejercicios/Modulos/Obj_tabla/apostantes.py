class Apostantes:
    def __init__(self, id=None, nombre=None, saldo=None): #clase con los atributos de la tabla
        self._id = id
        self._nombre = nombre
        self._saldo = saldo

    def __str__(self):
        return f'{self._id}, {self._nombre}, {self._saldo}'

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
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
