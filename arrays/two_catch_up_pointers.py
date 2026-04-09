numbers = [2, 3, 4, 5, 5, 7, 10]

def two_catch_up_pointers(numbers):
    # slow — это позиция, куда мы запишем следующее уникальное число
    slow = 0

    # fast — бежит по всему массиву от начала до конца
    for fast in range(1, len(numbers)):
        # Если нашли новое число, которое не равно текущему "правильному"
        if numbers[fast] != numbers[slow]:
            # Продвигаем медленный указатель
            slow += 1
            # Записываем туда новое число
            numbers[slow] = numbers[fast]

    # Возвращаем количество уникальных элементов
    return slow + 1

print(two_catch_up_pointers(numbers))