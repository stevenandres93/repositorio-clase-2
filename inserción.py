def __agregar_recursivo(self, nodo, dato):
    if dato < nodo.dato:
        if nodo.izquierda is None:
            nodo.izquierda = Nodo(dato)
        else:
            self.__agregar_recursivo(nodo.izquierda, dato)
    else:
        if nodo.derecha is None:
            nodo.derecha = Nodo(dato)
        else:
            self.__agregar_recursivo(nodo.derecha, dato)