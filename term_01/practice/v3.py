# Программа для поиска одинаковых кубов.
# Буланый Константин
# ИУ7-16Б
print('Читаю файл.')
input_file = open('input.txt', 'r', encoding='UTF8')
output_file = open('output.txt', 'w', encoding='UTF8')
print('Ищу одинаковые кубы.')
for line in input_file:
    if len(line) <= 1:
        output_file.write('\n')
        continue
    cube1 = line[:6]  # Первый куб.
    cube2 = line[6:12]  # Второй куб.
    if cube1 == cube2:
        same = True
    else:
        same = False
        for m in range(2):
            cube1_list = list(cube1)  # Грани первого куба в массиве.
            for i in range(3):
                up = cube1_list[0]  # Верхняя грань куба.
                down = cube1_list[5]  # Нижняя грань куба.
                sides = list(
                    cube1_list[1] + cube1_list[3] + cube1_list[4] + cube1_list[2])  # Оставшиеся грани массивом.
                if m == 1:  # Отзеркаливание.
                    up, down = down, up
                    sides = sides[-1::-1]
                cube1_list = list(cube1)
                for j in range(4):
                    if up + sides[0] + sides[3] + sides[1] + sides[2] + down == cube2:
                        same = True
                    else:
                        end = sides[0]  # Поворот куба на 90 градусов в горизонтальной плоскости.
                        for k in range(3):
                            sides[k] = sides[k + 1]
                        sides[3] = end
                cube1_list.insert(0, cube1_list[i + 1])  # Выбор новых верхней и нижней граней.
                cube1_list.pop(i + 2)
                cube1_list += cube1_list[4 - i]
                cube1_list.pop(4 - i)

    if same:
        output_file.write('TRUE\n')
    else:
        output_file.write('FALSE\n')
print('Записываю результаты.')
input_file.close()
output_file.close()
print('Закрываю файлы.')
