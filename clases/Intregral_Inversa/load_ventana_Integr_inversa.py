from PyQt5 import QtWidgets, uic
import sys
from clases.Intregral_Inversa.Integracion_inversa import BuscadorX


class VentanaCalcularX(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/Calcular_x.ui", self)
        self.show()
        self.botonc.clicked.connect(self.botonCalcularClick)

    def botonCalcularClick(self):
        p   = float(self.xedit.text())
        dof = int(self.dofedit.text())
        buscador = BuscadorX(p, dof)
        buscador.encontrar_x()
        self.resultadoI.setText(f"{buscador.x:.5f}")
