def power(p,n):
    if n==0:
        return 1
    else:
        return p*power(p,n-1)
p=int (input ("Enter the value of p:"))
n=int(input("Enter the value of n:"))
result=power(p,n)
print(result)
