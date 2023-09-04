import numpy as np
import plotly.graph_objects as go
import csv

path = "C:/Users/wyz96/Downloads/S Parameter Plot 1.csv"


class ReadData:
    def __init__(self) -> None:
        self.freq = np.zeros(401,)
        self.ds = np.zeros(401,)

    def read(self):
        with open(path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            # 设置跳过的行数
            cout = -1
            for data in reader:
                if cout == -1:
                    cout += 1
                    continue
                # 设置读取data的列
                if cout < 401:
                    self.freq[cout] = data[1]
                    self.ds[cout] = data[2]
                    cout += 1
        return self.freq, self.ds


class Prin:
    def __init__(self, freq, ds) -> None:
        # 创建图表对象
        fig = go.Figure()
        # 加入折线图
        fig.add_trace(
            go.Scatter(
                x=freq,
                y=ds,
            )
        )
        fig.update_layout(
            title="S11参数图",
            xaxis=dict(title="频率/GHz"),
            yaxis=dict(title="dB"),
            # 画布大小
            # width=800,
            # height=500,
        )
        fig.show()


if __name__ == "__main__":
    f, s = ReadData().read()
    Prin(f, s)
