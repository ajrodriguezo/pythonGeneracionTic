def bubble_sort (lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

numeros = [54, 12, 67, 89, 23, 45, 78, 90, 34, 56]
print(bubble_sort(numeros))