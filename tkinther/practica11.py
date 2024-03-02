from tkinter import Tk

#1.Creamos la ventana
Ventana = Tk() #uso de POO creando un objeto ventana
Ventana.title("ejemplo con 3 frames")
Ventana.geometry("600x400")

#2. colocamos frames de la ventana
seccion1 = Frame(Ventana, bg="red")
seccion1.pack(expand= True, fill='both')

seccion2 = Frame(Ventana, bg="yellow")
seccion2.pack()

seccion3 = Frame(Ventana, bg="black")
seccion3.pack()

#ejecuta la ventana
Ventana.mainloop()