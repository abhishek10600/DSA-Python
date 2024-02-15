def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        element = arr[i]
        while j > -1 and arr[j] > element:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = element


arr1 = [10, 6, 3, 8, 2, 1]
insertion_sort(arr1)
print(arr1)
