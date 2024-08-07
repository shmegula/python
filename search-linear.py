def linear_search(target, arr):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"{target} found at index {i}."
        else:
            pass
    return f"{target} not found."


x = ["1", "a", "2", "b", "3", "c"]
print(linear_search("b", x))