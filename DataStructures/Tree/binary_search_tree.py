
from DataStructures.Tree import bst_node as bn
from DataStructures.List import single_linked_list as sll

#New map
def new_map():
    
    map = {"root": None}
    return map

#Size
def size(tree):
    if is_empty(tree):
        return 0
    return tree["root"]["size"]
#is_empty
def is_empty(bst):
    
    if bst["root"] is None:
        return True
    else:
        return False
#Contains

def contains(bst, key):
    
    if get(bst, key) is None:
        return False
    else:
        return True

#Put
def put(tree, key, value):
    
    
    tree["root"] = insert_node(tree["root"], key, value)
    
    return tree

#Insert node    
def insert_node(root, key, value):
    
    node = bn.new_node(key, value)
        
    if root is None:
        
        return node

    elif root["key"] == key:
        
        root["value"] = value
            
    elif root["key"] > key:
        
        root["left"] = insert_node(root["left"], key, value)
        
    elif root["key"] < key:
        
        root["right"] = insert_node(root["right"], key, value)
    
    if root["left"] is not None:
        left_size = root["left"]["size"]
    else:
        left_size = 0
    if root["right"] is not None:
        right_size = root["right"]["size"]
    else: right_size = 0
    
    root["size"] = left_size + 1 + right_size
    
    return root

#value_set
def value_set(bst):
    lista = sll.new_list()
    return value_set_tree(bst["root"], lista)

def value_set_tree(root, lista):
    if root is None:
        return lista 
    else:
        sll.add_last(lista, root["value"])
        value_set_tree(root["left"], lista)
        value_set_tree(root["right"], lista)
    return lista

#get_min retorn la llave más a la izq. Retorna None si no hay ninguna.
def get_min(bst):
    if bst["root"] is None:
        return None
    else:
        return get_min_node(bst["root"])

def get_min_node(root):
    
    if root["left"] is None:
        return root["key"]
    
    else:
        return get_min_node(root["left"])

#delete_max
def delete_max(bst):
    if bst["root"] is not None:
        delete_max_tree(bst["root"])
        return bst
    else:
        return bst
    
def delete_max_tree(root):
    
    if root["right"]["right"] == None:
        
        if root["right"]["left"] is not None:
            root["right"] = root["right"]["left"]
        else:
            root["right"] = None
    else:
        return delete_max_tree(root["right"])
    
    if root["left"] is not None:
        left_size = root["left"]["size"]
    else:
        left_size = 0
    if root["right"] is not None:
        right_size = root["right"]["size"]
    else: right_size = 0
    
    root["size"] = left_size + 1 + right_size
    
    return root

#height
def height(bst):
    
    if bst["root"] == None:
        return 0
    
    else:
        return height_tree(bst["root"]) - 1

def height_tree(root):
    
    if root is None:
        return 0
    
    right = height_tree(root["right"])
    left = height_tree(root["left"])
    
    return 1 + max(right, left)
    
#Get
def get (my_bst, key):
    node= get_node(my_bst["root"], key)
    if node is None:
        return None
    return node["value"]
def get_node(root, key):
    if root is None:
        return None
    if key <root["key"]:
        return get_node(root["left"], key)
    if key > root["key"]:
        return get_node(root["right"], key)
    return root

#Key set
def key_set( my_bst):
    key_list = sll.new_list()
    return key_set_tree(my_bst["root"], key_list)

def key_set_tree(root, key_list):
    if root is None:
        return key_list
    
    key_set_tree(root["left"], key_list)
    sll.add_last(key_list, root["key"])
    key_set_tree(root["right"], key_list)
    
    return key_list

# Get max
def get_max(my_bst):
    node= get_max_node(my_bst["root"])
    if node is None:
        return None
    return node["key"]

def get_max_node(root):
    if root is None:
        return None
    if root["right"] is None:
        return root
    return get_max_node(root["right"])

#Delete min
def delete_min(my_bst):
    my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst

def delete_min_tree(root):
    if root is None:
        return None
    if root["left"] is None:
        return root["right"]

    root["left"] = delete_min_tree(root["left"])

    if root["left"] is not None:
        left_size = root["left"]["size"]
    else:
        left_size = 0
    if root["right"] is not None:
        right_size = root["right"]["size"]
    else:
        right_size = 0

    root["size"] = 1 + left_size + right_size
    return root
#Keys
def keys(my_bst, key_initial, key_final):
    list_key= sll.new_list()
    return keys_range(my_bst["root"], key_initial, key_final, list_key)

def keys_range(root, key_initial, key_final, list_key):
    
    if root is None: #No hay llaves que agregar
        return list_key
    
    if key_initial < root["key"]: #Se busca a la izquierda
        keys_range(root["left"], key_initial, key_final, list_key)
        
    if key_initial <= root["key"] <= key_final: # Si la llave esta dentro del rango se agrega a la lista
        sll.add_last(list_key, root["key"])
        
    if key_final > root["key"]: #Se busca a la derecha
        keys_range(root["right"], key_initial, key_final, list_key)
        
    return list_key
    
    
#Values
def values( my_bst, key_initial, key_final):
    list_value = sll.new_list()
    return values_range(my_bst["root"], key_initial, key_final, list_value)

def values_range( root, key_initial, key_final, list_value):
    
    if root is None:
        return list_value
    
    if key_initial < root["key"]:
        values_range(root["left"], key_initial, key_final, list_value)
        
    if key_initial <= root["key"] <= key_final:
        sll.add_last(list_value, root["value"])
        
    if key_final> root["key"]:
        values_range(root["right"], key_initial, key_final, list_value)
        
    return list_value


    
