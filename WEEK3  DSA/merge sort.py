def merge_sort(arr):
    if len(arr)<=1:
        return arr

    
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i=j=k=0

    while i<len(left) and j<len(right):

        if left[i]<=right[j]:
            arr[k]=left[i]

            i+=1

        else:
            arr[k]=right[j]

            j+=1

        k+=1

    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1

        
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

n=int(input("enter the number of elements to sort"))

arr=list(map(int,input("enter the elements").split()))


merge_sort(arr)

print("sorted array")

for elements in arr:
    print(elements,end=" ")

    
