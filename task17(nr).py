def is_binary(s):
    stripped = s.lstrip("-")
    return len(stripped) > 0 and all(c in "01" for c in stripped)


def get_binary(prompt):
    while True:
        raw = input(prompt).strip()
        if is_binary(raw):
            return raw
        print("Ошибка: введите число в двоичной системе.")


def binary_add_unsigned(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = []
    carry = 0
    for i in range(max_len - 1, -1, -1):
        s = int(a[i]) + int(b[i]) + carry
        result.append(str(s % 2))
        carry = s // 2
    if carry:
        result.append("1")
    return "".join(reversed(result))


def binary_subtract(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = []
    borrow = 0
    for i in range(max_len - 1, -1, -1):
        diff = int(a[i]) - int(b[i]) - borrow
        if diff < 0:
            diff += 2
            borrow = 1
        else:
            borrow = 0
        result.append(str(diff))
    return "".join(reversed(result)).lstrip("0") or "0"


def compare_unsigned(a, b):
    a = a.lstrip("0") or "0"
    b = b.lstrip("0") or "0"
    if len(a) != len(b):
        return 1 if len(a) > len(b) else -1
    if a > b:
        return 1
    elif a < b:
        return -1
    return 0


def binary_add(a_str, b_str):
    a_neg = a_str.startswith("-")
    b_neg = b_str.startswith("-")
    a_mag = a_str.lstrip("-").lstrip("0") or "0"
    b_mag = b_str.lstrip("-").lstrip("0") or "0"

    if a_neg == b_neg:
        res = binary_add_unsigned(a_mag, b_mag)
        return ("-" + res) if a_neg and res != "0" else res
    else:
        cmp = compare_unsigned(a_mag, b_mag)
        if cmp == 0:
            return "0"
        elif cmp > 0:
            res = binary_subtract(a_mag, b_mag)
            return ("-" + res) if a_neg else res
        else:
            res = binary_subtract(b_mag, a_mag)
            return ("-" + res) if b_neg else res


pos = get_binary("Введите положительное двоичное число: ")
while pos.startswith("-"):
    print("Ошибка: число должно быть положительным.")
    pos = get_binary("Введите положительное двоичное число: ")

neg = get_binary("Введите отрицательное двоичное число: ")
while not neg.startswith("-"):
    print("Ошибка: число должно быть отрицательным.")
    neg = get_binary("Введите отрицательное двоичное число: ")

result = binary_add(pos, neg)

pos_dec = int(pos, 2)
neg_dec = -int(neg.lstrip("-"), 2)
res_dec = pos_dec + neg_dec

print(f"{pos} + ({neg}) = {result}")
print(f"Проверка (в десятичной): {pos_dec} + ({neg_dec}) = {res_dec}")
