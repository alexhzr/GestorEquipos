# Gestor de equipos
[![Build Status](https://travis-ci.org/alexhzr/GestorEquipos.svg?branch=master)](https://travis-ci.org/alexhzr/GestorEquipos)

Proyecto para la asignatura Infraestructura Virtual (2018).

## Descripción del proyecto
Microservicio web pensado para gestionar distintos equipos deportivos. Abarca sección de plantillas y organización de partidas.

La idea es mantener una especie de agenda deportiva que organiza las partidas de distintos clubes. Se podría entender que una Agenda es una liga, por lo tanto, dentro irán los partidos de dicha liga. Dentro de **Agenda** se guardan, en formato de documento embebido, las partidas (objeto Partida).

**Partida** tiene referencias al equipo visitante y al equipo local, además del lugar donde se hará, una fecha y una hora. Estas partidas, como he mencionado, se guardan en una lista dentro de Agenda.

**Equipo** tiene un nombre y una lista de jugadores (objeto Jugador). Al igual que Agenda con Partida, los jugadores se guardan en una lista embebida dentro de Equipo.

**Jugador** tiene nombre (único), nick (único) y edad.

## Herramientas usadas
Voy a desarrollar el proyecto usando **Python 3.6 y Flask**. Necesito montar un servicio rápido y ligero, por lo que Flask me da justamente eso que pido. El paso de datos cliente-servidor y viceversa será en JSON. Django lo veo demasiado completo para hacer un microservicio. No voy a usar plantillas ni voy a tener un sistema complejo de clases, así que con Flask me basta y me sobra.

Para la base de datos voy a usar **MongoDB**. Ya la he usado varias veces y me parece un sistema de DB bastante útil y potente. Dado que voy a emplearlo, voy a hacer uso de las colecciones y los documentos embebidos. No tiene sentido elegir un proyecto en MongoDB y hacerlo siguiendo la estructura de las bases de datos SQL, con relaciones y demás.

De todas formas, he diseñado modelos para que mi aplicación use ORM. Para ello he usado **[Mongoengine](http://mongoengine.org/)**

He incluido una librería externa, **[mongoengine_goodjson](https://github.com/hiroaki-yamamoto/mongoengine-goodjson)**. Básicamente lo que hace es poner el JSON que exportan los modelos de Mongoengine de una forma más _human readable_.

Podría haberlo hecho con Node.js y Express, usando Mongoose como ORM, dado que ya sé hacerlo de esta manera, pero creo conveniente seguir moviéndose y aprendiendo, para no estancarse en lo mismo.

---

## Rutas y funcionamiento de la app

- `GET /inicializar_datos`: Inicializa la BD con datos de prueba.
- `GET /borrar_datos`: Borra los datos de la BD
- `GET /equipo`: Obtiene un listado de los equipos
- `GET /partida`: Obtiene un listado de las partidas
- `PUT /equipo`: Crea un equipo. Parámetros necesarios:
  - nombre: nombre del equipo

- `PUT /jugador`: Crea un jugador. Parámetros necesarios:
  - id_equipo: ObjectID del equipo
  - nombre: nombre del jugador
  - edad: edad del jugador
  - nick: nick del jugador

- `PUT /partida`: Crea una partida. Parámetros necesarios:
  - local: ObjectID del equipo local
  - visitante: ObjectID del equipo visitante
  - fecha: Fecha de la partida en formato dd/mm/yyyy
  - hora: Hora de la partida en formato hh:mm
  - lugar: Lugar del encuentro

## Tests
Para pasar los test he usado **[Pytest 3](https://docs.pytest.org/en/latest/)**. Los test se pasan bajo el fichero de tests `test.py`.

`pytest-3 test.py`


## Despliegue
Ahora mismo, el despliegue está en **[Heroku](https://gestor-equipos.herokuapp.com)**.
