# Программа для редактирования файлов.
# Буланый Константин
# ИУ7-16Б


def input_natural(natural_message, error_message):  # Проверка на натуральное число.
    while True:
        try:
            line = input(natural_message)
            if "e" in line or float(line) != int(line) or int(line) <= 0:
                print(error_message)
                continue
            return int(line)
        except ValueError:
            print(error_message)
            continue


def choose_read():  # Выбор файла на чтение.
    global file
    try:  # Если какой-то файл открыт, то он будет закрыт.
        file.close()
    except AttributeError:
        pass
    try:
        name = input('\nВведите имя файла: ')
        file = open(name, 'r', encoding='UTF8')
        print('Вы выбрали файл: ', name)
    except:
        print('Файл не найден.')


def create():  # Создание файла.
    global file
    try:  # Если какой-то файл открыт, то он будет закрыт.
        file.close()
    except AttributeError:
        pass
    try:
        name = input('\nВведите имя файла: ')
        file = open(name, 'w', encoding='UTF8')
        file.close()
        print('Вы создали файл: ', name)
        print('Файл закрыт.')

    except:
        print('Неправильно указано имя.')


def all_records():  # Вывод всех записей.
    global file
    if type(file) == bool:  # Если file - bool переменная, то файл не был выбран.
        print('Вы не выбрали файл.')
    else:
        heading = True  # Если True, то выведется заголовок.
        file.seek(0, 0)
        for line in file:
            if heading:
                print('|       Автор        |       Книга        |        Год         |')
                heading = False
            print('|{:^20}|{:^20}|{:^20}|'.format(line.split('|')[1], line.split('|')[2], line.split('|')[3]))


def one_field():  # Поиск по автору.
    global file
    if type(file) == bool:  # Если file - bool переменная, то файл не был выбран.
        print('Вы не выбрали файл.')
    else:
        author = input('Введите автора: ')
        found = True  # Если True, то выведется сообщение, что не найдено совпадений.
        heading = True  # Если True, то выведется заголовок.
        file.seek(0, 0)
        for line in file:
            if line.split('|')[1].lower() == author.lower():
                if heading:
                    print('|       Автор        |       Книга        |        Год         |')
                    heading = False
                print('|{:^20}|{:^20}|{:^20}|'.format(line.split('|')[1], line.split('|')[2], line.split('|')[3]))
                found = False
        if found:
            print('Совпадений не найдено.')


def two_field():  # Поиск по автору и году публикации.
    global file
    if type(file) == bool:  # Если file - bool переменная, то файл не был выбран.
        print('Вы не выбрали файл.')
    else:
        author = input('Введите автора: ')
        year = input_natural('Введите год публикации: ', 'Год публикации должен быть натуральным числом.')
        found = True  # Если True, то выведется сообщение, что не найдено совпадений.
        heading = True  # Если True, то выведется заголовок.
        file.seek(0, 0)
        for line in file:
            if line.split('|')[1].lower() == author.lower() and int(line.split('|')[3]) == year:
                if heading:
                    print('|       Автор        |       Книга        |        Год         |')
                    heading = False
                print('|{:^20}|{:^20}|{:^20}|'.format(line.split('|')[1], line.split('|')[2], line.split('|')[3]))
                found = False
        if found:
            print('Совпадений не найдено.')


def add_record():  # Добавление записей.
    global file
    try:  # Если какой-то файл открыт, то он будет закрыт.
        file.close()
    except AttributeError:
        pass

    name = input('\nВведите имя файла, в который хотите добавить запись: ')
    file = open(name, 'a', encoding='UTF8')
    print('Вы выбрали файл: ', name)

    while True:
        author = input('Введите имя автора: ')
        while len(author) > 19 or '|' in author:
            print('Неправильный ввод.')
            author = input('Введите имя автора: ')
        book = input('Введите название книги: ')
        while len(book) > 19 or '|' in author:
            print('Неправильный ввод.')
            book = input('Введите название книги: ')
        year = input('Введите год публикации: ')
        while len(year) > 19 or '|' in author:
            print('Неправильный ввод.')
            year = input_natural('Введите год публикации: ', 'Год публикации должен быть натуральным числом.')
        file.write('|' + author + '|' + book + '|' + year + '|\n')

        if input('Если хотите продолжнить запись, введите любую строку, иначе нажмите Enter: ') == '':
            print('Информация успешно записана, файл закрыт.')
            file.close()
            file = False
            break


def exit_prgm():  # Выход из программы.
    global ext, file
    ext = True
    try:
        file.close()
        print('Программа завершена успешно.')
    except AttributeError:
        print('Программа завершена успешно.')
        pass


ext = False  # Переменная, показывающая был ли инициализирован выход из программы.
file = False
while True:
    print('\nВведите номер операции, которую хотите выполнить:\n',
          '0. Открыть файл.\n',
          '1. Создать файл.\n',
          '2. Вывести все записи.\n',
          '3. Поиск по автору.\n',
          '4. Поиск по автору и году публикации.\n',
          '5. Добавить запись.\n',
          '6. Завершение программы.\n',
          'Ввод: ', sep='', end='')

    try:
        operation = int(input())
        if operation not in [0, 1, 2, 3, 4, 5, 6]:
            print('Некорректный ввод номера операции. Попробуйте снова.', end='')
        else:
            {0: choose_read, 1: create, 2: all_records,
             3: one_field, 4: two_field, 5: add_record, 6: exit_prgm}[operation]()
    except ValueError:
        print('Некорректный ввод номера операции. Попробуйте снова.', end='')

    if ext:
        break
