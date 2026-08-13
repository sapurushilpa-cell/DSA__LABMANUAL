def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)



n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))


sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)
