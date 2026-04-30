import math

# Método del Rectángulo para integración numérica

class Rectangulo(object):
    def __init__(self, f, a, b, n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n

    def integrar(self):
        h = (self.b - self.a) / self.n
        total = 0.0

        for i in range(self.n):
            x_i = self.a + i * h
            total += self.f(x_i) * h

        return total
