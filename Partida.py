

class Partida:
    def __init__(self, lugar, fecha, hora):
        self.lugar = lugar
        self.fecha = fecha
        self.hora = hora

    def detalles(self):
        print("Lugar: " + self.lugar)
        print("Fecha: " + self.fecha + " " + self.hora)
        print("------------------------")
