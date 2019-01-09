from mongoengine import *
import mongoengine_goodjson as gj
import datetime
from . import Jugador

connect('heroku_8jrhk4q8', host='mongodb://user:user1234@ds117334.mlab.com:17334/heroku_8jrhk4q8')


class Equipo(gj.Document):
    nombre = StringField(max_length=80, required=True)
    jugadores = ListField(EmbeddedDocumentField(Jugador.Jugador))

    def add_jugador(self, jugador):
        self.jugadores.append(jugador)

        self.save()

    def crear_jugador(self, nombre, edad, nick):
        jugador = Jugador.Jugador(nombre=nombre, edad=edad, nick=nick)
        self.jugadores.append(jugador)

        self.save()

    def tiene_jugador(self, nombre):
        for j in self.jugadores:
            if j.nombre == nombre:
                return True

        return False
