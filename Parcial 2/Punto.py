class Punto:

    #Constructores
    def __init__(self):
        self._coord_x = 0
        self._coord_y = 0

    def __init__(self, coord_x, coord_y):
        self._coord_x = coord_x
        self._coord_y = coord_y

    #Metodos getter y setter
    def getX(self):
        return self._coord_x
    
    def setX(self, coord_x):
        self._coord_x = coord_x

    def getY(self):
        return self._coord_y
    
    def setY(self, coord_y):
        self._coord_y = coord_y