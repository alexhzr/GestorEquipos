from flask import Flask, render_template, request, session, json
from pickleshare import *
app = Flask(__name__)

db = PickleShareDB('gestor-equipos-data')

@app.route('/')
def status():
    status = {
      "status": "OK",
      "ejemplo": {
        "ruta": "/listar",
        "valor": "{ 'respuesta':'vacio' }"
      }
    }

    response = app.response_class(
        response=json.dumps(status),
        status=200,
        mimetype='application/json'
    )

    return response

"""@app.route('/listar', methods=['POST'])
def listarPartidas():
    equipo = request.form['equipo']

@app.route('/crear_agenda', methods=['POST'])
def crearAgenda():
    equipo = request.form['equipo']

    if equipo in db:
        status = {
            "status": "ERROR",
            "mensaje": "El equipo ya existe"
          }
        }

        response = app.response_class(
            response=json.dumps(status),
            status=200,
            mimetype='application/json'
        )
    else:"""
