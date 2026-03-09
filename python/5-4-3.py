def identificarSaludo(palabra):
    saludo = "hello"
    contador = 0
    for n in palabra:
        if(n == saludo[contador]):
            contador += 1
            if contador == len(saludo):
                print("YES")
                return

    print("NO")

palabra = input("Ingrese la palabra: ")
identificarSaludo(palabra)