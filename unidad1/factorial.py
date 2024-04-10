"""
1. Escriba un algoritmo para calcular la factorial de un número. 
Recuerda que la factorial de un número n es el producto de todos los 
números enteros positivos desde 1 hasta n.
"""

def main():
    numero = int(input("Escribe un numero: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

if __name__ == "__main__":
    main()