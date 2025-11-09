import time
import os
import csv
from datetime import datetime

from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sll
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Tree import binary_search_tree as bst

csv.field_size_limit(2147483647)
data_dir = os.path.dirname(os.path.realpath("__file__")) + "/Data/"

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {"vuelos": None,
               "vuelos_minutos_retraso": None,
               "vuelos_minutos_anticipo": None}

    catalog["vuelos"] = lt.new_list()
    catalog["vuelos_minutos_retraso"] = rbt.new_map() #req1
    catalog["vuelos_minutos_anticipo"] = rbt.new_map() #req2
    
    return catalog

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    vuelos = load_vuelos(catalog, filename)
    vuelos_minutos_retraso = load_vuelos_retraso(catalog, filename)
    vuelos_minutos_anticipo = load_vuelos_anticipo(catalog, filename)
    
    return vuelos, vuelos_minutos_retraso, vuelos_minutos_anticipo

def load_vuelos(catalog, filename):
    vuelosfile = data_dir + "Challenge-3/" + filename
    input_file = csv.DictReader(open(vuelosfile, encoding="utf-8"))
    for vuelo in input_file:
        add_vuelo(catalog, vuelo)
    
    catalog["vuelos"] = lt.merge_sort(catalog["vuelos"], sort_crit_fecha)
    return size_load_vuelos(catalog)

def sort_crit_fecha(vuelo1, vuelo2):
    
    is_sorted = False
    formato = "%Y-%m-%d %H:%M"
    date1 = str(vuelo1["date"]) + " " + str(vuelo1["sched_dep_time"])
    date2 = str(vuelo2["date"]) + " " + str(vuelo2["sched_dep_time"])
    
    fecha1 = datetime.strptime(date1, formato)
    fecha2 = datetime.strptime(date2, formato)
    
    if fecha1 < fecha2:
        is_sorted = True
    
    return is_sorted

#add_vuelo
def add_vuelo(catalog, vuelo):
    
    vuel = new_vuelo(vuelo["id"], vuelo["date"], vuelo["dep_time"], vuelo["sched_dep_time"],
                     vuelo["arr_time"], vuelo["sched_arr_time"], vuelo["carrier"],
                     vuelo["flight"], vuelo["tailnum"], vuelo["origin"], vuelo["dest"],
                     vuelo["air_time"],vuelo["distance"], vuelo["name"])
    lt.add_last(catalog["vuelos"], vuel)

    return catalog

#new_vuelo
def new_vuelo(id, date, dep_time, sched_dep_time, arr_time, sched_arr_time, carrier, flight,
              tailnum, origin, dest, air_name, distance, name):
    
    new_vuelo = {"id": id, "date": date, "dep_time": dep_time, "sched_dep_time": sched_dep_time,
                 "arr_time": arr_time, "sched_arr_time": sched_arr_time, "carrier": carrier,
                    "flight": flight, "tailnum": tailnum, "origin": origin, "dest": dest,
                    "air_time": air_name, "distance": distance, "name": name}
    
    return new_vuelo

#size_vuelos
def size_load_vuelos(catalog):
    #vuelos en total cargados
    return lt.size(catalog["vuelos"])

def load_vuelos_retraso(catalog, filename):
    vuelosfile = "data/Challenge-3/" + filename
    input_file = csv.DictReader(open(vuelosfile, encoding="utf-8"))

    rbt_tree = catalog["vuelos_minutos_retraso"]

    for vuelo in input_file:
        retraso = calcular_retraso(vuelo["dep_time"], vuelo["sched_dep_time"])

        if retraso > 0:
            vuelo_dict = new_vuelo(
                vuelo["id"], vuelo["date"], vuelo["dep_time"], vuelo["sched_dep_time"],
                vuelo["arr_time"], vuelo["sched_arr_time"], vuelo["carrier"],
                vuelo["flight"], vuelo["tailnum"], vuelo["origin"], vuelo["dest"],
                vuelo["air_time"], vuelo["distance"], vuelo["name"]
            )

            lista = rbt.get(rbt_tree, retraso)

            if lista is None:
                lista = lt.new_list()

            lt.add_last(lista, vuelo_dict)
            rbt.put(rbt_tree, retraso, lista)

    return rbt.size(rbt_tree)
def load_vuelos_anticipo(catalog, filename):
    pass

def cinco_primeros_ultimos(catalog):
    
    vuelos = catalog["vuelos"]
    resultado1 = sll.new_list()
    resultado2 = sll.new_list()
    
    longitud = lt.size(vuelos)
    
    for i in range(0, 5):
        
        vuelo = lt.get_element(vuelos, i)
        vuelo = dic_vuelo(vuelo)
        sll.add_last(resultado1, vuelo)
    
    for x in range(longitud - 5, longitud):
        
        vuelo = lt.get_element(vuelos, x)
        vuelo = dic_vuelo(vuelo)
        sll.add_last(resultado2, vuelo)
        
    return resultado1, resultado2

def dic_vuelo(vuelo):
    
    res = {"date": vuelo["date"],
           "dep_time": vuelo["dep_time"],
           "arr_time": vuelo["arr_time"],
           "code_name": str(vuelo["carrier"]) + "-" + str(vuelo["name"]),
           "id": vuelo["id"],
           "origin": vuelo["origin"],
           "dest": vuelo["dest"],
           "air_time": vuelo["air_time"],
           "distance": vuelo["distance"]}
    
    return res
    
# Funciones de consulta sobre el catálogo


def req_1(catalog, codigo_aerolinea, rango):
    start = get_time()
    vuelos_rbt = catalog["vuelos_minutos_retraso"]
    vuelos_filtrados = lt.new_list()

    retrasos = rbt.keys(vuelos_rbt, rango[0], rango[1])
    for i in range(lt.size(retrasos)):
        retraso = lt.get_element(retrasos, i)
        lista_vuelos = rbt.get(vuelos_rbt, retraso)

        for j in range(lt.size(lista_vuelos)):
            vuelo = lt.get_element(lista_vuelos, j)
            if vuelo.get("carrier") == codigo_aerolinea:
                vuelo_filtrado = {
                    "id": vuelo["id"],
                    "flight": vuelo["flight"],
                    "date": vuelo["date"],
                    "name": vuelo["name"],
                    "carrier": vuelo["carrier"],
                    "origin": vuelo["origin"],
                    "dest": vuelo["dest"],
                    "retraso": retraso,
                    "dep_time": vuelo["dep_time"]
                }
                lt.add_last(vuelos_filtrados, vuelo_filtrado)

    vuelos_ordenados = ordenar_vuelos_fecha_retraso(vuelos_filtrados)
    total = lt.size(vuelos_ordenados)
    end = get_time()
    tiempo = delta_time(start, end)

    primeros = lt.sub_list(vuelos_ordenados, 0, min(5, total))
    ultimos_inicio = max(0, total - 5)
    ultimos = lt.sub_list(vuelos_ordenados, ultimos_inicio, total - ultimos_inicio)

    return {
        "tiempo": tiempo,
        "total": total,
        "primeros": primeros,
        "ultimos": ultimos
    }

#Funciones auxiliares requerimiento 1
def calcular_retraso(dep_time, sched_dep_time):
    formato = "%H:%M"
    real = datetime.strptime(dep_time, formato)
    sched = datetime.strptime(sched_dep_time, formato)

    minutos_retraso = (real - sched).total_seconds() / 60
    if minutos_retraso < -720:
        minutos_retraso += 1440
    elif minutos_retraso > 720:
        minutos_retraso -= 1440

    return int(minutos_retraso)

def sort_crit_fecha_real(v1, v2):
    formato = "%Y-%m-%d %H:%M"
    f1 = datetime.strptime(v1["date"] + " " + v1["dep_time"], formato)
    f2 = datetime.strptime(v2["date"] + " " + v2["dep_time"], formato)
    return f1 < f2

def sort_crit_retraso_fecha(v1, v2):
    if v1["retraso"] < v2["retraso"]:
        return True
    elif v1["retraso"] > v2["retraso"]:
        return False
    else:
        return sort_crit_fecha_real(v1, v2)

def ordenar_vuelos_fecha_retraso(lista_vuelos):
    return lt.merge_sort(lista_vuelos, sort_crit_retraso_fecha)


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
