# Программа для вычисления суммы ряда.
# Буланый Константин
# ИУ7-16Б

from math import fabs

x = float(input("Введите Х: "))
eps = float(input("Введите точность: "))
max_iter = int(input("Введите максимальное количество итераций: "))
step = int(input("Введите шаг печати: "))

# Вывод заголовка таблицы.
print("┌", "─" * 6, "┬", "─" * 15, "┬", "─" * 15, "┐", sep="")
print("│", " " * 2, "n", " " * 3, "│", " " * 7, "C", " " * 7, "│", " " * 7, "S", " " * 7, "│", sep="")
print("├", "─" * 6, "┼", "─" * 15, "┼", "─" * 15, "┤", sep="")

# Начальные значения.
total = 0  # Сумма ряда.
current = x  # Значение текущего члена.
n = 1  # Номер итерации.
current_step = 1  # Текущий шаг печати.

while fabs(current) > eps and n < max_iter:
    total += current

    # Вывод таблицы.
    if n == current_step:
        print("|{:^6}│{:^15.7}│{:^15.7}│".format(n, current, total))
        print("├", "─" * 6, "┼", "─" * 15, "┼", "─" * 15, "┤", sep="")
        current_step += step

    # Вычисление следующего члена последовательности.
    n += 1
    current = current * (2 * n - 3) * (2 * n - 3) * x * x / (2 * n - 1) / (2 * n - 2)

# Вывод последнего члена последовательности и конца таблицы.
total += current
print("|{:^6}│{:^15.7}│{:^15.7}│".format(n, current, total))
print("└", "─" * 6, "┴", "─" * 15, "┴", "─" * 15, "┘", sep="")

# Вывод значения суммы или сообщения о неудаче.
if fabs(current) > eps:
    # Изменение склонения в зависимости от количества итераций.
    if max_iter % 100 == 1:
        iterations = "итерацию"
    elif max_iter % 100 == 2 or max_iter == 3 or max_iter == 4:
        iterations = "итерации"
    else:
        iterations = "итераций"
    print("За", max_iter, iterations, "ряд не сошелся.")
else:
    print("Сумма ряда: {:.7}".format(total))
