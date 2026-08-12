def binary_search(arr,key,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==key:
        return mid
    elif arr[mid]>key:
        return binary_search(arr,key,low,mid-1)
    else:
        return binary_search(arr,key,mid+1,high)
    return 0
arr=list(map(int,input("enter the array").split()))
key=int(input("Enter the element to be searched:"))
print(binary_search(arr,key,0,len(arr)))

