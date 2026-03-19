from PyQt5 import QtWidgets, uic
import sys
from clases.integral.integracion_numerica import IntegracionNumerica


class VentanaIntegracion(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/integral.ui", self)
        self.show()
        self.botonc.clicked.connect(self.botonCalcularClick)

    def botonCalcularClick(self):
        x   = float(self.xedit.text())
        dof = int(self.dofedit.text())
        integracion = IntegracionNumerica(x, dof)
        integracion.integrar()
        self.resultadoI.setText(f"{integracion.resultado:.5f}")