"""Escribe dos funciones, celsius_a_fahrenheit y fahrenheit_a_celsius, 
que conviertan temperaturas de una escala a otra."""

def main():
    print("Bienvenido al conversor de temperaturas.")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = int(input("¿Qué conversión deseas realizar? "))
    if opcion == 1:
        celsius_a_fahrenheit()
    elif opcion == 2:
        fahrenheit_a_celsius()
    else:
        print("Opción inválida.")

def celsius_a_fahrenheit():
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C es equivalente a {fahrenheit:.2f}°F.")

def fahrenheit_a_celsius():
    fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F es equivalente a {celsius:.2f}°C.")
    
if __name__ == "__main__":
    main()