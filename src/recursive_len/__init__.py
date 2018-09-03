def recursive_len(arr):
    return 1 + recursive_len(arr[1:]) if arr else 0
