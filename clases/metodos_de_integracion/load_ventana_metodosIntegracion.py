from PyQt5 import QtWidgets, uic
import sys
import math

from clases.metodos_de_integracion.rectangulo import Rectangulo
from clases.metodos_de_integracion.trapecio import Trapecio
from clases.metodos_de_integracion.simpson import Simpson

class VentanaRectangulo(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/metodosInt.ui", self)
        self.show()

        self.integral1.clicked.connect(self.Integral1)
        self.integral2.clicked.connect(self.Integral2)
        self.integral3.clicked.connect(self.Integral3)

    def Integral1(self):
            f = lambda x: math.e**x
            a = -1
            b = 1
            n = 10

            rect = Rectangulo(f, a, b, n)
            resultado = rect.integrar()

            self.int1res.setText(f"{resultado:.6f}")

            f = lambda x: math.sin(x)
            a = 0
            b = math.pi
            n = 10

            rect = Rectangulo(f, a, b, n)
            resultado = rect.integrar()

            self.int2res.setText(f"{resultado:.6f}")
            f = lambda x: math.e**(x**2)
            a = 0
            b = 1
            n = 10

            rect = Rectangulo(f, a, b, n)
            resultado = rect.integrar()

            self.int3res.setText(f"{resultado:.6f}")
    
    def Integral2(self):
        f = lambda x: math.e**x
        a = -1
        b = 1
        n = 10

        simpson = Simpson(f, a, b, n)
        resultado = simpson.integrar()

        self.int1res.setText(f"{resultado:.6f}")

        f = lambda x: math.sin(x)
        a = 0
        b = math.pi
        n = 10

        simpson = Simpson(f, a, b, n)
        resultado = simpson.integrar()

        self.int2res.setText(f"{resultado:.6f}")
        f = lambda x: math.e**(x**2)
        a = 0
        b = 1
        n = 10

        simpson = Simpson(f, a, b, n)
        resultado = simpson.integrar()

        self.int3res.setText(f"{resultado:.6f}")

    def Integral3(self):
        f = lambda x: math.e**x
        a = -1
        b = 1
        n = 10

        trapecio = Trapecio(f, a, b, n)
        resultado = trapecio.integrar()

        self.int1res.setText(f"{resultado:.6f}")

        f = lambda x: math.sin(x)
        a = 0
        b = math.pi
        n = 10

        trapecio = Trapecio(f, a, b, n)
        resultado = trapecio.integrar()

        self.int2res.setText(f"{resultado:.6f}")
        f = lambda x: math.e**(x**2)
        a = 0
        b = 1
        n = 10

        trapecio = Trapecio(f, a, b, n)
        resultado = trapecio.integrar()

        self.int3res.setText(f"{resultado:.6f}")