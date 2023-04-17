import numpy as np
import plotly.graph_objects as go

# 定义电流元参数
I0 = 1  # 电流幅值
l = 0.5  # 电流长度（单位波长）
alpha = 0  # 电流相位
f = 100  # 频率（MHz）
w = 2 * np.pi * f  # 角频率
k = w / 3  # 波数
# 定义观察角度范围和分辨率
theta = np.linspace(0, np.pi, 180)  # 从0到180度，每一度一个点

if __name__ == "__main__":
    # 计算辐射强度
    E = I0 * l * np.cos(alpha) * np.sin(theta) / (2 * np.pi)  # 电场强度
    P = E**2 / (120 * np.pi)  # 辐射功率密度
    U = P * np.sin(theta)  # 辐射强度

    # 绘制辐射方向图
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=U, theta=theta * 180 / np.pi))  # 极坐标图
    fig.update_layout(title="电流元的辐射图")
    fig.show()
