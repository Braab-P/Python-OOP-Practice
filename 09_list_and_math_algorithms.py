# 13_list_and_math_algorithms.py

def get_next_prime(num: int) -> int:
    """Возвращает следующее простое число после num. Оптимизировано через корень."""
    candidate = num + 1
    while True:
        if candidate < 2:
            candidate += 1
            continue
        
        is_prime = True
        for i in range(2, int(candidate ** 0.5) + 1):
            if candidate % i == 0:
                is_prime = False
                break
                
        if is_prime:
            return candidate
        candidate += 1


def merge_two(a: list, b: list) -> list:
    """Слияние двух отсортированных списков (алгоритм двух указателей)."""
    i, j = 0, 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def quick_merge(lists: list) -> list:
    """Слияние нескольких отсортированных списков."""
    if not lists:
        return []
    result = lists[0]
    for lst in lists[1:]:
        result = merge_two(result, lst)
    return result


def get_unique(numbers: list) -> list:
    """Возвращает список уникальных элементов с сохранением порядка."""
    unique_list = []
    for item in numbers:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


if __name__ == '__main__':
    # Примеры использования
    print("Следующее простое после 13:", get_next_prime(13))
    
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    list3 = [0, 7, 8]
    print("Слияние трех списков:", quick_merge([list1, list2, list3]))
    
    print("Уникальные элементы:", get_unique([1, 2, 2, 3, 1, 4, 5, 4]))