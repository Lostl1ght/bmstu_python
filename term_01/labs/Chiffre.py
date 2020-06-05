matrix = [[0 for i in range(8)] for j in range(8)]

k = 1
for i in range(4):
    for j in range(4):
        matrix[i][j] = k
        k += 1

k = 0
for j in range(7, 3, -1):
    row = matrix[k][:4]
    for i in range(4):
        matrix[i][j] = row[i]
        matrix[j][7 - i] = row[i]
        matrix[7 - i][7 - j] = row[i]
    k += 1

for i in matrix:
    for m in i:
        print('{:3d}'.format(m), end=' ')
    print()
