# def find_lowest_number(arr):
#     minVal = arr[0]
#     for i in arr:
#         if (i < minVal):
#             minVal = i
#     return minVal


# arr = [9,8,7,6,5,4,1,3,2,-5]
# print(find_lowest_number(arr))

def find_lowest_number(arr):
    minVal = arr[0]
    for i in range(0, len(arr)):
        if (arr[i] < minVal):
            minVal = arr[i]
    return minVal


arr = [10, 1, 3, 4, -5,7,8]
print(find_lowest_number(arr))
