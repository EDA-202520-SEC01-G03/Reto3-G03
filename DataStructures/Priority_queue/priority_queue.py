from DataStructures.Priority_queue import pq_entry as pqe
from DataStructures.List import array_list as al

#1. default compare higher value
def default_compare_higher_value(father_node, child_node):
    return pqe.get_priority(father_node) >= pqe.get_priority(child_node)

#2. default compare lower value
def default_compare_lower_value(father_node, child_node):
    return pqe.get_priority(father_node) <= pqe.get_priority(child_node)

#3. exchange
def exchange(my_heap, i, j):
    return al.exchange(my_heap["elements"], i, j)

#4. priority
def priority(my_heap, parent, child):
    return my_heap["cmp_function"](parent, child)

#5. size
def size(my_heap):
    return my_heap["size"]+1

#6. is_empty
def is_empty(my_heap):
    return size(my_heap) == 0

#7 swim
def swim(my_heap, pos):
    while pos > 1:
        parent = pos //2
        child_node = al.get_element(my_heap["elements"], pos)
        parent_node = al.get_element(my_heap["elements"], parent)
        
        if not priority(my_heap, parent_node, child_node):
            exchange(my_heap, pos, parent)
            pos = parent
            
        else:
            pos = 1
        

#8. insert
def insert(my_heap, priority, value):
    new_entry = pqe.new_pq_entry(priority, value)
    al.add_last(my_heap["elements"], new_entry)
    my_heap["size"] += 1
    pos= size(my_heap)-1
    swim(my_heap, pos)
    return my_heap
    

#9. sink
def sink(my_heap, pos):
    heap_size= size(my_heap)-1
    child = pos * 2
    while child <= heap_size:
        if child < heap_size:
            left_child = al.get_element(my_heap["elements"], child)
            right_child = al.get_element(my_heap["elements"], child + 1)
            if not priority(my_heap, left_child, right_child):
                child += 1
                
        parent_node = al.get_element(my_heap["elements"], pos)
        child_node = al.get_element(my_heap["elements"], child)
        
        if not priority(my_heap, parent_node, child_node):
            exchange(my_heap, pos, child)
            pos = child
            child = pos * 2
        else:
            child = heap_size + 1
    

#10. remove
def remove(my_heap):
    if is_empty(my_heap):
        return None
    first_element = al.get_element(my_heap["elements"], 1)
    last_index = size(my_heap)-1
    exchange(my_heap, 1, last_index)
    al.remove_last(my_heap["elements"])
    my_heap["size"] -= 1
    sink(my_heap, 1)
    return pqe.get_value(first_element)

#11. get_first_priority
def get_first_priority(my_heap):
    if is_empty(my_heap):
        return None
    first_element = al.get_element(my_heap["elements"], 1)
    return first_element

#12. is present value
def is_present_value(my_heap, value):
    heap_size = size(my_heap)
    pos = 1
    resultado = -1

    while pos < heap_size and resultado == -1:
        current_entry = al.get_element(my_heap["elements"], pos)
        if current_entry is not None:
            current_value = pqe.get_value(current_entry)
            if current_value == value:
                resultado = pos
        pos += 1

    return resultado

#13. contains
def contains(my_heap, value):
    heap_size = size(my_heap)
    pos = 1
    encontrado = False

    while pos < heap_size and not encontrado:
        current_entry = al.get_element(my_heap["elements"], pos)
        if current_entry is not None:
            current_value = pqe.get_value(current_entry)
            if current_value == value:
                encontrado = True
        pos += 1

    return encontrado

#14. improve priority
def improve_priority(my_heap, priority, value):
    heap_size = size(my_heap)
    pos= 1
    actualizado= False
    
    while pos < heap_size and not actualizado:
        entrada = al.get_element(my_heap["elements"], pos)
        if pqe.get_value(entrada) == value:
            entrada["priority"] = priority
            actualizado = True
        else:
            pos += 1

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

#15. new heap
def new_heap(is_min_pq= True):
    elements= al.new_list()
    al.add_last(elements, None) 
    
    if is_min_pq:
        cmp_function= default_compare_lower_value
    else:
        cmp_function= default_compare_higher_value
        
    my_heap= {
        "elements": elements,
        "size": 0,
        "cmp_function": cmp_function
    }
    
    return my_heap