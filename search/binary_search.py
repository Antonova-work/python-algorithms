numbers = [1, 25, 50, 75, 100, 125, 150, 175]
target = 25

def binary_search(target, numbers):
    left = 0 # первый элемент
    right = len(numbers) - 1 # последний элемент

    while left <= right:
        mid = (left+right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            right = mid - 1 # сдвигаем правую границу влево (от того числа на котором стоим на 1)
        else:
            left = mid + 1 # сдвигаем левую границу вправо (от того числа на котором стоим на 1)
    return -1 # если нет в списке

result = binary_search(target, numbers)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")