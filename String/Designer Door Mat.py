N, M = map(int,input().split()) 
for i in range(1,N//2+1): 
    print (('.|.'*(2*i-1)).center(M,'-'))
print ('WELCOME'.center(M,'-'))
for i in reversed(range(1,N//2+1)):
    print (('.|.'*(2*i-1)).center(M,'-'))
