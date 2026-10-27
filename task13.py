from utils import get_int

print("а) Нахождение уникальных цифр числа")
n = get_int("Введите целое число: ")
digits = sorted(set(str(n)))
print("Уникальные цифры в возрастающем порядке:", digits)

print("б) A является строгим подмножеством B?")
A = set(input("Введите элементы множества A через пробел: ").strip().split())
B = set(input("Введите элементы множества B через пробел: ").strip().split())
print(f"A = {A}")
print(f"B = {B}")
print("A является строгим подмножеством B" if A < B else "A не является строгим подмножеством B")
