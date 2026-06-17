n=5
for i in range(0,n+1):
    for j in range(n-i+1,n+1,1):
        print(j,end="")
    print(0,end="")
    for j in range(n,n-i,-1):
        print(j,end="")
    print()    
    
