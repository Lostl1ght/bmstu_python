import random


def insertion(array):
    for i in range(1, len(array)):
        cur = i
        while cur > 0 and array[cur] < array[cur - 1]:
            array[cur], array[cur - 1] = array[cur - 1], array[cur]
            cur -= 1


def selection(array):
    for i in range(len(array) - 1):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[minimum], array[i] = array[i], array[minimum]


def insertion_bin(array):
    def binsearch(array, value, start, end):
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


def shell(array):
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            cur = i
            while cur > 0 and array[cur] < array[cur - gap]:
                array[cur], array[cur - gap] = array[cur - gap], array[cur]
                cur -= gap

        gap //= 2


def bubble(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]


def bubble_barrier(array):
    sortd = False
    while not sortd:
        sortd = True
        for i in range(len(array) - 1):
            if array[i + 1] < array[i]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sortd = False


def shaker(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        right -= 1

        for i in range(right, left, -1):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]

        left += 1


def quicksort(array, left, right):
    if left >= right:
        return

    i, j = left, right
    pivot = array[random.randint(left, right)]

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quicksort(array, left, j)
    quicksort(array, i, right)

#
# a = [random.randint(-40, 50) for x in range(random.randint(5, 13))]
# print(a)
# quicksort(a, 0, len(a) - 1)
# print(a)

a = [1,3,2,4]
insertion_bin(a)
print(a)
