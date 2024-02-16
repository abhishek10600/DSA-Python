def merge(arr, low, mid, high):
    left = arr[low:mid]
    right = arr[mid:high]
    i = 0
    j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    while i < len(left):
        arr[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right):
        arr[k] = right[j]
        j = j + 1
        k = k + 1


def merge_sort(arr, low, high):
    if high - low > 1:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid, high)
        merge(arr, low, mid, high)


arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
merge_sort(arr1, 0, len(arr1))
print(arr1)

# Time Complexity: O(nlog(n))