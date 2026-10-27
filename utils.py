def get_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("Ошибка: введите вещественное число")

def get_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")

def get_positive_int(prompt: str) -> int:
    while True:
        val = get_int(prompt)
        if val > 0:
            return val
        print("Ошибка: введите натуральное число.")
