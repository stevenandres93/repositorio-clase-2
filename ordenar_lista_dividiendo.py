def ordenar_lista_dividiendo(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        mitad_1 = lista[:mitad]
        mitad_2 = lista[mitad:]

        ordenar_lista_dividiendo(mitad_1)
        ordenar_lista_dividiendo(mitad_2)
        v1 = 0
        v2 = 0
        v3 = 0

        while v1 < len(mitad_1) and v2 < len(mitad_2):
            if mitad_1[v1] < mitad_2[v2]:
                lista[v3] = mitad_1[v1]
                v1 = v1 + 1
            else:
                lista[v3] = mitad_2[v2]
                v2 = v2 + 1
            v3 = v3 + 1

        while v1 < len(mitad_1):
            lista[v3] = mitad_1[v1]
            v1 = v1 + 1
            v3 = v3 + 1

        while v2 < len(mitad_2):
            lista[v3] = mitad_2[v2]
            v2 = v2 + 1
            v3 = v3 + 1


import random

Lista_para_ordenar = list()
for i in range(100000):
    Lista_para_ordenar.append(random.randrange(-999999, 999999))

print(Lista_para_ordenar)
ordenar_lista_dividiendo(Lista_para_ordenar)
print(Lista_para_ordenar)
