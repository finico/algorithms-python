def recursive_max(arr):
    if not arr:
        raise AssertionError("List can not be empty")

    head = arr[0]
    if len(arr) == 1:
        return head
    guess_max = recursive_max(arr[1:])
    return head if head > guess_max else guess_max
