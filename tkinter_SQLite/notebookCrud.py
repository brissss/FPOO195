from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

objControlador = Controlador()

def ejecutarInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())
    

#1. crear ventana
ventana  = Tk()
ventana .title("CRUD de Usuarios")
ventana.geometry("500x300")

#2. preparar el notebook para las pestañas
panel= ttk.Notebook(ventana)
panel.pack(fill='both', expand="yes")

#3. definimos las pestañas del notebook
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

#4. agregamos las pestañas
panel.add(pestana1, text="Crear Usuario")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="Consultar Usuarios")
panel.add(pestana4, text="Editar Usuario")
panel.add(pestana5, text="Eliminar Usuario")

#5 pestaña 1:formulario de insert
Label(pestana1, text="Registro de Usuarios", fg="blue", font=("modern",18)).pack()


var1 = tk.StringVar()
Label(pestana1, text="Nombre: ").pack()
Entry(pestana1, textvariable=var1).pack()

var2 = tk.StringVar()
Label(pestana1, text="Correo: ").pack()
Entry(pestana1, textvariable=var2).pack()

var3 = tk.StringVar()
Label(pestana1, text="Contraseña: ").pack()
Entry(pestana1, textvariable=var3).pack()

btn_guardar = tk.Button(pestana1, text="Guardar usuario", command=ejecutarInsert)
btn_guardar.pack()

ventana.mainloop()