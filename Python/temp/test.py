import numpy as np
import plotly.graph_objects as go


def prin():
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=[1, 2, 3, 4],
            y=[2, 4, 6, 8],
            name="h=4mm",
            line=dict(
                color='black',
                width=3,
            ),
            mode='lines+markers',
            marker=dict(
                symbol='square',
            )
        )
    )
    fig.update_layout(
        template='none',
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
            autorange=True,
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
            ticks='outside',
            ticklen=10,
            tickwidth=3,
            showticklabels=True,
            autorange=True,
        ),
        legend=dict(
            x=1.1,
            y=0,
            font=dict(
                family='Times New Roman',
                size=18,
                color="black",
            ),
            bordercolor='black',
            borderwidth=2
        ),
        # 设置不显示图例
        showlegend=True,
    )
    fig.show()


if __name__ == "__main__":
    prin()
