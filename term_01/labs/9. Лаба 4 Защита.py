# 5 вниз и 1 вправо "│"
from math import fabs

start = float(input("start "))
finish = float(input("finish "))
step = float(input("step "))

x = start
max_y = (x - 1) ** 2 - 5
min_y = max_y
while x <= finish:
    if fabs(x) < 1e-8:
        x = 0.0
    y = (x - 1) ** 2 - 5
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y
    x += step

x = start
down = max_y - min_y
while x <= finish:
    if fabs(x) < 1e-8:
        x = 0.0
    y = (x - 1) ** 2 - 5
    if y < 0:
        if fabs(x) < 1e-8:
            dist = round((y - min_y) / down * 100) + 8
            dist0 = round((0.0 - min_y) / down * 100) + 8
            print("{:7.4} ".format(x), "─" * dist, "*", "─" * (dist0 - dist), "┼", "─" * (100 - dist
                                                                                          - dist0 - 8), sep="")
        else:
            dist = round((y - min_y) / down * 100) + 8
            dist0 = round((0.0 - min_y) / down * 100) + 8
            print("{:7.4} ".format(x), " " * dist, "*", " " * (dist0 - dist), "|", " " * (100 - dist
                                                                                          - dist0 - 8),  sep="")
    elif fabs(y) < 1e-8:
        dist0 = round((0.0 - min_y) / down * 100) + 8
        print("{:7.4} ".format(x), " " * dist0, "*", " " * (100 - dist0), sep="")
    else:
        dist = round((y - min_y) / down * 100) + 9
        dist0 = round((0.0 - min_y) / down * 100) + 9
        print("{:7.4} ".format(x), " " * dist0, "|", " " * (dist - dist0), "*", " " * (100 - dist - dist0 - 8), sep="")
    x += step
