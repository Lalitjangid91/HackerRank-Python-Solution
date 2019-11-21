def count_substring(string, sub_string):
    c=0
    while True:
        f=string.find(sub_string)
        if f==-1:
            break
        c=c+1
        string=string[f+1:]
    return c
