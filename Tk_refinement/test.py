from math import sin, floor, log10


def f(x):
    return sin(x) #x * x - 2


def d2(x):
    return -sin(x) #2


def iterations(start, interval_end, step, eps):
    def refinement(a, b, eps):

        if abs(f(a)) < eps:
            return a, 0
        if abs(f(b)) < eps:
            return b, 0

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
        itrs = 0
        while abs(delta) > eps:
            itrs += 1
            delta = f(x) * (x - c) / (f(x) - f(c))
            x -= delta

        return x, itrs

    end = start + step
    results = []
    round_to = abs(int(floor(log10(eps))))

    while end < interval_end:
        if f(start) * f(end) <= 0.0:
            root, itrs = refinement(start, end, eps)
            if abs(root) < eps:
                root = 0.0
            results += [{'root': round(root, round_to), 'itrs': itrs}]

        start = end
        end += step
    root, itrs = refinement(start, end, eps)
    if abs(root) < eps:
        root = 0.0
    results += [{'root': round(root, round_to), 'itrs': itrs}]

    return results


# start = float(input("Start: "))
# interval_end = float(input("End: "))
# step = float(input("Step: "))
# eps = float(input("Eps: "))

start = 1
interval_end = 5
step = 4
eps = 1e-3

results = iterations(start, interval_end, step, eps)

for i in results:
    print(i)
