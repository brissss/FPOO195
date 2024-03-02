class Usuario:
    
    def __init__(self, i, nom, ape, sex, ed, cor, contra):
        self.__id = i
        self.__nombre = nom
        self.__apellidos = ape
        self.__sexo = sex
        self.__edad = ed
        self.__correo = cor
        self.__contrasena = contra
        
    
    def getId(self):
        return self.__id

    def setId(self, ix):
        self.__id = ix
    
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nx):
        self.__nombre = nx
    
    
    def getApellidos(self):
        return self.__apellidos

    def setApellidos(self, ax):
        self.__apellidos = ax
    
    def getSexo(self):
        return self.__sexo

    def setSexo(self, sx):
        self.__sexo = sx
    
    def getEdad(self):
        return self.__edad

    def setEdad(self, ex):
        self.__edad = ex
    
    def getCorreo(self):
        return self.__correo

    def setCorreo(self, cx):
        self.__correo = cx
    
    def getContrasena(self):
        return self.__contrasena

    def setContrasena(self, xcon):
        self.__contrasena = xcon

#metodos del usuario (crear, actualizar, eliminar, consultar)
    def crear(self):
        print("el usuario" + self.__nombre  + "creo su perfil")
            
    
    def actualizar(self):
        print("el usuario" + self.__nombre  + "actualizo sus datos")
        
            
    def eliminar(self):
        print("el usuario" + self.__nombre  + "elimino su perfil")
        
            
    def consultar(self):
        print("el usuario" + self.__nombre  + "consulto su perfil")

