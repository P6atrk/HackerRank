def key_0(x):
    return x[1]

def key_1(x):
    return x[0]

if __name__ == '__main__':
    list = []
    for _ in range(int(input())):
        list.append([input(), float(input())])
    list.sort(key = key_0)
    min = list[0][1]
    second = list[len(list) - 1][1]
    for i in list:
        if i[1] > min:
            second = i[1]
            break
    seconds = [i for i in list if i[1] > min and i[1] <= second]
    seconds.sort(key = key_1)
    second_names = [i[0] for i in seconds]
    print(*second_names, sep = "\n")