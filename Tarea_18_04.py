import os
def clear():
    print(" " * 100000000)
def busqueda():
    clear()
    print("\t\t\t|----------------------------------------------|")
    print("\t\t\t|      MENU DE VISUALIZACION DE ALUMNOS        |")
    print("\t\t\t|----------------------------------------------|")
    dato = input("INGRESE EL NUMERO DE CARNET: ")
    print("\t\t\t" + "CARNET".ljust(20, " ") + "NOMBRES".ljust(35, " ") + "CURSOS".ljust(35, " ") + "SECCION".ljust(35, " ") + "PUNTEOS".ljust(35," "))
    valor=1
    contador=1
    for estudiante in tabla:
        contador= contador +1
        if dato == estudiante:
            encontrado=1
            print("")
            print("\t\t\t", estudiante.ljust(15, " "), end="")
            for x in range(4):
                print(tabla[estudiante][x].ljust(35, " "), end="")
        else:
            valor= valor+1
    if contador==valor:
        print("")
        print("NO SE ENCONTRO NINGUN ALUMNO")
def Ingresar(carnet, nombre, curso, seccion, punteo):
            dicc = {carnet: [nombre, curso, seccion, punteo]}
            tabla.update(dicc)
def imprimir():
    clear()
    print("\t\t\t|----------------------------------------------|")
    print("\t\t\t|      MENU DE VISUALIZACION DE ALUMNOS        |")
    print("\t\t\t|----------------------------------------------|")
    print("\t\t\t"+"CARNET".ljust(20," ") + "NOMBRES".ljust(35," " ) + "CURSOS".ljust(35," " ) + "SECCION".ljust(35," " ) + "PUNTEOS".ljust(35," " ))
    for estudiante in tabla:
        print("")
        print("\t\t\t",estudiante.ljust(15," "), end="")
        for x in range(4):
            print(tabla[estudiante][x].ljust(35," "), end="")
def menu():
    clear()
    print("")
    print("CREADORES EDWIN ENRIQUE BARRERA CASTILLO, BRYAN ALEXANDER MORENO SARMIENTO, FERNANDO JOSE BARRERA LEON")
    print("\t\t\t|----------------------------------------------|")
    print("\t\t\t|      MENU SOBRE UN SISTEMA ESTUDIANTIL       |")
    print("\t\t\t|----------------------------------------------|")
    print("\t\t\t\t1) INGRESAR DATOS DE UN ALUMNO")
    print("\t\t\t\t2) VISUALIZAR LOS DATOS INGRSADOS")
    print("\t\t\t\t3) REALIZAR BUSQUEDA DE ESTUDIANTE")
    print("\t\t\t\t4) SALIDA DEL MENU")

tabla = {} ; dicc = {}
op = "1"
while str(op) != "4":
    menu()
    op=str(input("\t\t\t\t\tINGRESE UNA OPCION: "))
    if(str(op)=="1"):
        clear()
        print("\t\t\t|----------------------------------------------|")
        print("\t\t\t|         MENU PARA INGRESO DE ALUMNOS         |")
        print("\t\t\t|----------------------------------------------|")
        carnet = (input("\t\t\t\tINSERTE SU CARNE: "))
        nombre = (input("\t\t\t\tINSERTE SU NOMBRE: "))
        curso = (input("\t\t\t\tINSERTE SU CURSO: "))
        seccion = (input("\t\t\t\tINSERTE SU SECCION: "))
        punteo = (input("\t\t\t\tINSERTE SU PUNTEO: "))
        Ingresar(carnet, nombre, curso, seccion, punteo)
    elif (str(op)=="2"):
        imprimir()
        print("\t\t\t\t\t", end="")
        os.system("pause")
    elif (str(op)=="3"):
        busqueda()
        print("\t\t\t\t\t", end="")
        os.system("pause")
    elif (str(op)=="4"):
        print("")
        print("\t\t\t\t\tGRACIAS POR UTILIZAR EL PROGRAMA")
        print("\t\t\t\t\t", end="")
        os.system("pause")
    else:
        print("\t\t\t\t\tPOR FAVOR INGRESE UN VALOR CORRECTO")
        print("\t\t\t\t\t",end="")
        os.system("pause")



