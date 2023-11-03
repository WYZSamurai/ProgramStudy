import numpy as np
import plotly.graph_objects as go


class Prin:
    def __init__(self):
        x = np.linspace(20, 100, 100)
        y1 = 1/(x+1)
        y2 = 1/np.linspace(30, 40, 100)
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=x,
                y=y1,
                name="'Time-Related' Goods",
                line_color="rgb(224,103,66)",
                line_width=3
            )
        )
        fig.add_trace(
            go.Scatter(
                x=x,
                y=y2,
                name="'Time-Unrelated' Goods",
                line_color="rgb(68,149,162)",
                line_width=3
            )
        )
        fig.update_layout(
            title="Second Curve",
            title_font=dict(size=24),
            # 画布背景
            paper_bgcolor='rgba(0,0,0,0)',
            # 图标背景
            plot_bgcolor='rgba(0,0,0,0)',
            # 画布大小
            # width=800,
            # height=500,
            xaxis=dict(
                title="Time",
                showline=True,
                linecolor='black',
                linewidth=3,
                titlefont=dict(size=24,),
                # 设置坐标轴标签的字体及颜色
                # titlefont=dict(
                #     color='rgb(148, 103, 189)',
                #     size=24,
                # ),
                # 设置刻度的字体大小及颜色
                # tickfont=dict(
                #     color='rgb(148, 103, 189)',
                #     size=24,
                # ),
                # 设置是否显示刻度
                showticklabels=False,
            ),
            yaxis=dict(
                title="Valve",
                titlefont=dict(size=24,),
                showline=True,
                linecolor='black',
                linewidth=3,
                showticklabels=False,
            ),
            # 设置图例
            legend=dict(
                font=dict(
                    size=18,
                ),
            ),
        )
        fig.show()


if __name__ == "__main__":
    Prin()
