
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr
        

x = [3, 1, 4, 1, 5]
print(insertion_sort(x))
