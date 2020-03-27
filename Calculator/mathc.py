a1 = '10001000011.111'
a2 = '-1000100100.010'


print('Input nums:')
print(a1, a2, sep='\n')


def signum(a1: str, a2: str) -> (bool, bool):
    sign_a1 = True
    sign_a2 = True
    if a1[0] == '-':
        sign_a1 = False
    
    if a2[0] == '-':
        sign_a2 = False

    return sign_a1, sign_a2


def converter(a1: str, a2: str) -> (str, str, int, int):
    c1 = ''
    for i in a1:
        if i == '.':
            continue
        c1 += i
    c2 = ''
    for i in a2:
        if i == '.':
            continue
        c2 += i

    dot_len_a1 = 0
    if '.' in a1:
        dot_len_a1 = len(a1[a1.index('.'):]) - 1
    dot_len_a2 = 0
    if '.' in a2:
        dot_len_a2 = len(a2[a2.index('.'):]) - 1

    if dot_len_a1 > dot_len_a2:
        c2 += '0' * (dot_len_a1 - dot_len_a2)
        dot_len = dot_len_a1
    elif dot_len_a1 < dot_len_a2:
        c1 += '0' * (dot_len_a2 - dot_len_a1)
        dot_len = dot_len_a2
    else:
        dot_len = dot_len_a2

    length = 0
    len_c1 = len(c1)
    if '-' in c1:
        len_c1 -= 1
        c1 = c1[1:]
    len_c2 = len(c2)
    if '-' in c2:
        len_c2 -= 1
        c2 = c2[1:]

    while length < max(len_c1, len_c2):
        length += 1

    bb1 = c1[::-1] + '0' * (length - len_c1)

    bb2 = c2[::-1] + '0' * (length - len_c2)

    return bb1, bb2, length, dot_len


def normalizer(c: str, dot_len: int, minus_after_operation: bool, minus_because_signs: bool) -> str:
    k = 0
    if dot_len > 0:
        c = c[:dot_len] + '.' + c[dot_len:]
        while c[k] == '0':
            k += 1
    c = c[::-1]
    i = 0
    if '1' not in c:
        return '0'
    while c[i] == '0':
        i += 1
    
    if minus_after_operation == minus_because_signs:
        return c[i:len(c) - k]    
    return '-' + c[i:len(c) - k]


def adder(b1: str, b2: str, length: int) -> (str, bool):
    c = ''
    flag = False
    for i in range(length):
        if b1[i] == '0' and b2[i] == '0':
            if flag:
                c += '1'
            else:
                c += '0'
            flag = False

        if b1[i] == '1' and b2[i] == '0' or b1[i] == '0' and b2[i] == '1':
            if flag:
                c += '0'
                flag = True
            else:
                c += '1'
                flag = False
        if b1[i] == '1' and b2[i] == '1':
            if flag:
                c += '1'
            else:
                c += '0'
            flag = True
    if flag:
        c += '1'

    return c, True


def subtractor(b1: str, b2: str, length: int) -> (str, bool):
    minus = True
    if b1[::-1] < b2[::-1]:
        b1, b2 = b2, b1
        minus = False
    c = ''
    flag = False
    for i in range(length):        
        if b1[i] == '0' and b2[i] == '0':            
            if flag:
                c += '1'
                flag = True
            else:
                c += '0'
                flag = False

        if b1[i] == '1' and b2[i] == '0':
            if flag:
                c += '0'
                
            else:
                c += '1'
            flag = False

        if b1[i] == '0' and b2[i] == '1':
            if flag:
                c += '0'
            else:
                c += '1'
            flag = True
        
        if b1[i] == '1' and b2[i] == '1':
            if flag:
                c += '1'
                flag = True
            else:
                c += '0'
                flag = False

    return c, minus


def check(a1: str, a2: str) -> bool:
    error = False
    if a1 == '' or a2 == '':
        error = True
    for i in a1:
        if i not in '01.-':
            error = True
            break
    for i in a2:
        if i not in '01.-':
            error = True
            break
    if a1.count('.') > 1:
        error = True
    if a2.count('.') > 1:
        error = True
    if a1.count('-') > 1:
        error = True
    if a2.count('-') > 1:
        error = True 
    if '-' in a1 and a1.index('-') != 0 or '-' in a2 and a2.index('-') != 0:
        error = True
     
    if error:
        return True
    else:
        return False


def calculate(a1: str, a2: str, operation: bool) -> str:
    if check(a1, a2):
        return
    sign_a1, sign_a2 = signum(a1, a2)
    b1, b2, length, dot_len = converter(a1, a2)
    if operation:
        if sign_a1 is True and sign_a2 is True:
            c, minus_after_operation = adder(b1, b2, length)
            minus_because_signs = True
        if sign_a1 is False and sign_a2 is False:
            c, minus_after_operation = adder(b1, b2, length)
            minus_because_signs = False        
        if sign_a1 is True and sign_a2 is False:
            c, minus_after_operation = subtractor(b1, b2, length)
            if b1[::-1] >= b2[::-1]:
                minus_because_signs = True
            else:
                minus_because_signs = False
        if sign_a1 is False and sign_a2 is True:
            c, minus_after_operation = subtractor(b1, b2, length)
            if b1[::-1] >= b2[::-1]:
                minus_because_signs = False
            else:
                minus_because_signs = True
    else:
        if sign_a1 is True and sign_a2 is True:
            c, minus_after_operation = subtractor(b1, b2, length)
            minus_because_signs = True
        if sign_a1 is False and sign_a2 is True:
            c, minus_after_operation = adder(b1, b2, length)
            minus_because_signs = False
        if sign_a1 is False and sign_a2 is False:
            c, minus_after_operation = adder(b1, b2, length)
            if b1[::-1] >= b2[::-1]:
                minus_because_signs = False
            else:
                minus_because_signs = True
        if sign_a1 is True and sign_a2 is False:
            c, minus_after_operation = adder(b1, b2, length)
            minus_because_signs = True
    res = normalizer(c, dot_len, minus_after_operation, minus_because_signs)

    return res

res = calculate(a1, a2, True) 
print('\nResult:', res)