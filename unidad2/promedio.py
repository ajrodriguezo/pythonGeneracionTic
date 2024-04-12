grades = []

while True:
    grade = input("Ingrese la nota del estudiante (o 'salir' para terminar): ")
    if grade.lower() == "salir":
        break
    else:
        grades.append(float(grade))

average = sum(grades) / len(grades)
print(f"El promedio de las notas es: {average}")
