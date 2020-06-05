# Программа для поворота матрицы.
# Буланый Константин
# ИУ7-16Б


def check_natural(line):
    if set(line) in [{"0"}, {"-", "0"}, {"+", "0"}]:
        return False
    if "0" <= line[0] <= "9" or len(line) > 1 and line[0] == "+" and "0" <= line[1] <= "9":
        for j in range(1, len(line)):
            if not "0" <= line[j] <= "9":
                return False
    else:
        return False
    return True


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


n = input("Введите размер матрицы: ")
while not check_natural(n):
    print("Получено неверное значение. Ввод должен быть натуральным числом.")
    n = input("Введите размер матрицы еще раз: ")
n = int(n)

# Ввод матрицы
matrix = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        x = input("Введите {} элемент {} строки: ".format(j + 1, i + 1)).strip()
        while not check_float(x):
            print("Получено неверное значение. Ввод должен быть числом.")
            x = input("Введите {} элемент {} строки еще раз: ".format(j + 1, i + 1)).strip()
        matrix[i][j] = float(x)
print()

# Вывод исхохной матрицы.
print("Исходная матрица.")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
print()

k = n // 2  # Середина матрицы.
# Переворот матрицы низ-верх.
for i in range(k):
    matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]

# Переворот матрицы лево-право.
for i in range(n):
    for j in range(k):
        matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

# Вывод полученной матрицы.
print("Полученная матрица.")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
