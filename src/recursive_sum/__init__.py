def recursive_sum(arr):
    return 0 if not arr else arr[0] + recursive_sum(arr[1:])
