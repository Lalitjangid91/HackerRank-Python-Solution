import itertools
s,a=input().split()
s=''.join(sorted(s))
for j in range(1,int(a)+1):
    l=list(itertools.combinations(s,j))
    for i in l:
        print(''.join(i))
