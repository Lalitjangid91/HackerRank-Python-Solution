if __name__ == '__main__':
    n=int(input())
    d={}
    for i in range(n):
        name,*marks=input().split()
        d[name]=list(map(float,marks))
    name=input()
    t=sum(d[name])/3
    print("%.2f"%t)
