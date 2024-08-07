
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


x = [9, 1, 5, 7, 2, 8, 3, 6]
print(bubble_sort(x))