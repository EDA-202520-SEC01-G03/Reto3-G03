import sys
from tabulate import tabulate
from App import logic as l
from datetime import datetime
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
    vuelos, vuelos_minutos_retraso, vuelos_minutos_anticipo, vuelos_req_4, vuelos_index_req_5, vuelos_index_req_6 = l.load_data(control,"flights_large.csv")
    print("Número de vuelos cargados: " + str(vuelos) + "\n")

def print_load_data(control):
    inicio = l.get_time()
    resultado1, resultado2 = l.cinco_primeros_ultimos(control)
    
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
        
    final = l.get_time()
    tiempo = l.delta_time(inicio, final)
    print("Tiempo de carga: " + str(tiempo))
    
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

def print_req_2(control, codigo_aero, rango):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    tiempo, longitud, resultado = l.req_2(control, codigo_aero, rango)

    if resultado is not None:
        
        headers = ["ID", "Código del vuelo", "Fecha", "Aerolínea", "Código de la aero", "origen", "dest", "minutos anticipo"]
        if longitud > 10:
            
            print("Tiempo de carga: " + str(tiempo))
            print("Número total de vuelos que cumplen con el filtro del aeropuerto y del rango de anticipo: " + str(longitud))
            
            
            tabla1 = []
            tabla2 = []
            
            for x in range(0, 5):
                
                
                vuelo = lt.get_element(resultado, x)
                fila = [ vuelo["id"], vuelo["flight"], vuelo["date"], vuelo["name"], vuelo["carrier"], vuelo["origin"], vuelo["dest"], 
                        vuelo["min_anticipo"]]
                
                tabla1.append(fila)
                
            for y in range(longitud - 5 , longitud):
                
                vuelo = lt.get_element(resultado, y)
                fila = [ vuelo["id"], vuelo["flight"], vuelo["date"], vuelo["name"], vuelo["carrier"], vuelo["origin"], vuelo["dest"], 
                        vuelo["min_anticipo"]]
                
                tabla2.append(fila)
                
            print("Primeros cinco vuelos: \n")
            print(tabulate(tabla1, headers = headers, tablefmt = "grid"))
    
            print("Últimos cinco vuelos: \n")
            print(tabulate(tabla2, headers = headers, tablefmt = "grid"))
        
        else:
            tabla = []
            
            
            for x in range(longitud):
                
                vuelo = lt.get_element(resultado, x)
                
                fila = [ vuelo["id"], vuelo["flight"], vuelo["date"], vuelo["name"], vuelo["carrier"], vuelo["origin"], vuelo["dest"], 
                        vuelo["min_anticipo"]]
                
                tabla.append(fila)
            print("Los vuelos son: \n")
            print(tabulate(tabla, headers = headers, tablefmt = "grid"))
                
    else:
        print("No se encontraron vuelos dentro del rango o código aerolinea especificado.")

def print_req_4(control, rango, franja, N):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    tiempo, aerolineas = l.req_4(control, rango, franja)

    print("Tiempo de ejecución (ms): " + str(tiempo))
    print("Total de aerolíneas consideradas: " + str(N))
    
    longitud = lt.size(aerolineas)
    if longitud > 0:
        headers = ["Codigo aero", "Total vuelos", "Duración Promedio", "Distancia Promedio"]
        headers2 = ["ID", "Código", "Fecha-Hora programada de salida", "Origen", "Destino", "Duración"]
        
        tabla1 = []
        tabla2 = []
        for x in range(0, N):
            
            aerolinea = lt.get_element(aerolineas, x)
            vuelo = aerolinea["menor_duracion"]["info"]
            
            fila1 = [aerolinea["carrier"], aerolinea["numero_vuelos"], round(float(aerolinea["duración"] / aerolinea["numero_vuelos"]),2),
                    round(float(aerolinea["distancia"] / aerolinea["numero_vuelos"]),2) ]

            fila2 = [vuelo["id"], vuelo["flight"], str(vuelo["date"]) + " " + str(vuelo["sched_dep_time"]), vuelo["origin"], vuelo["dest"], vuelo["air_time"]]
            
            tabla1.append(fila1)
            tabla2.append(fila2)
    
        print("Requerimiento 4 información: \n")
        print(tabulate(tabla1, headers = headers, tablefmt = "grid"))
    
        print("Información de los vuelos con la menor duración:\n")
        print(tabulate(tabla2, headers = headers2, tablefmt = "grid"))
    
    
    
def print_req_5(control):
    print("\n Requerimiento 5: Aerolíneas más puntuales por destino y rango de fechas\n")

    destino = input("Ingrese el código del aeropuerto de destino (ej: JFK): ").strip().upper()
    fecha_inicio = input("Ingrese la fecha inicial (YYYY-MM-DD): ").strip()
    fecha_final = input("Ingrese la fecha final (YYYY-MM-DD): ").strip()
    n = int(input("Ingrese la cantidad N de aerolíneas más puntuales: "))

    resultado = l.req_5(control, destino, [fecha_inicio, fecha_final], n)

    print("\n Resultados generales del requerimiento 5:")
    resumen = [
        ["Tiempo de ejecución (ms)", resultado["tiempo"]],
        ["Total de aerolíneas consideradas", resultado["total_aerolineas"]]
    ]
    print(tabulate(resumen, headers=["Descripción", "Valor"], tablefmt="grid"))

    print("\n Aerolíneas más puntuales:")
    tabla = formato_tabla_req5(resultado["aerolineas"])
    headers = [
        "Código",
        "Total",
        "Puntualidad",
        "Duración",
        "Distancia",
        "ID Vuelo Largo",
        "Código Vuelo",
        "Fecha-Hora Llegada",
        "Origen",
        "Destino",
        "Duración Vuelo"
    ]
    print(tabulate(tabla, headers=headers, tablefmt="grid"))

def formato_tabla_req5(lista_aerolineas):
    tabla = []
    tam = lt.size(lista_aerolineas)
    i = 0

    while i < tam:
        aerolinea = lt.get_element(lista_aerolineas, i)
        vuelo = aerolinea["vuelo_max"]

        fila = [
            aerolinea["carrier"],
            aerolinea["total_vuelos"],
            aerolinea["prom_puntualidad"],
            aerolinea["prom_duracion"],
            aerolinea["prom_distancia"],
            vuelo["id"],
            vuelo["flight"],
            vuelo["fecha_llegada"],
            vuelo["origen"],
            vuelo["destino"],
            vuelo["duracion"]
        ]
        tabla.append(fila)
        i = i + 1

    return tabla

def print_req_6(control):
    print("\n Requerimiento 6: Aerolíneas más estables en su hora de salida\n")

    fecha_inicio = input("Ingrese la fecha inicial (YYYY-MM-DD): ").strip()
    fecha_final = input("Ingrese la fecha final (YYYY-MM-DD): ").strip()
    min_dist = float(input("Ingrese la distancia mínima (en millas): "))
    max_dist = float(input("Ingrese la distancia máxima (en millas): "))
    m = int(input("Ingrese la cantidad M de aerolíneas más estables: "))

    resultado = l.req_6(control, [fecha_inicio, fecha_final], [min_dist, max_dist], m)

    print("\n Resultados generales del requerimiento 6:")
    resumen = [
        ["Tiempo de ejecución (ms)", resultado["tiempo"]],
        ["Total de aerolíneas analizadas", resultado["total_aerolineas"]]
    ]
    print(tabulate(resumen, headers=["Descripción", "Valor"], tablefmt="grid"))

    print("\n Aerolíneas más estables:")
    tabla = formato_tabla_req6(resultado["aerolineas"])
    headers = [
        "Código",
        "Total",
        "Prom. Retraso",
        "Desviación Std",
        "ID Vuelo",
        "Cod Vuelo",
        "Fecha-Hora Salida",
        "Origen",
        "Destino"
    ]
    print(tabulate(tabla, headers=headers, tablefmt="grid"))
def formato_tabla_req6(lista_aerolineas):
    tabla = []
    tam = lt.size(lista_aerolineas)
    i = 0

    while i < tam:
        aerolinea = lt.get_element(lista_aerolineas, i)
        vuelo = aerolinea["vuelo_cercano"]

        fila = [
            aerolinea["carrier"],
            aerolinea["total_vuelos"],
            aerolinea["prom_retraso"],
            aerolinea["desviacion"],
            vuelo["id"],
            vuelo["flight"],
            vuelo["fecha_salida"],
            vuelo["origen"],
            vuelo["destino"]
        ]
        tabla.append(fila)
        i += 1

    return tabla
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
            codigo_aero = input("ingrese el código del aeropuerto de destino a analizar\n")
            print("Ahora, ingrese el rango de minutos:\n")
            
            ran = int(input("Desde:\n"))
            go = int(input("Hasta:\n"))
            
            rango = ran,go
            print_req_2(control, codigo_aero, rango)

        elif int(inputs) == 4:
            print("ingrese el rango de fechas\n")
            ran = str(input("Desde:\n"))
            go = str(input("Hasta:\n"))
            
            ran = datetime.strptime(ran, "%Y-%m-%d")
            go = datetime.strptime(go, "%Y-%m-%d")
            
            rango = ran,go
            
            print("Ahora, ingrese la franja horario programada de vuelos de salida\n")
            
            fran = str(input("Desde:\n"))
            ja = str(input("Hasta:\n"))
            
            fran = datetime.strptime(fran, "%H:%M")
            ja = datetime.strptime(ja, "%H:%M")
            
            franja = fran,ja
            
            n = int(input("Ingrese la cantidad de aerolíneas con mayor número de vuelos a mostrar:\n"))
            print_req_4(control, rango, franja, n)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
