from utils import get_float


def get_positive_float(prompt: str) -> float:
    while True:
        val = get_float(prompt)
        if val > 0:
            return val
        print("Ошибка: введите положительное вещественное число.")

price = get_positive_float("Введите цену 1 кг конфет (руб.): ")
print(f"{'Масса (кг)':<10} {'Стоимость (руб.)':>19}")
print('-' * 30)
weight = 1.2
while weight <= 2.0:
    print(f"{weight:<10.1f} {price * weight:>19.2f}")
    weight = round(weight + 0.2, 1)
