def selection_sort(arr):
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if (minIndex != i):
            arr[i], arr[minIndex] = arr[minIndex], arr[i]


arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
arr2 = [6, 3, 8, 2, 5, 9]
selection_sort(arr2)
print(arr2)
