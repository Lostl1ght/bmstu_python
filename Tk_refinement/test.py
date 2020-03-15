from math import log10, floor, sin, cos


def f(x):
    return sin(x)
    # return x ** 2 - 4


def d(x):
    return cos(x)
    # return 2 * x

def d2(x):
    return -sin(x)
    # return 2


def chord_method(start, end, eps):
    iterations = 0
    if d(start) * d2(start) < 0:
        x = start
        calculate = lambda x: x - f(x) * (end - x) / (f(end) - f(x))
    else:
        x = end
        calculate = lambda x: x - f(x) * (start - x) / (f(start) - f(x))

    x_prev, x = x, calculate(x)
    while abs(x - x_prev) >= eps:
        x_prev, x = x, calculate(x)
        iterations += 1

    return x, iterations

start = -10
ends = 10
step = 3
eps = 1e-3

end = start + step
while end < ends:
    if f(start) * f(end) < 0:
        x, iterations = chord_method(start, end, eps)
        print(x)
    start, end = end, end + step

x, iterations = chord_method(start, ends, eps)
print(x)    