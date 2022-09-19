#Importo la clase Contacto
from Parcial_5_Contacto import Contacto

class Agenda:
    #Metodo Constructor
    def __init__(self):
        self.contactos = [] #Lista de contactos
    
    #Metodo para crear un nuevo contacto
    def nuevo_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        email = input("Email: ")
        return Contacto(nombre, telefono, email)#Retorna un contacto con los datos ingresados
    
    #Metodo para saber si el contacto ya se encuentra en la lista
    def contiene_contacto(self, telefono):
        for contacto in self.contactos:
            if (contacto.get_telefono() == telefono):
                return True
        return False

    #Metodo para agregar un contacto a la lista
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    #Metodo para imprimir la lista de contactos
    def listar_contactos(self):
        for contacto in self.contactos:
            print("\nNombre: ",contacto.get_nombre())
            print("Telefono: ",contacto.get_telefono())
            print("Domicilio: ",contacto.get_email())
    
    #Metodo para buscar un contacto en la lista
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if(contacto.get_nombre() == nombre):
                return True
        return False
    
    #Metodo para eliminar un contacto de la lista
    def eliminar_contacto(self, telefono):
        for i in range(len(self.contactos)):
            if self.contactos[i].get_telefono() == telefono:
                del self.contactos[i]
                break   

    #Metodo para editar algun atributo de un contacto
    def editar_contacto(self,nombre):
        for contacto in self.contactos:
            if(contacto.get_nombre() == nombre):
                opcion = self.menu_editar()
                if(opcion == 1):
                    contacto.set_nombre(input("\nIngrese el nuevo nombre: "))
                elif(opcion == 2):
                    contacto.set_telefono(input("\nIngrese el nuevo telefono: "))
                elif(opcion == 3):
                    contacto.set_email(input("\nIngrese el nuevo email: "))
                elif(opcion == 4):
                    self.eliminar_contacto(contacto.get_telefono()) 
    
    #Metodo que muestra un menu para saber que se quiere editar del contacto
    def menu_editar(self):
        print('\n1. Editar Nombre')
        print('2. Editar Telefono')
        print('3. Editar email')
        print('4. Eliminar contacto')
        opcion = int(input("\nIngrese la opcion que desee editar: "))
        while(opcion < 0 or opcion > 4):#Ciclo para que se ingrese una opcion correcta
            opcion = int(input("\nIngrese una opcion correcta entre 1 y 4: "))
        return opcion