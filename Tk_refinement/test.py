from math import sin, floor, log10


def f(x):
    return sin(x) #x * x - 2


def d2(x):
    return -sin(x) #2


def iterations(start, interval_end, step, eps):
    def refinement(a, b, eps):

        if abs(f(a)) < eps:
            return a
        if abs(f(b)) < eps:
            return b

        if f(a) * d2(a) > 0.0:
            c = a
        elif f(b) * d2(b) > 0.0:
            c = b
        else:
            c = (a + b) / 2

        if f(a) * d2(a) < 0.0:
            x = a
        elif f(b) * d2(b) < 0.0:
            x = b

        delta = eps + 1.0

        while abs(delta) > eps:
            delta = f(x) * (x - c) / (f(x) - f(c))
            x -= delta

        return x

    end = start + step
    results = []
    while end < interval_end:
        itrs = 0
        if f(start) * f(end) <= 0.0:
            results += [refinement(start, end, eps)]

        start = end
        end += step
    results += [refinement(start, interval_end, eps)]

    return results


# start = float(input("Start: "))
# interval_end = float(input("End: "))
# step = float(input("Step: "))
# eps = float(input("Eps: "))

start = 0
interval_end = 10
step = 3
eps = 1e-3

results = iterations(start, interval_end, step, eps)

for i in results:
    print(i)
