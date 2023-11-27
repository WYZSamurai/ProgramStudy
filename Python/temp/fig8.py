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
            name="t=1mm",
            line=dict(
                color='black',
                width=3,
            ),
            marker=dict(
                symbol=0,
                size=10,
            ),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[0],
            y=data[2],
            name="t=2mm",
            line=dict(
                color='red',
                width=3,
            ),
            marker=dict(
                symbol=1,
                size=10,
            ),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[0],
            y=data[3],
            name="t=3mm",
            line=dict(
                color='blue',
                width=3,
            ),
            marker=dict(
                symbol=2,
                size=10,
            ),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[4],
            y=data[5],
            name="t=1mm",
            line=dict(
                color='black',
                width=3,
                dash='5px',
            ),
            marker=dict(
                symbol=0,
                size=10,
            ),
            yaxis='y2',
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[4],
            y=data[6],
            name="t=2mm",
            line=dict(
                color='red',
                width=3,
                dash='5px',
            ),
            marker=dict(
                symbol=1,
                size=10,
            ),
            yaxis='y2',
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data[4],
            y=data[7],
            name="t=3mm",
            line=dict(
                color='blue',
                width=3,
                dash='5px',
            ),
            marker=dict(
                symbol=2,
                size=10,
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
    axistitlefont = dict(
        color='black',
        family='Times New Roman',
        size=80,
    )
    tickfont = dict(
        color='black',
        family='Times New Roman',
        size=70,
    )
    legendfont = dict(
        color='black',
        family='Times New Roman',
        size=70,
    )
    margin = dict(
        l=250,
        r=600,
        t=50,
        b=200,
    )
    fig.update_layout(
        template='none',
        paper_bgcolor='white',
        plot_bgcolor='white',
        autosize=True,
        margin=margin,
        xaxis=dict(
            title="<b>L(mm)</b>",
            titlefont=axistitlefont,
            showline=True,
            linecolor='black',
            linewidth=3,
            showgrid=False,
            autorange=False,
            range=[7, 14],
            type='linear',
            ticks='outside',
            ticklen=10,
            tickwidth=3,
            tickfont=tickfont,
        ),
        xaxis2=dict(
            overlaying='x',
            side='top',
            showline=True,
            showgrid=False,
            linecolor='black',
            linewidth=1,
            ticks='',
            showticklabels=False,
            zeroline=False,
        ),
        yaxis=dict(
            title="<b>S<sub>11</sub>(dB)</b>",
            showgrid=False,
            titlefont=axistitlefont,
            showline=True,
            linecolor='black',
            linewidth=3,
            autorange=False,
            range=[-10, 0],
            type='linear',
            ticks='outside',
            ticklen=10,
            tickwidth=3,
            tickfont=tickfont,
            showticklabels=True,
        ),
        yaxis2=dict(
            overlaying='y',
            side='right',
            title='<b>S<sub>11</sub>phase(deg)</b>',
            titlefont=axistitlefont,
            showgrid=False,
            showline=True,
            zeroline=False,
            linecolor='black',
            linewidth=3,
            autorange=False,
            range=[-800, 50],
            type='linear',
            tickfont=tickfont,
            ticks='outside',
            ticklen=10,
            tickwidth=3,
            showticklabels=True,
        ),
        legend=dict(
            x=1.2,
            y=0,
            font=legendfont,
            bordercolor='black',
            borderwidth=2
        ),
        showlegend=True,
    )
    fig.show()


if __name__ == "__main__":
    path1 = "C:/Users/wyz96/Doc/Term1/2309/论文翻译/袁怀林软硬件验收/1学位论文/学位论文中的数据图表源文件/图6-8(a).csv"
    path2 = "C:/Users/wyz96/Doc/Term1/2309/论文翻译/袁怀林软硬件验收/1学位论文/学位论文中的数据图表源文件/图6-8(b).csv"
    skip = 0
    col = 4
    data1 = read(path1, skip, col)
    data2 = read(path2, skip, col)
    data = np.array(data1+data2)
    prin(data)
