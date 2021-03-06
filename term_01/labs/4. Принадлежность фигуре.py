# Программа для решения квадратных уравнений
# Буланый Константин
# ИУ7-16Б
from math import fabs

x, y = (float(i) for i in input("Введите х и у: ").split())  # Ввод координат точки

z = (y + 3 * fabs(x - 3) - 3 <= 0 and y >= 0)  # Вычисление принадлежности точки фигуре

# Вывод соответствующего результата
if z:
    print("Точка принадлежит заданной фигуре")
else:
    print("Точка НЕ принадлежит заданной фигуре")
