

#programa con funciones y un menu que nos permita convertir temperaturas a decision del usuario: centigrados = (fahrenheit - 32) * 5/9,
# fahrenheit = (centigrados * 9/5) + 32 y kelvin = centigrados + 273.15
def centigrados(fahrenheit):
    return ((fahrenheit - 32) * 5/9)

def fahrenheit (centigrados):
    return ((centigrados * 9/5) + 32)

def kelvin (centigrados):
    return (centigrados + 273.15)


def main():
    fahrenheit = int(input("ingrese una temperatura: "))
    conversion_centigrados = centigrados (fahrenheit)
    
    print(f"los grados a centigrados son: {conversion_centigrados}")
    

    centigrados = int(input("ingrese otra temperatura: "))
    conversion_fahrenheit = fahrenheit (centigrados)
    
    print(f"el volumen del cilindro es: {conversion_fahrenheit}")
    
    centigrados = int(input("ingrese una temperatura: "))
    conversion_kelvin = kelvin (centigrados)
    
    print(f"el volumen del cilindro es: {conversion_kelvin}")

main()



