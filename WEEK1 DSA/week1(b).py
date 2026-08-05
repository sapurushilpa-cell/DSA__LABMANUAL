def empid_Search(arr,target,n=0):
    if n==len(arr):
        return -1
    if arr[n]==target:
        return n
    return empid_Search(arr,target,n+1)
arr=[10,20,30,50,67,89,56]
result=empid_Search(arr,30)
if result!=-1:
    print("Element found at index:",result)
else:
    print("Element not found")
