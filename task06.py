from utils import get_int, get_positive_int

n = get_positive_int("Введите количество элементов: ")
lst = [get_int(f"  Элемент [{i+1}]: ") for i in range(n)]

if not any(x % 2 != 0 for x in lst):
    print("Нечётных чисел нет.")
else:
    result = [0 if x % 2 != 0 else x for x in lst]
    print("Список после обнуления нечётных чисел:", result)
