s1 = input()
s2=input()
i=0
j=0
l1=[]
l2=[]
while i<len(s1) and j<len(s2):
        if s1[i] == s2[j]:
            i+=1
            j+=1
        elif s1[i] != s2[j]:
            l1.append(s1[i])
            l2.append(s2[j])
            i+=1
            j+=1

print(l1)
print(l2)