menu=["patacon","encebolado","arepa","tigrillo"]

def imprimirMenu():
    print(menu)

imprimirMenu()

def imprimirOpciones():
    print(
        """
    1.      Añadir plato al menú.
    2.      Buscar en el menú.
    3.      Eliminar plato del menú.
    4.      Mostrar platos del menú.
    5.      Fin Programa
        
        """)
    

imprimirOpciones()
opcion=input("ingrese una opcion para el menu\n")

while opcion!=5:

    if(int(opcion)==1):
        nuevoPlato=input("1. Agregar un plato al menu: \n")
        menu.append(nuevoPlato)
        imprimirMenu()

    elif(int(opcion)==2):
        buscar=input("2. Buscar el plato a buscar: \n")
        if(buscar in menu):
            print("plato en contrado en la posisicon: ", menu.index(buscar))
        else:
            print("plato no encontrado: ",buscar)

    elif(int(opcion)==3):
        eliminar=input("3. ingrese el plato a eliminar: \n")
        if(eliminar in menu):
            print("elimnando en la posisicon: ", menu.index(eliminar))
            menu.remove(eliminar)
        else:
            print("plato no encontrado: ",eliminar)

    elif(int(opcion)==4):
        print("4.Imprimir menu")
        imprimirMenu()
    elif(int(opcion)==5):
        print("Programa terminado")
        break

    imprimirOpciones()
    opcion=input("ingrese una opcion para el menu")


