def main():
    precio = 50
    denominacion = [5, 10, 25]

    ingresado = 0
    adeudado = precio

    while adeudado > 0:
        moneda = int(input("Ingrese moneda (5, 10 o 25 centavos): "))

        if moneda in denominacion:
            ingresado += moneda
            adeudado -= moneda
            print("Ha ingresado", ingresado, "centavos y faltan", adeudado, "centavos")
        else:
            print("Moneda no válida")

    if ingresado > precio:
        print("Su cambio es de", ingresado - precio, "centavos")

if __name__ == "__main__":
    main()