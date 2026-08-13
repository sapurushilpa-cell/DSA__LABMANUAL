def insertion_sort(arr):
    n=len(arr)

    for i in range(1,n):
        key=arr[i]

        j=i-1

        while j>=0 and arr[j]>key:

            arr[j+1]=arr[j]

            j=j-1

        arr[j+1]=key

    return arr

arr=list(map(int,input("enter numbers to add in an array:").split()))

print(insertion_sort(arr))
