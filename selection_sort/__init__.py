def selection_sort(arr):
    res = arr.copy()

    for i in range(len(res) - 1):
        least = i

        for j in range(least + 1, len(res)):
            if res[j] < res[least]:
                least = j

        temp = res[i]
        res[i] = res[least]
        res[least] = temp

    return res
