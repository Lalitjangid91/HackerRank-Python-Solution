def merge_the_tools(string, k):
    for i in range(len(string)// k):
        t = ''
        for c in string[i * k : (i + 1) * k]:
            if c in t:
                continue
            t += c
        print(t)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
