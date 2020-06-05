operation = int(input("Введите номер операции (1. Зашифровать, 2. Расшифровать): "))
if operation == 1:
    key_word = input("Введите ключевое слово: ")
    word = input("Введите слово, которое хотите зашифровать: ")

    n_key_words = len(word) // len(key_word)
    helping_word = key_word * n_key_words + key_word[:len(word) % len(key_word)]

    # Алфавит от 97 до 122
    chiffre = ""
    for i in range(len(word)):
        line = ord(helping_word[i]) - 97
        column = ord(word[i]) - 97

        if 97 + line + column <= 122:
            symbol = chr(97 + line + column)
        else:
            symbol = chr(97 + line + column - 26)
        chiffre = chiffre + symbol

    print(chiffre)
else:
    key_word = input("Введите ключевое слово: ")
    word = input("Введите слово, которое хотите расшифровать: ")

    n_key_words = len(word) // len(key_word)
    helping_word = key_word * n_key_words + key_word[:len(word) % len(key_word)]

    message = ""
    for i in range(len(word)):
        line = ord(helping_word[i]) - 97
        letter = ord(word[i]) - 97
        column = letter - line
        if column < 0:
            column = column + 26
        symbol = chr(97 + column)
        message = message + symbol

    print(message)