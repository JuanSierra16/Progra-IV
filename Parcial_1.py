class Alumno:

    #Constructor
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
        self._aprobo = self.aprobo(self._nota)

    #Metodos getter y setter
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nota(self):
        return self._nota

    def set_nota(self, nota):
        self._nota = nota
    
    #Metodo para saber si un estudiante aprobo o reprobo
    def aprobo(self, nota):
        resultado = "Reprobo"
        if(nota >= 3):
            resultado = "Aprobo"
        return resultado

    #Metodo para la impresion de los datos
    def __str__(self):
        return '\nDatos Estudiante:\nNombre: {0}\nNota: {1}\nResultado: {2}\n'.format(self._nombre, self._nota, self._aprobo)

#Instanciando la clase
alumno = Alumno("Juan",4)
alumno2 = Alumno("Raul",2)
print(alumno,alumno2)