#Clase Padre
class Cuenta:
    #Metodo Constructor
    def __init__(self,titular,cantidad):
        self._titular = titular
        self._cantidad = cantidad
    
    #Metodos getter
    def get_titular(self):
        return self._titular
    
    def get_cantidad(self):
        return self._cantidad

    #Metodos setter
    def set_titular(self,titular):
        self._titular = titular
    
    def set_cantidad(self,cantidad):
        self._cantidad = cantidad
    
    #Metodo para mostrar los datos
    def mostrar_datos(self):
        print("Titular: ",self._titular,"\nCantidad: ",self._cantidad)
    

#Clase que hereda de la clase Cuenta
class CajaAhorro(Cuenta):
    #Metodo constructor con los atributos de la clase padre
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad) #super para heredar los atributos de la clase padre
    
    #Metodo para imprimir los datos de la clase CajaAhorro
    def mostrar_datos(self):
        print("\nDatos Cuenta Caja de Ahorros")
        super().mostrar_datos()

#Clase que hereda de la clase Cuenta
class PlazoFijo(Cuenta):
    #Metodo constructor con los atributos de la clase padre y ademas tiene atributos propios
    def __init__(self,titular,cantidad,plazo,interes):
        super().__init__(titular,cantidad)#super para heredar los atributos de la clase padre
        self._plazo = plazo
        self._interes = interes
    
    #Metodos getter
    def get_plazo(self):
        return self._plazo
    
    def get_interes(self):
        return self._interes

    #Metodos setter
    def set_plazo(self,plazo):
        self._plazo = plazo
    
    def set_interes(self,interes):
        self._interes = interes
    
    #Metodo para calcular el importe de interes
    def importe_interes(self):
        return (self._cantidad*self._interes/100)

    #Metodo para mostrar los datos de la clase PlazoFijo
    def mostrar_datos(self):
        print("\nDatos Cuenta Plazo Fijo")
        super().mostrar_datos()
        print("Plazo: ",self._plazo,"\nImporte de Interes:",self.importe_interes())

#Instanciando las clases
caja = CajaAhorro("Juan",4000)
caja.mostrar_datos()
plazo = PlazoFijo("Nando",9000,256,0.8)
plazo.mostrar_datos()