#Importacion de las clases Contacto y Agenda
from Parcial_5_Contacto import Contacto
from Parcial_5_Agenda import Agenda

if __name__=='__main__':

    #Instanciando un objeto de la clase Agenda
    agenda = Agenda()
        
    #Variable opcion sirve para navegar en el menu
    opcion = 1

    #Bucle para que imprimir el menu hasta que el usuario quiera cerrar la agenda
    while(0 < opcion and opcion < 6):
        #Imprimir lista de opciones
        print('\n\t__:AGENDA:__')
        print('1. Añadir Contacto')
        print('2. Lista de contactos')
        print('3. Buscar contacto')
        print('4. Editar Contacto')
        print('5. Cerrar Agenda')

        #Ingresando la opcion de tipo entero
        opcion = int(input('\nElija una opcion: '))

        #Ciclo para que el ususario ingrese una opcion correcta del menu
        while(opcion < 1 or opcion > 5):
            opcion = int(input('Elija la opcion correcta entre 1 y 4: '))

        #Condicionales para evaluar que opcion ingreso el usuario
        if opcion == 1:
            print('\nNuevo Contacto')
            contacto = agenda.nuevo_contacto()#LLama al metodo para crear un nuevo contacto
            if agenda.contiene_contacto(contacto.get_telefono()): #Evalua si el contacto ya se encuentra en la agenda
                print("\nEl contacto con telefono {0} ya exisite la agenda".format(contacto.get_telefono()))
            else:
                agenda.agregar_contacto(contacto)#Llama al metodo para agregar el contacto a la agenda
                print("\nEl contacto ha sido agregado")

        elif opcion == 2:
            print("\nLista de contactos")
            agenda.listar_contactos()#LLamado al metodo para listar contactos de la clase agenda

        elif opcion == 3:
            nombreBuscar = input("Ingrese el nombre del contacto a buscar: ")
            if(agenda.buscar_contacto(nombreBuscar)):#LLama al metodo para buscar un contacto que devuelve True o False
                print("\nEl contacto SI se encuentra en la agenda")
            else:
                print("\nEl contacto NO se encuentra en la agenda")

        elif opcion == 4:
            print("\nEditar contacto")
            nombre = input("Digite el nombre del contacto: ")
            if agenda.buscar_contacto(nombre):#Busca si el contacto se encuentra en la agenda
                agenda.editar_contacto(nombre)#Si lo encuentra, llama el metodo para editarlo
                print("El contacto ha sido editado")
            else:
                print("El contacto",nombre,"no existe")#Si no imprime un mensaje
                print("No se puede editar")

        elif opcion == 5:#Opcion para cerrar la agenda y que finalice el programa
            print('Agenda Cerrada...')
            break