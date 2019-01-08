# coding=utf-8
from .modelos import Agenda, Equipo, Jugador, Partida
from .app import *
import re


def test_datos_prueba():
    borrar_datos()
    inicializar_datos()
    assert Equipo.objects.count() == 4, "No se ha creado bien"
    assert len(Equipo.objects().get(nombre="Zurriagazo FC").jugadores) == 3, "No se han insertado todos los jugadores del ZFC"
    assert len(Equipo.objects().get(nombre="Papaya FC").jugadores) == 3, "No se han insertado todos los jugadores del Papaya"
    assert len(Equipo.objects().get(nombre="Átomos de Springfield").jugadores) == 3, "No se han insertado todos los jugadores del Átomos"
    assert len(Equipo.objects().get(nombre="Dummy Crash Dolls").jugadores) == 3, "No se han insertado todos los jugadores del DCT"

    assert len(Agenda.objects()) == 1, "No se ha inicializado bien la agenda"
    assert len(Agenda.objects[0].partidas) == 4, "No se han inicializado bien las partidas"

def test_crear_jugador():
    equipo = Equipo("Testing Team FC")
    assert len(equipo.jugadores) == 1, "No se crean bien los jugadores"
    
def test_crear_partida():
    agenda = Agenda.objects().first()
    assert agenda.crear_partida("Zurriagazo FC", "Átomos de Springfield", "Estadio Nuevo Méjico", "01/02/2020 20:30") == 1, "Error creando partida"

def test_contar_partidas():
    agenda = Agenda.objects().first()
    assert agenda.contar_partidas() == 5, "La cuenta de partidas está mal"
    assert agenda.contar_partidas(mes=1) == 4, "La cuenta por meses está mal"
    assert agenda.contar_partidas(year=2019) == 4, "La cuenta por años está mal"
    assert agenda.contar_partidas(mes=2) == 1, "La cuenta (febrero) está mal"
    assert agenda.contar_partidas(year=2020) == 1, "La cuenta (2020) está mal"

def test_formatear_fecha():
    agenda = Agenda.objects().first()
    patt = re.compile("^(0[1-9]|1\d|2\d|3[01])\/(0[1-9]|1\d|2\d|3[01])\/(19|20)\d{2}\s+(0[0-9]|1[0-9]|2[0-3])\:(0[0-9]|[1-5][0-9])$")
    assert patt.match(agenda.partidas[0].get_fecha()) is not None, "La fecha no sigue el formato establecido"
