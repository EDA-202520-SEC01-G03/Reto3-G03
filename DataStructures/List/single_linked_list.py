
from DataStructures.List import list_node as ln #se importa list_node.py

#Función new_list: Crea la lista de single_linked_list
def new_list():
    
    newlist = {
        "first": None,
        "last":None,
        "size": 0
    } 
    
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        if node != None:
            node = node["next"]
        searchpos += 1
    if node != None:
        return node["info"]
    else:
        raise Exception("No hay elementos en la lista.")
    
    

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count

#Add first single linked list
def add_first (my_list, element):
    """
    Adiciona un elemento al inicio de la lista sencillamente enlazada
    Parametros:
        my_list: la lista a la que se le va a adicionar el elemento
        elemento: el elemento a adicionar
    Retorna:
        La lista con el elemento adicionado al inicio
    """
    nodo= ln.new_single_node(element)
    nodo["next"]= my_list["first"]
    my_list["first"]= nodo
    
    if my_list["size"]==0:
        my_list["last"]= nodo
    my_list["size"] +=1
    return my_list

# Is empty single linked list
def is_empty(my_list):
    """
    Verifica si la lista sencillamente enlazada está vacía
    Parametros:
        my_list: la lista a verificar     
    Retornar:
        True si la lista está vacía, False en caso contrario   
    """
    is_empty= False
    if my_list["size"]==0:
        is_empty= True
        
    return is_empty

# last element single linked list
def last_element (my_list):
    """
    Determina el último elemento de la lista sencillamente enlazada
    Parametros:
        my_list: lista a la que se le va a determinar su último elemento
    Retorna:
        El último elemento de la lista
    """
    retorno = None
    if my_list["size"]>0:
        retorno= my_list["last"]["info"]
    return retorno

# delete element single linked list
def delete_element (my_list, pos):
    """
    Elimina un elemento en la posición dada de la lista sencillamente enlazada
    Parametros:
        my_list: La lista a la que se le va a eliminar el elemento
        pos: La posición del elemento que se va a eliminar
    Retorna:
        La lista con el elemento eliminado
    """
    if pos <0 or pos >= my_list["size"]:
        raise IndexError("Index out of range")
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
        if my_list["size"] == 1:
            my_list["last"] = None
    else:
        prev = my_list["first"]
        i = 0
        while i < pos - 1:
            prev = prev["next"]
            i += 1
        prev["next"] = prev["next"]["next"]
        if pos == my_list["size"] - 1:
            my_list["last"] = prev
    my_list["size"] -= 1
    return my_list

#Función add_last

def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista.
    parámetros:
    * my_list: Lista a la cual se le agregará el elemento.
    * element: Elemento a agregar a la lista.
    
    retorna:
    * La lista actualizada con el nuevo elemento agregado al final.
    
    """
    new_node = ln.new_single_node(element)
    
    if my_list["size"] == 0:
        
        my_list["first"] = new_node
        
    else:
        
        my_list["last"]["next"] = new_node
        
    my_list["last"] = new_node
    my_list["last"]["next"] = None
    my_list["size"] +=1
    
    return my_list

#Función remove_last

def remove_last(my_list):

    """
    Elimina el último elemento de la lista.
    parámetros:
    * my_list: Lista a la cual se le eliminará el elemento.
    
    retorna:
    * El elemnto eliminado.
    
    """
    
    if my_list["size"] == 0:
        raise Exception("No hay ningun elemento en la lista")
    
    if my_list["size"] == 1:
        eliminado = my_list["first"]["info"]
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] -=1
        
        return eliminado
    
    elif my_list["size"] > 1:
        
        previous = my_list["first"]
        next = my_list["first"]["next"]
            
        while next != my_list["last"]:
            previous = next
            next = next["next"]
        
        eliminado = my_list["last"]["info"]
        my_list["last"] = previous
        my_list["last"]["next"] = None
        my_list["size"] -=1
        
        return eliminado
    
#Función remove_first
def remove_first(my_list):
    
    """
    Elimina el primer elemento de la lista.
    parámetros:
    * my_list: Lista a la cual se le eliminará el elemento.
    
    retorna:
    * None si la lista está vacía.
    * Elemento eliminado.
    
    """
    if my_list["size"] == 0:
        raise Exception("No hay ningun elemento en la lista")
    else:
        eliminado = my_list["first"]["info"]
        my_list["first"] = my_list["first"]["next"]
        my_list["size"] -=1
        
        if my_list["size"] == 1:
            my_list["last"] = my_list["first"]
             
        return eliminado

#Función exchange

def exchange(my_list, pos1, pos2):
    
    if (pos1 < 0 or pos1 >= my_list["size"]) or (pos2 <0 or pos2 >= my_list["size"]):
        raise Exception("Las posiciones están fuera de rango")
    
    else: 
        node1 = my_list["first"]
        x = 0
    
        while x != pos1:
            node1 = node1["next"]
            x +=1
        
        node2 = my_list["first"]
        y = 0
    
        while y != pos2:
            node2 = node2["next"]
            y +=1  
    
        a = node1["info"] #se guarda la info del nodo1 en a para no perderla
        node1["info"] = node2["info"]
        node2["info"] = a
    
        return my_list
    

def first_element(my_list):
    
    """
    Retorna el primer elemento de la lista o None si está vacía.
    
    parametros: my_list: la lista.
    
    return: el primer elemento de la lista o None si está vacía.
    """
    
    if my_list["size"] == 0:
        return None
    return my_list["first"]["info"]

def size(my_list):
    """
    Retorna el tamaño de la lista

    parametros:
    my_list: lista

    Returns:
    El tamaño de la lista
    """
    return my_list["size"]

def insert_element(my_list, element, pos):
    
    """
    Inserta un elemento en la posición pos de la lista.

    parametros:
    my_list: la lista, element: el elemento a insertar, pos: la posición donde se va a insertar el elemento.

    Returns:
    La lista con el nuevo elemento insertado.
    """
    if pos < 0 or pos > my_list["size"]:
        raise Exception("Index out of range")
    if pos < 0 or pos > my_list["size"]:
        raise Exception("Index out of range")
    
    new = {"info": element, "next": None}
    if pos == 0:
        new["next"] = my_list["first"]
        my_list["first"] = new
    else:
        prev = my_list["first"]
        i = 0
        while i < pos - 1:
            prev = prev["next"]
            i += 1
        new["next"] = prev["next"]
        prev["next"] = new
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, element):
    
    """
    Cambia el elemento en la posición pos de la lista por element.

    parametros:
    my_list: la lista, element: el nuevo elemento, pos: la posición donde se va a cambiar el elemento.

    Returns:
    La lista con el elemento cambiado.
    """
    if pos < 0 or pos >= my_list["size"]:
        raise Exception("Index out of range")
    x = my_list["first"]
    i = 0
    while i < pos:
        x = x["next"]
        i += 1  
    x["info"] = element
    return my_list

def sub_list(my_list, pos_i, num_elements):
    
    """
    Retorna una sublista de la lista original, comenzando en la posición pos_i

    Parametros:
    my_list: la lista original, pos_i: la posición donde comienza la sublista, num_elements: el número de elementos de la sublista.

    Returns:
    La sublista creada a partir de la lista original.
    """
    if pos_i < 0 or pos_i > my_list["size"]:
        raise Exception("Index out of range")
    sublist = new_list()
    x = my_list["first"]
    
    i = 0
    while i < pos_i:
        x = x["next"]
        i += 1
    y = 0
    while y < num_elements and x is not None:
        add_last(sublist, x["info"])
        x = x["next"]
        y += 1
    return sublist

# Default sort criteria
def default_sort_criteria(element_1, element_2):
    is_sorted= False
    if element_1  < element_2:
        is_sorted= True
    return is_sorted

def mayor_sort_criteria(element_1, element_2):
    is_sorted= False
    if element_1  > element_2:
        is_sorted= True
    return is_sorted

#Funcion Selection sort
def selection_sort(my_list, sort_crit):
    actual= my_list["first"]
    i= 0
    
    while actual is not None:
        element1 = actual["info"]
        k= i
        nodo_2 = actual
        j = i
        
        while nodo_2 is not None:
            element2 = nodo_2["info"]
            
            if sort_crit(element2, element1)== True:
                element1 = element2
                k = j
            nodo_2 = nodo_2["next"]
            j+= 1
            
        exchange(my_list, i, k)
        actual = actual["next"]
        i += 1
    return my_list
            

#Función shell sort
def shell_sort(my_list, sort_crit):
    n = my_list["size"]
    if n == 0:
        return Exception("La lista está vacía")
    elif n == 1:
        return my_list
    else:
        h = 1
        while (3 * h) + 1 < n:
            h = (3 * h) + 1
        
        pos2 = h
        
        while h!= 1:
            pos1 = 0
            while pos2 < n:
                element1 = get_element(my_list, pos1)
                element2= get_element(my_list, pos2)
                if sort_crit(element1, element2) == False:
                    exchange(my_list, pos1, pos2)
                    
                pos1 +=1
                pos2 = pos1 + h
                
            h = h // 3
            
        insertion_sort(my_list, sort_crit)
        return my_list

#Funcion Insertion sort
def insertion_sort(my_list, sort_crit):
    n = my_list["size"]
    
    if my_list["size"] == 0:
        return Exception("La lista está vacía.")
    
    elif my_list["size"] == 1:
        return my_list
    
    else:
        i = 1
        
        while i < n:
            element1 = get_element(my_list, i)
            x = i -1
            while x >= 0:
                element2= get_element(my_list, x)
                if sort_crit(element2, element1) == False:
                    exchange(my_list, i, x)
                    i = x
                    
                x -=1
                
            i +=1
            
        return my_list

#Función merge_sort
def merge_sort(my_list, sort_crit):
    
    '''Ordena una lista. 
    
    Parámetros:
    
        - Lista a ordenar.
        
    retorna:
    
        - La lista ordenada
    '''
    n = size(my_list)
    if n == 0:
        return []
    
    if size(my_list) == 1:
        return my_list


    m = size(my_list) // 2
    
    subi = sub_list(my_list, 0, m)
    subj = sub_list(my_list, m, my_list["size"] - m)

    arr_izq = merge_sort(subi, sort_crit)
    arr_der = merge_sort(subj, sort_crit)

    i = 0
    j = 0
    k = 0
    
    while i < size(arr_izq) and j < size(arr_der):
        elementi = get_element(arr_izq, i)
        elementj = get_element(arr_der, j)
        
        if sort_crit(elementi, elementj) == True or elementi == elementj:
            
            change_info(my_list, k, elementi)
            i +=1
            
        elif sort_crit(elementj, elementi) == True:
            
            change_info(my_list, k, elementj)
            j +=1
        k +=1
        
    while i < size(arr_izq):
        elementi = get_element(arr_izq, i)
        change_info(my_list, k, elementi)
        i+=1
        k+=1
        
    
    while j < size(arr_der):
        elementj = get_element(arr_der, j)
        change_info(my_list, k, elementj)
        j +=1
        k +=1
            
    return my_list

#Funcion quick sort 
def quick_sort (my_list, sort_crit):
    if my_list["size"]<= 1:
        return my_list
    else:
        pivote = my_list["first"]["info"]
        menores = new_list()
        mayores = new_list()
        
        actual = my_list["first"]["next"]
        
        while actual is not None:
            valor = actual["info"]
            if sort_crit(valor, pivote):
                menores= add_last(menores, valor)
            else:
                mayores= add_last(mayores, valor)
            actual = actual["next"]
    menores_ordenados = quick_sort(menores, sort_crit)
    mayores_ordenados = quick_sort(mayores, sort_crit)
    
    resultado= new_list()
    actual = menores_ordenados["first"]
    while actual is not None:
        resultado = add_last(resultado, actual["info"])
        actual = actual["next"]
    resultado = add_last(resultado, pivote)
    
    actual = mayores_ordenados["first"]
    while actual is not None:
        resultado = add_last(resultado, actual["info"])
        actual = actual["next"]
    return resultado


