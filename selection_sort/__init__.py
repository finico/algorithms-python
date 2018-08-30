def find_smallest(arr):
    smallest_index = 0
    smallest = arr[smallest_index]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]

    return smallest_index


def selection_sort(arr):
    res = []

    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        res.append(arr.pop(smallest))

    return res
