from Partida import Partida

class Agenda:
    partidas = []
    nombre = ""

    def __init__(self, nombre):
        self.nombre = nombre

    def crearPartida(self, lugar, fecha, hora):
        p = Partida(lugar, fecha, hora)
        self.partidas.append(p)

    def listarPartidas(self, fecha=""):
        print("###### Agenda de partidas de " + self.nombre)
        for p in self.partidas:
            p.detalles()
