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
        numeros = '0123456789'

        todos_los_caracteres = caracteres_minusculas
        if self.incluir_mayusculas:
            todos_los_caracteres += caracteres_mayusculas
        if self.incluir_caracteres_especiales:
            todos_los_caracteres += caracteres_especiales
        todos_los_caracteres += numeros

        contrasena = ''.join(random.choice(todos_los_caracteres) for _ in range(self.longitud))
        return contrasena

def mostrar_contrasena(password):
    messagebox.showinfo("Contraseña generada", f"Contraseña generada: {password}")

def generar():
    ventana = Tk()
    ventana.title("Generador de Contraseñas :)")
    ventana.geometry("850x400")

    seccion1 = Frame(ventana)
    seccion1.pack(pady=20)

    Label(seccion1, text="Generador de Contraseñas", font=("Helvetica", 30)).pack()

    Label(seccion1, text="Longitud: ").pack()
    longitud_entry = Entry(seccion1)
    longitud_entry.pack()

    incluir_mayusculas = tk.BooleanVar()
    Checkbutton(seccion1, text="Incluir mayúsculas", variable=incluir_mayusculas).pack()

    incluir_caracteres = tk.BooleanVar()
    Checkbutton(seccion1, text="Incluir caracteres especiales", variable=incluir_caracteres).pack()
    
    Label(seccion1, text="Contraseña generada").pack()
    generada_entry = Entry(seccion1)
    generada_entry.pack()

    def generar_contrasena():
        try:
            longitud = int(longitud_entry.get())
            contrasena_generada = Generador(longitud, incluir_mayusculas.get(), incluir_caracteres.get()).generar_contrasena()
            mostrar_contrasena(contrasena_generada)
            generada_entry.delete(0, tk.END)
            generada_entry.insert(0, contrasena_generada)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese una longitud válida.")

    Button(seccion1, text="Generar Contraseña", command=generar_contrasena).pack()

    ventana.mainloop()
    
    def copiar_contraseña():
        Button(ventana, text="Copiar Contraseña", command=copiar_contraseña)

generar()
