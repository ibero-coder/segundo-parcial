import math

class RegresionLineal(object):
    def __init__(self, x: list, y: list):
        self.x = x
        self.y = y
        self.n = len(x)
        self.b0 = 0.0
        self.b1 = 0.0
        self.rxy = 0.0
        self.r2 = 0.0

    def calcular(self):
        n = self.n
        x = self.x
        y = self.y

        suma_x  = sum(x)
        suma_y  = sum(y)
        suma_x2 = sum(xi ** 2 for xi in x)
        suma_y2 = sum(yi ** 2 for yi in y)
        suma_xy = sum(x[i] * y[i] for i in range(n))

        x_avg = suma_x / n
        y_avg = suma_y / n

        self.b1 = (suma_xy - n * x_avg * y_avg) / (suma_x2 - n * x_avg ** 2)
        self.b0 = y_avg - self.b1 * x_avg

        num_r = n * suma_xy - suma_x * suma_y
        den_r = math.sqrt((n * suma_x2 - suma_x ** 2) * (n * suma_y2 - suma_y ** 2))

        self.rxy = num_r / den_r if den_r != 0 else 0.0
        self.r2  = self.rxy ** 2

    def predecir(self, xk: float) -> float:
        return self.b0 + self.b1 * xk
