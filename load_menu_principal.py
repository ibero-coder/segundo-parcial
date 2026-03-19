from PyQt5 import QtWidgets, uic
from clases.integral.integracion_numerica import IntegracionNumerica
from clases.RL.load_ventana_regresion import VentanaRegresion
from clases.RL.regresion_lineal import RegresionLineal
from clases.integral.load_ventana_integracion import VentanaIntegracion

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/proyectos.ui", self)
        self.showMaximized()
        self.show()

        self.actionRegresi_n_lineal.triggered.connect(self.regresion)
        self.actionIntegraci_n_numerica.triggered.connect(self.integracion)
        self.actionSalir.triggered.connect(self.salir)

    
    def regresion(self):
        regresion=VentanaRegresion()
        regresion.exec()

    def integracion(self):
        Integral=VentanaIntegracion()
        Integral.exec()

    def salir(self):
        self.close()
