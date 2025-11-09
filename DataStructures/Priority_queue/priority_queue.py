from DataStructures.Priority_queue import pq_entry as pqe
from DataStructures.List import array_list as al

# 1. Comparador por mayor prioridad
def default_compare_higher_value(father_node, child_node):
    return pqe.get_priority(father_node) >= pqe.get_priority(child_node)

# 2. Comparador por menor prioridad
def default_compare_lower_value(father_node, child_node):
    return pqe.get_priority(father_node) <= pqe.get_priority(child_node)

# 3. Intercambio de posiciones
def exchange(my_heap, i, j):
    al.exchange(my_heap["elements"], i, j)

# 4. Comparación de prioridad
def priority(my_heap, parent, child):
    return my_heap["cmp_function"](parent, child)

# 5. Tamaño del heap
def size(my_heap):
    return my_heap["size"]

# 6. Verifica si está vacío
def is_empty(my_heap):
    if size(my_heap) == 0:
        return True
    return False

# 7. Reordenamiento ascendente
def swim(my_heap, pos):
    condicion = pos > 1
    while condicion:
        parent = pos // 2
        child_node = al.get_element(my_heap["elements"], pos)
        parent_node = al.get_element(my_heap["elements"], parent)

        if priority(my_heap, parent_node, child_node) == False:
            exchange(my_heap, pos, parent)
            pos = parent
            condicion = pos > 1
        else:
            condicion = False

# 8. Inserción
def insert(my_heap, priority_value, value):
    new_entry = pqe.new_pq_entry(priority_value, value)
    al.add_last(my_heap["elements"], new_entry)
    my_heap["size"] = my_heap["size"] + 1
    swim(my_heap, my_heap["size"])
    return my_heap

# 9. Reordenamiento descendente
def sink(my_heap, pos):
    heap_size = size(my_heap)
    condicion = pos * 2 <= heap_size

    while condicion:
        child = pos * 2
        if child < heap_size:
            left = al.get_element(my_heap["elements"], child)
            right = al.get_element(my_heap["elements"], child + 1)
            if priority(my_heap, left, right) == False:
                child = child + 1

        parent_node = al.get_element(my_heap["elements"], pos)
        child_node = al.get_element(my_heap["elements"], child)

        if priority(my_heap, parent_node, child_node) == False:
            exchange(my_heap, pos, child)
            pos = child
            condicion = pos * 2 <= heap_size
        else:
            condicion = False

# 10. Eliminación del elemento con mayor prioridad
def remove(my_heap):
    if is_empty(my_heap) == True:
        return None

    first_entry = al.get_element(my_heap["elements"], 1)
    last_index = size(my_heap)
    exchange(my_heap, 1, last_index)
    al.remove_last(my_heap["elements"])
    my_heap["size"] = my_heap["size"] - 1
    sink(my_heap, 1)

    return pqe.get_value(first_entry)

# 11. Obtener el primer elemento (sin eliminar)
def get_first_priority(my_heap):
    if is_empty(my_heap) == True:
        return None
    return al.get_element(my_heap["elements"], 1)

# 12. Buscar posición de un valor
def is_present_value(my_heap, value):
    pos = 1
    resultado = -1
    limite = size(my_heap)

    while pos <= limite:
        entry = al.get_element(my_heap["elements"], pos)
        if pqe.get_value(entry) == value:
            resultado = pos
        pos = pos + 1

    return resultado

# 13. Verifica si contiene un valor
def contains(my_heap, value):
    pos = 1
    encontrado = False
    limite = size(my_heap)

    while pos <= limite:
        entry = al.get_element(my_heap["elements"], pos)
        if pqe.get_value(entry) == value:
            encontrado = True
        pos = pos + 1

    return encontrado

# 14. Mejorar prioridad de un valor
def improve_priority(my_heap, priority_value, value):
    pos = 1
    actualizado = False
    limite = size(my_heap)

    while pos <= limite:
        entry = al.get_element(my_heap["elements"], pos)
        if pqe.get_value(entry) == value:
            entry["priority"] = priority_value
            actualizado = True
        pos = pos + 1

    if actualizado == True:
        if pos > 1:
            parent = pos // 2
            parent_entry = al.get_element(my_heap["elements"], parent)
            actual_entry = al.get_element(my_heap["elements"], pos - 1)

            if priority(my_heap, parent_entry, actual_entry) == False:
                swim(my_heap, pos - 1)
            else:
                sink(my_heap, pos - 1)
        else:
            sink(my_heap, pos - 1)

    return my_heap

# 15. Crear nuevo heap
def new_heap(is_min_pq=True):
    elements = al.new_list()
    al.add_last(elements, None)

    if is_min_pq == True:
        cmp_function = default_compare_lower_value
    else:
        cmp_function = default_compare_higher_value

    heap = {
        "elements": elements,
        "size": 0,
        "cmp_function": cmp_function
    }

    return heap