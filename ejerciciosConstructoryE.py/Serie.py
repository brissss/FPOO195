class Serie:
    def __init__(self, titulo, genero="", calificacion=0):
        self.__titulo = titulo
        self.__horas_estimadas = 10
        self.__status = "Sin reproducir"
        self.__genero = genero
        self.__calificacion = calificacion

    def reproducir(self):
        return f"Reproduciendo {self.__titulo}"

    def agregar_a_mi_lista(self):
        return f"{self.__titulo} agregado a mi lista"

    def marcar_como_completada(self):
        self.__status = "Completada"
        return f"{self.__titulo} marcada como completada"

    def calificar(self, nueva_calificacion):
        if 0 <= nueva_calificacion <= 10:
            self.__calificacion = nueva_calificacion
            return f"Calificación de {self.__titulo} actualizada a {nueva_calificacion}"
        else:
            return "Calificación inválida. Debe estar entre 0 y 10."

    def __str__(self):
        return f"Título: {self.__titulo}, Horas Estimadas: {self.__horas_estimadas}, Status: {self.__status}, Género: {self.__genero}, Calificación: {self.__calificacion}"
