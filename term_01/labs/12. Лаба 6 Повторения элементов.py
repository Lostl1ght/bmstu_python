# Программа для посчета максимального количества повторений элементов массива.
# Буланый Константин
# ИУ7-16Б

from random import randint

# Ввод кол-ва эл-тов массива и проверка, является ли ввод натуральным числом.
print("Введите количество элементов массива натуральным числом: ", end="")
error = True
while error:
    n = input().strip()
    print()
    error = False
    for letter in n:
        if not "0" <= letter <= "9":
            error = True
    if n == "0":
        error = True
    if error:
        print("Количество элементов должно быть натуральным числом.\n"
              "Введите количество элементов массива снова: ", end="")
n = int(n)

# Ввод отрезка, из которого будут выбираться случайные числа, и проверка, является ли ввод целым числом.
segment = [0, 0]
message = ["Введите начало отрезка, из которого будут выбираться случайные числа, целым числом: ",
           "Введите конец отрезка целым числом: "]
message1 = ["Введите начало отрезка снова: ", "Введите конец отрезка снова: "]
for j in range(2):
    print(message[j], end="")
    error = True
    while error:
        segment[j] = input().strip()
        print()
        error = True
        non_numbers = 0
        numbers = 0
        for letter in segment[j]:
            if "0" <= letter <= "9":
                numbers += 1
            else:
                non_numbers += 1
        if numbers > 0:
            if non_numbers == 1 and segment[j][0] == "-":
                error = False
            elif non_numbers == 0:
                error = False
        if error:
            print("Начало отрезка должно быть целым числом.\n", message1[j], end="")
        elif j == 1 and int(segment[1]) < segment[0]:
            print("Конец отрезка должен быть больше начала.\n", message1[1], sep="", end="")
            error = True
    segment[j] = int(segment[j])

# Формирование массива.
array = []
for i in range(n):
    array.append(randint(segment[0], segment[1]))

# Сортировка пузырьком.
for i in range(n - 2):
    for j in range(n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

# Посчет кол-ва повторений и вывод массива.
print("Сформированный и отсортированный массив: {}".format(array[0]), end="")
count = 1
max_count = 1
for i in range(1, n):
    if array[i] == array[i - 1]:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 1
    print(" {}".format(array[i]), end="")
if count > max_count:
    max_count = count

print(".\n\nМаксимальное количество повторений элементов массива равно {}.\n".format(max_count))
