import numpy as np
import plotly.graph_objects as go
import csv

path = "C:/Users/wyz96/Downloads/EBG_S11.csv"


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
                # print(data)
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
    def __init__(self, freq1, ds1) -> None:
        # 创建图表对象
        fig = go.Figure()
        # 加入折线图
        fig.add_trace(
            go.Scatter(
                x=freq1,
                y=ds1,
                name="普通微带天线S参数图",
                line_color="deepskyblue",
            )
        )
        # fig.add_trace(
        #     go.Scatter(
        #         x=freq2,
        #         y=ds2,
        #         name="RIS结构S参数图",
        #         line_color="darkviolet",
        #     )
        # )
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
    f1, s1 = ReadData().read()
    # f2, s2 = ReadData().read(path2)
    Prin(f1, s1)
