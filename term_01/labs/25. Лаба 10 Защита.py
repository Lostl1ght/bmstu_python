from pickle import load, dump

first = open('first.txt', 'r', encoding='UTF8')
second = open('second.txt', 'r', encoding='UTF8')


num1 = first.readline()[:len(first.readline()) - 1]
num2 = second.readline()[:len(second.readline()) - 1]
result_num = int(num1) + int(num2)

result = open('result', 'wb')
dump(result_num, result)
result.close()

result = open('result', 'rb')

end = load(result)
print(end)

first.close()
second.close()
result.close()