"""a. Contar número repetidos
b. Eliminar numero repetidos
c. Remplazar los repetidos con 0"""

import random


lista = [random.randint(10, 20) for i in range(30)]
print("lista llena:", lista)


repetidos = 0
for i in range(len(lista)):
  for j in range(i + 1, len(lista)):
    if lista[i] == lista[j]:
      repetidos += 1

repetidos =  repetidos / 2   #porque hay dos veces la misma pareja de numeros

print("numero de elementos repetidos: ", repetidos)



lista_sin_repetidos = []
for elemento in lista:
  if elemento not in lista_sin_repetidos:
    lista_sin_repetidos.append(elemento)

print("lista sin elementos repetidos:", lista_sin_repetidos)



for i in range(len(lista)):
  for j in range(i + 1, len(lista)):
    if lista[i] == lista[j]:
      lista[j] = 0

print("lista con los elementos repetidos reemplazados por 0:", lista)