import itertools
s,a=input().split()
s=''.join(sorted(s))
l=list(itertools.combinations_with_replacement(s,int(a)))
for i in l:
    print(''.join(i))
