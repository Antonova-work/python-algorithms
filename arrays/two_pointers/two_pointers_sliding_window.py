numbers = [2, 3, 4, 5, 5, 7, 10]
target = 3

def sliding_window(numbers, target):
    # Считаем сумму самого первого окна
    current_sum = sum(numbers[:target])
    max_sum = current_sum

    # Начинаем "скользить"
    # i — это индекс элемента, который приходит в окно
    for i in range(target, len(numbers)):
        # Прибавляем новенького, вычитаем старенького (который стоял target позиций назад)
        current_sum += numbers[i] - numbers[i - target]

        # Обновляем максимум
        max_sum = max(max_sum, current_sum)

    return max_sum

print(sliding_window(numbers, target))