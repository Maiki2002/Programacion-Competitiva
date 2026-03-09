def decoding(palabra):
    palabraDecodificada = [""] * (len(palabra))
    contador = 1
    contadorIn = 0
    contadorFin = 1

    while( contador <= len(palabra)):
        if contador % 2:
            print("Colocando en la posición: " + str(len(palabra)-contadorFin) + " la letra " + str(palabra[len(palabra)-contador]))
            palabraDecodificada[len(palabra)-contadorFin] = palabra[len(palabra)-contador]
            contadorFin += 1
        else:
            print("Colocando en la posición: " + str(contadorIn) + " la letra " + str(palabra[len(palabra)-contador]))
            palabraDecodificada[contadorIn] = str(palabra[len(palabra)-contador])
            contadorIn += 1
        contador += 1
    print(palabraDecodificada)

palabra = input("Ingresa la palabra: ")
decoding(list(palabra))
