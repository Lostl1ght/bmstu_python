a = [int(x) for x in input().split()]
n = len(a)

for i in range(n - 2):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

k = 0
lenS = 0
for i in range(n):
    c = 0
    for j in range(n):
        if a[k] == a[j]:
            c += 1
    if c == 1:
        lenS += 1
        end = a[k]
        for m in range(k, n - 1):
            a[m] = a[m + 1]
        a[n - 1] = end
    else:
        k += 1

# if lenS == 0:
#     print("all are same")
# elif lenS == n:
#     print("all are different")
# else:
#     for i in range(n - lenS, n):
#         print(a[i], end=" ")

if lenS == 0:
    print("all are same")
elif lenS == n:
    print("all are different")
else:
    brk = a[n - lenS]
    m = 1
    for i in range(n - 1):
        if a[i] == brk:
            break
        while a[i] == a[i + 1]:
            for j in range(i + 1, n - 1):
                a[j] = a[j + 1]
        else:
            m += 1
    for i in range(m - 1):
        print(a[i], end=" ")
