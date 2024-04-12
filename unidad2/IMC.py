def main():
    peso = float(input("Introduce tu peso en kg: "))
    altura = float(input("Introduce tu altura en metros: "))
    imc(peso, altura)

def imc(peso, altura):
    imc = round(peso / (altura ** 2), 2)
    print("Tu índice de masa corporal es", imc)
    if imc < 18.5:
        print("Estás bajo de peso")
    elif imc < 24.9:
        print("Estás en tu peso ideal")
    elif imc < 29.9:
        print("Tienes sobrepeso")
    else:
        print("Tienes obesidad")    
        
    

if __name__ == "__main__":
    main()