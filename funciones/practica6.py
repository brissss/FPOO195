#ejercicio 1

def factura_total(cantidad_inicial, iva = 21):
    return cantidad_inicial + (cantidad_inicial * iva/100)
    
def main():
    cantidad_inicial = float(input("ingresar la factura inicial: "))
    factura_final = factura_total (cantidad_inicial)
    
    print(f"el total de la factura es: {factura_final}")
   
   
main()

#ejercicio 2 - terminado
#Escribir una función que calcule el área de un círculo y otra que
#calcule el volumen de un cilindro usando la primera función.

"""def area_circulo(radio, pi = 3.1416):
    return (pi * (radio*radio))

def volumen_cilindro (area_final, altura):
    return (area_final * altura)


def main():
    radio = float(input("ingrese el radio del circulo: "))
    area_final = area_circulo (radio)
    
    print(f"el area del circulo es: {area_final}")
    

    altura = float(input("ingrese la altura del cilindro: "))
    volumen_final = volumen_cilindro (area_final, altura)
    
    print(f"el volumen del cilindro es: {volumen_final}")

main()"""

#ejercicio 3
#Escribir una función que convierta un número decimal en binario y
#otra que convierta un número binario en decimal.

"""def decimal_a_binario (decimal):
  return bin(decimal).replace("0b", "")

def binario_a_decimal (binario):
    return int(binario, 2)

def main():
    decimal = int(input("ingrese un numero decimal entero: "))
    conversion_decimal = decimal_a_binario (decimal)
    
    print (f"el numero decimal ingresado en binario es igual a: {conversion_decimal}")
    

    binario = input("ingrese un numero binario: ")
    conversion_binario = binario_a_decimal (binario)
    
    print (f"el numero binario ingresado en decimal es: {conversion_binario}")
    
main()"""

