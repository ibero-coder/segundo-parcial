import math
from clases.integral.integracion_numerica import IntegracionNumerica


class BuscadorX(object):
    def __init__(self, p: float, dof: int):
        self.p   = p
        self.dof = dof
        self.x   = 0.0
        self.E   = 0.000001

    def integrar_(self, x_: float):
        if x_ <= 0:
            return 0.0
        integracion = IntegracionNumerica(x_, self.dof)
        integracion.integrar()
        return integracion.resultado

    def encontrar_x(self):
        x_ = 1.0
        d = 0.5
        error_anterior = 0

        while True:
            resultado = self.integrar_(x_)
            error  = self.p - resultado

            if abs(error) < self.E:
                break

            if error_anterior != 0 and error * error_anterior < 0:
                d /= 2

            error_anterior = error

            if error > 0:
                x_ += d
            else:
                x_ -= d

            if x_ <= 0:
                x_ = 1e-10

        self.x = x_

