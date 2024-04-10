def main():
    palabra = input ("Escribe una palabra: ")
    resultado =  twttrr(palabra)
    print("La palabra es: " + ''.join(resultado))
    
def twttrr(pal):
    pal = pal.lower()
    sal = []
    for z in range(len(pal)):
        if pal[z] not in ["a", "e", "i", "o", "u", " "]:
            sal.append(pal[z])
    return sal
    
if __name__ == "__main__":
    main()