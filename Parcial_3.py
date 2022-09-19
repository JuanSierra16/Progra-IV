class Triangulo:

    #Metodo Constructor
    def __init__(self,lado1,lado2,lado3):
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3
        self._tipo = self.tipo_triangulo(self._lado1, self._lado2, self._lado3)
        self._mayor = self.lado_mayor(self._lado1, self._lado2, self._lado3)
    
    #Metodos getter y setter
    def get_lado1(self):
        return self._lado1

    def get_lado2(self):
        return self._lado2

    def get_lado3(self):
        return self._lado3

    def set_lado1(self,lado1):
        self._lado1 = lado1
    
    def set_lado1(self,lado2):
        self._lado2 = lado2

    def set_lado1(self,lado3):
        self._lado3 = lado3
    
    #Metodo para saber de que tipo es el triangulo con base a los lados
    def tipo_triangulo(self,lado1,lado2,lado3):
        if(lado1 == lado2 and lado2 == lado3):
            return "Es equilatero" #Todos sus lados son iguales
        elif(lado1 != lado2 and lado2 != lado3 and lado1 != lado3):
            return "Es escaleno" #Todos los lados tiene una medida distinta
        else:
            return "Es iscoceles" #Dos lados iguales y uno distinto
    
    #Metodo para saber cual es el lado mayor
    def lado_mayor(self,lado1,lado2,lado3):
        mayor = lado1;
        if(lado1>=lado2 and lado1>=lado3):
            mayor = lado1
        elif(lado2>=lado1 and lado2>=lado3):
            mayor = lado2
        elif(lado3>=lado1 and lado3>=lado2):
            mayor = lado3
        return mayor
    
    #Metodo para la impresion de los datos
    def __str__(self):
        return '\nDatos del triangulo:\nLados: ({0},{1},{2})\nLado Mayor: {3}\nTipo: {4}\n'.format(self._lado1, self._lado2, self._lado3, self._mayor, self._tipo)

#Instanciando la clase
triangulo = Triangulo(3,3,3)
triangulo2 = Triangulo(3,3,2)
triangulo3 = Triangulo(2,4,4)
triangulo4 = Triangulo(1,3,1)
triangulo5 = Triangulo(3,4,5)
triangulo6 = Triangulo(6,2,5)
triangulo7 = Triangulo(1,5,4)
print(triangulo, triangulo2, triangulo3, triangulo4, triangulo5, triangulo6, triangulo7)