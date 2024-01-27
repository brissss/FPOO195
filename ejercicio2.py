nombre = str( input("Introduce tu nombre completo: "))

print(nombre.upper())

print(nombre.lower())


nombreApellidos = nombre.split()
inicialesMayuscula = [parte[0].upper() for parte in nombreApellidos]
iniciales = ' '.join(inicialesMayuscula)

print(iniciales)
