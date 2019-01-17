
# Gestor de equipos
[![Build Status](https://travis-ci.org/alexhzr/GestorEquipos.svg?branch=master)](https://travis-ci.org/alexhzr/GestorEquipos) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Proyecto para la asignatura Infraestructura Virtual (2018).

## Descripción del proyecto
Microservicio web pensado para gestionar distintos equipos deportivos. Abarca sección de plantillas y organización de partidas.

La idea es mantener una especie de agenda deportiva que organiza las partidas de distintos clubes. Se podría entender que una Agenda es una liga, por lo tanto, dentro irán los partidos de dicha liga. Dentro de **Agenda** se guardan, en formato de documento embebido, las partidas (objeto Partida).

**Partida** tiene referencias al equipo visitante y al equipo local, además del lugar donde se hará, una fecha y una hora. Estas partidas, como he mencionado, se guardan en una lista dentro de Agenda.

**Equipo** tiene un nombre y una lista de jugadores (objeto Jugador). Al igual que Agenda con Partida, los jugadores se guardan en una lista embebida dentro de Equipo.

**Jugador** tiene nombre (único), nick (único) y edad.

---

## Rutas y funcionamiento de la app
Para ejecutar la aplicación, clonar el repositorio o hacer un fork:

```$ git clone https://github.com/alexhzr/GestorEquipos.git```

Instalar las dependencias

```$ pip3 install requeriments.txt```


Ejecutar con:

```python3 app.py```

La aplicación funciona de manera REST. Esto quiere decir que no cuenta con una interfaz web ni ningún tipo de IU. Para poder hacer algunas pruebas, se puede usar alguna aplicación estilo [Postman](https://www.getpostman.com/) y utilizar las rutas que defino aquí abajo.

- `GET /inicializar_datos`: Inicializa la BD con datos de prueba.
- `GET /borrar_datos`: Borra los datos de la BD
- `GET /equipo`: Obtiene un listado de los equipos
- `GET /partida`: Obtiene un listado de las partidas
- `GET /partida/proxima/:id_equipo`: Obtiene la partida más próxima para ese equipo

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


# Documentación del proyecto

Toda la **[documentación del proyecto](https://github.com/alexhzr/GestorEquipos/tree/master/docs)** se encuentra en el directorio ``docs``.

# Despliegue

Despliegue https://gestor-equipos.herokuapp.com
Contenedor: https://gestorequipos-docker.herokuapp.com/
Enlace a DockerHub: https://hub.docker.com/r/alexhzr/gestor-equipos
