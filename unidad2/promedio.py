<<<<<<< HEAD
grade = []
=======
grades = []
>>>>>>> 70050f0c0a198d39fd515d9e0b9f009275b8ea67

<<<<<<< HEAD
while True:
    grade = input
=======
while True:
    grade = input("Ingrese la nota del estudiante (o 'salir' para terminar): ")
    if grade.lower() == "salir":
        break
    else:
        grades.append(float(grade))

average = sum(grades) / len(grades)
print(f"El promedio de las notas es: {average}")

>>>>>>> 70050f0c0a198d39fd515d9e0b9f009275b8ea67
