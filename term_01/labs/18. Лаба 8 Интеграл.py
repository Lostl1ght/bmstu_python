from math import fabs


def check_natural(line):
    try:
        if "e" in line or float(line) != int(line) or int(line) <= 0:
            return False
        return True
    except ValueError:
        return False


def check_float(line):
    try:
        float(line)
        return True
    except ValueError:
        return False


def integral(a):
    return a * a


def antiderivative(a, b):
    zero = 0
    l = 3
    if a < zero < b:
        return b ** l / l + a ** l / l
    if a >= zero:
        return b ** l / l - a ** l / l
    if b <= zero:
        return -(b ** l / l - a ** l / l)


start = input("Введите начало отрезка: ")
while not check_float(start):
    print("Неверный ввод. Введено не число.")
    start = input("Введите начало отрезка еще раз: ")
start = float(start)

finish = input("Введите конец отрезка: ")
while not check_float(finish) or float(finish) <= start:
    print("Неверный ввод. Введено не число или конец меньше или равен началу.")
    finish = input("Введите конец отрезка еще раз: ")
finish = float(finish)

fragmentation = [0, 0]
message = ["Введите первое число разбиений: ", "Введите второе число разбиений: ",
           "Введите превое число разбиений еще раз: ", "Введите второе число разбиений еще раз: "]

for i in range(2):
    fragmentation[i] = input(message[i])
    while not check_natural(fragmentation[i]):
        print("Неверный ввод. Введено не натуральное число.")
        fragmentation[i] = input(message[i + 2])
    fragmentation[i] = int(fragmentation[i])

# Шаг вычислений.
step = [0, 0]
for i in range(2):
    step[i] = (finish - start) / fragmentation[i]

# Метод средних прямоугольников
area_rectangle = [0, 0]
for i in range(2):
    x = start
    rectangle = integral(x) * step[i] / 2
    area_rectangle[i] += fabs(rectangle)
    x += step[i]

    while x < finish:
        rectangle = integral(x) * step[i]
        area_rectangle[i] += fabs(rectangle)
        x += step[i]

    rectangle = integral(x) * step[i] / 2
    area_rectangle[i] += fabs(rectangle)

# Метод парабол.
area_parabola = [0, 0]
for i in range(2):
    if fragmentation[i] % 2 == 1:
        area_parabola[i] = "-"
        continue
    x = start
    for j in range(fragmentation[i] + 1):
        parabola = integral(x)
        if j != 0 and j != fragmentation[i]:
            if j % 2 == 0:
                parabola *= 2
            else:
                parabola *= 4
        area_parabola[i] += fabs(parabola)
        x += step[i]
    area_parabola[i] *= step[i] / 3

# Вывод таблицы
print("┌", "─" * 6, "┬", "─" * 14, "┬", "─" * 14, "┐", sep="")
print("│", " " * 2, "  ", " " * 2, "│", " " * 5, "Rec", " " * 6, "│", " " * 5, "Par", " " * 6, "│", sep="")
for i in range(2):
    print("├", "─" * 6, "┼", "─" * 14, "┼", "─" * 14, "┤", sep="")
    print("│", " " * 2, "N", i + 1, " " * 2, "│", "{:^14.7}".format(area_rectangle[i]), "│",
          "{:^14.7}".format(area_parabola[i]), "│", sep="")
print("└", "─" * 6, "┴", "─" * 14, "┴", "─" * 14, "┘", sep="")

eps = input("Введите точность: ")
while not check_float(eps):
    print("Неверный ввод. Введено не число.")
    eps = input("Введите точность еще раз: ")
eps = float(eps)
fragmentation_eps = 1

if fabs(antiderivative(start, finish) - area_parabola[0]) <= fabs(antiderivative(start, finish) - area_rectangle[0]):
    # Получение более точного ответа методом прямоугольников.

    area_rectangle_eps = -1.0
    while fabs(antiderivative(start, finish) - area_rectangle_eps) > eps:
        fragmentation_eps *= 2

        area_rectangle_eps = 0
        x = start
        step_eps = (finish - start) / fragmentation_eps
        rectangle = integral(x) * step_eps / 2
        area_rectangle_eps += fabs(rectangle)
        x += step_eps

        while x < finish:
            rectangle = integral(x) * step_eps
            area_rectangle_eps += fabs(rectangle)
            x += step_eps

        rectangle = integral(x) * step_eps / 2
        area_rectangle_eps += fabs(rectangle)

    print("\nЭталонное значение интеграла: {:.7}".format(antiderivative(start, finish)))
    print("Метод средних прямоугольников наименее точный.")
    print("Заданной точности удалось достигнуть при использовании {} разбиений. "
          "Полученное значение интеграла равно: {:.7}".format(fragmentation_eps, area_rectangle_eps))


else:
    # Получение более точного ответа методом парабол.
    area_parabola_eps = -1.0
    while fabs(antiderivative(start, finish) - area_parabola_eps) > eps:
        fragmentation_eps *= 2
        x = start
        step_eps = (finish - start) / fragmentation_eps
        for j in range(fragmentation_eps + 1):
            parabola = integral(x)
            if j != 0 and j != fragmentation_eps:
                if j % 2 == 0:
                    parabola *= 2
                else:
                    parabola *= 4
            area_parabola_eps += fabs(parabola)
            x += step_eps
        area_parabola_eps *= step_eps / 3

    print("\nЭталонное значение интеграла: {:.7}".format(antiderivative(start, finish)))
    print("Метод парабол наименее точный.")
    print("Заданной точности удалось достигнуть при использовании {} разбиений. "
          "Полученное значение интеграла равно: {:.7}".format(fragmentation_eps, area_parabola_eps))
