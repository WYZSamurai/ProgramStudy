import plotly.graph_objects as go
import numpy as np

# 生成一些随机数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 使用plotly.express创建折线图
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=x,
        y=y,
    )
)

# 使用legend属性来控制图例的样式，将图例分为两列
fig.update_layout(
    legend=dict(
        orientation="h",  # 设置图例的方向为水平
        x=0.5,  # 设置图例的水平位置为图形的中心
        y=-0.1,  # 设置图例的垂直位置为图形的下方
        xanchor="center",  # 设置图例的水平锚点为中心
        yanchor="top",  # 设置图例的垂直锚点为顶部
        bordercolor='black',
        borderwidth=2,
    ),
    showlegend=True,
)

# 显示图形
fig.show()
