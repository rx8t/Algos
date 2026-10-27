print("а) Поиск элемента в кортеже")
t = tuple(input("Введите элементы кортежа через пробел: ").strip().split())
print("Кортеж:", t)
elem = input("Элемент для поиска: ").strip()
count = t.count(elem)
if count:
    print(f"Элемент найден, вхождений: {count}")
else:
    print("Элемент не найден.")

print("б) Список строк -> кортеж без повторений")
raw2 = input("Введите строки через пробел: ").strip().split()
result = tuple(dict.fromkeys(raw2))
print("Исходный список :", raw2)
print("Кортеж без повторений:", result)
