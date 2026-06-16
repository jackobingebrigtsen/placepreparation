n=int(input("Enter the no of elements:"))
nums=[]
for i in range(n):
    t=int(input("Enter the elements:"))
    nums.append(t)
print(nums)
target=int(input("Enter the target value:"))
if nums[n-1]<target:
    print(n)
for i in range(n):
    if nums[i]==target:
        print(i)
    elif nums[i]>target and nums[i-1]<target:
        print(i)  