if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max = max(arr)
    second = -101
    for i in arr:
        if i > second and i < max:
            second = i
    print(second)