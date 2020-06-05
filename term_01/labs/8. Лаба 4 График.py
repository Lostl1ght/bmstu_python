# Программа для вычисления значений функций, их вывода в виде таблицы и построения графика.
# Буланый Константин
# ИУ7-16Б

from math import sqrt, tan, cos, pi, fabs

start = float(input("Введите начало отрезка: "))

finish = float(input("Введите конец отрезка: "))
while finish < start:
    print("Конец отрезка не может быть меньше начала.")
    finish = float(input("Введите конец отрезка снова: "))

step = float(input("Введите шаг: "))
while step <= 0.0:
    print("Шаг может быть только положительным.")
    step = float(input("Введите шаг снова: "))

# Вывод заголовка таблицы.
print("┌", "─" * 14, "┬", "─" * 14, "┬", "─" * 14, "┐", sep="")
print("│", " " * 6, " X ", " " * 5, "│", " " * 6, "Y1 ", " " * 5, "│", " " * 6, "Y2 ", " " * 5, "│", sep="")
print("├", "─" * 14, "┼", "─" * 14, "┼", "─" * 14, "┤", sep="")

# Начальный минимум Y2 и точки.
x = start
min_y2 = tan(0.2 * x + 0.3) - x ** 2 + 3
min_x2 = x

# Это все понадобится, когда нужно будет стоить график
# и down может стать < или = 0.
if finish < 0.0:
    min_y1 = 0.0
    min_x1 = 0.0
elif fabs(finish) < 1e-8:
    min_y1 = -2.0
    min_x1 = 0.0
else:
    while x < 0.0:
        x += step
    min_y1 = sqrt(x) - 2 * cos(pi * x / 2)
    min_x1 = x
# Начальный максимум Y1 и точка.
max_y1 = -2.0
max_x1 = 0.0

# Вычисление значений функций и вывод таблицы; поиск минимумов/максимумов и их точек.
x = start
while x <= finish:
    if fabs(x) < 1e-8:  # Это нужно, потому что при шаге < 1 0 плохо отображается.
        x = 0.0

    print("|{:^14.5}│".format(x), end="")

    if x < 0.0:
        print(" Нет значения │", end="")
    else:
        function_1 = sqrt(x) - 2 * cos(pi * x / 2)
        print("{:^14.5}|".format(function_1), end="")
        # Поиск маскимума Y1 и точки.
        if function_1 > max_y1:
            max_y1 = function_1
            max_x1 = x
        # Поиск минимума Y1 и точки.
        if function_1 < min_y1:
            min_y1 = function_1
            min_x1 = x

    function_2 = tan(0.2 * x + 0.3) - x ** 2 + 3
    # Поиск минимума Y2 и точки.
    if function_2 < min_y2:
        min_y2 = function_2
        min_x2 = x

    print("{:^14.5}|".format(function_2))

    if x > finish - step:
        break

    print("├", "─" * 14, "┼", "─" * 14, "┼", "─" * 14, "┤", sep="")
    x += step

# Вывод нижней линии.
print("└", "─" * 14, "┴", "─" * 14, "┴", "─" * 14, "┘", sep="")

print("\nМинимальное значение функции Y2: {:.5}.".format(min_y2))
print("Точка, в которой Y2 принимает минимальное значение: {:.5}.\n".format(min_x2))

###
# Оси и график.
down = max_y1 - min_y1  # Знаменатель для dist.
if fabs(down) < 1e-8:  # Случай, когда только одна точка будет нарисована.
    print(" " * 7, "{:^7.2}".format(min_y1), sep="")
    print(" " * 9, "└", sep="")
    print(" " * 9, "*", sep="")
elif down < 0.0:  # Когда ничего не будет нарисовано.
    print("На этом диапазоне X функция Y1 не определена.\nГрафик построить невозможно.")
else:  # Все остальные случаи.
    ###
    # ЧЕРЧЕНИЕ ОСИ Y.
    dashes_count = int(input("Введите количество делений(от 4 до 8): ")) + 1
    while dashes_count < 5 or dashes_count > 9:
        dashes_count = int(input("Введите корректное количество делений(от 4 до 8): ")) + 1
    print()

    # Вывод значений над делениями.
    print(" " * 6, "{:^7.2}".format(min_y1), sep="", end="")

    dash_dist = 76 // dashes_count  # Расстояние между делениями.
    incr = (max_y1 - min_y1) / dashes_count  # Цена деления.
    y = min_y1  # Значение деления.
    for i in range(dashes_count - 1):
        y += incr
        print(" " * (dash_dist - 7), "{:^7.2}".format(y), sep="", end="")
    print(" " * (86 - 18 - (dashes_count - 1) * (dash_dist - 1) - dashes_count), "{:^7.2}".format(max_y1), sep="")

    # Черчение прямой
    print(" " * 9, "└", sep="", end="")
    for i in range(dashes_count - 1):
        print("─" * (dash_dist - 1), "┴", sep="", end="")
    print("─" * (86 - 11 - (dashes_count - 1) * (dash_dist - 1) - dashes_count), "┘", sep="")

    ###
    # ЧЕРЧЕНИЕ ГРАФИКА.
    x = start  # Аргумент функции Y1.
    while x <= finish:
        if fabs(x) < 1e-8:  # Это нужно, потому что при шаге < 1 0 плохо отображается.
            x = 0.0

        if x >= 0.0:
            function_1 = sqrt(x) - 2 * cos(pi * x / 2)

            if min_y1 < 0.0 and max_y1 > 0.0:  # Критерий отображения оси Х.
                if function_1 < 0.0:
                    dist = round((function_1 - min_y1) / down * 75)  # Расстояние от левого края до звездочки.
                    print("{:8.5} ".format(x), " " * dist, "*", sep="", end="")
                    dist = round((0.0 - min_y1) / down * 75) - dist  # Расстояние от звездочки до оси Х.
                    print(" " * dist, "│", sep="")
                elif fabs(function_1) < 1e-8:
                    dist = round((0.0 - min_y1) / down * 75) + 1  # Расстояние от левого края до звездочки.
                    print("{:8.5} ".format(x), " " * dist, "*", sep="")
                else:
                    dist = round((0.0 - min_y1) / down * 75) + 1  # Расстояние от левого края до оси Х.
                    print("{:8.5} ".format(x), " " * dist, "│", sep="", end="")
                    dist = round((function_1 - min_y1) / down * 75) - dist - 1  # Расстояние от оси Х до звездочки.
                    print(" " * dist, "*", sep="")
            else:
                dist = round((function_1 - min_y1) / down * 75)  # Расстояние от левого края до звездочки.
                print("{:8.5} ".format(x), " " * dist, "*", sep="")

        else:
            print("{:8.5} ".format(x), end="")

            if min_y1 < 0.0 and max_y1 > 0.0:  # Критерий отображения оси Х.
                dist = round((0.0 - min_y1) / down * 75) + 1  # Расстояние от левого края до оси Х, когда не оп Y1
                print(" " * dist, "│", sep="")                # когда не определена функция Y1.

        x += step
print()
