class Calculadora:

    #Metodo Constructor
    def __init__(self,numero1=0,numero2=0):
        #Pido los valores por teclado
        self._numero1 = int(input("\nIngrese el primer número: "))
        self._numero2 = int(input("Ingrese el segundo número: "))
    
    #Metodos getter and setter
    def get_numero1(self):
        return self._numero1
    
    def get_numero2(self):
        return self._numero2

    def set_numero1(self,numero1):
        self._numero1 = numero1

    def set_numero2(self,numero2):
        self._numero2 = numero2

    #Metodo para sumar los dos numeros
    def suma(self):
        return self._numero1 + self._numero2
    
    #Metodo para restar los dos numeros
    def resta(self):
        return self._numero1 - self._numero2
    
    #Metodo para multiplicar los dos numeros
    def mult(self):
        return self._numero1 * self._numero2

    #Metodo para dividir los dos numeros
    def div(self):
        return self._numero1 / self._numero2

    #Metodo para la impresion de los datos
    def __str__(self):
        return '\nValores Ingresados: {0},  {1}\nSuma: {2}\nResta: {3}\nMultiplicacion: {4}\nDivision: {5}\n'.format(self._numero1, self._numero2, self.suma(), self.resta(), self.mult(), self.div())

#Instanciando la clase
operacion = Calculadora()
print(operacion)