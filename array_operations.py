def find_max_min(arr):
    """Находит максимальное и минимальное значение в массиве."""
    if not arr:
        raise ValueError("Массив пуст")
    return max(arr), min(arr)

def remove_duplicates(arr):
    """Удаляет дубликаты из массива, сохраняя порядок элементов."""
    seen = set()
    return [x for x in arr if not (x in seen or seen.add(x))]

def bubble_sort(arr):
    """Сортирует массив методом пузырька."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr