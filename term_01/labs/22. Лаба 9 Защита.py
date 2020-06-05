input_num = int(input('number: '))

# m = 1000
# d = 500
# c = 100
# l = 50
# x = 10
# i = 1

output = ''

output += input_num // 1000 * 'm'

input_num %= 1000




if input_num > 899:
    output += 'cm'

    input_num %= 100

    if input_num > 89:
        output += 'xc'

        input_num %= 10

        if input_num > 8:
            output += 'ix'
        else:
            output += input_num * 'i'

    else:
        output += input_num // 50 * 'l'

        input_num %= 50
        if input_num > 39:
            output += 'xl'

            input_num %= 10

            if input_num > 8:
                output += 'ix'
            else:
                output += input_num * 'i'

        else:
            output += input_num // 10 * 'x'

            input_num %= 10

            if input_num > 8:
                output += 'ix'
            else:
                output += input_num * 'i'

else:

    output += input_num // 500 * 'd'

    input_num %= 500

    if input_num > 399:
        output += 'cd'

        input_num %= 100

        if input_num > 89:
            output += 'xc'

            input_num %= 10

            if input_num > 8:
                output += 'ix'
            else:
                output += input_num * 'l'
        else:
            output += input_num // 50 * 'l'

            input_num %= 50
            if input_num > 39:
                output += 'xl'
            else:
                output += input_num // 10 * 'x'
    else:

        output += input_num // 100 * 'c'

        input_num %= 100

        if input_num > 89:
            output += 'xc'

            input_num %= 10

            if input_num > 8:
                output += 'ix'
            else:
                output += input_num * 'l'
        else:
            output += input_num // 50 * 'l'

            input_num %= 50
            if input_num > 39:
                output += 'xl'
            else:
                output += input_num // 10 * 'x'

print('out: ', output)