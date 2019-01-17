from flask import json
from mongoengine import *
import mongoengine_goodjson as gj
import datetime
from . import Equipo

connect('heroku_8jrhk4q8', host='mongodb://user:user1234@ds117334.mlab.com:17334/heroku_8jrhk4q8')

class Partida(gj.EmbeddedDocument):
    lugar = StringField(max_length=100, required=True)
    fecha = DateTimeField(required=True)
    equipo_local = ReferenceField(Equipo.Equipo)
    equipo_visitante = ReferenceField(Equipo.Equipo)

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

    def to_json(self):
        p = {
            "equipo_local": self.equipo_local.nombre,
            "equipo_visitante": self.equipo_visitante.nombre,
            "lugar": self.lugar,
            "fecha": self.get_fecha()
        }

        return json.loads(json.dumps(p))
