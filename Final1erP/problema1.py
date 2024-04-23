# 1. Se necesita una lista donde el usuario introduzca 6 palabras, completada la lista
# el programa debe ordenar la lista en orden alfabético, como resultado debe
# imprimir la lista original y la lista ordenada. Valor: 4 pts.

   
palabra1 = input("ingrese la primer palabra: ")
palabra2 = input("ingrese la segunda palabra: ")
palabra3 = input("ingrese la tercer palabra: ")
palabra4 = input("ingrese la cuarta palabra: ")
palabra5 = input("ingrese la quinta palabra: ")
palabra6 = input("ingrese la sexta palabra: ")



listaOriginal = [palabra1, palabra2, palabra3, palabra4, palabra5, palabra6]
print(f"La lista original es: {listaOriginal}")


listaOrdenada = sorted(listaOriginal)
print(f"La lista ordenada es: {listaOrdenada}")

