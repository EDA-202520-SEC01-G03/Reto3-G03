import sys
from tabulate import tabulate
from App import logic as l
import time
from DataStructures.List import single_linked_list as sll
from DataStructures.List import array_list as lt

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    control = l.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    vuelos, vuelos_minutos_retraso, vuelos_minutos_anticipo = l.load_data(control,"flights_test.csv")
    print("Número de vuelos cargados: " + str(vuelos) + "\n")

def print_load_data(control):
    inicio = l.get_time()
    resultado1, resultado2 = l.cinco_primeros_ultimos(control)
    final = l.get_time()
    
    tiempo = l.delta_time(inicio, final)
    
    print("Tiempo de carga: " + str(tiempo))
    tabla1 = []
    for i in range(sll.size(resultado1)):
        vuelo = sll.get_element(resultado1, i)
        fila = [
            vuelo["date"],
            vuelo["dep_time"],
            vuelo["arr_time"],
            vuelo["code_name"],
            vuelo["id"],
            vuelo["origin"],
            vuelo["dest"],
            vuelo["air_time"],
            vuelo["distance"]
        ]
        
        tabla1.append(fila)
        
    tabla2 = []
    for i in range(sll.size(resultado2)):
        vuelo = sll.get_element(resultado2, i)
        fila = [
            vuelo["date"],
            vuelo["dep_time"],
            vuelo["arr_time"],
            vuelo["code_name"],
            vuelo["id"],
            vuelo["origin"],
            vuelo["dest"],
            vuelo["air_time"],
            vuelo["distance"]
        ]
        
        tabla2.append(fila)
        
    headers = [
        "Fecha",
        "hora salida", "hora llegada",
        "aerolinea",
        "id",
        "origen",
        "destino",
        "duración [min]",
        "distancia [mi]"
    ]
    
    print("Primeros cinco vuelos: \n")
    print(tabulate(tabla1, headers = headers, tablefmt = "grid"))
    
    print("Últimos cinco vuelos: \n")
    print(tabulate(tabla2, headers = headers, tablefmt = "grid"))
        

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass
    

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    codigo= input("Ingrese el código de la aerolínea (ej: UA): ").strip().upper()
    min_retraso= int(input("Ingrese el mínimo de minutos de retraso: "))
    max_retraso= int(input("Ingrese el máximo de minutos de retraso: "))
    rango= [min_retraso, max_retraso]
    
    resultado= l.req_1(control, codigo, rango)
    
    print("\n Resultados generales Requerimiento 1:")
    resumen= [
        ["Tiempo de ejecución (ms)", resultado["tiempo"]],
        ["Total de vuelos encontrados", resultado["total"]]
        
    ]
    print(tabulate(resumen, headers=["Descripción", "Valor"], tablefmt="grid"))
    
    print("\n Primeros 5 vuelos:")
    tabla_primeros= formato_tabla_req1(resultado["primeros"])
    print(tabulate(tabla_primeros, headers=["ID", "Código", "Fecha", "Aerolínea", "Carrier", "Origen", "Destino", "Retraso"],
                     tablefmt="grid"))
    
    print("\n Últimos 5 vuelos:")
    tabla_ultimos= formato_tabla_req1(resultado["ultimos"])
    print(tabulate(tabla_ultimos, headers=["ID", "Código", "Fecha", "Aerolínea", "Carrier", "Origen", "Destino", "Retraso"],
                    tablefmt="grid"))
    
#Funcion auxiliar print req 1
def formato_tabla_req1(lista_vuelos):
    tabla=[]
    tam= lt.size(lista_vuelos)
    for i in range(tam):
        vuelo= lt.get_element(lista_vuelos, i)
        fila=[
            vuelo["id"],
            vuelo["flight"],
            vuelo["date"],
            vuelo["name"],
            vuelo["carrier"],
            vuelo["origin"],
            vuelo["dest"],
            vuelo["retraso"]
        ]
        tabla.append(fila)
    return tabla

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            load_data(control)
            print_load_data(control)
    
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
