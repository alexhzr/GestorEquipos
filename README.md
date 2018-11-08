# Gestor de equipos
[![Build Status](https://travis-ci.org/alexhzr/GestorEquipos.svg?branch=master)](https://travis-ci.org/alexhzr/GestorEquipos)

Proyecto para la asignatura Infraestructura Virtual (2018)
## Descripción del proyecto
Microservicio web pensado para gestionar distintos equipos deportivos. Abarca sección de plantillas, gastos y organización de partidas.

La idea es mantener una especie de agenda deportiva para un club, asociación o equipo, mediante la cual una serie de administradores serán los encargados de ir publicando los eventos con sus datos (fecha, lugar, equipo, descripción...) y el resto de usuarios podrá consultarla de manera fácil y rápida. También tener guardados a los jugadores y alguna libreta sencilla de gastos.

## Herramientas usadas
Voy a desarrollar el proyecto usando Python y Flask. Necesito montar un servicio rápido y ligero, por lo que Flask me da justamente eso que pido. El paso de datos cliente-servidor y viceversa será en JSON.

En el momento de usar base de datos, usaré MongoDB.
