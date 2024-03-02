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
            
        

        
