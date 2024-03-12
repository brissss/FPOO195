class Persona:
    
    
#constructor    
    def __init__(self):
        self.__listaBD = []
        
        
# Metodos del CRUD
    def Insertar (self, id, nom, edad ):
        self.__listaBD.append( { "Id":id, "Nombre": nom, "Edad" :edad } )


    def consultarTodos (self):
        print (self.__listaBD)
        
    def buscarUsuario(self,id):
        for usuario in self.__listaBD: 
            if usuario['Id'] == id:
                print (usuario)
            else:
                print ("Usuario no encontrado")
    
    def eliminar(self,id):
        for usuario in self.__listaBD:
            if usuario['Id'] == id:
                self.__listaBD.remove (usuario)
                print(":: Usuario Eliminado ::")
            
            self.consultarTodos()
            
    def editar (self,id, nom, edad):
        for usuario in self.__listaBD:
            if usuario['Id'] == id:
                usuario['Nombre'] = nom
                usuario['Edad'] = edad
                print(":: Usuario Editado ::")
                
#You, 15 hours ago • Simulacion CRI
            self. consultarTodos ()