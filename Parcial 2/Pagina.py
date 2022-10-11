class Pagina:
    
    #Constructor
    def __init__(self, contenido, numero):
        self._contenido = contenido
        self._numero = numero
    
    #Metodos getter y setter
    def getContenido(self):
        return self._contenido
    
    def getNumero(self):
        return self._numero

    def setContenido(self, contenido):
        self._contenido = contenido
    
    def setNumero(self, numero):
        self._numero = numero