def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
        return lista

numero = [54, 12, 67, 89, 23, 45, 78, 90, 34, 56]
print(insertion_sort(numero))