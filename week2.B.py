def binary_search(arr,key,low,high):
    mid=(low+high)//2

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_search(arr,key,mid + 1,high)
        else:
            return binary_search(arr,key,low,mid-1)
           
    return -1

arr=list(map(int,input("enter numbers to add in array").split()))
key = int(input("Enter number to search for: "))

if arr!=sorted(arr):
    arr.sort()
    print(binary_search(arr,key,0,len(arr)))

else:
    print(binary_search(arr,key,0,len(arr)))


