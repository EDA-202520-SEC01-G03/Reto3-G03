import time
import os
import csv
from datetime import datetime

from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sll
from DataStructures.Tree import red_black_tree as rbt

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
    
    catalog["vuelos"] = lt.quick_sort(catalog["vuelos"], sort_crit_fecha)
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
    pass

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


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


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
