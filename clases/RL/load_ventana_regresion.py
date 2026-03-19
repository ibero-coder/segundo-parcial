from PyQt5 import QtWidgets, uic
from clases.RL.regresion_lineal import RegresionLineal
from PyQt5.QtWidgets import QApplication, QDialog
import sys


ESTIMATED_PROXY  = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
PLAN_ADDED_MOD   = [163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130]
ACTUAL_ADDED_MOD = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
ACTUAL_DEV_HOURS = [15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]

XK = 386

ESPERADOS = {
    1: {"b0": -22.55,  "b1": 1.7279,   "rxy": 0.9545, "r2": 0.9111, "yk": 644.429},
    2: {"b0": -4.039,  "b1": 0.1681,   "rxy": 0.9333, "r2": 0.8711, "yk": 60.858},
    3: {"b0": -23.92,  "b1": 1.43097,  "rxy": 0.9631, "r2": 0.9276, "yk": 528.4294},
    4: {"b0": -4.604,  "b1": 0.140164, "rxy": 0.9480, "r2": 0.8988, "yk": 49.4994},
}


class VentanaRegresion(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/regresion lineal.ui", self)
        self.show()

        self.prueba1.clicked.connect(self.botonCaso1Click)
        self.prueba2.clicked.connect(self.botonCaso2Click)
        self.prueba3.clicked.connect(self.botonCaso3Click)
        self.prueba4.clicked.connect(self.botonCaso4Click)


    def botonCaso1Click(self):
        self._ejecutarCaso(1, ESTIMATED_PROXY, ACTUAL_ADDED_MOD)

    def botonCaso2Click(self):
        self._ejecutarCaso(2, ESTIMATED_PROXY, ACTUAL_DEV_HOURS)

    def botonCaso3Click(self):
        self._ejecutarCaso(3, PLAN_ADDED_MOD, ACTUAL_ADDED_MOD)

    def botonCaso4Click(self):
        self._ejecutarCaso(4, PLAN_ADDED_MOD, ACTUAL_DEV_HOURS)


    def _ejecutarCaso(self, numero: int, x: list, y: list):
        regresion = RegresionLineal(x, y)
        regresion.calcular()
        yk = regresion.predecir(XK)

        self._mostrarCalculados(regresion, yk)
        self._mostrarEsperados(numero)

    def _mostrarCalculados(self, regresion: RegresionLineal, yk: float):
        self.resultado1.setText(f"{regresion.b0:.4f}")
        self.resultado2.setText(f"{regresion.b1:.4f}")
        self.resultado3.setText(f"{regresion.rxy:.4f}")
        self.resultado4.setText(f"{regresion.r2:.4f}")
        self.resultado5.setText(f"{yk:.4f}")

    def _mostrarEsperados(self, numero: int):
        esp = ESPERADOS[numero]
        self.valor1.setText(f"{esp['b0']:.4f}")
        self.valor2.setText(f"{esp['b1']:.4f}")
        self.valor3.setText(f"{esp['rxy']:.4f}")
        self.valor4.setText(f"{esp['r2']:.4f}")
        self.valor5.setText(f"{esp['yk']:.4f}")
