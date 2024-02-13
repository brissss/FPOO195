"""1. Sumatoria de los elementos de la lista
2. Numero mayor de la lista
3. Numero menor de la lista
4. Promedio
5. Moda: es el valor que más se repite de un conjunto de datos
6. Rango: es la diferencia entre el valor máximo y el valor mínimo de un
conjunto de datos"""

def crear_tupla():
  n = int(input("Ingrese los numeros que decea que contenga su tupla: "))
  tupla = ()
  for i in range(n):
    numero = int(input(f"Ingrese el numero de la posicion {i + 1}: "))
    tupla += (numero,)
  return tupla


def sumatoria(tupla):
  sumatoria = 0
  for numero in tupla:
    sumatoria += numero
  return sumatoria


def numero_mayor(tupla):
  numero_mayor = tupla[0]
  for numero in tupla:
    if numero > numero_mayor:
      numero_mayor = numero
  return numero_mayor


def numero_menor(tupla):
  numero_menor = tupla[0]
  for numero in tupla:
    if numero < numero_menor:
      numero_menor = numero
  return numero_menor


def promedio(tupla):
  sumatoria = sumatoria(tupla)
  n = len(tupla)
  promedio = sumatoria / n
  return promedio


def moda(tupla):
  frecuencias = {}
  for numero in tupla:
    if numero not in frecuencias:
      frecuencias[numero] = 1
    else:
      frecuencias[numero] += 1
  moda = max(frecuencias, key=frecuencias.get)
  return moda


def rango(tupla):
  numero_mayor = numero_mayor(tupla)
  numero_menor = numero_menor(tupla)
  rango = numero_mayor - numero_menor
  return rango


def menu():
  print("menu funcional:")
  print("1. Sumatoria de los elementos de la lista")
  print("2. Numero mayor de la lista")
  print("3. Numero menor de la lista")
  print("4. Promedio")
  print("5. Moda: es el valor que más se repite de un conjunto de datos")
  print("6. Rango: es la diferencia entre el valor maximo y el valor minimo de un conjunto de datos")
  opcion = int(input("Elija una opcion: "))
  return opcion


def main():
  tupla = crear_tupla()
  opcion = menu()
  if opcion == 1:
    print(f"La sumatoria de los elementos de la tupla es {sumatoria(tupla)}")
  elif opcion == 2:
    print(f"El numero mayor de la tupla es {numero_mayor(tupla)}")
  elif opcion == 3:
    print(f"El numero menor de la tupla es {numero_menor(tupla)}")
  elif opcion == 4:
    print(f"El promedio de los elementos de la tupla es {promedio(tupla)}")
  elif opcion == 5:
    print(f"La moda de la tupla es {moda(tupla)}")
  elif opcion == 6:
    print(f"El rango de la tupla es {rango(tupla)}")
  else:
    print("Opcion no valida")


if __name__ == "__main__":
  main()