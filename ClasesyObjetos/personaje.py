class Personaje:
    
    #atributo de personaje
    
    def __init__(self, nom, esp, alt):
        self.nombre = nom
        self.especie = esp
        self.altura = alt
    
    #metodos del personaje
    def correr(self, estado):
        if (estado):
            print("el personaje" + self.nombre + "esta corriendo")
        else:
            print("el personaje" + self.nombre + "esta muerto")
            
    
    def lanzarGranada(self):
            print(self.nombre  + "pego una granada")
            
            
    def recargarArma(self, municion):
        cargador = 25
        cargadro = cargador + municion
        print("arma recargada" +  str(cargador) + "%")
        

