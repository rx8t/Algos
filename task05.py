from utils import get_positive_int

n = get_positive_int("Введите натуральное число n: ")

total = 0.0
factorial = 1
for k in range(1, n + 1):
    factorial *= k
    total += 1.0 / factorial

print(f"Сумма 1 + 1/2! + ... + 1/{n}! = {total:.8f}")