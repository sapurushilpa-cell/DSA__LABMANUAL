def launch(n):
    print(n)
    if n>1:
        n-=1
        return launch(n)
    print("LAUNCH")
result=launch(10)   
