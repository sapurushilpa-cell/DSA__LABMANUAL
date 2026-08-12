def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
        else:
            i=i+1
    return 0
arr=list(map(int,input("eneter a array").split()))
key=int(input("Enter the element to be searched:"))
print(linear_search(arr,key))
