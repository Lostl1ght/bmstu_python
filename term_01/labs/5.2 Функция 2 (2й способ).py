# Программа для вычисления значения функции 3 2-м способом
# Буланый Константин
# ИУ7-16Б
from math import fabs

x = float(input("Введите х: "))  # Ввод х

# Вычисление значения функции и вывод полученного результата
if 1 < x < 3 or -1 > x > -3:
    y = -fabs(fabs(x) - 2) + 1
    print("Значение функции равно: {:.3}".format(y))
else:
    print("Значение функции равно: 0")
