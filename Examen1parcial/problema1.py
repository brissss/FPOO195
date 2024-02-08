
#problema 1
def convertir_temperaturas(temperatura, unidad_origen, unidad_destino):


  if unidad_origen == "fahrenheit":
    temperatura = (temperatura - 32) * 5/9
  elif unidad_origen == "kelvin":
    temperatura = temperatura - 273.15


  if unidad_destino == "fahrenheit":
    temperatura = (temperatura * 9/5) + 32
  elif unidad_destino == "kelvin":
    temperatura = temperatura + 273.15


  return temperatura



opciones = {
  "1": "Convertir de Celsius a Fahrenheit",
  "2": "Convertir de Celsius a Kelvin",
  "3": "Convertir de Fahrenheit a Celsius",
  "4": "Convertir de Fahrenheit a Kelvin",
  "5": "Convertir de Kelvin a Celsius",
  "6": "Convertir de Kelvin a Fahrenheit",
  "7": "Salir"
}

print("Menú de opciones:")
for opcion, descripcion in opciones.items():
  print(f"{opcion}: {descripcion}")



opcion = input("Elige una opción: ")



if opcion == "1":
  temperatura = float(input("Introduce la temperatura en Celsius: "))
  unidad_destino = "fahrenheit"
elif opcion == "2":
  temperatura = float(input("Introduce la temperatura en Celsius: "))
  unidad_destino = "kelvin"
elif opcion == "3":
  temperatura = float(input("Introduce la temperatura en Fahrenheit: "))
  unidad_destino = "celsius"
elif opcion == "4":
  temperatura = float(input("Introduce la temperatura en Fahrenheit: "))
  unidad_destino = "kelvin"
elif opcion == "5":
  temperatura = float(input("Introduce la temperatura en Kelvin: "))
  unidad_destino = "celsius"
elif opcion == "6":
  temperatura = float(input("Introduce la temperatura en Kelvin: "))
  unidad_destino = "fahrenheit"
else:
  print("Opción no válida.")
  exit()


temperatura_convertida = convertir_temperaturas(temperatura, "celsius", unidad_destino)
print(f"La temperatura convertida es {temperatura_convertida} {unidad_destino}.")



