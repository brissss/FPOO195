from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador if denominador != 0 else 1

    def simplificar(self):
        divisor_comun = gcd(self.__numerador, self.__denominador)
        self.__numerador //= divisor_comun
        self.__denominador //= divisor_comun

    def sumar(self, otra):
        nuevo_numerador = self.__numerador * otra.__denominador + self.__denominador * otra.__numerador
        nuevo_denominador = self.__denominador * otra.__denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def restar(self, otra):
        nuevo_numerador = self.__numerador * otra.__denominador - self.__denominador * otra.__numerador
        nuevo_denominador = self.__denominador * otra.__denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def multiplicar(self, otra):
        nuevo_numerador = self.__numerador * otra.__numerador
        nuevo_denominador = self.__denominador * otra.__denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def dividir(self, otra):
        nuevo_numerador = self.__numerador * otra.__denominador
        nuevo_denominador = self.__denominador * otra.__numerador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __str__(self):
        return f"{self.__numerador}/{self.__denominador}"
