# Программа для решения квадратных уравнений
# Буланый Константин
# ИУ7-16Б
from math import sqrt

a, b, c = (float(i) for i in input('Введите коэффициенты: ').split())
if a == 0:
    if b == 0:
        if c == 0:
            print('Решение - все действительные числа.')
        else:
            print('Нет решений.')
    else:
        x = -c / b
        print('Решение: ', '{:.3}'.format(x))
else:
    d = b * b - 4 * a * c  # d - дискриминант
    if d < 0:
        print('Нет действительных решений')
    else:
        if d == 0:
            x = -b / (2 * a)
            print('Одно решение: {:.3}'.format(x))
        else:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            print('Два решения: {:.3} {:.3}'.format(x1, x2))
