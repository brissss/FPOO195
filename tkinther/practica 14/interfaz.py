import tkinter as tk
from tkinter import messagebox

from clase import *

def consultar_datos():
    num_cuenta = cuenta_entry.get()
    cuenta = cuentas.get(num_cuenta)
    if cuenta:
        titular_var.set(cuenta.titular)
        edad_var.set(cuenta.edad)
        saldo_var.set(cuenta.consultar_saldo())
    else:
        messagebox.showerror("Error", "Cuenta no registrada.")

def operacion_cuenta(operacion):
    num_cuenta = cuenta_entry.get()
    cuenta = cuentas.get(num_cuenta)
    if cuenta:
        try:
            cantidad = float(cantidad_entry.get())
            if operacion == 'ingresar':
                cuenta.ingresar_efectivo(cantidad)
            elif operacion == 'retirar':
                cuenta.retirar_efectivo(cantidad)
            saldo_var.set(cuenta.consultar_saldo())
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Primero consulta los datos de la cuenta.")

def depositar_efectivo():
    num_cuenta_destino = deposito_entry.get()
    cuenta_destino = cuentas.get(num_cuenta_destino)
    if cuenta_destino:
        try:
            cantidad = float(cantidad_deposito_entry.get())
            cuenta_destino.ingresar_efectivo(cantidad)
            messagebox.showinfo("Depósito realizado", f"Se ha depositado {cantidad} a la cuenta {num_cuenta_destino}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Cuenta destino no registrada.")

cuentas = {
    '1234567890': Cuenta('1234567890', 'Briseida Garcia', 20, 1000.0),
    '0987654321': Cuenta('0987654321', 'Michelle Quintero', 24, 2000.0),
}

root = tk.Tk()
root.title("Administración de Cuentas")

titular_var = tk.StringVar()
edad_var = tk.StringVar()
saldo_var = tk.StringVar()

titulo_label = tk.Label(root, text="Caja Popular", font=("Arial", 30, "bold"))
titulo_label.pack(pady=10)


cuenta_label = tk.Label(root, text="Número de Cuenta:", font=("Arial", 20, "bold"))
cuenta_label.pack()
cuenta_entry = tk.Entry(root)
cuenta_entry.pack()

consultar_btn = tk.Button(root, text="Consultar datos", command=consultar_datos)
consultar_btn.pack()

titular_label = tk.Label(root, textvariable=titular_var)
titular_label.pack()
edad_label = tk.Label(root, textvariable=edad_var)
edad_label.pack()
saldo_label = tk.Label(root, textvariable=saldo_var)
saldo_label.pack()

#ingreso y retiro de efectivo
ingresar_label = tk.Label(root, text="Ingresar/Retirar Efectivo", font=("Arial", 20, "bold"))
ingresar_label.pack()

cantidad_label = tk.Label(root, text="Cantidad:", font=("Arial", 15))
cantidad_label.pack()
cantidad_entry = tk.Entry(root)
cantidad_entry.pack()

ingresar_btn = tk.Button(root, text="Ingresar Efectivo", command=lambda: operacion_cuenta('ingresar'))
ingresar_btn.pack()

retirar_btn = tk.Button(root, text="Retirar Efectivo", command=lambda: operacion_cuenta('retirar'))
retirar_btn.pack(pady=20)

#deposito a cuentas
depositar_label = tk.Label(root, text="Deposito a otra cuenta", font=("Arial", 20, "bold"))
depositar_label.pack()

deposito_label = tk.Label(root, text="Cuenta Origen:", font=("Arial", 15))
deposito_label.pack()
deposito_entry = tk.Entry(root)
deposito_entry.pack()

deposito_label = tk.Label(root, text="Cuenta Destino:", font=("Arial", 15))
deposito_label.pack()
deposito_entry = tk.Entry(root)
deposito_entry.pack()

cantidad_deposito_label = tk.Label(root, text="Cantidad:", font=("Arial", 15))
cantidad_deposito_label.pack()
cantidad_deposito_entry = tk.Entry(root)
cantidad_deposito_entry.pack()

depositar_btn = tk.Button(root, text="Depositar", command=depositar_efectivo)
depositar_btn.pack()

root.mainloop()
