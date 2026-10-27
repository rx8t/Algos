from utils import get_int, get_positive_int

n = get_positive_int("Введите количество элементов: ")
lst = [get_int(f"  Элемент [{i+1}]: ") for i in range(n)]

result = sorted(x for x in lst if x % 3 == 0)
if result:
    print("Числа кратные 3 по возрастанию:", result)
else:
    print("В списке нет чисел кратных 3.")
