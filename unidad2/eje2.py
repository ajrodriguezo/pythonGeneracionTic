"""Escribe una función area_circulo que acepte un argumento de radio y calcule el área del círculo correspondiente. 
Recuerda que el área de un círculo se calcula como pi * radio**2."""

def main():
    radio = float(input("Ingresa el radio del círculo: "))
    area_circulo(radio)

def area_circulo(radio):
    area = 3.14159 * radio**2
    print(f"El área del círculo es {area:.2f} u².a")

if __name__ == "__main__":
    main()
    
    