def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == x:
            return mid

        if guess > x:
            high = mid - 1
        else:
            low = mid + 1

    return None
