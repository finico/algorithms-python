def recursive_max(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0]
    x = recursive_max(arr[1:])
    return arr[0] if arr[0] > x else x
