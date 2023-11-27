import numpy as np
import plotly.graph_objects as go


def prin(data: np.array):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data[0],
            y=data[1],
            # 下标
            name="x<sub>2</sub>",
            line=dict(
                color='blue',
                width=3,
                # 设置虚线
                # dash='5px',
            ),
            # 设置节点形状
            marker=dict(
                symbol='square',
            ),
            # 次坐标轴
            # yaxis='y2',
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
    # 设置画布字体、坐标轴字体、刻度字体、图例字体
    titlefont = dict(
        size=24,
        family="Times New Roman"
    )
    axistitlefont = dict(
        color='red',
        size=24,
        family='Times New Roman',
    )
    tickfont = dict(
        color='rgb(148, 103, 189)',
        size=20,
        family='Times New Roman',
    )
    legendfont = dict(
        family='Times New Roman',
        size=18,
        color="black",
    )
    margin = dict(
        l=150,
        r=100,
        t=100,
        b=100,
    )
    fig.update_layout(
        # 画布标题
        title="Second Curve",
        title_font=titlefont,
        # 画布背景
        paper_bgcolor='white',
        # 图标背景
        plot_bgcolor='white',
        # 画布大小
        autosize=True,
        margin=margin,
        # width=1200,
        # height=800,
        template='simple_white',
        xaxis=dict(
            # 坐标轴显示
            showline=True,
            linecolor='black',
            linewidth=3,
            # 设置坐标轴的标签
            title="$L_2$(mm)",
            # 设置坐标轴标签的字体及颜色
            titlefont=axistitlefont,
            # 设置是否显示网格线
            showgrid=True,
            # 设置是否显示零线
            zeroline=True,
            # 刻度
            # ticks='outside',
            # ticklen=10,
            # tickwidth=3,
            # 设置刻度的字体大小及颜色
            tickfont=tickfont,
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
        # 设置图例
        legend=dict(
            x=0.7,
            y=0.6,
            font=legendfont,
            # bgcolor='#E2E2E2',
            bordercolor='black',
            borderwidth=2
        ),
        # 设置不显示图例
        showlegend=True,
    )
    fig.show()
