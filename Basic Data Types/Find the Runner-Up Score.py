if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split())
    print(sorted(set(a))[-2])
