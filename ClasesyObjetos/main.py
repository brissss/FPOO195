# esta forma es para importar todo lo que tiene el archivo
# en este caso el archivo se llama 'Personaje', tambien la clase

from Personaje import *
from Armas import *

#solicitar datos del spartan:
nombreS = input('Escribe el nombre de tu Spartan:\n ')
especieS = input('Escribe la Especie de tu Spartan:\n')
alturaS = float(input('Ingresa la altura de tu Spartan:\n '))

# datos del nemesis
print("")
nombreN = input('Escribe el nombre de tu Nemesis:\n ')
especieN = input('Escribe la Especie de tu Nemesis:\n')
alturaN = float(input('Ingresa la altura de tu Nemesis:\n '))

spartan = Personaje(especieS,nombreS,alturaS)
nemesis = Personaje(especieN,nombreN,alturaN)
Arma = Armas()

print('===== Datos del Spartan ======')
print(spartan.getNombre())
print(spartan.getEspecie())
print(spartan.getAltura())
print("")

# atributos nemesis 
print('===== Datos del villano ======')
print(nemesis.getNombre())
print(nemesis.getEspecie())
print(nemesis.getAltura())
print("")

spartan.__pensar()
