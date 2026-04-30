import math

# Método de Simpson para integración numérica

class Simpson(object):
    def __init__(self, f, a, b, n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n

    def integrar(self):
        if self.n % 2 != 0:
            raise ValueError("El número de subintervalos (n) debe ser par para el método de Simpson.")
        
        h = (self.b - self.a) / self.n
        total = self.f(self.a) + self.f(self.b)

        for i in range(1, self.n):
            x_i = self.a + i * h
            if i % 2 == 0:
                total += 2 * self.f(x_i)
            else:
                total += 4 * self.f(x_i)

        return (h / 3) * total