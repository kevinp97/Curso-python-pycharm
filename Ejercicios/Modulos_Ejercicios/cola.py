class Cola:
    '''
    Esta clase esta hecha para crear objetos como la sala de espera y poder añadir y eliminar objetos de la lista
    '''
    def __init__(self):
        self.items = [] #cola vacia

    def encolar(self, x):
        self.items.append(x) #añadimos elemento a cola

    def desencolar(self):
        #elimina elementos y si es 0 da value error
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        return self.items == [] #deveulve true si la cola esta vacia