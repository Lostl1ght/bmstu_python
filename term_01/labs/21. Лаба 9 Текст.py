# Программа для редактирования текста.
# Буланый Константин
# ИУ7-16Б


input_text = open('text.txt', 'r', encoding='UTF8')
text = []
for line in input_text:
    text += [line]


def menu(a):
    try:
        if 1 <= int(a) <= 7:
            func = {1: widen, 2: left, 3: right, 4: replace_word, 5: delete, 6: replace_epx, 7: sent}
            func[int(a)]()
            return True
        else:
            return False
    except ValueError:
        return False


def widen():
    left()
    max_len = 0  # Максимальная длина строки.
    for i in range(len(text)):
        if len(text[i]) > max_len:
            max_len = len(text[i])

    for j in range(len(text)):
        array_line = text[j].split()  # Строка в массиве без пробелов

        spaces = max_len - len(text[j]) + len(array_line) - 1  # Количество пробелов, которые нужно добавить.

        if len(array_line) == 1:
            array_line[0] = array_line[0].center(spaces)
        elif len(array_line) == 0:
            continue
        else:
            k = 0
            for i in range(spaces):
                array_line[k] += ' '  # Добавляются пробелы до нужной ширины.
                k += 1
                if k == len(array_line) - 1:
                    k = 0

        text[j] = ''.join(array_line)


def left():
    for j in range(len(text)):
        array_line = text[j].split()  # Строка в массиве без пробелов

        for i in range(len(array_line) - 1):
            array_line[i] += ' '  # Добавляются пробелы до нужной ширины.
        text[j] = ''.join(array_line)


def right():
    left()
    max_len = 0  # Максимальная длина строки.
    for i in range(len(text)):
        if len(text[i]) > max_len:
            max_len = len(text[i])

    for j in range(len(text)):
        array_line = text[j].split()  # Строка в массиве без пробелов.

        for i in range(len(array_line) - 1):
            array_line[i] += ' '  # Добавляются пробелы до нужной ширины.
        text[j] = ''.join(array_line).rjust(max_len)


def replace_word():
    old = input('Введите слово, которое хотите заменить (с маленькой буквы): ')
    new = input('Введите слово, на которое хотите заменить: ')

    for j in range(len(text)):
        array_line = text[j].split()
        for i in range(len(array_line)):
            if array_line[i].lower() == old:
                array_line[i] = new
            elif array_line[i][:len(array_line[i]) - 1].lower() == old:
                array_line[i] = new + array_line[i][len(array_line[i]) - 1]
            if i != len(array_line) - 1:
                array_line[i] += ' '

            text[j] = ''.join(array_line)


def delete():
    word = input('Введите слово, которое хотите удалить: ')
    for j in range(len(text)):
        array_line = text[j].split()
        for i in range(len(array_line)):
            if array_line[i].lower() == word:
                array_line[i] = ''
            elif array_line[i][:len(array_line[i]) - 1].lower() == word:
                array_line[i] = '' + array_line[i][len(array_line[i]) - 1]
            if i != len(array_line) - 1:
                array_line[i] += ' '

            text[j] = ''.join(array_line)


def replace_epx():
    for j in range(len(text)):
        array_line = text[j].split()
        for i in range(len(array_line)):
            if '+' in array_line[i]:
                try:
                    k = array_line[i].index('+')
                    if '.' in array_line[i]:
                        array_line[i] = array_line[i][:len(array_line[i]) - 1]
                    result = int(array_line[i][:k]) + int(array_line[i][k + 1:])
                    array_line[i] = str(result)
                except ValueError:
                    pass

            if '-' in array_line[i]:
                try:
                    k = array_line[i].index('-')
                    if '.' in array_line[i]:
                        array_line[i] = array_line[i][:len(array_line[i]) - 1]
                    result = int(array_line[i][:k]) - int(array_line[i][k + 1:])
                    array_line[i] = str(result)
                except ValueError:
                    pass

            if i != len(array_line) - 1:
                array_line[i] += ' '
            text[j] = ''.join(array_line)


def sent():
    text_array = []  # Текст в массиве без ,;:
    for line_i in text:
        text_array += line_i[:len(line_i) - 1].split()
    for i in range(len(text_array)):
        if text_array[i][len(text_array[i]) - 1] in ',;:':
            text_array[i] = text_array[i][:len(text_array[i]) - 1]

    vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п',
                  'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь']

    sentences = []  # Текст в массиве, разбитый по предложениям.
    k = 0
    for i in range(len(text_array)):
        if text_array[i][len(text_array[i]) - 1] in '.!?':
            sentences += [text_array[k:i + 1]]
            k = i + 1

    for i in range(len(sentences)):
        sentences[i][len(sentences[i]) - 1] = sentences[i][len(sentences[i]) - 1][:len(sentences[i][len(sentences[i]) - 1][:len(sentences[i][len(sentences[i]) - 1]) - 1])]

    max_sent = -1
    max_words = 0
    for i in range(len(sentences)):  # Предложения.
        n_words = 0
        for j in range(len(sentences[i])):  # Слова.

            if sentences[i][j][0].lower() in vowels:  # Буквы.
                first = vowels
                second = consonants
            elif sentences[i][j][0].lower() in consonants:
                first = consonants
                second = vowels
            else:
                continue

            if len(sentences[i][j]) % 2 == 0:
                w = len(sentences[i][j])  # Конец пос-ти range ниже.
            else:
                w = len(sentences[i][j]) - 1
                if sentences[i][j][len(sentences[i][j]) - 1] not in first:
                    continue

            for k in range(0, w, 2):
                if sentences[i][j][k].lower() not in first or sentences[i][j][k + 1].lower() not in second:
                    break
                if k == w - 2:
                    n_words += 1

        if n_words > max_words:
            max_words = n_words
            max_sent = i

    print('Предложение номер {} - предложение с макс. слов, где гласные чередуются с согласными.'.format(max_sent + 1))


for line in text:
    print(line, end='')

while True:
    print('\nВведите номер операции, которую хотите выполнить:\n',
          '1. Выровнять по ширине.\n',
          '2. Выровнять по левому краю.\n',
          '3. Выровнять по правому краю\n',
          '4. Заменить слово.\n',
          '5. Удалить слово.\n',
          '6. Заменить сложение и вычитание значением.\n',
          '7. Посчитать кол-во предложений с макс. слов, где гласные чередуются с согласными.\n',
          'Если хотите завершить программу, введите любую другую строку.\n',
          'Ввод: ', sep='', end='')

    flg = menu(input())
    print()
    if not flg:
        print('Программа завершена успешно.')
        break

    for line in text:
        print(line)

input_text.close()
