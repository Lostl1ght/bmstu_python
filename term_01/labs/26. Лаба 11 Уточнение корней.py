# Программа для уточнения корней.
# Буланый Константин
# ИУ7-16Б
from math import fabs, log10, floor, sin


# Проверка ввода чисел.
def input_float(float_message, error_message):
    while True:
        try:
            return float(input(float_message))
        except ValueError:
            print(error_message)
            continue


# Ввод данных.
interval_start = input_float('Введите начало интервала: ', 'Введите корректное число.')
interval_end = input_float('Ввелите конец интервала: ', 'Введите корректное число.')

while interval_end <= interval_start:
    print('Введите корректное число.')
    interval_end = input_float('Ввелите конец интервала: ', 'Введите корректное число.')

step = input_float('Введите длину шага: ', 'Введите корректное число.')
while step <= 0.0:
    print('Введите корректное число.')
    step = input_float('Введите длину шага: ', 'Введите корректное число.')

eps = input_float('Введите точность: ', 'Введите корректное число.')


# Функция, для которой ищутся корни.
def f(a):
    if a is None:
        return None
    return sin(a)


# Вторая производная.
def derivative2(a):
    return -sin(a)


# Уточнение корня.
def refinement(a, b):
    global point_error, iters, segment
    delta_x = eps + 1.0
    segment += 1
    if derivative2(a) * f(a) > 0.0:
        x0 = a
        x = b
    else:
        x0 = b
        x = a
    while fabs(delta_x) > eps:
        iters += 1
        delta_x = f(x) * (x - x0) / (f(x) - f(x0))
        x -= delta_x
    return x


start = interval_start  # Начало отрезка.
end = interval_start + step  # Конец отрезка.
results = []  # Результаты вычислений.
segment = 0  # Номер отрезка.
round_to = abs(int(floor(log10(eps))))  # Число, до которого округлять результаты.
flag = False
while end <= interval_end:
    if flag:
        flag = False
        continue
    iters = 0
    point_error = False  # В отрезке точка перегиба.
    if fabs(f(end)) < eps:
        segment += 1
        flag = True
        results += [{'segment': segment, 'start': round(start, round_to + 1),
                     'end': round(end, round_to + 1), 'root': end, 'f': round(f(end), round_to + 2),
                     'iter': iters, 'error': point_error}]
    if f(start) * f(end) < 0.0:
        root = refinement(start, end)
        results += [{'segment': segment, 'start': round(start, round_to + 1),
                     'end': round(end, round_to + 1), 'root': round(root, round_to), 'f': round(f(root), round_to + 2),
                     'iter': iters, 'error': point_error}]

    if end == interval_end:
        break
    start = end
    end += step

# Вывод таблицы.
print('┌─────────┬────────────┬───────────┬───────────────┬────────────────┬───────────────┐')
print('│ N от-ка │  Х начала  │  Х конца  │    Х корня    │ Значение ф-ции │ Кол-во ит-ций │')
for i in range(len(results)):
    print('├─────────┼────────────┼───────────┼───────────────┼────────────────┼───────────────┤')
    print('│{:^9d}│{:^12.7}│{:^11.7}│'.format(results[i]['segment'], results[i]['start'], results[i]['end']), end='')
    print('{:^15.7}│{:^16.0e}│{:^15}│'.format(results[i]['root'], results[i]['f'], results[i]['iter']))
print('└─────────┴────────────┴───────────┴───────────────┴────────────────┴───────────────┘')
