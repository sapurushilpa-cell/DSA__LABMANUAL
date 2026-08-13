def bubble_sort(arr):
    n=len(arr)

    for i in range (n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

n=int(input("enter the number of elements to be sorted:"
            ))

arr=list(map(int,input("enter the elements into the array").split()))

print("sorted array")
bubble_sort(arr)

for i in arr:
    print(i,end="  ") 
