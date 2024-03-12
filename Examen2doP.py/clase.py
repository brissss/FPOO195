from tkinter import Tk, Frame, Label, Entry, Button, Checkbutton, messagebox
import interfaz
import tkinter as tk

class GeneradorM:
    def __init__(self, nombre, apellido_paterno, apellido_materno, nacimiento, carrera):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.nacimiento = nacimiento
        self.carrera = carrera
        self.ano = '2024'
        self.digitos_aleatorios = '1234567890'
    
        
def mostrar_matricula(matricula):
    messagebox.showinfo("Matricula generada", f"Matricula generada: {matricula}")
        
        
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
    
    
    
        
        
            
    def generar_matricula():
        try:
            nombre = str(nombre_entry.get())
            apellidoP = str(nombre_entry.get())
            apellidoM = str(nombre_entry.get())
            matricula_generada = GeneradorM(nombre, apellidoP, apellidoM).generar_matricula()
            mostrar_matricula(matricula_generada)
            generada_entry.delete(0, tk.END)
            generada_entry.insert(0, matricula_generada)
        except ValueError:
            messagebox.showerror("Error", "Por favor llene todos los campos.")
            
    Button(seccion1, text="Generar Matricula", command=generar_matricula).pack()
        
    ventana.mainloop()

generar()