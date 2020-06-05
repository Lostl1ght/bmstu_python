def integral(a):
    return a * a * a - 10


start = float(input("start: "))
finish = float(input("finish: "))
frag = int(input("fragmentation: "))
step = (finish - start) / frag
x = start
area = 0
for i in range(frag):
    area += step * integral(x)
    x += step
print("left rectangle method area: ", area)
