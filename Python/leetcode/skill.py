# 输入n，接下来输入n行,并进行分割
def io1():
    n = int(input())
    s: list[list[str]] = []
    for i in range(0, n):
        s.append(input().strip().split(" "))
    return s


# 一直接受输入直到EOF
def io2():
    while True:
        try:
            s = input()
        except EOFError:
            break
        # print(s)


# 分割字符串
def fun1():
    s = input()
    a = s.strip().split(" ")


# 自定义排序
def fun2():
    a = [
        [1, 2, 3],
        [3, 3, 1],
        [2, 1, 2],
    ]
    a.sort(key=lambda x: x[1], reverse=True)
    # print(a)


if __name__ == "__main__":
    pass
