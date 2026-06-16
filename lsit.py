l=[]
n=int(input("Enter the total number:"))
for i in range(n):
    t=int(input("enter teh elements:"))
    l.append(t)
print(l)    
x=int(input("Enter the number to insert:"))
if l[0] > x:
    print(f"NULL,{l[0]}")
elif l[n-1] < x:
    print(f"{l[n-1]},NULL")
for i in range(n):
    if l[i] > x and l[i-1] < x:
        print(f"{l[i-1]},{l[i]}")
    elif l[i]==x:
        print(f"{x} is already present")