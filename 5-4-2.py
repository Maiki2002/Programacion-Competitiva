def decoding(palabra):
    palabraDecodificada = []
    posicion = 0

    while len(palabra) > 0:
        print(palabra)

        if(len(palabra)%2):
            print("Lista impar")
            print("Insertando en " + str((len(palabraDecodificada)-1)-posicion) + " la palabra " + str(palabra[0]))
            palabraDecodificada.insert((len(palabraDecodificada)-1)-posicion, palabra[0])
            palabra.pop(0)
            posicion = posicion + 1
        else:
            print("Lista par")
            print("Insertando en " + str(posicion) + " la palabra " + str(palabra[0]))
            palabraDecodificada.insert(posicion, palabra[0])
            palabra.pop(0)
            posicion = posicion + 1

        print("Palabra Decodificada: "+ str(palabraDecodificada))

palabra = input("Ingresa la palabra: ")
decoding(list(reversed(palabra)))
