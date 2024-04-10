"""
3. Implementa un algoritmo que ordene una lista de números de menor a mayor. 
Puedes usar cualquier algoritmo de ordenación que prefieras.
"""

def main():
    num = input ("Escribe una serie de números separados por coma: ")
    resultado =  ordenar(num)
    print("La serie ordenada es " + ''.join(resultado))

def ordenar(num):
    num = num.split(",")
    num.sort()
    return num

if __name__ == "__main__":  
    main()  
    