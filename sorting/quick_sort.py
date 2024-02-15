def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)
        quick_sort(arr, low, p_index - 1)
        quick_sort(arr, p_index + 1, high)


arr1 = [10, 9, 8, 5, 4, 3, 2, 1]
quick_sort(arr1, 0, len(arr1) - 1)
print(arr1)


# Time complexity = O(nlog(n))
