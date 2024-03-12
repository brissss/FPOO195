import tkinter as tk
from tkinter import Tk, messagebox, simpledialog  

class matricula:
    def __init__(self, master):
        self.master = master
        master.title("Matriculas Escolares")
        
        #inputs
        self.nombre_label = tk.Label(master, text="Nombre:")
        self.nombre_entry = tk.Entry(master)
        self.apep_label = tk.Label(master, text="Apellido Paterno:")
        self.apep_entry = tk.Entry(master)
        self.apem_label = tk.Label(master, text="Apellido Materno:")
        self.apem_entry = tk.Entry(master)
        self.nacimiento_label = tk.Label(master, text="Año de nacimiento:")
        self.nacimiento_entry = tk.Entry(master)
        self.carrera_label = tk.Label(master, text="Carrera:")
        self.carrera_entry = tk.Entry(master)
        
        #botones
        self.generar_btn = tk.Button(master, text="Generar Matricula") #command=)
        
        #ejecutar ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = matricula(root)
    root.mainloop()
        
        