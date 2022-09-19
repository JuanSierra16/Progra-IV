class Cliente:
    #Constructor
    def __init__(self,nombre):
        self._nombre = nombre
        self._cantidad = 0
    
    #Metodos getter
    def get_nombre(self):
        return self._nombre
    
    def get_cantidad(self):
        return self._cantidad
    
    #Metodos setter
    def set_nombre(self,nombre):
        self._nombre = nombre
    
    def set_cantidad(self,cantidad):
        self._cantidad = cantidad

    #Metodo para depositar un monto
    def depositar(self, monto):
        self._cantidad += monto
    
    #Metodo para extraer un monto
    def extraer(self, monto):
        self._cantidad -= monto

    #Metodo para mostar la cantidad total de dinero
    def mostrar_total(self):
        print("La cantidad total de",self._nombre,"es:",self._cantidad)


class Banco:

    #Metodo Constructor
    def __init__(self):
        #Instancio 3 clientes de la clase cliente como atributos de la clase Banco
        self.cliente1 = Cliente("Juan")
        self.cliente2 = Cliente("Lucas")
        self.cliente3 = Cliente("Sofia")
    
    #Metodo para realizar las operaciones de los clientes
    def operar(self):
        self.cliente1.depositar(500)
        self.cliente2.depositar(1000)
        self.cliente3.depositar(600)
        self.cliente1.extraer(100)

    #Metodo para imprimir el deposito total de los clientes
    def deposito_total(self):
        self.cliente1.mostrar_total()
        self.cliente2.mostrar_total()
        self.cliente3.mostrar_total()
        total = self.cliente1._cantidad + self.cliente2._cantidad + self.cliente3._cantidad
        print("\nLa cantidad total de dinero que se ha depositado es",total,"\n")

#Instanciando un objeto banco de la clase Banco
banco = Banco()
banco.operar()
banco.deposito_total()