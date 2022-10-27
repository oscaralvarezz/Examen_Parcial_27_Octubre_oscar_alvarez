class Alumno:
    def init(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("¡El alumno se creó con exito!")

    def calificacion(self):
        if self.nota<=5:
            resultado = "El alumno ha suspendido con un: {}".format(self.nota)
        else:
            resultado = "El alumno ha aprobado con un: {}".format(self.nota)
            return resultado

calificacion = Alumno
print(calificacion("oscar", 9))