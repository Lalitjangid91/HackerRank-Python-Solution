from itertools import combinations
n=input()
l=input().split()
r=int(input())
l=list(combinations(list(l),r))
c=0
for i in l:
    i=list(i)
    for j in i:
        if j=='a':
            c+=1
            break
print(c/len(l))
