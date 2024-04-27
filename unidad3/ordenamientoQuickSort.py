def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    
    return quick_sort(izquierda) + medio + quick_sort(derecha)

numeros = [54, 12, 67, 89, 23, 45, 78, 90, 34, 56]
ordenados = quick_sort(numeros)
print(ordenados)