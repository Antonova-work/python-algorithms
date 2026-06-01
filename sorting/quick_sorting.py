numbers = [5, 4, 3, 2, 1]

def quicksort(arr, low=0, high=None):
    # назначаем индекс крайнему элементу справа
    if high is None:
        high = len(arr)-1

    if low < high:
        # забираем индекс правильного места опорного элемента
        pivot_index = partition(arr, low, high)
        # рекурсивно сортируем левую и правую часть от опорного элемента, который на своём месте
        quicksort(arr, low, pivot_index-1)
        quicksort(arr, pivot_index+1, high)

    return arr


def partition(arr, low, high):
    # назначаем опорный элемент последним
    pivot = arr[high]
    # берём начальный индекс для элементов меньше опорного -1
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            # расширяем "массив" элементов меньше опорного
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

print(quicksort(numbers))