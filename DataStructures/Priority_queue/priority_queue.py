from DataStructures.Priority_queue import pq_entry as pqe
from DataStructures.List import array_list as al

def default_compare_higher_value(father_node, child_node):
    return pqe.get_priority(father_node) >= pqe.get_priority(child_node)

def default_compare_lower_value(father_node, child_node):
    return pqe.get_priority(father_node) <= pqe.get_priority(child_node)

def exchange(my_heap, i, j):
    return al.exchange(my_heap["elements"], i, j)

def priority(my_heap, parent, child):
    return my_heap["cmp_function"](parent, child)

def size(my_heap):
    return my_heap["size"]

def is_empty(my_heap):
    return size(my_heap) == 0

def swim(my_heap, pos):
    valid = True
    while valid:
        if pos > 1:
            parent = pos // 2
            child_node = al.get_element(my_heap["elements"], pos)
            parent_node = al.get_element(my_heap["elements"], parent)
            if not priority(my_heap, parent_node, child_node):
                exchange(my_heap, pos, parent)
                pos = parent
            else:
                valid = False
        else:
            valid = False

def insert(my_heap, priority_value, value):
    new_entry = pqe.new_pq_entry(priority_value, value)
    al.add_last(my_heap["elements"], new_entry)
    my_heap["size"] += 1
    swim(my_heap, size(my_heap))
    return my_heap

def sink(my_heap, pos):
    heap_size = size(my_heap)
    child = pos * 2
    valid = True

    while valid:
        if child <= heap_size:
            if child < heap_size:
                left_child = al.get_element(my_heap["elements"], child)
                right_child = al.get_element(my_heap["elements"], child + 1)
                if not priority(my_heap, left_child, right_child):
                    child = child + 1

            parent_node = al.get_element(my_heap["elements"], pos)
            child_node = al.get_element(my_heap["elements"], child)

            if not priority(my_heap, parent_node, child_node):
                exchange(my_heap, pos, child)
                pos = child
                child = pos * 2
            else:
                valid = False
        else:
            valid = False

def remove(my_heap):
    if is_empty(my_heap):
        return None
    first_element = al.get_element(my_heap["elements"], 1)
    last_index = size(my_heap)
    exchange(my_heap, 1, last_index)
    al.remove_last(my_heap["elements"])
    my_heap["size"] -= 1
    sink(my_heap, 1)
    return pqe.get_value(first_element)

def get_first_priority(my_heap):
    if is_empty(my_heap):
        return None
    first_element = al.get_element(my_heap["elements"], 1)
    return pqe.get_priority(first_element)

def is_present_value(my_heap, value):
    heap_size = size(my_heap)
    pos = 1
    resultado = -1
    valid = True

    while valid:
        if pos <= heap_size and resultado == -1:
            current_entry = al.get_element(my_heap["elements"], pos)
            if current_entry is not None:
                current_value = pqe.get_value(current_entry)
                if current_value == value:
                    resultado = pos
            pos = pos + 1
        else:
            valid = False

    return resultado

def contains(my_heap, value):
    heap_size = size(my_heap)
    pos = 1
    encontrado = False
    valid = True

    while valid:
        if pos <= heap_size and not encontrado:
            current_entry = al.get_element(my_heap["elements"], pos)
            if current_entry is not None:
                current_value = pqe.get_value(current_entry)
                if current_value == value:
                    encontrado = True
            pos = pos + 1
        else:
            valid = False

    return encontrado

def improve_priority(my_heap, priority_value, value):
    heap_size = size(my_heap)
    pos = 1
    actualizado = False
    valid = True

    while valid:
        if pos <= heap_size and not actualizado:
            entrada = al.get_element(my_heap["elements"], pos)
            if pqe.get_value(entrada) == value:
                entrada["priority"] = priority_value
                actualizado = True
            else:
                pos = pos + 1
        else:
            valid = False

    if actualizado:
        if pos > 1:
            padre = pos // 2
            padre_entry = al.get_element(my_heap["elements"], padre)
            actual_entry = al.get_element(my_heap["elements"], pos)
            if not priority(my_heap, padre_entry, actual_entry):
                swim(my_heap, pos)
            else:
                sink(my_heap, pos)
        else:
            sink(my_heap, pos)

    return my_heap

def new_heap(is_min_pq=True):
    elements = al.new_list()
    al.add_last(elements, None)

    if is_min_pq:
        cmp_function = default_compare_lower_value
    else:
        cmp_function = default_compare_higher_value

    my_heap = {
        "elements": elements,
        "size": 0,
        "cmp_function": cmp_function
    }

    return my_heap