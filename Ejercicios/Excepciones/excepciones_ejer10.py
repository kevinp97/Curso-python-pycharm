class Instrumento_no_afinado_correctamente(Exception):

    def __init__(self, mensaje):
        self.message = mensaje
