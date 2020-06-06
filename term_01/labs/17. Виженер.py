operation = int(input("Введите номер операции (1. Зашифровать, 2. Расшифровать): "))
start = 33
end = 122
length = end - start + 1
if operation == 1:
    key_word = input("Введите ключевое слово: ")
    word = input("Введите слово, которое хотите зашифровать: ")

    n_key_words = len(word) // len(key_word)
    helping_word = key_word * n_key_words + key_word[:len(word) % len(key_word)]

    # Алфавит от start до end
    chiffre = ""
    for i in range(len(word)):
        line = ord(helping_word[i]) - start
        column = ord(word[i]) - start

        if start + line + column <= end:
            symbol = chr(start + line + column)
        else:
            symbol = chr(start + line + column - length)
        chiffre = chiffre + symbol

    print(chiffre)
else:
    key_word = input("Введите ключевое слово: ")
    word = input("Введите слово, которое хотите расшифровать: ")

    n_key_words = len(word) // len(key_word)
    helping_word = key_word * n_key_words + key_word[:len(word) % len(key_word)]

    message = ""
    for i in range(len(word)):
        line = ord(helping_word[i]) - start
        letter = ord(word[i]) - start
        column = letter - line
        if column < 0:
            column = column + length
        symbol = chr(start + column)
        message = message + symbol

    print(message)