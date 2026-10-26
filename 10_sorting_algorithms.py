def bubble_sort(arr: list) -> list:
    """Реализация пузырьковой сортировки."""
    n = len(arr)
    # Создаем копию, чтобы не менять исходный список
    sorted_arr = arr.copy() 
    for i in range(n - 1):
        for j in range(n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr


def selection_sort(arr: list) -> list:
    """Реализация сортировки выбором (через поиск минимума)."""
    sort_a = []
    # Копируем массив, так как pop() изменяет его
    temp_arr = arr.copy() 
    while temp_arr:
        min_index = temp_arr.index(min(temp_arr))
        sort_a.append(temp_arr.pop(min_index))
    return sort_a


if __name__ == '__main__':
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", test_array)
    print("Пузырьковая сортировка:", bubble_sort(test_array))
    print("Сортировка выбором:", selection_sort(test_array))