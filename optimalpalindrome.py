def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
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