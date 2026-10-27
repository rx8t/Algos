from utils import get_float

print("Система: A1*x + B1*y = C1")
print("         A2*x + B2*y = C2")
A1 = get_float("A1: "); B1 = get_float("B1: "); C1 = get_float("C1: ")
A2 = get_float("A2: "); B2 = get_float("B2: "); C2 = get_float("C2: ")

det = A1*B2 - A2*B1
if det == 0:
    print("Система не имеет единственного решения (определитель равен 0).")
else:
    x = (C1*B2 - C2*B1) / det
    y = (A1*C2 - A2*C1) / det
    print(f"Решение: x = {x:.6f}, y = {y:.6f}")
