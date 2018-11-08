# coding=utf-8
import Partida
from Agenda import Agenda


agenda = Agenda("Villazarcillo FC")

def test_crearAgenda():
    assert agenda.nombre != "", "La agenda no se ha creado bien"

def test_crearPartida():
    agenda.crearPartida("Montejicar", "12/02/2020", "20:30")
    assert agenda.partidas[0].lugar != "", "La partida no se ha creado bien"
    assert agenda.partidas[0].fecha != -1, "La partida no se ha creado bien"

def test_contarPartidas():
    assert agenda.contarPartidas() != 0, "La cuenta de partiads está mal"
