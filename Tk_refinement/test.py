from math import sin, floor, log10


def f(x):
    return sin(x)


def d2(x):
    return -sin(x)


def iterations(start, interval_end, step, eps):
    def refinement(a, b, eps):
        def error(a, b):
            c = b - eps
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
            if itrs > 100:
                return error(a, b)
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

    i = 0
    length = len(results)
    while i < length - 1:
        if abs(results[i]['root'] - results[i + 1]['root']) < eps:
            results.pop(i + 1)
            length -= 1
        i += 1
    return results


# start = float(input("Start: "))
# interval_end = float(input("End: "))
# step = float(input("Step: "))
# eps = float(input("Eps: "))

start = -20
interval_end = 20
step = 3
eps = 1e-5

results = iterations(start, interval_end, step, eps)

for i in results:
    print(i)
