from utils import get_float, get_positive_int

print("а) Сумма значений словаря")
n = get_positive_int("Количество пар ключ-значение: ")
d = {}
for _ in range(n):
    key = input("Ключ: ").strip()
    d[key] = get_float("  Значение (число): ")
print("Словарь:", d)
print("Сумма значений:", sum(d.values()))

print("б) Список -> словарь вложенных словарей")
elems = input("Введите элементы через пробел: ").strip().split()
nested = {item: {} for item in elems}
print("Результат:", nested)

print("в) Все ли значения словаря одинаковы?")
m = get_positive_int("Количество пар ключ-значение: ")
d2 = {}
for _ in range(m):
    key = input("Ключ: ").strip()
    d2[key] = input("Значение: ").strip()
all_same = " " if len(set(d2.values())) <= 1 else " не"
print("Словарь:", d2)
print(f"Значения{all_same}одинаковы")
