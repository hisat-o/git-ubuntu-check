import math

def f(x):
    return 4 * math.exp(-x) * math.sin(x) - 1

def regulaFalsi(a, b, tol):
    while abs(b - a) >= tol:
        # Calculate the point c using Regula-Falsi method
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(c) == 0.0:
            return c

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c

if __name__ == "__main__":
    a = 0.0  # Lower bound of interval
    b = 0.5  # Upper bound of interval
    tolerance = 0.001  # Tolerance for accuracy

    root = regulaFalsi(a, b, tolerance)

    print("The root of the equation 4e^(-x)sin(x) - 1 = 0 within the interval [0, 0.5] is approximately:", root)

