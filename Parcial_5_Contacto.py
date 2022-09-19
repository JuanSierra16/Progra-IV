class Contacto:

    #Constructor
    def __init__(self,nombre,telefono,email):
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
    
    #Metodos getter
    def get_nombre(self):
        return self._nombre

    def get_telefono(self):
        return self._telefono

    def get_email(self):
        return self._email

    #Metodos setter
    def set_nombre(self,nombre):
        self._nombre = nombre

    def set_telefono(self,telefono):
        self._telefono = telefono

    def set_email(self,email):
        self._email = email

    #Metodo para la impresion de los datos
    def __str__(self):
        return 'DNI: {0}\nNombre: {1}\nTelefono: {2}n\Email: {3}\n'.format(self._nombre, self._telefono, self._email)