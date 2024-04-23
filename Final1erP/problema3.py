#3. Realiza un programa que solicite 10 números y los almacene en una lista, una vez
#completada el usuario tendrá 2 opciones a elegir:
#1. Imprimir lista invertida
#2. Imprimir lista sin números repetidos


numeros = []
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)


print("Elige alguna de las opciones:")
print("1. Imprimir lista invertida")
print("2. Imprimir lista sin numeros repetidos")
opcion = int(input("Opcion: "))


if opcion == 1:
    lista_invertida = numeros[::-1]
    print("Lista invertida:", lista_invertida)


elif opcion == 2:
    lista_sin_repetidos = list(set(numeros))
    print("Lista sin numeros repetidos: ", lista_sin_repetidos)


else:
    print("Opcion invalida.")