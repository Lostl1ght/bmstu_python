import time
from random import randint


def gettimeofday() -> None:
    return round(time.time() * 1000)


def insertion_bin(array: list) -> None:
    def binsearch(array: list, value: int, start: int, end: int) -> int:
        if start >= end:
            if array[start] > value:
                return start
            else:
                return start + 1

        mid = (start + end) // 2

        if array[mid] > value:
            return binsearch(array, value, start, mid - 1)
        elif array[mid] < value:
            return binsearch(array, value, mid + 1, end)
        else:
            return mid

    for i in range(1, len(array)):
        pos = binsearch(array, array[i], 0, i - 1)
        for j in range(i, pos, -1):
            array[j], array[j - 1] = array[j - 1], array[j]


def count(n: int, leng: int) -> float:
    a = []
    for i in range(n):
        a.append(randint(-1000, 1000))

    summ = 0
    for i in range(leng):
        print('Try', i + 1)    
        start = gettimeofday()
        insertion_bin(a[:])
        end = gettimeofday()
        print(end - start)
        summ += end - start

    return summ / leng

print(count(1000, 10))