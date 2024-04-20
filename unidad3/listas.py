def main():
    shopping_list = []
    
    while True:
        print("Lista de compras")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar lista")   
        print("4. Salir")   
        
        opcion = int(input("¿Qué operación deseas realizar? :"))
        
        if opcion == 1:
            producto = input("Ingresa el producto: ")
            shopping_list.append(producto)
        elif opcion == 2:
            try:
                producto = input("Ingresa el producto a eliminar: ")
                shopping_list.remove(producto)
            except ValueError:
                print("El producto no se encuentra en la lista.")
        elif opcion == 3:
            print("Lista de compras:")
            for producto in shopping_list:
                print(producto)
        elif opcion == 4:
            print("Gracias por usar la lista de compras.")
            break   
        else:   
            print("Opción inválida.")

if __name__ == "__main__":
    main()