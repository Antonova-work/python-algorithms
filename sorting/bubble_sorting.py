numbers = [45, 35, 25, 55, 15, 65, 95, 85, 105, 75]

n = len(numbers)

# по числу пар
for i in range(n - 1):
    swapped = False # чтобы вовремя остановить цикл
    # чтобы не трогать уже отсортированный "хвост"
    for j in range(n - i - 1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            swapped = True # продолжаем если была перестановка
    # останавливаем цикл если swapped = False (перестановок не было)
    if not swapped:
        break

print(numbers)