sentence = input("Введите строку со словами: ").strip()
while not sentence:
    print("  Ошибка: строка не должна быть пустой.")
    sentence = input("Введите строку со словами: ").strip()

words = sentence.split()
longest = max(words, key=len)
print("Длина самого длинного слова:", len(longest))
