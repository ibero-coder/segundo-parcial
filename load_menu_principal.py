from PyQt5 import QtWidgets, uic
from clases.RL.load_ventana_regresion import VentanaRegresion
from clases.integral.load_ventana_integracion import VentanaIntegracion
from clases.Intregral_Inversa.load_ventana_Integr_inversa import VentanaCalcularX
from clases.correlacion.load_ventana_correlacion import VentanaPrograma4

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/proyectos.ui", self)
        self.showMaximized()
        self.show()

        self.actionCalcular_x.triggered.connect(self.calcular_x)
        self.actionRegresion.triggered.connect(self.regresion)
        self.actionIntegracion.triggered.connect(self.integracion)
        self.actionPrograma4.triggered.connect(self.programa_4)
        self.actionSalir.triggered.connect(self.salir)

    def regresion(self):
        self.ventana_regresion = VentanaRegresion()
        self.ventana_regresion.show()


    def integracion(self):

        self.ventana_integracion = VentanaIntegracion()
        self.ventana_integracion.show()

    def calcular_x(self):
        
        self.ventana_calcular_x = VentanaCalcularX()
        self.ventana_calcular_x.show()

    def programa_4(self):
        self.ventana_programa4 = VentanaPrograma4()
        self.ventana_programa4.show()

    def salir(self):
        self.close()