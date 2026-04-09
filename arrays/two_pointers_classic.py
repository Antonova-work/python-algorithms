numbers = [2, 3, 4, 5, 7, 10]
target = 10


def two_pointers_classic(numbers, target):
    # Расставляем указатели по краям
    left = 0
    right = len(numbers) - 1

    # Двигаемся, пока они не встретились
    while left < right:
        current_val = numbers[left] + numbers[right]

        if current_val == target:
            return [numbers[left], numbers[right]]  # Нашли решение

        if current_val < target:
            left += 1  # Нужно увеличить сумму - двигаем левый край вправо
        else:
            right -= 1  # Нужно уменьшить сумму - двигаем правый край влево

    return [-1, -1]  # Ничего не нашли

print(two_pointers_classic(numbers, target))