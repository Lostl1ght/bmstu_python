# Программа для .
# Буланый Константин
# ИУ7-16Б


def input_float(float_message, error_message):
    while True:
        try:
            return float(input(float_message))
        except ValueError:
            print(error_message)
            continue


def input_int(int_message, error_message):
    while True:
        try:
            line = input(int_message)
            if "e" in line or float(line) != int(line):
                print(error_message)
                continue
            return int(line)
        except ValueError:
            print(error_message)
            continue


def input_natural(natural_message, error_message):
    while True:
        try:
            line = input(natural_message)
            if "e" in line or float(line) != int(line) or int(line) <= 0:
                print(error_message)
                continue
            return int(line)
        except ValueError:
            print(error_message)
            continue


def check_float(line):
    while True:
        try:
            float(line)
            return True
        except ValueError:
            return False


def check_int(line):
    try:
        if "e" in line or float(line) != int(line):
            return False
        return True
    except ValueError:
        return False


def check_natural(line):
    try:
        if "e" in line or float(line) != int(line) or int(line) <= 0:
            return False
        return True
    except ValueError:
        return False


# ┬────────
# │ Ошибка
# ┼────────
# ┴────────
# if results[i]['error']:
    #     print('       ─       │       ──       │       ─       ', end='')
    # else:
# print('│{:^8s}│'.format(str(results[i]['error'])))

# print('Столбец Ошибка указывает, получилось ли уточнить корень. Если не получилось, то это значит, ',
#       'что в отрезок, где был локализован корень, попала точка перегиба. Попробуйте шаг меньше.', sep='\n')

    # else:
    #     point_error = True  # В отрезке точка перегиба.
    #     return None
# derivative2(b) * f(b) > 0.0:
#6.0 * (2.0 * a * a - 1.0)
#a * a * a * a - 3.0 * a * a + 1.0