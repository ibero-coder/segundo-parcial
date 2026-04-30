from PyQt5 import QtWidgets, uic
from clases.RL.load_ventana_regresion import VentanaRegresion
from clases.integral.load_ventana_integracion import VentanaIntegracion
from clases.Intregral_Inversa.load_ventana_Integr_inversa import VentanaCalcularX
from clases.correlacion.load_ventana_correlacion import VentanaPrograma4
from clases.metodos_de_integracion.load_ventana_metodosIntegracion import VentanaRectangulo

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
        self.actionFINAL.triggered.connect(self.final)
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

    def final(self):
        self.ventana_final = VentanaRectangulo()
        self.ventana_final.show()

    def salir(self):
        self.close()