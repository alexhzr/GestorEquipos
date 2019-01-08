from mongoengine import *
import mongoengine_goodjson as gj
import datetime
from .constantes import *

connect('heroku_8jrhk4q8', host='mongodb://user:user1234@ds117334.mlab.com:17334/heroku_8jrhk4q8')

class Jugador(gj.EmbeddedDocument):
    nombre = StringField(max_length=200, required=True, unique=True)
    edad = IntField(required=True)
    nick = StringField(max_length=50, required=True, unique=True)

    def cambiar_nombre(self, n):
        nombre = n


class Equipo(gj.Document):
    nombre = StringField(max_length=80, required=True)
    jugadores = ListField(EmbeddedDocumentField(Jugador))

    def add_jugador(self, jugador):
        self.jugadores.append(jugador)

        self.save()

    def add_jugador(self, nombre, edad, nick):
        jugador = Jugador(nombre=nombre, edad=edad, nick=nick)
        self.jugadores.append(jugador)

        self.save()

    def tiene_jugador(self, nombre):
        for j in self.jugadores:
            if j.nombre == nombre:
                return True

        return False

class Partida(gj.EmbeddedDocument):
    lugar = StringField(max_length=100, required=True)
    fecha = DateTimeField(required=True)
    equipo_local = ReferenceField(Equipo)
    equipo_visitante = ReferenceField(Equipo)

    def formatear_fecha(self, fecha, hora):
        fechaSeparada = fecha.split("/")
        dia = int(fechaSeparada[0])
        mes = int(fechaSeparada[1])
        year = int(fechaSeparada[2])

        horaSeparada = hora.split(":")
        hora = int(horaSeparada[0])
        minutos = int(horaSeparada[1])

        self.fecha = datetime.datetime(year, mes, dia, hora, minutos)

    def get_fecha(self):
        return self.fecha.strftime("%d/%m/%Y %H:%M")


class Agenda(gj.Document):
    partidas = ListField(EmbeddedDocumentField(Partida))

    def hay_partida(self, lugar, fecha):
        for p in partidas:
            if p.lugar == lugar and p.fecha == fecha:
                return true

        return false

    def add_partida(self, p):
        self.partidas.append(p)

    def crear_partida(self, local, visitante, lugar, fecha, hora):
        e_local = Equipo.objects(nombre=local)
        e_visitante = Equipo.objects(nombre=visitante)

        if not e_local and not e_visitante:
            e_local = Equipo.objects(id=local)
            e_visitante = Equipo.objects(id=visitante)

        if e_local and e_visitante:
            e_local = e_local.first()
            e_visitante = e_visitante.first()

            p = Partida(equipo_local = e_local.id, equipo_visitante = e_visitante.id, lugar=lugar)
            p.formatear_fecha(fecha, hora)

            self.partidas.append(p)
            self.save()

            return OK

        else:
            return ERROR


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
