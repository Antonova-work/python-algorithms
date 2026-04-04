numbers = [30, 50, 20, 99, 53, 11, 81, 54]
target = 50

def linear_search(target, numbers):
    # индекс, число (элемент списка)
    for i, num in enumerate(numbers):
        if target == num:
            return i
    return -1 # если нет в списке

result = linear_search(target, numbers)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
