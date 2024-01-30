#ejercicio 1

"""numero = int(input("ingresa un numero entero positivo: "))

for numero in range (1, numero + 1, 2):
    print(end, )
    
    or num in range(1,11):
    if num % 2 == 1:
        suma += num
    print("los numeros son los siguientes:  ")"""
    
#ejercicio 2

"""numero = int(input("ingrese un numero entero positivo: "))

while contador <= numero:
      print(contador)
      contador <= 0
else:
    print("el bucle ha terminado normalmente")"""
    


#ejercicio 3

"""contador = 1
while contador <= 5:
    print(contador)
    #colocar aqui el print, para que el bucle imprima el 3
    if contador == 10: #para que el bucle termine al mo
        break
    print(contador)
    contador <= 1
else:
    print("el bucle se ha terminado")
    print("la tabla de multiplicar se ha mostrado correctamente")"""

#ejercicio 4

#numero = int(input("ingrese un numero entero: "))

#ejercicio 5
palabra = str(input("ingrese una palabra: "))
letra = str(input("ingrese una letra: "))
contador_letra = 0
for letra in palabra:
    if letra.lower() in palabra:
        contador_letra += 1
        
    print(f"la palabra", palabra, "tiene", contador_letra, "letras.")