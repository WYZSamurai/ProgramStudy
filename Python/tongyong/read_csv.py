import numpy as np
import csv

path = "C:/Users/wyz96/Doc/Term1/24元/net/24_hori/"


class ReadData:
    def __init__(self) -> None:
        self.data = np.zeros(181,)

    def read(self, path):
        with open(path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            # 设置跳过的行数
            cout = -1
            for data in reader:
                if cout == -1:
                    cout += 1
                    continue
                # 设置读取data的列
                self.data[cout] = data[1]
                cout += 1
        return self.data
