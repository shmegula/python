
def selection_sort(n):
    for i in range(len(n)):
        min_index = i
        for j in range(i + 1, len(n)):
            if n[j] < n[min_index]:
                min_index = j
        n[i], n[min_index] = n[min_index], n[i]
    return n


num_list = [9, 4, 7, 21, 56, 32, 43, 22, 12, 11, 10, 19]
print(selection_sort(num_list))

                
