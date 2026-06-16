s1 = input()
s2=input()
i=0
j=0
while i<len(s1) and j<len(s2):
        if s1[i] == s2[j]:
            i+=1
            j+=1
        elif s1[i] != s2[j]:
            print(s1[i])
            i+=1
            j+=1