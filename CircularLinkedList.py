from LinkedListNode import *
class ListaCircular:
    def __init__(self):
        self.first = None
        self.size = 0

    # Retorna la cantidad de elementos en la lista
    def get_size(self):
        return self.size

    # Retorna el i-ésimo elemento de la lista, contando desde 1
    def get_node(self, i):
        if self.size == 0:
            return -1
        s = self.first
        for x in range(1, i):
            s = s.next
        return s.value

    # Retorna el índice del elemento si existiese, de lo contario retorna -1
    def exists(self, num):
        s = self.first
        for x in range(self.size):
            if int(s.value) == num:
                return x
            s = s.next
        return -1

    # Elimina el i-ésimo elemento y retorna la referencia al siguiente nodo del eliminado
    def delete(self, i):
        if self.size == 0:
            return None
        # Avanzar hasta quedar en la posición anterior al elemento a eliminar
        s = self.first
        if (i == 1):  # Primer elemento es un caso especial
            # Recorremos hasta el último nodo para que quede en el nodo anterior al primero
            for x in range(1, self.size):
                s = s.next
        else:
            # Caso general
            for x in range(1, i - 1):
                s = s.next
        # Aquí estamos en el nodo anterior al que queremos eliminar, ahora lo eliminamos.
        print("Eliminado: ", s.next.value)
        s.next = s.next.next  # Cambio la referencia
        self.size -= 1
        return s.next  # Retornar el siguiente al eliminado

    def add(self, v):
        if self.size == 0:  # No elementos
            self.first = LinkedListNode(v)
            self.first.next = self.first  # Lista Circular
            self.size += 1
            return
        # Si existen elementos
        # Como lo inserto al final, apunta al primero
        nodo_nuevo = LinkedListNode(v, self.first)
        ultimo_antiguo = self.first
        for x in range(1, self.size):
            ultimo_antiguo = ultimo_antiguo.next
        ultimo_antiguo.next = nodo_nuevo  # Ahora apunta al nuevo
        self.size += 1

