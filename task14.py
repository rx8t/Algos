from utils import get_float


def get_nonzero_float(prompt: str) -> float:
    while True:
        val = get_float(prompt)
        if val != 0:
            return val
        print("Ошибка: введите вещественное число не равное нулю.")


def Quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


x = get_nonzero_float("Введите координату x != 0: ")
y = get_nonzero_float("Введите координату y != 0: ")

q = Quarter(x, y)
print(f"Точка ({x}, {y}) находится в {q}-й координатной четверти.")
