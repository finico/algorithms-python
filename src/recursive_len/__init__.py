def recursive_len(arr):
    if arr:
        return 1 + recursive_len(arr[1:])
    else:
        return 0
