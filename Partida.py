import datetime

class Partida:
    lugar = ""
    fecha = -1
    
    def __init__(self, lugar, fecha, hora):
        self.lugar = lugar

        fechaSeparada = fecha.split("/")
        dia = int(fechaSeparada[0])
        mes = int(fechaSeparada[1])
        year = int(fechaSeparada[2])

        horaSeparada = hora.split(":")
        hora = int(horaSeparada[0])
        minutos = int(horaSeparada[1])

        self.fecha = datetime.datetime(year, mes, dia, hora, minutos)

    def detalles(self):
        print("Lugar: " + self.lugar)
        print("Fecha: " + self.fecha.strftime("%d/%m/%y %H:%M"))
        print("------------------------")
