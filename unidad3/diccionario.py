# crear un diccionario
puntajes={"Juan":10,"Maria":8,"Pedro":9,"Luis":7}

#accder a los valores por clave

print(puntajes["Juan"]) #imprime 10

#modificar un valor
puntajes['Pedro'] = 10
print(puntajes) # imprime {'Juan': 10, 'Maria': 8, 'Pedro': 10, 'Luis': 7}

#agregar un nuevo elemento
puntajes['Ana']=9
print(puntajes) # imprime {'Juan': 10, 'Maria': 8, 'Pedro': 10, 'Luis': 7, 'Ana': 9}

#eliminar un elemento
del puntajes['Luis']
print(puntajes) # imprime {'Juan': 10, 'Maria': 8, 'Pedro': 10, 'Ana': 9}
