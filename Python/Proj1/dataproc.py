import numpy as np
import csv


path = "C:/Users/wyz96/Doc/Term1/24元/net/24_hori/"


class ReadData:
    # 读入单个单元数据
    def __init__(self) -> None:
        self.mag_data = np.zeros(181,)
        self.ang_data = np.zeros(181,)

    # 读入该单元振幅
    def mag(self, i=1):
        with open(path+"mag"+str(i)+".csv", mode="r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            # 设置计数器
            cout = -1
            for data in reader:
                if cout == -1:
                    cout += 1
                    continue
                self.mag_data[cout] = data[1]
                cout += 1
        return self.mag_data

    # 读入该单元角度
    def ang(self, i=1):
        with open(path+"ang_deg"+str(i)+".csv", mode="r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            # 设置计数器
            cout = -1
            for data in reader:
                if cout == -1:
                    cout += 1
                    continue
                self.ang_data[cout] = data[1]
                cout += 1
        return self.ang_data


class MakeMatrix:
    # 创建振幅和角度矩阵
    def __init__(self) -> None:
        self.mag = np.zeros((24, 181))
        self.ang = np.zeros((24, 181))

    def func(self):
        for i in range(1, 25):
            # 读取第i个单元数据
            magd = ReadData().mag(i)
            angd = ReadData().ang(i)
            for j in range(181):
                self.mag[i-1, j] = magd[j]
                self.ang[i-1, j] = angd[j]
        return self.mag, self.ang


class Contouring:
    # 旁瓣抑制波束赋形
    def __init__(self) -> None:
        self.theta_0 = None
        self.sll = None

    def func(self, batch=1):
        # 主瓣指向范围为：70~110度，电平为0db，整数
        self.theta_0 = np.random.randint(70, 111, size=(batch,))
        # 旁瓣电平为-30~-20db
        self.sll = np.random.randint(20, 31, size=(batch, 1))
        wd = self.sll
        # sll的shape为(batch,181)，表示方向图每一度的电平大小
        self.sll = self.sll*-1*np.ones((batch, 181), dtype=np.float64)
        # 赋形
        for i in range(batch):
            self.sll[i,
                     self.theta_0[i]-1-wd[i][0]:self.theta_0[i]+wd[i][0]] = 0
        return self.theta_0, self.sll


if __name__ == "__main__":
    # pass

    a, b = Contouring().func(3)
    print(a.shape, b.shape)
    print(a)
    print(b)
