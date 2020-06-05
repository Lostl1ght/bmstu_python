def check_float(line):
    check_point = False
    check_e = False

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


def check_int(line):
    if "0" <= line[0] <= "9" or len(line) > 1 and line[0] in "-+" and "0" <= line[1] <= "9":
        for j in range(1, len(line)):
            if not "0" <= line[j] <= "9":
                return False
    else:
        return False
    return True


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
