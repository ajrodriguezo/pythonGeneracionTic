musica = [('Yellow Submarine', 'The Beatles',9.2),
            ('The Wall', 'Pink Floyd',9.0),
            ('Revolver', 'The Beatles',8.8),
            ('London Calling', 'The Clash',9.3),
            ('Born to Run', 'Bruce Springsteen',9.7),
            ('Who\'s Next', 'The Who',9.6)]

def buscar_cancion(nombre):
    for cancion in musica:
        if cancion[0].upper() == nombre.upper():
            return cancion
    return "Canción no encontrada"

def buscar_artista(artista):
    canciones_artista = []
    for cancion in musica:
        if cancion[1].upper() == artista.upper():
            canciones_artista.append(cancion)
    return canciones_artista

def main():
    print("Catálogo de canciones")
    print("1. Buscar por nombre canción")
    print("2. Buscar por artista")
    print("3. Salir")
    
    opcion = int(input("¿Qué operación deseas realizar? :"))
    
    if opcion == 1:
        nombre = input("Ingresa el nombre de la canción: ")
        resultado = buscar_cancion(nombre)
        print(resultado)
        
    elif opcion == 2:
        artista = input("Ingresa el nombre del artista: ")
        resultado = buscar_artista(artista)
        for cancion in resultado:
            print(cancion)
    
    elif opcion == 3:
        print("Gracias por usar el catálogo de canciones.")

if __name__ == "__main__":
    main()

#34261