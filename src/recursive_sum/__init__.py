def recursive_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursive_sum(arr[1:])
