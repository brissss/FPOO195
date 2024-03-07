import tkinter as tk

class VentanaLogin:
    def __init__(self):
        self._ventana = tk.Tk()
        self._ventana.title("Login")
        self._ventana.geometry("600x400")
        

        # crear widgets
        self._correo_entry = tk.Entry(self._ventana)
        self._contrasena_entry = tk.Entry(self._ventana, show="*")
        self._boton_validar = tk.Button(self._ventana, text="Validar", command= self._validar_login)
        self._boton_editar = tk.Button(self._ventana, text="Editar usuario")
        self._boton_eliminar = tk.Button(self._ventana, text="Eliminar usuario")

        # widgets
        self._correo_entry.pack()
        self._contrasena_entry.pack()
        self._boton_validar.pack()
        self._boton_editar.pack()
        self._boton_eliminar.pack()

        # correo y contraseña 
        self._correo_predeterminado = "briss@gmail.com"
        self._contrasena_predeterminada = "1234567890"

        # iniciar 
        self._ventana.mainloop()

    def _validar_login(self):
        correo = self._correo_entry.get()
        contrasena = self._contrasena_entry.get()

        if not correo or not contrasena:
            self._mostrar_mensaje_error("Correo o contraseña vacios")
        else:
            if correo == self._correo_predeterminado and contrasena == self._contrasena_predeterminada:
                self._mostrar_mensaje_bienvenida("Bienvenido")
            else:
                self._mostrar_mensaje_error("Correo o contraseña incorrectos")

    def _mostrar_mensaje_bienvenida(self, mensaje):
        tk.messagebox.showinfo("Login", mensaje)

    def _mostrar_mensaje_error(self, mensaje):
        tk.messagebox.showerror("Login", mensaje)


ventana_login = VentanaLogin()

