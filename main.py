from funciones import *
import json
import csv


def menu_principal():
    
    #INICIALIZO LA FUNCION PARA QUE NO HAYA ERRORES Y QUE ESTE SIN DECLARAR
    lista_servicios = []

    while True:
        menu_opciones()
        
        
        opcion = input("Ingrese la opcion deseada: ")

        if opcion == '1':
            lista_servicios = cargar_archivo("data.json")
            if lista_servicios:
                print("Archivo json leído correctamente.")
            else:
                print("Error al leer el archivo json.")

        #UTILIZO LA EXCEPCION UnboundLocalError parara que salte un mensaje diciendo que la variable lista servicios no se inicializo y se tiene que leer el archivo primero
        
        elif opcion == '2':
            try:
                if lista_servicios:
                    imprimir_lista(lista_servicios)
                else:
                    print("Primero debe cargar un archivo CSV.")
            except UnboundLocalError:
                print("Debes leer el archivo json para continuar")
                
        elif opcion == '3':
            try:
                if lista_servicios:
                    lista_servicios = asignar_totales(lista_servicios)
                    print("Totales asignados correctamente.")
                else:
                    print("Primero debe cargar un archivo CSV.")
            except UnboundLocalError:
                print("Debes leer el archivo json para continuar")  

        elif opcion == '4':
            try:
                if lista_servicios:
                    tipo = input("Ingrese el tipo de servicio a filtrar: Numeros del 1 al 3")
                    filtrar_por_tipo(lista_servicios, tipo)
                else:
                    print("Seleccione una opcion valida.")
            except UnboundLocalError:
                print("Debes leer el archivo json para continuar")
                
        elif opcion == '5':
            try:
                if lista_servicios:
                    print(mostrar_servicios(lista_servicios))
                else:
                    print("Primero debe cargar un archivo CSV.")
            except UnboundLocalError:
                print("Debes leer el archivo json para continuar")

        elif opcion == '6':
            try:
                if lista_servicios:
                    guardar_servicios(lista_servicios)
                    print("Listado guardado correctamente en un archivo JSON.")
                else:
                    print("Primero debe cargar un archivo CSV.")
            except UnboundLocalError:
                print("Debes leer el archivo json para continuar")
        elif opcion == '7':
            print("Gracias por usar el programa.")
            break
        else:
            print("Seleccione una opción correcta")

menu_principal()