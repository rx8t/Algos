import math

from utils import get_float

a = get_float("Введите значение a: ")
x = get_float("Введите значение x: ")
y = a / (x**2 + 1) - math.cos(2 * x - 1)
print(f"Значеник функции y = {y:.6f}")
