from DataStructures.Map import map_functions as mp
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as arr
from DataStructures.List import single_linked_list as sll



#new map 
def new_map (num_elements, load_factor, prime=109245121):
    capacity= mp.next_prime(int(num_elements//load_factor))
    
    tabla= arr.new_list()
    for _ in range(capacity):
        arr.add_last(tabla, sll.new_list())
    
    nuevo_map={
        "prime": prime,
        "capacity": capacity,
        "scale": 1,
        "shift": 0,
        "table": tabla,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }
    return nuevo_map

#Funcion auxiliar
#default compare
def default_compare(key, element):
    if (key == me.get_key(element)):
        return 0
    elif (key > me.get_key(element)):
        return 1
    return -1

#contains
def contains(my_map, key):
    pos= mp.hash_value(my_map, key)
    bucket= arr.get_element(my_map["table"], pos)
    
    actual = bucket["first"]
    while actual is not None:
        entry = actual["info"]
        if default_compare(key, entry)==0:
            return True
        actual = actual["next"]
    return False

#is empty
def is_empty(my_map):
    if my_map["size"]== 0:
        return True
    else:
        return False

def size(my_map):
    return my_map["size"]

def key_set(my_map):
    llaves = arr.new_list()

    for i in range(my_map["capacity"]):
        bucket = my_map["table"]["elements"][i]
        nodo = bucket["first"]

        while nodo is not None:
            arr.add_last(llaves, nodo["info"]["key"])
            nodo = nodo["next"]

    return llaves
    
def value_set(my_map):
    valores= arr.new_list()
    for i in range(my_map["capacity"]):
        bucket= arr.get_element(my_map["table"], i)
        nodo= bucket["first"]
        
        while nodo is not None:
            arr.add_last(valores, nodo["info"]["value"])
            nodo= nodo["next"]
    return valores

#retorna False, None si no lo encuentra.
def search_key(map, key):
    
    found = False
    if contains(map, key) == False:
        return found, None, None
    else:
        l_hash = mp.hash_value(map, key)
        bucket = map["table"]["elements"][l_hash]
        i = 0
        current = bucket["first"]
        
        while current is not None:
            if current["info"]["key"] == key:
                return found, i, bucket
            current= current["next"]
            i +=1
        return True, i, bucket

def remove(map, key):
    
    found, pos, bucket = search_key(map, key)
    if found and pos is not None:
        sll.delete_element(bucket, pos)
        map["size"] -= 1
        map["current_factor"] = map["size"] / map["capacity"]
        return True
    return False


def get(map, key):
    
    l_hash = mp.hash_value(map, key)
    bucket = map["table"]["elements"][l_hash]
    current = bucket["first"]
    
    while current != None:
        
        if current["info"]["key"] == key:
            return current["info"]["value"]
        current = current["next"]
        
    return None

def put(map, key, value):
    
    info = search_key(map, key)
    l_hash = mp.hash_value(map, key)
    new_entry = me.new_map_entry(key, value)
    if info[0]:
        
        sll.change_info(info[2], info[1], new_entry)
    else:
        sll.add_last(map["table"]["elements"][l_hash], new_entry)
        map["size"] +=1

    map["current_factor"] =  map["size"] / map["capacity"]
    if map["current_factor"] > map["limit_factor"]:
        rehash(map)

    return map

def rehash(map):
    new_capacity = mp.next_prime(map["capacity"] * 2)
    new_table = arr.new_list()

    for _ in range(new_capacity):
        new_bucket = sll.new_list()
        arr.add_last(new_table, new_bucket)

    old_table = map["table"]["elements"]
    map["table"] = new_table
    map["capacity"] = new_capacity
    map["size"] = 0  # Reiniciar el conteo antes de reinsertar

    for bucket in old_table:
        element = bucket["first"]
        while element is not None:
            entry = element["info"]
            if entry["key"] is not None and entry["key"] != "__EMPTY__":
                l_hash = mp.hash_value(map, entry["key"])
                sll.add_last(map["table"]["elements"][l_hash], entry)
                map["size"] += 1
            element = element["next"]

    map["current_factor"] = map["size"] / map["capacity"]
    return map
    
