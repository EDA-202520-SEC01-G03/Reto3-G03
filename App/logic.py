import time
import os
import csv
from datetime import datetime

from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sll
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Priority_queue import priority_queue as pq

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
    catalog["vuelos_req_4"] = rbt.new_map() #req5
    catalog["index_req_5"] = None #req5
    catalog["index_req_6"] = None #req6
    
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
    vuelos_req_4 = load_vuelos_req_4(catalog, filename)
    vuelos_index_req_5 = load_vuelos_req_5(catalog, filename)
    vuelos_index_req_6 = load_vuelos_req_6(catalog, filename)
    
    return vuelos, vuelos_minutos_retraso, vuelos_minutos_anticipo, vuelos_req_4, vuelos_index_req_5, vuelos_index_req_6

#vuelos
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

#vuelos retraso 
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

#vuelos_anticipo
def load_vuelos_anticipo(catalog, filename):
    vuelosfile = data_dir + "Challenge-3/" + filename
    inputfile = csv.DictReader(open(vuelosfile, encoding="utf-8"))
    red_black = rbt.new_map()
    catalog["vuelos_minutos_anticipo"] = red_black
    for vuelo in inputfile:
        add_vuelo_anticipo(catalog, vuelo)
    
    return rbt.size(catalog["vuelos_minutos_anticipo"])

def add_vuelo_anticipo(catalog, vuelo):
    
    red_black = catalog["vuelos_minutos_anticipo"]
    
    minutos = calcular_minutos(vuelo["sched_arr_time"], vuelo["arr_time"])
    
    if minutos is not None:
        
        if minutos < 0:
            
            minutos = int(abs(minutos)) #minutos es int
            llave = rbt.get(red_black, minutos) #map_linear_probing o None
            vuelo_dic = dic_anticipo(vuelo, minutos)
            
            if llave is None: #si no existe en el árbol
                
                mapa = mp.new_map(15, 0.5) #se crea la tabla
                lista = lt.new_list() #se crea una lista
                
                lt.add_last(lista, vuelo_dic)
                mapa = mp.put(mapa, str(vuelo["dest"]), lista) #se pone en el mapa la lista (codigo llave)
                
                rbt.put(red_black, minutos, mapa) #se pone el mapa y los minutos en el arbol

            
            else: #si existe en el árbol
                
                info = mp.contains(llave, str(vuelo["dest"])) #si ya existe la tabla, se busca el codigo del aeropuerto destino
                
                if info: #si existe, se añade a la  lista de el vuelo
                    
                    
                    lista = mp.get(llave, str(vuelo["dest"]))
                    lt.add_last(lista, vuelo_dic)
                    mp.put(llave, str(vuelo["dest"]), lista)
                    rbt.put(red_black, minutos, llave)
                    
                else: #si no existe, se mete al mapa el nuevo codigo del aeropuerto destino
                    
                    lista = lt.new_list() #se crea una lista
                    lt.add_last(lista, vuelo_dic)
                    mapa = mp.put(llave, str(vuelo["dest"]), lista) #se pone en el mapa la lista (codigo llave)
                    rbt.put(red_black, minutos, llave)
    return catalog

#funciones auxiliares
def calcular_minutos(sarr_time, arr_time):
    
    if (sarr_time != "" or arr_time != "") or (sarr_time is not None or arr_time is not None):
        
        sarr_time = datetime.strptime(str(sarr_time), "%H:%M")
        arr_time = datetime.strptime(str(arr_time), "%H:%M")

        minutos = (arr_time - sarr_time).total_seconds() / 60

        if minutos < -720:
            minutos += 1440
        elif minutos > 720:
            minutos -= 1440

        return int(minutos)
    
    else:
        return None
    
def dic_anticipo(vuelo, minutos):
    
    vuel = {"id": vuelo["id"], "flight": vuelo["flight"], "date": vuelo["date"],
            "name": vuelo["name"],"carrier": vuelo["carrier"], "origin": vuelo["origin"], 
            "dest": vuelo["dest"], "min_anticipo": minutos, "arr_time": vuelo["arr_time"]}
    
    return vuel

#vuelos requerimiento 4

def load_vuelos_req_4(catalog, filename):
    
    vuelosfile = data_dir + "Challenge-3/" + filename
    inputfile = csv.DictReader(open(vuelosfile, encoding="utf-8"))
    red_black = rbt.new_map()
    catalog["vuelos_req_4"] = red_black
    for vuelo in inputfile:
        add_vuelo_req_4(catalog, vuelo)
    
    
    return catalog

def add_vuelo_req_4(catalog, vuelo):
    
    red_black = catalog["vuelos_req_4"]
    info0 = rbt.contains(red_black, str(vuelo["date"])) #si la fecha no existe en el arbol
    
    if info0 is False:
        
        lista = lt.new_list()
        lt.add_last(lista, vuelo)
        rbt.put(red_black, str(vuelo["date"]), lista)
        
    else:
        lista = rbt.get(red_black, str(vuelo["date"]))
        lt.add_last(lista, vuelo)
        rbt.put(red_black, str(vuelo["date"]), lista)
    
    return catalog

#funcion auxiliar
            
#vuelos requerimiento 5
def load_vuelos_req_5(catalog, filename):
    vuelosfile = "data/Challenge-3/" + filename
    input_file = csv.DictReader(open(vuelosfile, encoding="utf-8"))
    index_rbt = rbt.new_map()

    for vuelo in input_file:
        if vuelo["date"].strip() != "" and vuelo["arr_time"].strip() != "" and vuelo["sched_arr_time"].strip() != "" and vuelo["dest"].strip() != "":
            puntualidad = calcular_puntualidad(vuelo["arr_time"], vuelo["sched_arr_time"])
            vuelo_dict = new_vuelo(
                vuelo["id"], vuelo["date"], vuelo["dep_time"], vuelo["sched_dep_time"],
                vuelo["arr_time"], vuelo["sched_arr_time"], vuelo["carrier"],
                vuelo["flight"], vuelo["tailnum"], vuelo["origin"], vuelo["dest"],
                vuelo["air_time"], vuelo["distance"], vuelo["name"]
            )

            vuelo_dict["distancia"] = float(vuelo["distance"]) if vuelo["distance"] != "" else 0
            vuelo_dict["duracion"] = float(vuelo["air_time"]) if vuelo["air_time"] != "" else 0
            vuelo_dict["puntualidad"] = puntualidad

            fecha = vuelo["date"]
            aerolinea = vuelo["carrier"]

            fecha_map = rbt.get(index_rbt, fecha)
            if fecha_map is None:
                fecha_map = mp.new_map(100, 0.75)

            cola = mp.get(fecha_map, aerolinea)
            if cola is None:
                cola = pq.new_heap(is_min_pq=False)

            pq.insert(cola, vuelo_dict["distancia"], vuelo_dict)
            mp.put(fecha_map, aerolinea, cola)
            rbt.put(index_rbt, fecha, fecha_map)

    catalog["index_req_5"] = index_rbt
    return rbt.size(index_rbt)

def calcular_puntualidad(arr_time, sched_arr_time):
    formato = "%H:%M"
    real = datetime.strptime(arr_time, formato)
    sched = datetime.strptime(sched_arr_time, formato)
    minutos = (real - sched).total_seconds() / 60

    if minutos < -720:
        minutos += 1440
    elif minutos > 720:
        minutos -= 1440

    return abs(minutos)

#vuelos requerimiento 6
def load_vuelos_req_6(catalog, filename):
    vuelosfile = "data/Challenge-3/" + filename
    input_file = csv.DictReader(open(vuelosfile, encoding="utf-8"))
    index_rbt = rbt.new_map()

    for vuelo in input_file:
        if vuelo["date"].strip() != "" and vuelo["dep_time"].strip() != "" and vuelo["sched_dep_time"].strip() != "" and vuelo["distance"].strip() != "" and vuelo["carrier"].strip() != "":
            retraso = calcular_retraso_salida(vuelo["dep_time"], vuelo["sched_dep_time"])
            vuelo_dict = new_vuelo(
                vuelo["id"], vuelo["date"], vuelo["dep_time"], vuelo["sched_dep_time"],
                vuelo["arr_time"], vuelo["sched_arr_time"], vuelo["carrier"],
                vuelo["flight"], vuelo["tailnum"], vuelo["origin"], vuelo["dest"],
                vuelo["air_time"], vuelo["distance"], vuelo["name"]
            )

            vuelo_dict["retraso_salida"] = retraso
            vuelo_dict["distancia"] = float(vuelo["distance"])
            fecha = vuelo["date"]

            lista = rbt.get(index_rbt, fecha)
            if lista is None:
                lista = lt.new_list()
            lt.add_last(lista, vuelo_dict)
            rbt.put(index_rbt, fecha, lista)

    catalog["index_req_6"] = index_rbt
    return rbt.size(index_rbt)

def calcular_retraso_salida(dep_time, sched_dep_time):
    formato = "%H:%M"
    real = datetime.strptime(dep_time, formato)
    sched = datetime.strptime(sched_dep_time, formato)
    minutos = (real - sched).total_seconds() / 60

    if minutos < -720:
        minutos += 1440
    elif minutos > 720:
        minutos -= 1440

    return minutos


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


#requerimiento 2
def req_2(catalog, codigo_aero, rango): #rango es una tupla
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    inicio = get_time()
    red_black = catalog["vuelos_minutos_anticipo"]
    
    #organizar de forma ascendente el anticipo
    array_vuelos = rbt.values(red_black, int(rango[0]), int(rango[1])) #llaves = array
    resultado = lt.new_list()
    
    if array_vuelos is not None and (lt.size(array_vuelos) > 0):
        for x in range(lt.size(array_vuelos)):#o(m) número de elementos en array_vuelos
            
            mapa = lt.get_element(array_vuelos, x)
            
            if mapa is not None:
                
                lista = mp.get(mapa, str(codigo_aero))
            
                if lista is not None:
                    
                    for y in range(lt.size(lista)):
                        
                        element = lt.get_element(lista, y)
                        lt.add_last(resultado, element)
                

        resultado = lt.quick_sort(resultado, sort_crit_anticipo)
        longitud = lt.size(resultado)
        final = get_time()
        tiempo = delta_time(inicio, final)
        
        return tiempo, longitud, resultado
    
    else:
        final = get_time()
        tiempo = delta_time(inicio, final)
        return tiempo, 0, None

#función auxiliar 
def sort_crit_anticipo(vuelo1, vuelo2):
    
    is_sorted = False
    if int(vuelo1["min_anticipo"]) < int(vuelo2["min_anticipo"]):
        
        is_sorted = True
        
    elif int(vuelo1["min_anticipo"]) == int(vuelo2["min_anticipo"]):
        
        fecha1 = datetime.strptime(str(vuelo1["date"]) + " " + str(vuelo1["arr_time"]), "%Y-%m-%d %H:%M") 
        fecha2 = datetime.strptime(str(vuelo2["date"]) + " " + str(vuelo2["arr_time"]), "%Y-%m-%d %H:%M") 

        if fecha1 < fecha2:
            
            is_sorted = True
           
    return is_sorted
#requerimiento 4
def req_4(catalog, rango, franja):#rango tupla, franja1 str, franja2 str, N int
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    inicio = get_time()
    
    red_black = catalog["vuelos_req_4"]
    lista_fechas = rbt.values(red_black, str(rango[0]), str(rango[1])) #array_list
    
    
    mapa = mp.new_map(12, 0.5)
    
    for x in range(lt.size(lista_fechas)): #o(n) n = fechas en el rango
        
        fechas = lt.get_element(lista_fechas, x) #se accede al array de cada fecha
        
        for y in range(lt.size(fechas)):
            
            vuelo = lt.get_element(fechas, y)
    
            vuelo_hour = datetime.strptime(str(vuelo["sched_dep_time"]), "%H:%M")
            if franja[0] <= vuelo_hour <= franja[1]:
                
                info = mp.contains(mapa, str(vuelo["carrier"]))
                
                if info is False:
                    
                    diccionario =  {"carrier": str(vuelo["carrier"]), "numero_vuelos": 1, "duración": float(vuelo["air_time"]) ,
                        "distancia": float(vuelo["distance"]) ,"menor_duracion": {"menor": float(vuelo["air_time"]), "info": vuelo}, "vuelos": lt.new_list()}
                    lt.add_last(diccionario["vuelos"], vuelo)
                    mp.put(mapa, str(vuelo["carrier"]), diccionario)
                    
                else:
                    diccionario = mp.get(mapa, str(vuelo["carrier"]))
                    diccionario["numero_vuelos"] +=1
                    diccionario["duración"] += float(vuelo["air_time"])
                    diccionario["distancia"] += float(vuelo["distance"])
                    lt.add_last(diccionario["vuelos"], vuelo)
                    
                    if float(vuelo["air_time"]) < diccionario["menor_duracion"]["menor"]:
                        
                        diccionario["menor_duracion"] = {"menor": float(vuelo["air_time"]), "info": vuelo}
                        
                    elif float(vuelo["air_time"]) == diccionario["menor_duracion"]["menor"]:
                        
                        vuelo2 = diccionario["menor_duracion"]["info"]
                        fecha1 = datetime.strptime(str(vuelo["date"]) + " " + str(vuelo["sched_dep_time"]), "%Y-%m-%d %H:%M")
                        fecha2 = datetime.strptime(str(vuelo2["date"]) + " " + str(vuelo2["sched_dep_time"]), "%Y-%m-%d %H:%M")
                        
                        if fecha1 < fecha2:
                            
                            diccionario["menor_duracion"] = {"menor": float(vuelo["air_time"]), "info": vuelo}
                        
    aerolineas = mp.value_set(mapa) #array_list con diccionario de cada aerolinea
    aerolineas = lt.merge_sort(aerolineas, sort_crit_req4)
    
    final = get_time()
    tiempo = delta_time(inicio, final)
    return tiempo, aerolineas
        
#funciones auxiliares

def sort_crit_req4(dic1, dic2):
    
    is_sorted = False
    if int(dic1["numero_vuelos"]) > int(dic2["numero_vuelos"]):
        is_sorted = True
        
    if int(dic1["numero_vuelos"]) == int(dic2["numero_vuelos"]):
        
        if dic1["carrier"].upper() < dic2["carrier"].upper():
            is_sorted = True
    
    return is_sorted
    
    
#requerimiento 5
def req_5(catalog, destino, rango_fechas, n):
    start = get_time()
    index = catalog["index_req_5"]
    fechas = rbt.keys(index, rango_fechas[0], rango_fechas[1])
    aerolineas_map = agrupar_vuelos_por_aerolinea(index, destino, fechas)

    resumen = lt.new_list()
    aerolineas = mp.key_set(aerolineas_map)

    for i in range(lt.size(aerolineas)):
        aerolinea = lt.get_element(aerolineas, i)
        vuelos = mp.get(aerolineas_map, aerolinea)
        if vuelos is not None and lt.size(vuelos) > 0:
            resumen_aerolinea = calcular_metricas_aerolinea(aerolinea, vuelos)
            lt.add_last(resumen, resumen_aerolinea)

    resumen_ordenado = ordenar_resumen_por_puntualidad(resumen)
    top_n = lt.sub_list(resumen_ordenado, 0, min(n, lt.size(resumen_ordenado)))
    end = get_time()

    return {
        "tiempo": delta_time(start, end),
        "total_aerolineas": lt.size(top_n),
        "aerolineas": top_n
    }

def agrupar_vuelos_por_aerolinea(index, destino, fechas):
    aerolineas_map = mp.new_map(200, 0.75)

    for i in range(lt.size(fechas)):
        fecha = lt.get_element(fechas, i)
        fecha_map = rbt.get(index, fecha)

        if fecha_map is not None:
            aerolineas = mp.key_set(fecha_map)

            for j in range(lt.size(aerolineas)):
                aerolinea = lt.get_element(aerolineas, j)
                cola = mp.get(fecha_map, aerolinea)
                vuelos = cola["elements"]["elements"]
                tam_v = lt.size(cola["elements"])

                for k in range(1, tam_v):
                    entry = vuelos[k]
                    vuelo = entry["value"]

                    if vuelo["dest"] == destino:
                        lista = mp.get(aerolineas_map, aerolinea)
                        if lista is None:
                            lista = lt.new_list()
                        lt.add_last(lista, vuelo)
                        mp.put(aerolineas_map, aerolinea, lista)

    return aerolineas_map

def calcular_metricas_aerolinea(aerolinea, vuelos):
    total = lt.size(vuelos)
    suma_puntualidad = 0
    suma_duracion = 0
    suma_distancia = 0
    vuelo_max = None
    max_dist = -1

    for i in range(total):
        vuelo = lt.get_element(vuelos, i)
        suma_puntualidad += vuelo["puntualidad"]
        suma_duracion += vuelo["duracion"]
        suma_distancia += vuelo["distancia"]

        if vuelo["distancia"] > max_dist:
            max_dist = vuelo["distancia"]
            vuelo_max = vuelo

    resumen = {
        "carrier": aerolinea,
        "total_vuelos": total,
        "prom_puntualidad": round(suma_puntualidad / total, 2),
        "prom_duracion": round(suma_duracion / total, 2),
        "prom_distancia": round(suma_distancia / total, 2),
        "vuelo_max": {
            "id": vuelo_max["id"],
            "flight": vuelo_max["flight"],
            "fecha_llegada": vuelo_max["date"] + " " + vuelo_max["arr_time"],
            "origen": vuelo_max["origin"],
            "destino": vuelo_max["dest"],
            "duracion": vuelo_max["duracion"]
        }
    }

    return resumen

def criterio_orden_puntualidad(a, b):
    if a["prom_puntualidad"] < b["prom_puntualidad"]:
        return True
    if a["prom_puntualidad"] > b["prom_puntualidad"]:
        return False
    return a["carrier"] < b["carrier"]

def ordenar_resumen_por_puntualidad(resumen):
    return lt.merge_sort(resumen, criterio_orden_puntualidad)


#Requerimiento 6
def req_6(catalog, rango_fechas, rango_distancias, m):
    start = get_time()
    index = catalog["index_req_6"]
    fechas = rbt.keys(index, rango_fechas[0], rango_fechas[1])
    aerolineas_map = mp.new_map(200, 0.75)

    for i in range(lt.size(fechas)):
        fecha = lt.get_element(fechas, i)
        lista = rbt.get(index, fecha)

        for j in range(lt.size(lista)):
            vuelo = lt.get_element(lista, j)
            if rango_distancias[0] <= vuelo["distancia"] <= rango_distancias[1]:
                aerolinea = vuelo["carrier"]
                vuelos = mp.get(aerolineas_map, aerolinea)
                if vuelos is None:
                    vuelos = lt.new_list()
                lt.add_last(vuelos, vuelo)
                mp.put(aerolineas_map, aerolinea, vuelos)

    resumen = lt.new_list()
    aerolineas = mp.key_set(aerolineas_map)

    for i in range(lt.size(aerolineas)):
        aerolinea = lt.get_element(aerolineas, i)
        vuelos = mp.get(aerolineas_map, aerolinea)
        if vuelos is not None and lt.size(vuelos) > 0:
            resumen_aerolinea = calcular_metricas_estabilidad(aerolinea, vuelos)
            lt.add_last(resumen, resumen_aerolinea)

    pq_estables = pq.new_heap(is_min_pq=True)

    for i in range(lt.size(resumen)):
        r = lt.get_element(resumen, i)
        prioridad = (r["desviacion"], r["prom_retraso"])
        pq.insert(pq_estables, prioridad, r)

    top_m = lt.new_list()
    for _ in range(min(m, pq.size(pq_estables))):
        entry = pq.remove(pq_estables)
        lt.add_last(top_m, entry)

    end = get_time()
    tiempo = delta_time(start, end)
    return {
        "tiempo": tiempo,
        "total_aerolineas": lt.size(top_m),
        "aerolineas": top_m
    }
    
#Funciones auxiliares requerimiento 6    
def calcular_metricas_estabilidad(aerolinea, vuelos):
    total = lt.size(vuelos)
    suma = 0
    retrasos = []

    for i in range(total):
        vuelo = lt.get_element(vuelos, i)
        r = vuelo["retraso_salida"]
        suma += r
        retrasos.append(r)

    promedio = suma / total

    suma_cuadrados = 0
    for r in retrasos:
        diferencia = r - promedio
        suma_cuadrados += diferencia ** 2

    varianza = suma_cuadrados / total
    desviacion = round(varianza ** 0.5, 2)

    vuelo_cercano = buscar_vuelo_cercano(vuelos, promedio)

    resumen = {
        "carrier": aerolinea,
        "total_vuelos": total,
        "prom_retraso": round(promedio, 2),
        "desviacion": desviacion,
        "vuelo_cercano": {
            "id": vuelo_cercano["id"],
            "flight": vuelo_cercano["flight"],
            "fecha_salida": vuelo_cercano["date"] + " " + vuelo_cercano["dep_time"],
            "origen": vuelo_cercano["origin"],
            "destino": vuelo_cercano["dest"]
        }
    }

    return resumen

def buscar_vuelo_cercano(vuelos, promedio):
    min_dif = float("inf")
    vuelo_cercano = None

    for i in range(lt.size(vuelos)):
        vuelo = lt.get_element(vuelos, i)
        dif = abs(vuelo["retraso_salida"] - promedio)
        if dif < min_dif:
            min_dif = dif
            vuelo_cercano = vuelo

    return vuelo_cercano

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
