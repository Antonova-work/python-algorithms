numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def kadanes_algorithm(numbers):
    current_max = numbers[0] # текущее максимальное подмассивов, заканчивающихся на текущей позиции
    global_max = numbers[0] # самая большая сумма из всех подмассивов

    # начинаем проверять со второго элемента в массиве
    for num in numbers[1:]:
        current_max = max(num, num+current_max) # выбираем - выгоднее начать новый подмассив или добавить в текущий

        if current_max > global_max:
            global_max = current_max

    return global_max

print(kadanes_algorithm(numbers))