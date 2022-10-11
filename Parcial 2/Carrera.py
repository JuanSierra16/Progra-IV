class Carrera:
    #Composicion

    #Constructor
    def __init__(self, distancia, ronda, fecha):
        self._distancia = distancia
        self._ronda = ronda
        self._fecha = fecha
    
    #Metodos getter y setter
    def getDistancia(self):
        return self._distancia

    def setDistancia(self, distancia):
        self._distancia = distancia

    def getRonda(self):
        return self._ronda

    def setRonda(self, ronda):
        self._ronda = ronda

    def getFecha(self):
        return self._fecha

    def setFecha(self, fecha):
        self._fecha = fecha