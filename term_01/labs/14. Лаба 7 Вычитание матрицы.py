# Программа для вычитания матрицы.
# Буланый Константин
# ИУ7-16Б


def check_float(line):
    check_point = check_e = False
    if "0" <= line[0] <= "9" or len(line) > 1 and line[0] in "-+." and "0" <= line[1] <= "9":
        if line[0] == ".":
            check_point = True
        for j in range(1, len(line)):
            if ("0" <= line[j] <= "9" or line[j] == "." and not check_point
                    or line[j] == "e" and not check_e or line[j] in "+-" and line[j - 1] == "e"):
                if line[j] == ".":
                    check_point = True
                if line[j] == "e":
                    if len(line) > j + 2:
                        check_e = True
                        check_point = True
                    elif len(line) > j + 1:
                        if "0" <= line[j + 1] <= "9":
                            for letter in line[j + 1:]:
                                if letter in "+-":
                                    return False
                    else:
                        return False
            else:
                return False

    else:
        return False
    return True


# Ввод матрицы
matrix = [[0 for i in range(5)] for j in range(5)]
for i in range(5):
    for j in range(5):
        x = input("Введите {} элемент {} строки: ".format(j + 1, i + 1)).strip()
        while not check_float(x):
            print("Получено неверное значение. Ввод должен быть числом.")
            x = input("Введите {} элемент {} строки еще раз: ".format(j + 1, i + 1)).strip()
        matrix[i][j] = float(x)
print()

# Вывод исходной матрицы
print("Исходная матрица.")
for i in range(5):
    for j in range(5):
        print("{:-9.5}".format(matrix[i][j]), end=" ")
    print()

# Удаление элементов главной диагонали.
for i in range(5):
    matrix[i].remove(matrix[i][i])

# Вывод полученной матрицы и поиск строки с максимальным количеством отрицательных элементом.
line_max_negatives = 1
max_negatives = 0
print("Полученная матрица.")
for j in range(5):
    negatives_count = 0
    for i in range(4):
        if matrix[j][i] < 0:
            negatives_count += 1
        print("{:-9.5}".format(matrix[j][i]), end=" ")
    if negatives_count > max_negatives:
        max_negatives = negatives_count
        line_max_negatives = j
    print()
print()

if max_negatives != 0:
    print("\nБольше всего отрицательных элементов в {} строке.".format(line_max_negatives + 1))
else:
    print("\nНи в одной строке нет отрицательных элементов.")
