def partition(arr, low, high):
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quicksort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low<high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)


arr = [10, 3, 7, 5, 7, 2, 9, 4, 18, 23, 8]
n = len(arr)
quicksort(arr, 0, n-1)
print("sorted array is")
for i in range(n):
    print("%d" % arr[i])

