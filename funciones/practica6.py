#ejercicio 1

def factura_total(cantidad_inicial, iva = 21):
    return cantidad_inicial + (cantidad_inicial * iva/100)
    
def main():
    cantidad_inicial = float(input("ingresar la factura inicial: "))
    factura_final = factura_total (cantidad_inicial)
    
    print(f"el total de la factura es: {factura_final}")
   
   
main()

#ejercicio 2


