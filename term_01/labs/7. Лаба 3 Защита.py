from math import sqrt

x = [0] * 3
y = [0] * 3
x[0], y[0] = (int(i) for i in input("First x and y: ").split())
x[1], y[1] = (int(i) for i in input("Second x and y: ").split())
x[2], y[2] = (int(i) for i in input("Third x and y: ").split())

x_v = [0] * 3
y_v = [0] * 3
for i in range(3):
    x_v[i] = x[(i + 1) % 3] - x[i]
    y_v[i] = y[(i + 1) % 3] - y[i]

len_v = [0.0] * 3
for i in range(3):
    len_v[i] = sqrt(x_v[i] ** 2 + y_v[i] ** 2)

min_len = len_v[0]
i_min = 0
for i in range(2):
    if len_v[i + 1] < min_len:
        min_len = len_v[i + 1]
        i_min = i + 1

x_med = x_v[i_min] / 2
y_med = y_v[i_min] / 2

s_ind = [0, 1, 2]
s_ind.remove((i_min + 1) % 3)
s_ind.remove(i_min)

x_middle = x_med + x[i_min]
y_middle = y_med + y[i_min]

xxx = x_middle - x[s_ind[0]]
yyy = y_middle - y[s_ind[0]]
len_med = sqrt(xxx ** 2 + yyy ** 2)

print("Median length is {:.8}".format(len_med))
