Lista_para_ordenar = [88, 24, 54, 96]
print(Lista_para_ordenar)


def ordenar_una_lista(lista):
    recorrido = len(lista) - 1
    for j in range(0, recorrido):
        for i in range(len(lista)):
            if i + 1 < len(lista) and lista[i] > lista[i + 1]:
                variable_temporal = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = variable_temporal
    return lista


ordenar_una_lista(Lista_para_ordenar)
print(Lista_para_ordenar)
