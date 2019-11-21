def swap_case(s):
    s=list(s)
    for i in range(len(s)):
        if ord(s[i])>=65 and ord(s[i])<=90:
            s[i]=ord(s[i])+32
        elif ord(s[i])>=97 and ord(s[i])<=122:
            s[i]=ord(s[i])-32
        else:
            s[i]=ord(s[i])
    l=[]
    for i in range(len(s)):
        l.append(chr(s[i]))
    s=''.join(l)
    return s
