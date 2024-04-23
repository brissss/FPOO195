#4. Crea un programa que solicite un numero de 3 dígitos, validar que se cumpla
#siempre esta condición, con el numero de 3 dígitos calcula el valor de suma de
#sus dígitos, Ejemplo numero=435 - Resultado: 12


numero = input("Ingrese un número de 3 dígitos: ")

while len(numero) != 3 or not numero.isdigit():
    numero = input("Ingrese un número de 3 dígitos: ")


suma_digitos = 0
for digito in numero:
    suma_digitos += int(digito)


print(f"El número ingresado es: {numero}")
print(f"La suma de sus dígitos es: {suma_digitos}")