from xml.etree.ElementTree import PI
from Punto import Punto #Importacion de la clase Punto
import math

class CircunferenciaCentrada:

    #Constructores
    def __init__(self):
        self._PI = 3.1416
        self._radio = 0.0
        self._centro = Punto()

    def __init__(self, radio, x, y):
        self._PI = 3.1416
        self._radio = radio
        self._centro = Punto(x,y)

    #Metodos
    def getRadio(self):
        return self._radio

    def setRadio(self,radio):
        self._radio = radio
    
    def getDiametro(self):
        return (self._radio*2)
    
    def setDiametro(self, diametro):
        self._radio = (diametro/2)
    
    def getLongitud(self):
        return (2*self._PI*self.radio)

    def setLongitud(self, longitud):
        self._radio = (longitud)/(2*self._PI);

    def getArea(self):
        return (self._PI*(self._radio*self._radio))

    def setArea(self, area):
        self._radio = math.sqrt((area)/(self._PI))

    def getXCentro(self):
        return self._centro.getX()
    
    def setXCentro(self,x):
        self._centro.setX(x)
    
    def getYCentro(self):
        return self._centro.getY()
    
    def setYCentro(self, y):
        self._centro.setY(y)

    def trasladarCircunferenciaCentrada(self, x, y):
        self._centro.setX(self._centro.getX()+x)
        self._centro.setY(self._centro.getY()+y)