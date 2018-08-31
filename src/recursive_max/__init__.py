def recursive_max(arr):
    if not arr:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        x = recursive_max(arr[1:])
        return arr[0] > x and arr[0] or x
