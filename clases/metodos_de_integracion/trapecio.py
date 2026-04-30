import math

# Método del trapecio para integración numérica

class Trapecio(object):
    def __init__(self, f, a, b, n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n

    def integrar(self):
        h = (self.b - self.a) / self.n
        total = (self.f(self.a) + self.f(self.b)) / 2.0

        for i in range(1, self.n):
            x_i = self.a + i * h
            total += self.f(x_i)

        return total * h