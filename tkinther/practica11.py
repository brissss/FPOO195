from tkinter import Tk, Frame, Button, messagebox

#metodo para mensaje
def mostrarMensajes():
    print(messagebox.showinfo('showinfo', 'information'))
    print(messagebox.showerror('showinfo', 'error'))
    print(messagebox.showwarning('showinfo', 'warning'))
    print(messagebox.askokcancel(message= "¿Desea continuar?",title="soy el titulo"))

#
def addbtn():
    botonVerde.config(text="+")
    botonRosa = Button(seccion3, text="Nuevo", bg="#06e813", fg="black" )
    botonRosa.configure(height=2, width=10)
    botonRosa.pack()


#1.Creamos la ventana
Ventana = Tk() #uso de POO creando un objeto ventana
Ventana.title("ejemplo con 3 frames")
Ventana.geometry("600x400")

#2. colocamos frames de la ventana
seccion1 = Frame(Ventana, bg="red")
seccion1.pack(expand= True, fill='both')

seccion2 = Frame(Ventana, bg="yellow")
seccion2.pack(expand= True, fill='both')

seccion3 = Frame(Ventana, bg="blue")
seccion3.pack(expand= True, fill='both')



#posiocionar botones

#place
botonAzul = Button(seccion1, text="azul", bg="#000000", fg="black" )
botonAzul.place(x=60, y=60, width=100, height=30)

#grid
botonNegro = Button(seccion2, text="negro", bg="black", fg="black" )
botonNegro.configure(height=2, width=10)
botonNegro.grid(row= 0, column=1)

botonAmarillo = Button(seccion2, text="amarillo", bg="yellow", fg="black", command=mostrarMensajes )#command ligar el mensaje con el boton
botonAmarillo.configure(height=2, width=10)
botonAmarillo.grid(row= 0, column=2)

#pack
botonVerde = Button(seccion3, text="black", bg="#06e813", fg="black", command=addbtn)
botonVerde.configure(height=2, width=10)
botonVerde.pack()



#ejecuta la ventana
Ventana.mainloop()