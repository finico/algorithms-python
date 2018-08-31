def find_smallest(arr, x):
    for i in range(x + 1, len(arr)):
        if arr[i] < arr[x]:
            x = i
    return x


def selection_sort(src_arr):
    arr = src_arr.copy()
    for i in range(len(arr) - 1):
        least = find_smallest(arr, i)
        arr[i], arr[least] = arr[least], arr[i]
    return arr
