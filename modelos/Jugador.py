from mongoengine import *
import mongoengine_goodjson as gj
import datetime

connect('heroku_8jrhk4q8', host='mongodb://user:user1234@ds117334.mlab.com:17334/heroku_8jrhk4q8')

class Jugador(gj.EmbeddedDocument):
    nombre = StringField(max_length=200, required=True, unique=True)
    edad = IntField(required=True)
    nick = StringField(max_length=50, required=True, unique=True)

    def cambiar_nombre(self, n):
        nombre = n
