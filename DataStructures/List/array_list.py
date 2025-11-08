from random import shuffle

#Primera función que crea la lista de arreglo 

def new_list():
    
    newlist = {
        "elements": [],
        "size":0
    
    }
    
    return newlist
# Función 12 Lab 3
def get_element( my_list, index):
    if index < my_list["size"]:
        return my_list["elements"][index]

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def size(my_list):
    """
    Retorna el tamaño de la lista

    parametros:
    my_list: lista

    Returns:
    El tamaño de la lista
    """
    return my_list["size"]

def get_first_element(my_list):
    """
    Retorna el primer elemento de la lista o None si está vacía.
    
    parametros: my_list: la lista.
    
    return: el primer elemento de la lista o None si está vacía.
    """
    if my_list["size"] == 0:
        return None
    return my_list["elements"][0]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range (0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info)==0:
                keyexist= True
                break
        if keyexist:
            return keypos
    return -1

#Add first array
def add_first( my_list, element):
    """
    Adiciona un elemento al inicio de la lista array
    Parametros:
        my_list: la lista a la que se le va a adicionar el elemento
        element: el elemento a adicionar
    Retorna:
        La lista con el elemento adicionado al inicio
    """
    my_list["elements"].insert(0, element)
    my_list["size"] +=1
    return my_list

# Is empty array
def is_empty(my_list):
    """
    Verifica si la lista array está vacía
    Parametros:
        my_list: la lista a verificar
    Retorna:
        True si la lista está vacía, False en el caso contrario
    """
    is_empty= False
    longitud= my_list["size"]
    if longitud==0:
        is_empty= True
    return is_empty


# last element array
def get_last_element (my_list):
    """
    Determina el último elemento de la lista array
    Parametros:
        my_list: lista a la que se le va a determinar su último elemento
    Retorna:
        El último elemento de la lista   
    """
    if my_list["size"]>0:
        return my_list["elements"][my_list["size"]-1]
    else:
        raise IndexError("La lista está vacía")
    

# delete element array
def delete_element (my_list, pos):
    """
    Elimina un elemento en la posición dada de la lista array
    Parametros:
        my_list: La lista a la que se le va a eliminar el elemento
        pos: La posición del elemento que se va a eliminar
    Retorna:
        La lista con el elemento eliminado
    """
    del my_list["elements"][pos]
    my_list["size"] -=1
    return my_list

#Función remove_first

def remove_first(my_list):
    
    """
    Elimina el primer elemento de la lista.
    
    parámetros:
    * my_list : lista 
    
    retorna:
    * None si la lista está vacía.
    * Elemento eliminado.
    
    """
    
    if my_list["size"] == 0:
        return None
    else:
        eliminado = my_list["elements"][0]
        del my_list["elements"][0]
        my_list["size"] -=1
        
        return eliminado
    
#Función remove_last

def remove_last(my_list):

    """
    Elimina el último elemento de la lista.
    
    parámetros:
    * my_list : lista 
    
    retorna:
    * None si la lista está vacía.
    * Elemento eliminado.
    
    """
    if my_list["size"] == 0:
        
        return None
    else:
        eliminado = my_list["elements"][-1]
        del my_list["elements"][-1]
        my_list["size"] -=1
        return eliminado
    
#Función change_info

def change_info(my_list, position, element):
    
    """
    Cambia el elemento en la posición dada por el nuevo elemento.
    
    parámetros:
    * my_list : lista 
    * position : posición del elemento a cambiar
    * element : nuevo elemento
    
    retorna:
    * None si la posición es inválida.
    * La lista actualizada con el elemento cambiado.
    
    """
    if (position < 0) or (position >= my_list["size"]):
        return None
    else:
        my_list["elements"][position] = element
        return my_list
    

def insert_element(my_list, element, pos):
    """
    Inserta un elemento en la posición pos de la lista. La primera posición es 1.

    parametros:
    my_list: la lista, element: el elemento a insertar, pos: la posición a insertar.

    Returns:
    La lista con el nuevo elemento insertado.
    """
    size = my_list["size"]
    if pos < 0 or pos > size:
        raise IndexError("Index out of range")
    
    else:
        my_list["size"] +=1
        return my_list["elements"].insert(pos,element)
    


def exchange(my_list, pos_1, pos_2):
    """
    Intercambia dos elementos de la lista.

    parametros:
    my_list: la lista, pos_1: la posición del primer elemento a intercambiar, pos_2: la posición del segundo elemento a intercambiar.

    Returns:
    La lista con los elementos intercambiados.
    """
    if pos_1 < 0 or pos_1 > my_list["size"] or pos_2 < 0 or pos_2 > my_list["size"]:
        raise IndexError("Index out of range")
    x = my_list["elements"][pos_1]
    my_list["elements"][pos_1] = my_list["elements"][pos_2]
    my_list["elements"][pos_2] = x
    return my_list

def sub_list(my_list, pos_i, num_elements):
    """
    Retorna una sublista de la lista dada una posición inicial y el número de elementos.

    Parametros:
    my_list: la lista original, pos_i: la posición donde comienza la sublista, num_elements: el número de elementos de la sublista.

    Returns:
    La sublista creada.
    """
    if pos_i < 0 or pos_i > my_list["size"]:
        raise IndexError("Index out of range")
    else:
        sub_list = new_list()
        sub_list["elements"] = my_list["elements"][pos_i:pos_i+num_elements]
        sub_list["size"] = num_elements
        
        return sub_list

# Default sort criteria
def default_sort_criteria (element_1, element_2):
    is_sorted= False
    if element_1  < element_2:
        is_sorted= True
    return is_sorted

#Funcion selection sort
def selection_sort(my_list, sort_crit):
    for i in range (size(my_list)):
        element1 = get_element(my_list, i)
        k= i
        for j in range (i, size(my_list)):
            element2 = get_element(my_list, j)
            if sort_crit (element2, element1):
                element1 =element2
                k= j
        exchange ( my_list, i, k)
    return my_list
#Función shell short
def shell_sort(my_list, cmp_function):
    
    if my_list is None:
        return Exception("La lista es nula")
    
    elif my_list["size"] == 1:
        return my_list
    
    else:
        h = 1
        n = my_list["size"]
        while (3*h) + 1 < n:
            h = (3 * h) + 1
            
        
        pos2 = h 
        while h != 1:
            pos1 = 0
            while pos2 < n:
                element1 = get_element(my_list, pos1)
                element2 = get_element(my_list, pos2)
                if cmp_function(element1, element2) == False:
                    exchange(my_list, pos1, pos2)

                pos1 +=1
                pos2 = pos1 + h
            h = h // 3
        
        insertion_sort(my_list, cmp_function) 
        return my_list

#Función insertion sort               
def insertion_sort(my_list, sort_crit):
    
    
    if my_list == 0:
        return []
    elif my_list["size"] == 1:
        return my_list
    else:
        n = my_list["size"]
        
        for i in range(1,n):
            j = i
            while j >0 and sort_crit(get_element(my_list, j-1), get_element(my_list,j)) == False:
                    exchange(my_list, j, j-1)
                    j-=1
        return my_list
    
#Función merge sort
def merge_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list
    
    mid = my_list["size"] // 2
    lado_izquierdo = sub_list(my_list, 0, mid)
    lado_derecho = sub_list(my_list, mid, my_list["size"] - mid)
    
    iz_ordenado = merge_sort(lado_izquierdo, sort_crit)
    der_ordenado = merge_sort(lado_derecho, sort_crit)
    
    merged_list = new_list()
    i = j = 0

    while i < iz_ordenado["size"] and j < der_ordenado["size"]:
        elem_iz = iz_ordenado["elements"][i]
        elem_der = der_ordenado["elements"][j]
        
        if sort_crit(elem_iz, elem_der):
            add_last(merged_list, elem_iz)
            i += 1
        else:
            add_last(merged_list, elem_der)
            j += 1
    
    while i < iz_ordenado["size"]:
        add_last(merged_list, iz_ordenado["elements"][i])
        i += 1
    
    while j < der_ordenado["size"]:
        add_last(merged_list, der_ordenado["elements"][j])
        j += 1
    
    return merged_list
        
#Función quick_sort
def quick_sort(my_list, sort_crit):
    
    shuffle(my_list["elements"])
    if my_list["size"] == 0:
        return my_list
    if my_list["size"] == 1:
        return my_list

    
    peque = 0
    pivote = get_element(my_list, my_list["size"] -1)
    pos = my_list["size"] -1
    
    for i in range(pos):
        elementi = get_element(my_list,i)
        
        if sort_crit(elementi, pivote) == True:
            exchange(my_list, i, peque)
            peque +=1
            

    exchange(my_list, peque, pos)

    izq = {"elements":my_list["elements"][:peque], "size":peque}
    dere = {"elements":my_list["elements"][peque+1:], "size": 0}
    dere["size"] = len(dere["elements"])
    
    izq = quick_sort(izq, sort_crit)
    dere = quick_sort(dere, sort_crit)
    
    return {"elements": izq["elements"] + [pivote] + dere["elements"], "size": my_list["size"]}



    