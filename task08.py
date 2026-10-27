from utils import get_int, get_positive_int


def get_positive_even_int(prompt: str) -> int:
    while True:
        val = get_positive_int(prompt)
        if val % 2 == 0:
            return val
        print("Ошибка: введите чётное натуральное число.")

def print_matrix(m):
    for row in m:
        print("  ".join(f"{x:4}" for x in row))

M = get_positive_even_int("Введите M - число строк (чётное): ")
N = get_positive_even_int("Введите N - число столбцов (чётное): ")
matrix = [[get_int(f"[{i+1}][{j+1}]: ") for j in range(N)] for i in range(M)]

print("Исходная матрица:")
print_matrix(matrix)

dm, dn = M // 2, N // 2
for i in range(dm):
    for j in range(dn):
        matrix[i][j], matrix[i+dm][j+dn] = matrix[i+dm][j+dn], matrix[i][j]

print("Матрица после перестановки верхней левой и нижней правой четвертей:")
print_matrix(matrix)