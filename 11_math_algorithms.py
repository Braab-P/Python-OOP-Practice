def find_max_divisor_sum(start: int, end: int) -> tuple:
    """
    Находит число в диапазоне [start, end] с максимальной суммой делителей.
    Возвращает кортеж (число, сумма).
    """
    max_sum = 0
    max_x = 0

    for i in range(start, end + 1):
        total = 0
        for j in range(1, i + 1):
            if i % j == 0:
                total += j
        if total >= max_sum:
            max_sum = total
            max_x = i
            
    return max_x, max_sum


if __name__ == '__main__':
    a, b = 10, 20
    number, sum_of_divs = find_max_divisor_sum(a, b)
    print(f"В диапазоне от {a} до {b} число с максимальной суммой делителей:")
    print(f"Число {number} (сумма делителей: {sum_of_divs})")