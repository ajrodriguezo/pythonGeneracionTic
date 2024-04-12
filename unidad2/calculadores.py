import principal

def main():
    opcion = 0
    while opcion != 6:
        print("calculadora")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. salir")

        opcion = int(input("¿Qué operación deseas realizar? "))

        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))

        if opcion == 1:
            resultado = principal.suma(numero1, numero2)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == 2:
            resultado =principal.resta(numero1, numero2)
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == 3:
            resultado = principal.multiplicacion(numero1, numero2)
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == 4:
            resultado = principal.division(numero1, numero2)
            print(f"El resultado de la división es: {resultado}")
        elif opcion == 5:
            resultado = principal.potencia(numero1, numero2)
            print(f"El resultado de la potencia es: {resultado}")
        else:
            print("Opción inválida.")
            break

if __name__ == "__main__":
    main()