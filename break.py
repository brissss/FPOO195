#ejemplo 1

contador = 1
while contador <= 5:
    #colocar aqui el print, para que el bucle imprima el 3
    if contador == 3: #para que el bucle termine al momento de llegar al 3
        break
    print(contador)
    contador += 1
else:
    print("el bucle se ha terminado")