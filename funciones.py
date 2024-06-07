import json

def cargar_archivo(archivo):
    """
    Carga un archivo JSON y devuelve una lista de servicios.
    Recibe como parametro el nombre del archivo
    Retorna la lista de serv
    """
    try:
        with open(archivo, 'r') as archivo:
            lista_servicios = json.load(archivo)
        return lista_servicios
    except FileNotFoundError:
        print(f"Hubo un error: El archivo {archivo} no existe.")
        return False

def imprimir_lista(lista):
    """
    Recibe como parametro la lista de servicios ya leida anteriormente
    Muestra por pantalla la tabla
    """
    print(f"{'id':<4}{'descripcion':<20}{'tipo':<10}{'precio_unitario':<15}{'cantidad':<10}{'total':<10}")
    for i in lista:
        total = i.get('servicio', False)
        print(f"{i['id_servicio']:<4}{i['descripcion']:<20}{i['tipo']:<10}{i['precioUnitario']:<15}{i['cantidad']:<10}{i['totalServicio']:<10}")

def asignar_totales(lista):
    """
    Usamos lambda para asignar el total calculado que esta en 0
    Recibe como parametro la lista de servicios ya leida
    Retorna los totales en formato lista
    """
    calcular = lambda x: int(x['cantidad']) * float(x['precioUnitario'])
    for i in lista:
        i['totalServicio'] = calcular(i)
    return lista

def filtrar_por_tipo(lista_servicios, tipo):
    """
    guarda el resultado en un nuevo archivo json y los guarda segun el filtro(que es un numero valido)
    """
    filtro = []
    for i in lista_servicios:
        if i['tipo'] == tipo:
            filtro.append(i)
    
    if filtro:
        nombre_archivo = f"filtrar_{tipo}.json"
        try:
            with open(nombre_archivo, 'w') as archivo:
                json.dump(filtro, archivo)
            print(f"Archivo {nombre_archivo} creado correctamente.")
        except ValueError:
            print(f"Error al crear el archivo filtrado")
    else:
        print(f"No se encontraron servicios del tipo {tipo}.")


def mostrar_servicios(lista_servicios):
    """
    Ordena con el metodo sorted con una funcion lambda dentro
    retorna esa misma lista ordenada
    """
    lista_ordenada = sorted(lista_servicios, key=lambda x: x['descripcion'])
    return lista_ordenada
def guardar_servicios(lista_servicios):
    """
    Guardara em un archivo json los datos guardados de la lista recibida anteriormente
    Reutilizo la funcion mostrar_servicios para el ordenamiento
    """
    calcular = mostrar_servicios(lista_servicios)
    nombre_archivo = "ordenados.json"
    try:
        with open(nombre_archivo, 'w') as archivo:
            json.dump(calcular, archivo)
    except Exception as e:
        print(f"Error al guardar el archivo json {nombre_archivo}")

#FUNCIONES PARA MENU DE OPCIONES

def menu_opciones():
    """
    Retorna las opciones de menu
    """
    menu = print("1. Cargar archivo \n2. Imprimir lista \n3. Asignar totales. \n4. Filtrar por tipo \n5. Mostrar servicios \n6. Guardar servicios \n7. Salir del programa")
    return menu
  
