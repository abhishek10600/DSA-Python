def binary_search(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 4
print(binary_search(arr1, 0, len(arr1) - 1, key))
