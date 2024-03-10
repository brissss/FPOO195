class Personaje:
    
    #atributo de personaje
    
    def __init__(self, nom, esp, alt):
        self.__nombre = nom
        self.__especie = esp
        self.__altura = alt
        
    
    #metodos del personaje
    def correr(self, estado):
        if (estado):
            print("el personaje" + self.__nombre + "esta corriendo")
        else:
            print("el personaje" + self.__nombre + "esta muerto")
            
    
    def lanzarGranada(self):
            print(self.__nombre  + "pego una granada")
        
            
            
    def recargarArma(self, municion):
        cargador = 25
        cargadro = cargador + municion
        print("arma recargada" +  str(cargador) + "%")
    
    def _pensar(self):
        print(self.__nombre  + "esta pensando")
        

 def generar_password(self):
        generador = GeneradorPassword()
        self.password = generador.generar_password(self.longitud, self.mayusculas, self.caracteres_especiales)

    def mostrar_password(self):
        mb.showinfo("Contraseña generada", self.password)

    def copiar_password(self):
        self.ventana.clipboard_clear()
        self.ventana.clipboard_append(self.password)

    def comprobar_fortaleza(self):
        # TODO: Implementar la lógica para comprobar la fortaleza de la contraseña
        pass

    def iniciar_interfaz(self):
        # Contenedor principal
        frame_principal = tk.Frame(self.ventana)
        frame_principal.pack()

    
        label_longitud = tk.Label(frame_principal, text="Longitud de la contraseña:")
        label_longitud.pack(side=tk.LEFT)

       
        entry_longitud = tk.Entry(frame_principal, width=5)
        entry_longitud.insert(0, str(self.longitud))
        entry_longitud.pack(side=tk.LEFT)

        checkbutton_mayusculas = tk.Checkbutton(frame_principal, text="Incluir mayúsculas")
        checkbutton_mayusculas.pack(side=tk.LEFT)

       
        checkbutton_caracteres_especiales = tk.Checkbutton(frame_principal, text="Incluir caracteres especiales")
        checkbutton_caracteres_especiales.pack(side=tk.LEFT)

        
        boton_generar = tk.Button(frame_principal, text="Generar contraseña", command=self.generar_password)
        boton_generar.pack(side=tk.LEFT)

       
        entry_password = tk.Entry(frame_principal, width=30)
        entry_password.pack(side=tk.TOP)

     
        boton_mostrar = tk.Button(frame_principal, text="Mostrar contraseña", command=self.mostrar_password)
        boton_mostrar.pack(side=tk.LEFT)

        
        boton_copiar = tk.Button(frame_principal, text="Copiar contraseña", command=self.copiar_password)
        boton_copiar.pack(side=tk.LEFT)

        
        boton_comprobar = tk.Button(frame_principal, text="Comprobar fortaleza", command=self.comprobar_fortaleza)
        boton_comprobar.pack(side=tk.LEFT)

        self.ventana.mainloop

            
        

        
