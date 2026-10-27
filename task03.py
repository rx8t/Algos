from utils import get_float


def get_nonzero_float(prompt: str) -> float:
    while True:
        val = get_float(prompt)
        if val != 0:
            return val
        print("Ошибка: введите вещественное число не равное нулю.")

a = get_nonzero_float("Введите значение a (не равное 0): ")
x = get_float("Введите значение x: ")

y = 2*a*x**2 - 1 if x > 1 else 1 / a
print(f"Значение функции y = {y:.6f}")
