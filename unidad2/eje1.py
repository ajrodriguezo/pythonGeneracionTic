"""Escribe una función saludo que acepte un argumento de nombre y retorne un saludo personalizado.
Por ejemplo, saludo('Alice') debería retornar '¡Hola, Alice!'."""

def main():
    nombre = input("Ingresa tu nombre: ")
    saludo(nombre)

def saludo(nombre):
    print(f"¡Hola, {nombre}!")
    
if __name__ == "__main__":
    main() 
    
    