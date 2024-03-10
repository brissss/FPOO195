from tkinter import Tk, Frame, Label, Entry, Button, Checkbutton, messagebox
import random
import tkinter as tk

class Generador:
    def __init__(self, longitud=8, incluir_mayusculas=True, incluir_caracteres_especiales=True):
        self.longitud = longitud
        self.incluir_mayusculas = incluir_mayusculas
        self.incluir_caracteres_especiales = incluir_caracteres_especiales

    def generar_contrasena(self):
        caracteres_minusculas = 'abcdefghijklmnopqrstuvwxyz'
        caracteres_mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        caracteres_especiales = '!@#$%^&*()-_=+[]{};:,.<>?'

        todos_los_caracteres = caracteres_minusculas
        if self.incluir_mayusculas:
            todos_los_caracteres += caracteres_mayusculas
        if self.incluir_caracteres_especiales:
            todos_los_caracteres += caracteres_especiales
        todos_los_caracteres += numeros

        contrasena = ''.join(random.choice(todos_los_caracteres) for _ in range(self.longitud))
        return contrasena

