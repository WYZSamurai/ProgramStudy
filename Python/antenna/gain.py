import numpy as np
import plotly.graph_objects as go
import csv

path = "C:/Users/wyz96/Downloads/Gain Plot 2.csv"


class ReadData:
    def __init__(self) -> None:
        self.theta = np.zeros(181,)
        self.phi0_gain = np.zeros(181,)
        self.phi90_gain = np.zeros(181,)

    def read(self):
        with open(path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            # 设置跳过的行数
            cout = -1
            # 按行扫描，data为该次的行数组
            for data in reader:
                if cout == -1:
                    cout += 1
                    # print(data)
                    continue
                # 设置读取data的列
                if cout < 181:
                    self.theta[cout] = data[3]
                    self.phi0_gain[cout] = data[4]
                    cout += 1
                else:
                    self.phi90_gain[cout-181] = data[4]
                    cout += 1
        return self.theta, self.phi0_gain, self.phi90_gain


class Prin:
    def __init__(self, theta, phi0, phi90) -> None:
        # 创建图表对象
        fig = go.Figure()
        # 加入折线图
        fig.add_trace(
            go.Scatterpolar(
                r=phi0,
                theta=theta,
                mode="lines",
                name="phi=0",
                line_color="darkviolet",
                opacity=0.8,
            )
        )
        fig.add_trace(
            go.Scatterpolar(
                r=phi90,
                theta=theta,
                mode="lines",
                name="phi=90",
                line_color="deepskyblue",
                opacity=0.8,
            )
        )
        fig.show()


if __name__ == "__main__":
    theta, phi0, phi90 = ReadData().read()
    Prin(theta, phi0, phi90)
