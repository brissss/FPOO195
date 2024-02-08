#ejercicio 1
"""numero = int(input("ingresa un numero entero positivo: ")) 
        
suma = 0
for num in range(1,numero):
    if num % 2 != 0:
        suma += num
    print(f"la suma de los numeros pares del 1 al 10 e:  {suma} ")"""
    
#ejercicio 2 - terminado

"""numero = int(input("ingrese un numero entero positivo: "))

for atras in range (numero, -1, -1):
    if atras == 0:
        print(atras)
    else:
        print(atras, end=",")"""

#ejercicio 3 - terminado

"""for i in range(1, 11):
    print("tabla de multiplicar", i)
    for j in range (1,11):
        print(i, "x", j, "=", i*j)
    print()"""
    
#ejercicio 4 - casi terminado
"""numero = int(input("ingrese un numero entero: "))

for i in range(1, numero + 1, 2):
    for j in range(i, 0, - 2):
        print(j, end= "")
    print()"""
   
    
#ejercicio 5 - terminado
"""frase = str(input("ingrese por favor una frase: "))
letra = str(input("ingresd una letra: "))

contador = 0
for letra2 in frase:
    if letra2 == letra:
        contador += 1
print("la letra", letra, "aparece", contador, "veces en la frase.")"""

#ejercicio 6
saldo = 0
while True:
    operacion = input("ingrese una operación, D para depósito, R para retiro: ")
    if operacion == "":
        break
    monto = int(input("Ingrese el monto: "))
    if operacion == "D":
        saldo += monto
    elif operacion == "R":
        saldo -= monto
    print(f"operación: ", operacion, monto, "y", "saldo actual: ", saldo)
print(f"resultado del saldo final: ", saldo)
  yield numero


#ejercicio 7 - terminado
"""numero = int(input("ingrese un numero para la base del arbol: "))

i = numero - 1
j = 1

while i >= 0:
    print(' ' * i + '*' * j + ' ' * i)
    j += 2
    i -= 1"""