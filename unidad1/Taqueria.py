def main():

    menu={
        "TACOS": 1.25,
        "BURRITOS": 8.00,
        "QUESADILLAS": 7.50,
        "TORTAS": 4.50,
        "TAMALES": 1.75,
        "SOPES": 6.25,
        "CHURROS": 1.00,
        "HORCHATA": 1.50,
        "JAMAICA": 1.50,
        "COCA-COLA": 0.25,
        "JARRITOS": 1.50,
    }
    order_total = 0.0
    while True:
        try:
            item = input("Que deseas ordenar? ")
        except EOFError:
            break 
        item = item.upper()
        if item in menu:
            order_total += menu[item]
            print(f"El precio de {item} es ${menu[item]}")
            print(f"El precio de su orde es ${order_total}")
        elif item == "CONTROL-D":
            print(f"El total de su orden es ${order_total}")
            break
        else:
            print(f"Lo siento, no tenemos {item} en el menu")
            
if __name__ == "__main__":
    main()