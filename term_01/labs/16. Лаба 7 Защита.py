# Еденичная матрица пользовательн вводит число, если меньше 0, то заполняется нижний трейгольник, иначе верхний
# Среднее ар ненулевых елементов и поделить каждый элемент на это число

matrix = [[0 for i in range(5)] for j in range(5)]

for i in range(5):
    for j in range(5):
        if i == j:
            matrix[i][j] = 1
for line in matrix:
    print(line)
n = float(input())
if n < 0:
    k = 1
    for i in range(1, 5):
        for j in range(k):
            matrix[i][j] = n
        k += 1
else:
    k = 1
    for i in range(1, 5):
        for j in range(k):
            matrix[j][i] = n
        k += 1

for line in matrix:
    print(line)


s = (n * 10 + 5) / 15
for i in range(5):
    for j in range(5):
        matrix[i][j] /= s

for line in matrix:
    print(line)

print(s)

