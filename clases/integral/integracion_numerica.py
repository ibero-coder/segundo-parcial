import math

class IntegracionNumerica(object):
    def __init__(self, x: float, dof: int):
        self.x = x
        self.dof = dof
        self.resultado = 0.0
        self.E = 0.00001
        self.num_seg_inicial = 10

    def gamma(self, n: float) -> float:
        if n == 0.5:
            return math.sqrt(math.pi)
        elif n == 1.0:
            return 1.0
        else:
            return (n - 1) * self.gamma(n - 1)

    def funcionT(self, xi: float) -> float:
        dof = self.dof
        numerador   = self.gamma((dof + 1) / 2)
        denominador = math.sqrt(dof * math.pi) * self.gamma(dof / 2)
        constante   = numerador / denominador
        potencia    = -((dof + 1) / 2)
        return constante * ((1 + (xi ** 2) / dof) ** potencia)

    def simpson(self, num_seg: int) -> float:
        W = self.x / num_seg
        suma_impares = sum(4 * self.funcionT(i * W) for i in range(1, num_seg, 2))
        suma_pares   = sum(2 * self.funcionT(i * W) for i in range(2, num_seg - 1, 2))
        return (W / 3) * (self.funcionT(0) + suma_impares + suma_pares + self.funcionT(self.x))

    def integrar(self):
        num_seg    = self.num_seg_inicial
        p_anterior = self.simpson(num_seg)
        while True:
            num_seg  *= 2
            p_nuevo   = self.simpson(num_seg)
            if abs(p_nuevo - p_anterior) < self.E:
                break
            p_anterior = p_nuevo
        self.resultado = p_nuevo