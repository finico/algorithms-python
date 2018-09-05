def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less, greater = [], []
    for i in range(1, len(arr)):
        x = arr[i]
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)
