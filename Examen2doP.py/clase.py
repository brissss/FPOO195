from tkinter import Tk, Frame, Label, Entry, Button, Checkbutton, messagebox
import tkinter as tk

class GeneradorM:
    def __init__(self, longitud=8, incluir_mayusculas=True, incluir_caracteres_especiales=True):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.nacimiento = nacimiento
        self.carrera = carrera
    
    def generar_matricula(self):
        
    
    
    def generar():
        ventana = Tk()
        ventana.title("Generador de Matriculas :)")
        ventana.geometry("850x400")
        
        seccion1 = Frame(ventana)
        seccion1.pack(pady=20)
        
        Label(seccion1, text="Matriculas Escolares", font=("Helvetica", 30)).pack()
        
        Label(seccion1, text="Nombre: ").pack()
        nombre_entry = Entry(seccion1)
        nombre_entry.pack()
        
        Label(seccion1, text="Apellido Paterno: ").pack()
        apep_entry = Entry(seccion1)
        apep_entry.pack()
        
        Label(seccion1, text="Apellido Materno: ").pack()
        apem_entry = Entry(seccion1)
        apem_entry.pack()
        
        Label(seccion1, text="Año de Nacimiento: ").pack()
        nacimiento_entry = Entry(seccion1)
        nacimiento_entry.pack()
        
        Label(seccion1, text="Carrera: ").pack()
        carrera_entry = Entry(seccion1)
        carrera_entry.pack()
        
        Label(seccion1, text="Matricula").pack()
        generada_entry = Entry(seccion1)
        generada_entry.pack()
        
        ventana.mainloop()