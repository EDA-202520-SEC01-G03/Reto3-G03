
from DataStructures.Map import map_functions as mp
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as arr
import random as r




def new_map(num_keys, load_factor, prime = 109345121):
    

    capacity = mp.next_prime(num_keys // load_factor)
    scale = r.randint(1, prime- 1)
    shift = r.randint(0, prime- 1)
    hash_table = {'prime': prime,
                    'capacity': capacity,
                    'scale': 1, 
                    'shift': 0,
                    'table': arr.new_list(),
                    'current_factor': 0,
                    'limit_factor': load_factor,
                    'size': 0,
                    'type': 'PROBE_HASH_MAP'}
        
    for i in range(capacity):
            
        entry = me.new_map_entry(None, None)
        arr.add_last(hash_table['table'], entry)
            
    return hash_table

        
#Funciones auxiliares
#Default compare        
def default_compare(key, entry):
    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1

#Is_ available
def is_available( table, pos):
    entry= arr.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry)== "__EMPTY__":
        return True
    return False

#Find_slot
def find_slot( my_map, key, hash_value):
    first_avail= None
    found= False
    ocupied = False
    while not found:
        if is_available(my_map["table"], hash_value):
            if first_avail is None:
                first_avail= hash_value
            entry = arr.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
                found= True
        elif default_compare (key, arr.get_element(my_map["table"],hash_value))==0:
            first_avail= hash_value
            found= True
            ocupied= True
        hash_value= (hash_value+ 1)% my_map["capacity"]
    return ocupied, first_avail

#Contains
def contains( my_map, key):
    hash= mp.hash_value(my_map, key)
    found, _ = find_slot(my_map, key, hash)
    return found

#Is empty
def is_empty(my_map):
    if my_map["size"]== 0:
        return True
    else:
        return False
    
#Key set
def key_set(my_map):
    llaves= arr.new_list()
    for entry in my_map["table"]["elements"]:
        llave= me.get_key(entry)
        if llave is not None and llave != "__EMPTY__":
            arr.add_last(llaves, llave)
    return llaves

#Value set
def value_set(my_map):
    valores= arr.new_list()
    for entry in my_map["table"]["elements"]:
        valor= me.get_value(entry)
        if valor is not None and valor != "__EMPTY__":
            arr.add_last(valores, valor)
    return valores


#Size 
def size(my_map):
    return my_map["size"]



def rehash(map):
    
    nueva_capacidad = mp.next_prime(map["capacity"] *2)
    map["capacity"] = nueva_capacidad
    map_table = map["table"]
    lista = arr.new_list()
    size = 0
    
    for i in range(nueva_capacidad): #se crea entradas y se añaden a una lista vacia 
        
        entry = me.new_map_entry(None, None)
        arr.add_last(lista, entry)
    
    
    for dict in map_table["elements"]: 
        print(dict)
        key = me.get_key(dict)
        
        if (key != None) and (key != "__EMPTY__"):

            l_hash = mp.hash_value(map, key)
            arr.change_info(lista, l_hash, dict)
            
    
    
    #entradas new map son vacias 
    map["table"] = lista
    map["current_factor"] = map["size"] / map["limit_factor"]
    
    return map

def remove (my_map, key):
    
    hash = mp.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash)
    if found:
        my_map["table"]["elements"][pos]["key"]= "__EMPTY__"
        my_map["table"]["elements"][pos]["value"]= "__EMPTY__"
        my_map["size"] -= 1
        
        total= my_map["capacity"]
        my_map["current_factor"] = my_map["size"]/ total
    return my_map    
        
def put(mapa, key, value):
    l_hash = mp.hash_value(mapa, key)  # índice de la llave
    info = find_slot(mapa, key, l_hash)  # (ocupied, index)

    if info[0] == False:
        new = me.new_map_entry(key, value)
        arr.change_info(mapa["table"], info[1], new)
        mapa["size"] += 1
    elif info[0] == True:
        entry = me.set_value(arr.get_element(mapa["table"], info[1]), value)
        arr.change_info(mapa["table"], info[1], entry)

    mapa["current_factor"] = mapa["size"] / mapa["capacity"]
    if mapa["current_factor"] > mapa["limit_factor"]:
        rehash(mapa)

    return mapa

    return mapa

def get(map, key):
    
    l_hash = mp.hash_value(map, key)
    info = find_slot(map, key, l_hash)
    
    if info[0] == False:
        return None
    else:
        return me.get_value(map["table"]["elements"][info[1]])
            
    
       