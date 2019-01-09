from mongoengine import *
import mongoengine_goodjson as gj
import datetime
#from .Partida import Partida as Partida
from . import Partida
from . import Equipo

connect('heroku_8jrhk4q8', host='mongodb://user:user1234@ds117334.mlab.com:17334/heroku_8jrhk4q8')

class Agenda(gj.Document):
    partidas = ListField(EmbeddedDocumentField(Partida.Partida))

    def hay_partida(self, lugar, fecha):
        for p in partidas:
            if p.lugar == lugar and p.fecha == fecha:
                return true

        return false

    def add_partida(self, p):
        self.partidas.append(p)

    def crear_partida(self, local, visitante, lugar, fecha, hora):
        e_local = Equipo.Equipo.objects(nombre=local)
        e_visitante = Equipo.Equipo.objects(nombre=visitante)

        if not e_local and not e_visitante:
            e_local = Equipo.Equipo.objects(id=local)
            e_visitante = Equipo.Equipo.objects(id=visitante)

        if e_local and e_visitante:
            e_local = e_local.first()
            e_visitante = e_visitante.first()

            p = Partida.Partida(equipo_local = e_local.id, equipo_visitante = e_visitante.id, lugar=lugar)
            p.formatear_fecha(fecha, hora)

            self.partidas.append(p)
            self.save()

            return True

        else:
            return False


    def contar_partidas(self, mes=-1, year=-1):
        numPartidas = 0

        if mes != -1:
            if year == -1:
                year = datetime.datetime.now().year

            for p in self.partidas:
                if p.fecha.date().month == mes:
                    numPartidas += 1

        elif year != -1:
            for p in self.partidas:
                if p.fecha.date().year == year:
                    numPartidas += 1

        else:
            for p in self.partidas:
                numPartidas += 1

        return numPartidas
