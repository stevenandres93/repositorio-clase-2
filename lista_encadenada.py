class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente_nodo = None


class ListaEncadenada:
    def __init__(self):
        self.longitud = 0
        self.primer_nodo = None

    def insertar_dato(self, dato):
        if self.longitud == 0:
            self.primer_nodo = Nodo(dato)
        else:
            ultimo_nodo = self.obtener_ultimo_nodo()
            ultimo_nodo.siguiente_nodo = Nodo(dato)
        self.longitud += 1

    def obtener_ultimo_dato(self):
        if self.longitud > 0:
            penultimo_nodo = self.primer_nodo
            while penultimo_nodo.siguiente_nodo.siguiente_nodo is not None:
                penultimo_nodo = penultimo_nodo.siguiente_nodo

            ultimo_nodo = penultimo_nodo.siguiente_nodo

            penultimo_nodo.siguiente_nodo = None

            self.longitud -= 1
            return ultimo_nodo.dato
        else:
            return None

    def obtener_ultimo_nodo(self):
        if self.primer_nodo is None:
            return None
        else:
            nodo_temp = self.primer_nodo
            while nodo_temp.siguiente_nodo is not None:
                nodo_temp = nodo_temp.siguiente_nodo
            return nodo_temp

    def __str__(self):
        if self.longitud > 0:
            l = list()
            nodo_temporal = self.primer_nodo
            while nodo_temporal.siguiente_nodo is not None:
                l.append(nodo_temporal.dato)
                nodo_temporal = nodo_temporal.siguiente_nodo

            l.append(nodo_temporal.dato)

            return str(l)
        else:
            return str(list())


le1 = ListaEncadenada()
print(le1)

le1.insertar_dato(2)
print(le1)
le1.insertar_dato(3)
print(le1)
le1.insertar_dato(5)
print(le1)

print(le1.obtener_ultimo_dato())
print(le1)
print(le1.obtener_ultimo_dato())
print(le1)
