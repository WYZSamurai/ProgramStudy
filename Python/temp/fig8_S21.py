import numpy as np
import plotly.graph_objects as go
import csv


def read(path="", skip=1, col=2):
    data = []
    for i in range(col):
        with open(path, mode="r", encoding="utf-8") as csvfile:
            temp = []
            cout = -skip
            reader = csv.reader(csvfile)
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
            name="h=4mm",
            line=dict(
                color='black',
                width=3,
            ),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[0],
            y=data[2],
            name="h=5mm",
            line=dict(
                color='red',
                width=3,
            ),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[0],
            y=data[3],
            name="h=6mm",
            line=dict(
                color='blue',
                width=3,
            ),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[0],
            y=data[4],
            name="h=7mm",
            line=dict(
                color='green',
                width=3,
            ),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[0],
            y=data[5],
            name="h=8mm",
            line=dict(
                color='purple',
                width=3,
            ),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[6],
            y=data[7],
            name="h=4mm",
            line=dict(
                color='black',
                width=3,
                dash='5px',
            ),
            yaxis='y2',
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[6],
            y=data[8],
            name="h=5mm",
            line=dict(
                color='red',
                width=3,
                dash='5px',
            ),
            yaxis='y2',
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[6],
            y=data[9],
            name="h=6mm",
            line=dict(
                color='blue',
                width=3,
                dash='5px',
            ),
            yaxis='y2',
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[6],
            y=data[10],
            name="h=7mm",
            line=dict(
                color='green',
                width=3,
                dash='5px',
            ),
            yaxis='y2',
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[6],
            y=data[11],
            name="h=8mm",
            line=dict(
                color='purple',
                width=3,
                dash='5px',
            ),
            yaxis='y2',
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[],
            y=[],
            xaxis='x2',
        )
    )
    fig.update_layout(
        template='simple_white',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        width=1200,
        height=800,
        xaxis=dict(
            showline=True,
            linecolor='black',
            linewidth=3,
            title="L(mm)",
            titlefont=dict(
                size=24,
                family='Times New Roman',
            ),
            autorange=False,
            range=[7, 14],
            type='linear',
        ),
        xaxis2=dict(
            overlaying='x',
            side='top',
            showline=True,
            linecolor='black',
            linewidth=1,
            showticklabels=False,
        ),
        yaxis=dict(
            title="S21(dB)",
            titlefont=dict(
                size=24,
                family='Times New Roman',
            ),
            showline=True,
            linecolor='black',
            linewidth=3,
            showticklabels=True,
            autorange=False,
            range=[-40, 0],
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
            tickfont=dict(
                family='Times New Roman',
                # size=24,
            ),
            showline=True,
            linecolor='black',
            linewidth=3,
            showticklabels=True,
            autorange=False,
            range=[-400, 200],
            type='linear',
        ),

        # 设置图例
        legend=dict(
            x=1.1,
            y=0,
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
    path2 = "C:/Users/wyz96/Downloads/图6-5(b).csv"
    # 设置跳过的行数
    skip = 0
    # 设置读取的列数
    col = 6

    data1 = read(path1, skip, col)
    data2 = read(path2, skip, col)
    data = np.array(data1+data2)

    prin(data)
