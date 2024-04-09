from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *
from GeneradorPDF import *
import os

objControlador = Controlador()
objPDF = GeneradorPDF()

def ejecutarInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())

def ejecutarBusqueda():
    usuarioBD = objControlador.buscarUsuario(varBus.get())
    if txtBusquedaUsuario:  
        txtBusquedaUsuario.delete('1.0', END)  
        if usuarioBD:
            for usuario in usuarioBD:
                txtBusquedaUsuario.insert(END, f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}\n")
        else:
            txtBusquedaUsuario.insert(END, "No se encontró el usuario.")

#funcion consultar usuario
def ejecutarUsuarios():
    usuarios = objControlador.mostrarTodosUsuarios()
    texto_usuarios = ''
    for usuario in usuarios:
        texto_usuarios += f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}, Contrasena: {usuario[3]}\n"
    
    textRegistrototal.delete(1.0, "end")
    textRegistrototal.insert("end", texto_usuarios)

#funcion para ejecutar o crear el pdf
def ejecutaPDF():
    if varTitulo== "":
        messagebox.showwarning("Importante", "Escribe un nombre al pdf")
    else:
        objPDF.add_page()
        objPDF.chapter_body()
        objPDF.output(str(varTitulo.get() + ".pdf"))
        rutaPDF = "/Users/brissgarcia/Documents/GitHub/FPOO195/tkinter_SQLite/" + varTitulo.get() + ".pdf"
        messagebox.showinfo("Archivo creado", "PDF disponible en carpeta")
        os.system(f"start {rutaPDF}")
    

       

#1. crear ventana
ventana  = Tk()
ventana .title("CRUD de Usuarios")
ventana.geometry("800x600")

#2. preparar el notebook para las pestañas
panel= ttk.Notebook(ventana)
panel.pack(fill='both', expand="yes")

#3. definimos las pestañas del notebook
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)
pestana6 = ttk.Frame(panel)

#4. agregamos las pestañas
panel.add(pestana1, text="Crear Usuario")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="Consultar Usuarios")
panel.add(pestana4, text="Editar Usuario")
panel.add(pestana5, text="Borrar Usuario")
panel.add(pestana6, text="Exportar PDF")

#5 pestaña 1:formulario de insert
Label(pestana1, text="Registro de Usuarios", fg="red", font=("modern",25)).pack()


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

#6 pestaña 2: buscar ususario
Label(pestana2, text="Buscar Usuario", fg="red", font=("modern",25)).pack()

varBus = tk.StringVar()
Label(pestana2, text="Id: ").pack()
Entry(pestana2, textvariable=varBus).pack()

Button(pestana2, text="Buscar Usuario", command=ejecutarBusqueda).pack()

Label(pestana2, text="Registrado", fg="white", font=("modern",18)).pack()
#tk.Text(pestana2, height=5, width=52).pack()
txtBusquedaUsuario = tk.Text(pestana2, height=5, width=60)
txtBusquedaUsuario.pack()

#7 pestaña 3: consultar usuarios
Label(pestana3, text="Consultar Usuarios", fg="white", font=("Modern", 18)).pack()

Button(pestana3, text="Consultar", command=ejecutarUsuarios).pack()

Label(pestana3, text="Todos los Registros", fg="white", font=("mono", 18)).pack()
textRegistrototal = tk.Text(pestana3, height=30, width=120)
textRegistrototal.pack()

#8 pestaña 4: editar usuario
Label(pestana4, text="Editar Usuario", fg="white", font=("Modern", 25)).pack()

#9 pestaña 5: borrar usuario
Label(pestana5, text="Borrar Usuario", fg="white", font=("Modern", 25)).pack()

#10 pestaña 6: reportes en pdf
Label(pestana6, text="Reporte Usuarios en PDF", fg="red", font=("Modern", 25)).pack()

varTitulo = tk.StringVar()
Label(pestana6, text="Titulo del archivo:", fg="white", font=("Modern", 12)).pack()
Entry(pestana6, textvariable=varTitulo).pack()

Button(pestana6, text="Crear Reporte PDF", command=ejecutaPDF).pack()

ventana.mainloop()