from math import fabs, sin, cos

interval_start = float(input('Введите начало интервала: '))
interval_end = float(input('Ввелите конец интервала: '))

step = float(input('Введите длину шага: '))

eps = float(input('Введите точность: '))


def f(a):
    return sin(a)


def derivative1(a):
    return cos(a)


def derivative2(a):
    return -sin(a)


def refinement(a, b):
    delta_x = eps + 1.0

    if derivative1(b) < 0:
        x0 = b
        while fabs(delta_x) > eps:
            delta_x = f(x0) / derivative1(x0)
            x0 -= delta_x
        return x0
    else:
        x0 = a
        while fabs(delta_x) > eps:
            delta_x = f(x0) / derivative1(x0)
            x0 -= delta_x
        return x0


start = interval_start
end = interval_start + step
flag = False
while end <= interval_end:
    if flag:
        flag = False
        continue
    if fabs(f(start)) < eps:
        flag = True
        print(start)
    if f(start) * f(end) < 0.0:
        root = refinement(start, end)
        print(root)
    if end == interval_end:
        break
    start = end
    end += step
