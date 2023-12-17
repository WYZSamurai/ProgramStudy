import csv


def read(path="", skip=1, col=2):
    # 设置文件路径
    # 设置跳过的行数
    # 设置读取的列数
    data = []
    # 按行扫描，每列都循环一次，共col次
    for i in range(col):
        with open(path, mode="r", encoding="utf-8") as csvfile:
            temp = []
            cout = -skip
            # 设置扫描器
            reader = csv.reader(csvfile)
            # d为逐行扫描的数据
            for d in reader:
                if cout < 0:
                    cout += 1
                    continue
                temp.append(float(d[i]))
            data.append(temp)
    return data
