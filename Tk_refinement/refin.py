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

# def pack(roots, eps):
#     r = str(abs(int(floor(log10(eps)))))
#     form = '{:.' + str(r) + 'f}'

#     for i in range(roots):


#     i = 1
#     n = len(roots)
#     while i < n:
#         if roots[i][:len(roots[i]) - 2] == roots[i - 1][:len(roots[i - 1]) - 2]:
#             roots.pop(i - 1)
#             n -= 1
#         i += 1
    
    
#     form.format(x)


start = 0
ends = 10
step = 3
eps = 1e-3

roots = []

end = start + step
while end < ends:
    if abs(f(start)) < eps:
        x, iterations = start, 0
        roots += [{'root': x, 'iterations': iterations, 'start': start, 'end': end}]
    elif abs(f(end)) < eps:
        x, iterations = end, 0
        roots += [{'root': x, 'iterations': iterations, 'start': start, 'end': end}]
    elif f(start) * f(end) < 0:
        x, iterations = chord_method(start, end, eps)
        roots += [{'root': x, 'iterations': iterations, 'start': start, 'end': end}]
    start, end = end, end + step
else:
    if abs(f(start)) < eps:
        x, iterations = start, 0
        roots += [{'root': x, 'iterations': iterations, 'start': start, 'end': end}]
    elif abs(f(ends)) < eps:
        x, iterations = ends, 0
        roots += [{'root': x, 'iterations': iterations, 'start': start, 'end': end}]
    elif f(start) * f(end) < 0:
        x, iterations = chord_method(start, ends, eps)
        roots += [{'root': x, 'iterations': iterations, 'start': start, 'end': end}]

for i in roots:
    print(i)