
#problema 2
def generar_multiplos_de_10():
  numero = 10
  while numero <= 10000:
    yield numero

    numero += 10

multiplos_de_10 = generar_multiplos_de_10()

for multiplo_de_10 in multiplos_de_10:
  print(multiplo_de_10)