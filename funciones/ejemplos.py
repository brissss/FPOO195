#ejemplo 1
def suma(*numeros):
   resultado= sum (numeros)
   print("suma:", resultado)
suma(1,2,3,4)

#ejemplo 2
import math 

def area_cuadrado(lado):
   return lado ** 2

def main():
   lado_cuadrado=float(input("ingrese el valor del lado: "))
   area_result = area_cuadrado(lado_cuadrado)

   print(f"area del cuadrado: {area_result}")
   
main()
