def main():
    masa = float(input("Introduce tu masa en kg: "))
    energia(masa)

def energia(masa):
    energia = masa * 299792458 ** 2
    print("La energía que se libera es", energia, "julios")
    if energia < 1.0 * 10 ** 9:
        print("La energía liberada es menor a 1 GJ")
    elif energia < 1.0 * 10 ** 12:
        print("La energía liberada es menor a 1 TJ")
    elif energia < 1.0 * 10 ** 15:
        print("La energía liberada es menor a 1 PJ")
    else:
        print("La energía liberada es mayor a 1 PJ")

if __name__ == "__main__":
    main()