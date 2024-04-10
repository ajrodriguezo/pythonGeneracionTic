"""
2. Escriba un algoritmo para determinar si una palabra es un palíndromo.
Un palíndromo es una palabra que se lee igual al revés que al derecho.
"""

def main():
    palabra = input ("Escribe una palabra: ")
    resultado =  palindormo(palabra)
    print("La palabra es " + ''.join(resultado))
    
def palindormo(pal):
    pal = pal.lower()
    pal = pal.replace(" ", "")
    sal = []
    if pal == pal[::-1]:
        resultado = "un palindromo"
    else:
        resultado = "no es un palindromo"
    return resultado

if __name__ == "__main__":
    main()