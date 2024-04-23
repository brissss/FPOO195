#5. Se requiere un programa que procese una lista que guarde N números a petición
#del usuario una vez completada la lista el programa debe imprimir 2 resultados la
#sumatoria de los números pares y la sumatoria de los números impares:



lista = int(input("Ingrese la cantidad de números que desea ingresar: "))

numeros = []
for i in range(lista):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)


suma_pares = 0
suma_impares = 0

for num in numeros:
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num


print(f"La sumatoria de los numeros pares es: {suma_pares}")
print(f"La sumatoria de los numeros impares es: {suma_impares}")
    




