n = int(input("Enter number of intervals: "))
l=[]
for i in range(n):
    start=int(input("start:"))
    end=int(input("end:"))
    l.append([start,end])
print("Original:", l)

# 1. ALWAYS sort by start time first to make overlapping intervals adjacent
l.sort()

r=[]
for i in range(n):
    # 2. If r is empty or current interval doesn't overlap with the last one in r
    if not r or r[-1][1] < l[i][0]:
        r.append(l[i])
    else:
        # 3. Overlap found: Update the end time of the last interval in r
        r[-1][1] = max(r[-1][1], l[i][1])

print("Merged:", r)
