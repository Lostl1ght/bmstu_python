# Программа для посчета количества перемен знака.
# Буланый Константин
# ИУ7-16Б


def lord_farquaad(x, y):  # Функция, проверяющая правильность научного ввода.
    count_of_e = 0
    count_of_minuses = 0
    count_of_pluses = 0
    count_of_dots = 0
    for letter_in_e_word in element:
        if letter_in_e_word == "e":
            count_of_e += 1
        if letter_in_e_word == "-":
            count_of_minuses += 1
        if letter_in_e_word == "+":
            count_of_pluses += 1
        if letter_in_e_word == ".":
            count_of_dots += 1

    if count_of_e == 1:
        if numbers > 1 and y < element.index("e") < len(element) - 2:  # Проверка положения Е.
            if element[element.index("e") + 1] == "-" and count_of_pluses == 0 and count_of_minuses == 1 + y:
                if "." not in element:
                    return x  # Целая мантисса и 'отрицательная' экспонента.
                elif y < element.index(".") < element.index("e") and count_of_dots == 1:
                    return x  # Дробная мантисса и 'отрицательная' экспонента.
                else:
                    return "oops"  # Неправильный ввод.
            elif element[element.index("e") + 1] == "+" and count_of_pluses == 1 and count_of_minuses == y:
                if "." not in element:
                    return x  # Целая мантисса и 'положительная' экспонента.
                elif y < element.index(".") < element.index("e") and count_of_dots == 1:
                    return x  # Дробная мантисса и 'положительная' экспонента.
                # Ниже - сигнал о неправильном вводе.
                else:
                    return "oops"
            else:
                return "oops"
        else:
            return "oops"
    else:
        return "oops"


print("Введите количество элементов массива натуральным числом: ", end="")
error = True
while error:
    n = input().strip()
    print()
    error = True
    non_numbers = 0
    numbers = 0
    for letter in n:
        if "0" <= letter <= "9":
            numbers += 1
        else:
            non_numbers += 1
    if numbers > 0:
        if non_numbers == 1 and n[0] == "+":
            error = False
        elif non_numbers == 0:
            error = False
    if n == "0":
        error = True
    if error:
        print("Количество элементов должно быть натуральным числом.\n"
              "Введите количество элементов массива снова: ", end="")

n = int(n)
array = []
print("\nВводите элементы массива в таком формате: (-)x, (-)x.y, (-)x(.z)e(+/-)y, где х, у, z - целые числа.")
print("Вводите элементы массива по одному в строке.\n")

i = 1
while i <= n:
    element = input("Введите элемент номер {}: ".format(i)).strip()
    print()
    repeat = False  # Если эта переменная станет True, вам стоит подумать о решениях, которые вы принимаете в жизни.
    for letter in element:
        if not ("0" <= letter <= "9" or letter == "e" or letter == "+" or letter == "-" or letter == "."):
            repeat = True  # Перезапуск ввода, если есть символы, невозможные при любом варианте ввода числа.
    if not repeat:
        non_numbers = 0  # Количество не цифр.
        numbers = 0  # Количество цифр.
        zeros = 0
        for letter in element:  # Подсчет не цифрЮ цифр и нулей.
            if "0" <= letter <= "9":
                numbers += 1
                if letter == "0":
                    zeros += 1
            else:
                non_numbers += 1

        if "." in element and non_numbers == 1 and zeros == len(element) - 1:
            array.append("0")  # Это ноль (он не имеет знака, т.ч при переходе отр.-0 или пол.-0 можно считать,
            # что смена знака произошла: его удалили).

        else:
            if element[0] == "-":  # Это отрицательное число (если это число).
                if non_numbers == 1 and numbers > 0:
                    array.append("-")  # Это целове отрицательное число.
                elif non_numbers == 2 and "." in element and numbers > 0:
                    array.append("-")  # Это отрицательная десятичная дробь.
                elif "e" in element:
                    his_royal_decision = lord_farquaad("-", 1)
                    if his_royal_decision != "oops":
                        array.append(his_royal_decision)  # Это научный вид.
                    else:
                        repeat = True
                else:
                    repeat = True

            else:  # Это положительное число (если это число).
                if numbers > 0 and non_numbers == 0:
                    array.append("+")  # Это целове положительное число.
                elif numbers > 0 and non_numbers == 1 and "+" in element:
                    array.append("+")  # Это целове положительное число.
                elif non_numbers == 1 and "." in element and numbers > 0:
                    array.append("+")  # Это положительная десятичная дробь.
                elif "e" in element:
                    his_royal_decision = lord_farquaad("+", 0)
                    if his_royal_decision != "oops":
                        array.append(his_royal_decision)  # Это научный вид.
                    else:
                        repeat = True
                else:
                    repeat = True

    # Если ввод неправильный итерация повторяется, иначе ввод продолжается.
    if repeat:
        print("Неверный ввод числа.\nПопробуйте еще раз.\n")
    else:
        i += 1

sign_changes = 0
for i in range(1, len(array)):
    if array[i] != array[i - 1]:
        sign_changes += 1

print(array)
print("Количество смен знака равно {}.".format(sign_changes))
