class Persona:

    #Metodo Constructor
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
        self._mayor = self.es_mayor(self._edad)
    
    #Metodos getter y setter
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self,nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad
    
    #Metodo para saber si la persona es mayor de edad o no
    def es_mayor(self,edad):
        mayor = "No es mayor de edad"
        if(edad >= 18):
            mayor = "Es mayor de edad"
        return mayor

    #Metodo para la impresion de los datos
    def __str__(self):
        return '\nDatos de la Persona:\nNombre: {0}\nEdad: {1}\n{2}\n'.format(self._nombre, self._edad, self._mayor)

#Instanciando la clase
persona1 = Persona("Juan",18)
persona2 = Persona("Nath",15)
print(persona1, persona2)