def linear_search(lista, elemto):
    for i in range(len(lista)):
        if lista[i] == elemto:
            return i
    return -1

# Busqueda lenear o lierar search
numeros=[54, 12, 67, 89, 23, 45, 78, 90, 34, 56]
elemento_Buscado = 89

inice = linear_search(numeros, elemento_Buscado)
if inice != -1:
    print(f"El elemento {elemento_Buscado} se encuentra en la posicion {inice+1}")
else:
    print(f"El elemento {elemento_Buscado} no se encuentra en la lista")