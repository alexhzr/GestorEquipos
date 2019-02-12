import os
from flask import Flask, render_template, request, session, json, jsonify
from mongoengine import *
from bson.objectid import ObjectId

from modelos.Jugador import Jugador as Jugador
from modelos.Equipo import Equipo as Equipo
from modelos.Partida import Partida as Partida
from modelos.Agenda import Agenda as Agenda

#app = Flask(__name__)

#connect('heroku_8jrhk4q8', host='mongodb://user:user1234@ds117334.mlab.com:17334')

def create_app():
    app = Flask(__name__)

    @app.route('/ping')
    def ping():
        return jsonify(ping='pong')

    @app.route('/borrar_datos')
    def borrar_datos():
        Equipo.objects.delete()
        Agenda.objects.delete()

        respuesta = {
            "status": "OK", "mensaje": "Base de datos limpiada"
        }

        return jsonify(respuesta)

    @app.route('/inicializar_datos')
    def inicializar_datos():
        if Equipo.objects().count() != 0:
            borrar_datos()
            respuesta = {
                "status": "FAILED",
                "reason": "Ya está inicializada la BD con datos de prueba."
            }

        else:
            agenda = Agenda()

            datos = {
                "equipos" : [
                    { "Papaya FC": [
                        { "nombre": "Jason Osuna", "edad": 23, "nick": "Jason" },
                        { "nombre": "Wisin Romeldo", "edad": 21, "nick": "Wisin" },
                        { "nombre": "Welintong Quiw", "edad": 20, "nick": "El Campeón" }
                    ]},

                    { "Zurriagazo FC": [
                        { "nombre": "Bernardo Gado", "edad": 26, "nick": "Berni" },
                        { "nombre": "Horacio Fameldas", "edad": 23, "nick": "Horace" },
                        { "nombre": "Euladio Contreras", "edad": 19, "nick": "El Contreras" }
                    ]},

                    { "Átomos de Springfield": [
                        { "nombre": "Homer Simpson", "edad": 41, "nick": "Da Homa" },
                        { "nombre": "Ned Flanders", "edad": 54, "nick": "Flanders" },
                        { "nombre": "Moe Swislak", "edad": 42, "nick": "Moé" }
                    ]} ,

                    { "Dummy Crash Dolls": [
                        { "nombre": "Moñeco 1", "edad": 1, "nick": "Moñeco1" },
                        { "nombre": "Moñeco 2", "edad": 1, "nick": "Moñeco2" },
                        { "nombre": "Moñeco 3", "edad": 1, "nick": "Moñeco3" }
                    ]}
                ],
                "partidos": [
                    {   "local": "Papaya FC",
                        "visitante": "Zurriagazo FC",
                        "lugar": "Estadio Santa Juana",
                        "fecha": "10/01/2019",
                        "hora": "12:00"
                    },
                    {   "local": "Dummy Crash Dolls",
                        "visitante": "Átomos de Springfield",
                        "lugar": "Estadio de Prueba 01",
                        "fecha": "15/01/2019",
                        "hora": "18:00"
                    },
                    {   "local": "Átomos de Springfield",
                        "visitante": "Papaya FC",
                        "lugar": "Estadio Duff de Springfield",
                        "fecha": "20/01/2019",
                        "hora": "21:00"
                    },
                    {   "local": "Zurriagazo FC",
                        "visitante": "Papaya FC",
                        "lugar": "Estadio Santa Euladia",
                        "fecha": "25/01/2019",
                        "hora": "12:00"
                    }
                ]
            }

            keys = [ "Papaya FC", "Zurriagazo FC", "Átomos de Springfield", "Dummy Crash Dolls" ]
            i = 0

            for e in datos['equipos']:
                equipo = Equipo(nombre=keys[i])

                for j in datos['equipos'][i][keys[i]]:
                    jugador = Jugador(nombre=j['nombre'], edad=j['edad'], nick=j['nick'])
                    equipo.add_jugador(jugador)

                equipo.save()
                i += 1

            for p in datos['partidos']:
                local = p['local']
                visitante = p['visitante']
                lugar = p['lugar']
                fecha = p['fecha']
                hora = p['hora']

                i += 1

                if not agenda.crear_partida(local, visitante, lugar, fecha, hora):
                    respuesta = { "status": "ERROR", "mensaje": "Fallo creando partida" }

                    return jsonify(respuesta)

                agenda.save()

            respuesta = {
                "status": "OK", "mensaje": "Insertados datos de prueba"
            }

        return jsonify(respuesta)

    @app.route('/status', methods=['GET'])
    def status():
        respuesta = json.loads('{"equipos": [{"id": "5c3f6b61e4198711fc898544", "jugadores": [{"edad": 23, "nick": "Jason", "nombre": "Jason Osuna"}, {"edad": 21, "nick": "Wisin", "nombre": "Wisin Romeldo"}, {"edad": 20, "nick": "El Campe\u00f3n", "nombre": "Welintong Quiw"}], "nombre": "Papaya FC"}, {"id": "5c3f6b62e4198711fc898545", "jugadores": [{"edad": 26, "nick": "Berni", "nombre": "Bernardo Gado"}, {"edad": 23, "nick": "Horace", "nombre": "Horacio Fameldas"}, {"edad": 19, "nick": "El Contreras", "nombre": "Euladio Contreras"}], "nombre": "Zurriagazo FC"}, {"id": "5c3f6b63e4198711fc898546", "jugadores": [{"edad": 41, "nick": "Da Homa", "nombre": "Homer Simpson"}, {"edad": 54, "nick": "Flanders", "nombre": "Ned Flanders"}, {"edad": 42, "nick": "Mo\u00e9", "nombre": "Moe Swislak"}], "nombre": "\u00c1tomos de Springfield"}, {"id": "5c3f6b64e4198711fc898547", "jugadores": [{"edad": 1, "nick": "Moñeco1", "nombre": "Moñeco 1"}, {"edad": 1, "nick": "Moñeco2", "nombre": "Moñeco 2"}, {"edad": 1, "nick": "Moñeco3", "nombre": "Moñeco 3"}], "nombre": "Dummy Crash Dolls"}, {"id": "5c3f6b69e4198711fc898549", "jugadores": [{"edad": 23, "nick": "Test_1", "nombre": "Testero Uno"}], "nombre": "Testing Team FC"}]}')
        status = {
          "status": "OK",
          "ejemplo": {
            "ruta": "GET /equipo",
            "valor": respuesta
          }
        }

        return jsonify(status)

    """
    ############################ RUTAS PARA EQUIPO ############################
    """
    @app.route('/equipo', methods=['GET'])
    def listar_equipos():
        equipos = []
        if Equipo.objects.count != 0:
            for equipo in Equipo.objects:
                equipos.append(json.loads(equipo.to_json()))

            respuesta = { "status" : "OK", "equipos" : equipos }

        else:
            respuesta = { "status": "OK", "equipos" : 0 }

        return jsonify(respuesta)


    @app.route('/equipo', methods=['PUT'])
    def crearEquipo():
        nombre_equipo = request.args.get('nombre')
        equipo = Equipo.objects(nombre=nombre_equipo)

        if equipo:
            respuesta = {
                "status": "FAILED",
                "error": "Ya existe ese equipo"
            }

        else:
            equipo = Equipo(nombre=nombre_equipo)
            equipo.save()

            respuesta = {
                "status": "OK",
                "id_equipo": str(equipo.id)
            }

        return jsonify(respuesta)


    """
    ############################ RUTAS PARA JUGADOR ############################
    """
    @app.route('/jugador', methods=['PUT'])
    def crearJugador():
        id_equipo = request.args.get("id_equipo")
        equipo = Equipo.objects(id=id_equipo)

        if not equipo:
            respuesta = {
                "status": "FAILED",
                "error": "Ese equipo no existe en la BD"
            }

        else:
            nombre_jugador = request.args.get('nombre')
            equipo = equipo.first()

            if equipo.tiene_jugador(nombre_jugador):
                respuesta = {
                    "status": "FAILED",
                    "error": "Ya existe ese jugador"
                }

            else:
                jugador = Jugador(nombre=nombre_jugador)
                jugador.edad = request.args.get('edad')
                jugador.nick = request.args.get('nick')

                equipo.add_jugador(jugador)
                equipo.save()

                respuesta = {
                    "status": "OK",
                    "jugador_creado": json.loads(jugador.to_json()),
                    "equipo": json.loads(equipo.to_json())
                }

        return jsonify(respuesta)

    """
    ############################ RUTAS PARA PARTIDA ############################
    """

    @app.route('/partida', methods=['GET'])
    def listar_partidas():
        agenda = Agenda.objects.first()

        partidas = []
        if len(agenda.partidas) != 0:
            for p in agenda.partidas:
                #partidas.append(json.loads(p.to_json()))
                partidas.append(p.to_json())

            respuesta = { "status" : "OK", "partidas" : partidas }

        else:
            respuesta = { "status": "OK", "partidas" : 0 }

        return jsonify(respuesta)

    @app.route('/partida/proxima/<id_equipo>')
    def partida_mas_proxima(id_equipo):
        equipo = Equipo.objects(id=id_equipo)

        if not equipo:
            respuesta = {
                "status": "FAILED",
                "error": "Ese equipo no existe en la BD"
            }

        else:
            equipo = equipo.first()
            partidas = Agenda.objects.first().partidas
            partida_mas_proxima = partidas[0]
            for p in partidas:
                if p.equipo_local.id == equipo.id or p.equipo_visitante.id == equipo.id:
                    if partida_mas_proxima.fecha > p.fecha:
                        partida_mas_proxima = p;

            respuesta = {
                "status": "OK",
                "partida": partida_mas_proxima.to_json()
            }

        return jsonify(respuesta)

    @app.route('/partida', methods=['PUT'])
    def crear_partida():
        idLocal = request.args.get("local")
        idVisitante = request.args.get("visitante")
        fecha = request.args.get("fecha")
        hora = request.args.get("hora")
        lugar = request.args.get("lugar")

        local = Equipo.objects(id=idLocal)
        visitante = Equipo.objects(id=idVisitante)

        if not local or not visitante:
            respuesta = {
                "status": "FAILED",
                "error": "Ese equipo no existe en la BD"
            }

        elif local and visitante:
            agenda = Agenda.objects.first()
            local = local.first()
            visitante = visitante.first()

            if agenda.crear_partida(local.id, visitante.id, lugar, fecha, hora):
                respuesta = {
                    "status": "OK",
                    "mensaje": "Creada partida correctamente para la partida de " + fecha + " " + hora + " en " + lugar
                }
            else:
                respuesta = {
                    "status": "ERROR",
                    "mensaje": "Error creando la partida"
                }

        return jsonify(respuesta)

        if __name__ == "__main__":
            if 'PORT' in os.environ: p = os.environ['PORT']
            else: p = 5000

            #app = create_app()
            app.run(host="0.0.0.0", port=p)

    return app
