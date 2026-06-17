def palindrome(s):
    i=0
    j=len(s) - 1
    while i<j:
        if s[i]!=s[j]:
            return False
        i=i+1
        j=j-1
    return True
l=[]
s=input("Enter the string:")
for i in range(0,len(s),1):
    for j in range(i,len(s)):
        l.append(s[i:j])
print(l)        
r=set()
for sub in l:
    if len(sub)>2 and palindrome(sub):
        r.add(sub)
print(r)