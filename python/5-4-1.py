def palabrasAbreviadas(contador):
    data = input("Ingrese la palabra " + str(contador+1) + " : ")

    if len(data)-1 < 100:
        if len(data) > 10:
            abr = str(data[0]) + str(len(data)-2) + str(data[len(data)-1])
            return abr 
        else:
            return data
    else:
        print("Máximo 100 caracteres")
    

x = int(input("Ingrese cuantas palabras ingresará: "))
palabras = []

if x <= 100 | x >= 1:
    for lineas in range(0,x):
        palabras.append(palabrasAbreviadas(lineas))

    for palabra in palabras:
        print(palabra)
else:
    print("El valor debe ser entre 1 y 100")