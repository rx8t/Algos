from utils import get_int, get_positive_int


def SwapCol(A, k1, k2):
    for row in A:
        row[k1], row[k2] = row[k2], row[k1]


def print_matrix(m):
    for row in m:
        print("  " + "  ".join(f"{x:4d}" for x in row))


def get_col_index(prompt, n):
    while True:
        val = get_int(prompt)
        if 1 <= val <= n:
            return val - 1
        print(f"  Ошибка: номер столбца должен быть от 1 до {n}.")


M = get_positive_int("Введите M - число строк: ")
N = get_positive_int("Введите N - число столбцов: ")
matrix = [[get_int(f"[{i+1}][{j+1}]: ") for j in range(N)] for i in range(M)]

print("Исходная матрица:")
print_matrix(matrix)

k1 = get_col_index(f"Введите номер первого столбца K1 (от 1 до {N}): ", N)
k2 = get_col_index(f"Введите номер второго столбца K2 (1 от до{N}): ", N)

SwapCol(matrix, k1, k2)

print(f"Матрица после перестановки столбцов {k1+1} и {k2+1}:")
print_matrix(matrix)
