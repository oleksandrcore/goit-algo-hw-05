def binary_search(arr, value):
    left = 0
    right = len(arr) - 1
    iterations = 0

    while left <= right:
        iterations += 1
        middle = (left + right) // 2

        if arr[middle] == value:
            return iterations, arr[middle]
        elif arr[middle] < value:
            left = middle + 1
        else:
            right = middle - 1

    return iterations, arr[right] if right >= 0 else arr[0]

arr = [1.7, 2.1, 3, 4.8, 6.0, 7, 8.4]
target = 5.5

iterations, upper_bound = binary_search(arr, target)
print("Iterations:", iterations)
print("Upper Bound:", upper_bound)
