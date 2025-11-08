from DataStructures.Tree.rbt_node import RED, BLACK, new_node, change_color, is_red
from DataStructures.List import single_linked_list as  sll
# new map
def new_map():
    return {"root": None,
            "type": "RBT"}
#get size
def get_size(node):
    size = 0
    if node is not None:
        size = node["size"]
    return size

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

def contains(rbt, key):
    
    if get(rbt, key) is None:
        return False
    else:
        return True

#is_empty
def is_empty(rbt):
    
    if rbt["root"] is None:
        return True
    else:
        return False
    
#value_set
def value_set(rbt):
    lista = sll.new_list()
    return value_set_tree(rbt["root"], lista)

def value_set_tree(root, lista):
    if root is None:
        return lista 
    else:
        sll.add_last(lista, root["value"])
        value_set_tree(root["left"], lista)
        value_set_tree(root["right"], lista)
    return lista

#get_min
def get_min(rbt):
    if rbt["root"] is None:
        return None
    else:
        return get_min_node(rbt["root"])

def get_min_node(root):
    
    if root["left"] is None:
        return root["key"]
    
    else:
        return get_min_node(root["left"])

#keys
def keys(rbt, key_initial, key_final):
    
    lista = sll.new_list()
    
    if rbt["root"] is None:
        return lista
    
    else:
        return keys_range(rbt["root"], key_initial, key_final, lista)
    
def keys_range(root, key_initial, key_final, lista):

    if root is None:
        
        return lista
    
    elif root["key"] < key_initial:
        
        return keys_range(root["right"], key_initial, key_final, lista)
    
    elif key_initial <= root["key"] <= key_final:
        
        sll.add_last(lista, root["key"])
    
    elif root["key"] > key_initial:
        
        return keys_range(root["left"], key_initial, key_final, lista)
    
    return lista

# rotate left
def rotate_left(node_rbt):
    x= node_rbt["right"]
    node_rbt["right"] = x["left"]
    x["left"] = node_rbt
    x["color"] = node_rbt["color"]
    node_rbt["color"] = RED
    x["size"] = node_rbt["size"]
    node_rbt["size"] = 1 + get_size(node_rbt["left"]) + get_size(node_rbt["right"])
    return x

# rotate right
def rotate_right(node_rbt):
    x = node_rbt["left"]
    node_rbt["left"] = x["right"]
    x["right"] = node_rbt
    x["color"] = node_rbt["color"]
    node_rbt["color"] = RED
    x["size"] = node_rbt["size"]
    node_rbt["size"] = 1 + get_size(node_rbt["left"]) + get_size(node_rbt["right"])
    return x

# flip colors
def flip_colors(node_rbt):
    change_color(node_rbt, RED)
    change_color(node_rbt["left"], BLACK)
    change_color(node_rbt["right"], BLACK)
    
# insert node    
def insert_node(root, key, value):
    
    if root is None:
        return new_node(key, value, RED)
    
    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
        
    if is_red(root["right"]) and not is_red(root["left"]):
        root = rotate_left(root)
    if is_red(root["left"]) and is_red(root["left"]["left"]):
        root = rotate_right(root)
    if is_red(root["left"]) and is_red(root["right"]):
        flip_colors(root)
        
    root["size"] = 1 + get_size(root["left"]) + get_size(root["right"])
    return root



# put
def put(my_rbt, key, value):
    my_rbt["root"] = insert_node(my_rbt.get("root"), key, value)
    change_color(my_rbt["root"], BLACK)
    return my_rbt

# size 
def size(my_rbt):
    return size_tree(my_rbt.get("root"))

# size tree
def size_tree(root):
    if root is None:
        return 0
    return root["size"]

#key set
def key_set(my_rbt):
    key_list = sll.new_list()
    return key_set_tree(my_rbt.get("root"), key_list)

# key set node
def key_set_tree( root, key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        sll.add_last(key_list, root["key"])
        key_set_tree(root["right"], key_list)
    return key_list

#get max
def get_max(my_rbt):
    return get_max_node(my_rbt.get("root"))

# get max tree
def get_max_node(root):
    
    if root is None:
        return None

    current = root
    while current["right"] is not None:
        current = current["right"]
    return current["key"]


# height
def height(my_rbt):
    return height_tree(my_rbt.get("root"))

def height_tree(root):
    if root is None:
        return -1  
    left_height = height_tree(root["left"])
    right_height = height_tree(root["right"])
    return 1 + max(left_height, right_height)

# values
def values(my_rbt, key_initial, key_final):
    value_list= sll.new_list()
    return values_range(my_rbt.get("root"), key_initial, key_final, value_list)

# values range
def values_range(root, key_lo, key_hi, list_values):
    if root is None:
        return list_values

    if key_lo < root["key"]:
        values_range(root["left"], key_lo, key_hi, list_values)

    if key_lo <= root["key"] and root["key"] <= key_hi:
        sll.add_last(list_values, root["value"])

    if key_hi > root["key"]:
        values_range(root["right"], key_lo, key_hi, list_values)

    return list_values
