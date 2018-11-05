import Partida
from Agenda import Agenda

a = Agenda("Villazarcillo FC")
a.crearPartida("Montejicar", "12/02/2020", "20:30")
a.crearPartida("Alhendín", "23/06/2019", "19:15")
a.crearPartida("Jun", "14/04/2020", "14:00")

a.listarPartidas()
