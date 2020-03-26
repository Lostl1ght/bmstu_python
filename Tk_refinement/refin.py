from math import log10, floor, sin, cos
import scipy.optimize as optimize


def f(x):
    # return sin(x)
    # return x ** 2 - 4
    return (x - 1) ** 3 - 2

def d(x):
    # return cos(x)
    # return 2 * x
    return 3 * (x - 1) ** 2

def d2(x):
    # return -sin(x)
    # return 2
    return 6 * (x - 1)


def chord_method(start, ends, step, eps):

    def refinement(start, end, eps):
        iterations = 0
        if d(start) * d2(start) < 0:
            x = start
            def calculate(x): return x - f(x) * (end - x) / (f(end) - f(x))
        else:
            x = end
            def calculate(x): return x - f(x) * (start - x) / (f(start) - f(x))

        x_prev, x = x, calculate(x)
        while abs(x - x_prev) >= eps:
            x_prev, x = x, calculate(x)
            iterations += 1

        return x, iterations

    def pack(roots, eps):
        r = str(abs(int(floor(log10(eps)))))
        form = '{:.' + str(r) + 'f}'

        for i in range(len(roots)):
            if abs(roots[i]['root']) < eps:
                roots[i]['root'] = abs(roots[i]['root'])
            roots[i]['root'] = form.format(roots[i]['root'])

        i = 1
        n = len(roots)
        while i < n:
            if roots[i]['root'][:len(roots[i]['root']) - 2] == roots[i - 1]['root'][:len(roots[i - 1]['root']) - 2]:
                roots.pop(i - 1)
                n -= 1
            i += 1

        max_len_root = 0
        max_len_it = 0
        max_len_start = 0
        max_len_end = 0
        for i in roots:
            if len(i['root']) > max_len_root:
                max_len_root = len(i['root'])
            if len(str(i['iterations'])) > max_len_it:
                max_len_it = len(str(i['iterations']))
            if len(str(i['start'])) > max_len_start:
                max_len_start = len(str(i['start']))
            if len(str(i['end'])) > max_len_end:
                max_len_end = len(str(i['end']))

        for i in range(len(roots)):
            roots[i]['root'] = ' ' * (max_len_root - len(roots[i]['root'])) + roots[i]['root']
            roots[i]['iterations'] = ' ' * (max_len_it - len(str(roots[i]['iterations']))) + str(roots[i]['iterations'])
            roots[i]['start'] = ' ' * (max_len_start - len(str(roots[i]['start']))) + str(roots[i]['start'])
            roots[i]['end'] = ' ' * (max_len_end - len(str(roots[i]['end']))) + str(roots[i]['end'])

    roots = []

    end = start + step
    while end < ends:
        if abs(f(start)) < eps:
            x, iterations = start, 0
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': end}]
        elif abs(f(end)) < eps:
            x, iterations = end, 0
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': end}]
        elif f(start) * f(end) < 0:
            x, iterations = refinement(start, end, eps)
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': end}]
        start, end = end, end + step
    else:
        if abs(f(start)) < eps:
            x, iterations = start, 0
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': ends}]
        elif abs(f(ends)) < eps:
            x, iterations = ends, 0
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': ends}]
        elif f(start) * f(ends) < 0:
            x, iterations = refinement(start, ends, eps)
            roots += [{'root': x, 'iterations': iterations,
                       'start': start, 'end': ends}]

    pack(roots, eps)

    return roots




start = -10
ends = 10
step = 2
eps = 1e-4

def bisect(start, ends, step):
    end = start + step
    inflation = []
    eps = 1e-7
    round_to = abs(int(floor(log10(eps))))
    while start < ends:
        if abs(d2(start)) < 1e-3:
            inflation.append(round(start, round_to))
        elif abs(d2(end)) < 1e-3:
            inflation.append(round(end, round_to))
        elif d2(start) * d2(end) < 0:
            x = optimize.bisect(d2, start, end, rtol=eps)
            inflation.append(round(x, round_to))
        start, end = end, end + step
    else:
        if d2(start) * d2(ends) < 0:
            x = optimize.bisect(d2, start, ends, rtol=1e-3)
            inflation.append(round(x, round_to))

    return inflation


roots = chord_method(start, ends, step, eps)

for i in roots:
    print(i)

inflation = bisect(start, ends, step)

for i in inflation:
    print(i)