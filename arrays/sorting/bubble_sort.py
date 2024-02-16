def bubble_sort(arr):
    for i in range(len(arr) - 1):
        # optimization
        flag = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # optimization
                flag = 1
        # optimization
        if flag == 0:
            break


arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bubble_sort(arr2)
print(arr2)


# time complexity: O(n*n)
