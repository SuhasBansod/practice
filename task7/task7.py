if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    b = list(arr)
    d = list()
    for i in b:
        if i not in d:
            d.append(i)
        else :
            continue
    New= sorted(d, reverse=True)
    print(New[1])