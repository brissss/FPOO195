#ejercicio 1
contraGuardada = "Briseidagarcia"

contraSolicitada = input("Ingrese la contraseña: ")

if contraGuardada.lower() == contraSolicitada.lower():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta, ingrese de nuevo.")


#ejercicio 2
numero = int(input("ingresa un numero entero: "))
if numero % 2 == 0:
    print("el numero ingresado es par")
else:
    print("el numero ingresado es impar")
    
#ejercicio 3
edad = int(input("Ingrese su edad: "))

if edad < 4:
    costo_entrada = 0 
elif 4 <= edad <= 18:
    costo_entrada = 110  
else:
    costo_entrada = 190  

print("El precio de la entrada para un cliente de", edad, "años es:", costo_entrada)

#ejercicio 4
cadena = str(input("ingrese una palabra: "))
cadena = cadena.replace("", "").lower()
    

if cadena == cadena[::-1]:
        print("La cadena es un palíndromo.")
else:
        print("La cadena no es un palíndromo.")



      

