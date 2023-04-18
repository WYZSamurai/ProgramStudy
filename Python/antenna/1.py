import numpy as np
import plotly.graph_objects as go

if __name__ == "__main__":
    theta = np.linspace(0, 2 * np.pi, 360)
    r = np.sin(theta)  # 辐射强度

    # 绘制辐射方向图
    fig = go.Figure()
    # fig.add_trace(go.Scatterpolar(r=r, theta=theta * 180 / np.pi))  # 极坐标图
    # fig.update_layout(title="电流元的辐射图")
    fig.show()
