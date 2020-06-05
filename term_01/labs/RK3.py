odd = 0
even = 0
file = open('input.txt', 'r', encoding='UTF8')
out = open('output.txt', 'w', encoding='UTF8')

for i in file:
    if int(i[:len(i) - 1]) % 2 == 1:
        odd += 1
    else:
        even += 1

file.seek(0, 0)
for i in file:
    if int(i[:len(i) - 1]) % 2 == 1:
        max_odd = int(i[:len(i) - 1])
        min_odd = int(i[:len(i) - 1])

file.seek(0, 0)
for i in file:
    if int(i[:len(i) - 1]) % 2 == 1:
        if int(i[:len(i) - 1]) > max_odd:
            max_odd = int(i[:len(i) - 1])
        if int(i[:len(i) - 1]) < min_odd:
            min_odd = int(i[:len(i) - 1])

k_max_odd = 0
file.seek(0, 0)
for i in file:
    if int(i[:len(i) - 1]) % 2 == 1:
        if int(i[:len(i) - 1]) == max_odd:
            k_max_odd += 1
last_min_odd = min_odd - 1

for k in range(odd):
    file.seek(0, 0)
    for i in file:
        if int(i[:len(i) - 1]) % 2 == 1:
            if int(i[:len(i) - 1]) < min_odd and int(i[:len(i) - 1]) > last_min_odd:
                min_odd = int(i[:len(i) - 1])

    file.seek(0, 0)
    for i in file:
        if int(i[:len(i) - 1]) % 2 == 1 and int(i[:len(i) - 1]) == min_odd:
            if min_odd == max_odd and k_max_odd > 0:
                out.write(str(min_odd) + '\n')
                k_max_odd -= 1
            elif min_odd != max_odd:
                out.write(str(min_odd) + '\n')
            else:
                break

    last_min_odd = min_odd
    min_odd = max_odd

file.seek(0, 0)
for i in file:
    if int(i[:len(i) - 1]) % 2 == 0:
        max_even = int(i[:len(i) - 1])
        min_even = int(i[:len(i) - 1])

file.seek(0, 0)
for i in file:
    if int(i[:len(i) - 1]) % 2 == 0:
        if int(i[:len(i) - 1]) > max_even:
            max_even = int(i[:len(i) - 1])
        if int(i[:len(i) - 1]) < min_even:
            min_even = int(i[:len(i) - 1])

k_max_even = 0
file.seek(0, 0)
for i in file:
    if int(i[:len(i) - 1]) % 2 == 0:
        if int(i[:len(i) - 1]) == max_even:
            k_max_even += 1
last_min_even = min_even - 1

for k in range(even):
    file.seek(0, 0)
    for i in file:
        if int(i[:len(i) - 1]) % 2 == 0:
            if int(i[:len(i) - 1]) < min_even and int(i[:len(i) - 1]) > last_min_even:
                min_even = int(i[:len(i) - 1])

    file.seek(0, 0)
    for i in file:
        if int(i[:len(i) - 1]) % 2 == 0 and int(i[:len(i) - 1]) == min_even:
            if min_even == max_even and k_max_even > 0:
                out.write(str(min_even) + '\n')
                k_max_even -= 1
            elif min_even != max_even:
                out.write(str(min_even) + '\n')
            else:
                break

    last_min_even = min_even
    min_even = max_even

file.close()
out.close()
