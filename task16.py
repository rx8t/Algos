def filter_numbers(numbers, condition=None):
    if condition is None:
        return numbers
    return [x for x in numbers if condition(x)]


def transform_numbers(numbers, transform_function=None):
    if transform_function is None:
        return numbers
    return [transform_function(x) for x in numbers]


def cube_numbers(*lists):
    return [x**3 for lst in lists for x in lst]


def product_non_zero(*args):
    result = 1
    for x in args:
        if x != 0:
            result *= x
    return result


def get_num_list(prompt):
    while True:
        raw = input(prompt).strip().split()
        try:
            return [float(x.replace(",", ".")) for x in raw]
        except ValueError:
            print("Ошибка: вводите вещественные числа через пробел.")


print("а) filter_numbers")
nums = get_num_list("Введите список чисел: ")
print("Без фильтра:       ", filter_numbers(nums))
print("Только чётные int: ", filter_numbers(nums, condition=lambda x: x % 2 == 0))
print("Только > 0:        ", filter_numbers(nums, condition=lambda x: x > 0))

print("б) transform_numbers")
nums2 = get_num_list("Введите список чисел: ")
print("Без преобразования:", transform_numbers(nums2))
print("Кубы: ", transform_numbers(nums2, transform_function=lambda x: x**3))
print("Квадраты: ", transform_numbers(nums2, transform_function=lambda x: x**2))

print("в) cube_numbers")
lst1 = get_num_list("Введите первый список чисел: ")
lst2 = get_num_list("Введите второй список чисел: ")
print("Кубы всех чисел:", cube_numbers(lst1, lst2))

print("г) product_non_zero")
nums3 = get_num_list("Введите числа: ")
print("Произведение ненулевых:", product_non_zero(*nums3))
