class Libro:

    #Constructor
    def __init__(self, titulo, isbn, autor, añoPublicacion):
        self._titulo = titulo
        self._isbn = isbn
        self._autor = autor
        self._añoPublicacion = añoPublicacion

    #Metodos
    def getTitulo(self):
        return self._titulo

    def setTitulo(self, titulo):
        self._titulo = titulo
    
    def getIsbn(self):
        return self._isbn

    def setIsbn(self,isbn):
        self._isbn = isbn

    def getAutor(self):
        return self._autor
    
    def setAutor(self, autor):
        self._autor = autor

    def getAñoPublicacion(self):
        return self._añoPublicacion

    def setAñoPublicacion(self, añoPublicacion):
        self._añoPublicacion = añoPublicacion