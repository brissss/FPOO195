def invertirFrase (fraseSolicitada):
     return fraseSolicitada [::-1]

frase = str(input("Ingrese la frase a invertir: "))

fraseInvertida = invertirFrase(frase)

print("La frase invertida es: ", fraseInvertida)