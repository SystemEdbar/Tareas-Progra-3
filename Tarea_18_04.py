import os
tabla = {} ; dicc = {}; op = "0"
def clear(): #ES COMO Si FUERA UN COMANDO
    print(" " * 25000000)
def pause(): #ES COMO SI FUERA UN COMANDO
    print("\t\t\t\t\t", end="")
    os.system("pause")
def imprimir_busqueda(): #METODO DE IMPRESION Y VERIFICACION DE BUSQUEDA
    def imprimir(): #METODO DE IMPRESION
        print(""); print("\t\t\t", estudiante.ljust(20, " "), end="")
        for x in range(4):
            print(tabla[estudiante][x].ljust(35, " "), end="")
    print("\t\t\t" + "CARNET".ljust(20, " ") + "NOMBRES".ljust(35, " ") + "CURSOS".ljust(35, " ") + "SECCION".ljust(35, " ") + "PUNTEOS".ljust(35," "))
    valor=1
    contador=1
    for estudiante in tabla:
        contador= contador +1
        if dato == "TODOS":
            imprimir()
        elif dato == estudiante:
            encontrado=1; imprimir()
        else:
            valor= valor+1
    if contador==valor:
        print(""); print("\t\t\tNO SE ENCONTRO NINGUN ALUMNO")
def menu():
    print("\t\t\tCREADORES EDWIN ENRIQUE BARRERA CASTILLO, BRYAN ALEXANDER MORENO SARMIENTO, FERNANDO JOSE BARRERA LEON")
    encabezado(op)
    print("\t\t\t\t1) INGRESAR DATOS DE UN ALUMNO")
    print("\t\t\t\t2) VISUALIZAR LOS DATOS INGRSADOS")
    print("\t\t\t\t3) REALIZAR BUSQUEDA DE ESTUDIANTE")
    print("\t\t\t\t4) SALIDA DEL MENU")
def encabezado(op):#ENCABEZADO PARA MENU Y OPCIONES
    opciones = ("MENU SOBRE UN SISTEMA ESTUDIANTIL", "   MENU PARA INGRESO DE ALUMNOS  ", "MENU DE VISUALIZACION DE ALUMNOS ","MENU DE BUSQUEDA SOBRE UN ALUMNO ")
    print("\t\t\t|----------------------------------------------|")
    print("\t\t\t|      " , opciones[int(op)] , "     |")
    print("\t\t\t|----------------------------------------------|")
def ingresar(): #METODO DE INGRESAR DATOS
    carnet = (input("\t\t\t\tINSERTE SU CARNE: "))
    nombre = (input("\t\t\t\tINSERTE SU NOMBRE: "))
    curso = (input("\t\t\t\tINSERTE SU CURSO: "))
    seccion = (input("\t\t\t\tINSERTE SU SECCION: "))
    punteo = (input("\t\t\t\tINSERTE SU PUNTEO: "))
    dicc = {carnet: [nombre, curso, seccion, punteo]}#PRIMERO SE CREA UN DICCIONARIO TEMPORAL PARA ACTUALIZAR EL PRINCIPAL
    tabla.update(dicc) #SI EL ALUMNO ESTA INGRESADO EL DICCIONARIO NO LO ALMACENA Y TAMPOCO LO MODIFICA
while str(op) != "4":
    clear()
    op = "0" #SE DECLARA NUEVAMENTE POR LAS OPCIONES DE ENCABEZADO
    menu()
    op=str(input("\t\t\t\t\tINGRESE UNA OPCION: ")) #MENU DE OPCIONES
    if(str(op)=="1"):
        clear(); encabezado(op); ingresar()
    elif (str(op)=="2"):
        clear(); encabezado(op); dato="TODOS"; imprimir_busqueda(); pause()
    elif (str(op)=="3"):
        clear(); encabezado(op); dato = input("\t\t\tINGRESE EL NUMERO DE CARNET: "); imprimir_busqueda(); pause()
    elif (str(op)=="4"):
        print(""); print("\t\t\t\t\tGRACIAS POR UTILIZAR EL PROGRAMA"); pause()
    else:
        print("\t\t\t\t\tPOR FAVOR INGRESE UN VALOR CORRECTO"); pause()



