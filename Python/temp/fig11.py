import numpy as np
import plotly.graph_objects as go
import csv


def read(path="", skip=1, col=2):
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


def prin(data: np.array):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data[0],
            y=data[1],
            name="Amplitude Change Curve",
            line=dict(
                color='blue',
                width=3,
                # 设置虚线
                # dash='5px',
            ),
            # 次坐标轴
            # yaxis='y2',
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[2],
            y=data[3],
            name="Phase Change Curve",
            line=dict(
                color='red',
                width=3,
                dash='5px',
            ),
            yaxis='y2'
        )
    )
    # 添加顶部黑线
    fig.add_trace(
        go.Scatter(
            x=[],
            y=[],
            xaxis='x2',
        )
    )
    fig.update_layout(
        # title="Second Curve",
        # title_font=dict(
        #     size=24,
        #     family="Times New Roman"
        # ),
        # 画布背景
        paper_bgcolor='rgba(0,0,0,0)',
        # 图标背景
        plot_bgcolor='rgba(0,0,0,0)',
        # 画布大小
        width=1200,
        height=800,

        xaxis=dict(
            # 坐标轴显示
            showline=True,
            linecolor='black',
            linewidth=3,
            # 设置坐标轴的标签
            title="L(mm)",
            # 设置坐标轴标签的字体及颜色
            titlefont=dict(
                # color='black',
                size=24,
                family='Times New Roman',
            ),
            # 设置刻度的字体大小及颜色
            # tickfont=dict(
            #     color='rgb(148, 103, 189)',
            #     size=24,
            # ),
            # 设置是否显示刻度
            # showticklabels=False,
            # 设置刻度旋转的角度
            # tickangle=270,
            # 设置刻度的范围及刻度
            autorange=False,
            range=[7, 14],
            type='linear',
        ),
        xaxis2=dict(
            # 设置第二坐标轴的在的方向，如果第二坐标轴是纵向，设置为'y'
            overlaying='x',
            # 设置第二坐标轴的位置，或者是'bottom',如果第二坐标轴是纵向，设置为'right'或者'left'
            side='top',
            showline=True,
            linecolor='black',
            linewidth=1,
            showticklabels=False,
        ),

        yaxis=dict(
            title="S11(dB)",
            titlefont=dict(
                size=24,
                family='Times New Roman',
            ),
            showline=True,
            linecolor='black',
            linewidth=3,
            showticklabels=True,
            autorange=False,
            range=[-10, 0],
            type='linear',
        ),
        yaxis2=dict(
            overlaying='y',
            side='right',
            title='S11phase(deg)',
            titlefont=dict(
                family='Times New Roman',
                color='black',
                size=24
            ),
            showline=True,
            linecolor='black',
            linewidth=3,
            showticklabels=True,
            autorange=False,
            range=[-800, 0],
            type='linear',
        ),

        # 设置图例
        legend=dict(
            x=0.7,
            y=0.6,
            font=dict(
                family='Times New Roman',
                size=18,
                color="black",
            ),
            # bgcolor='#E2E2E2',
            bordercolor='black',
            borderwidth=2
        ),
        # 设置不显示图例
        showlegend=True,
    )
    fig.show()


if __name__ == "__main__":

    # 设置文件路径
    path1 = "C:/Users/wyz96/Downloads/图6-5(a).csv"
    path2 = "C:/Users/wyz96/Downloads/图6-11(d).csv"
    # 设置跳过的行数
    skip = 1
    # 设置读取的列数
    col = 2

    data = []
    data1 = read(path1, 1, 2)
    data2 = read(path2, 1, 2)
    data = np.array(data1+data2)

    prin(data)
