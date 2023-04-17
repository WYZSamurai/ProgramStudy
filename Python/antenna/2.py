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
phi = np.linspace(0, 2 * np.pi, 360)  # 从0到360度，每一度一个点
THETA, PHI = np.meshgrid(theta, phi)  # 生成网格

if __name__ == "__main__":
    # 计算辐射强度
    E = I0 * l * np.cos(alpha) * np.sin(THETA) / (2 * np.pi)  # 电场强度
    P = E**2 / (120 * np.pi)  # 辐射功率密度
    U = P * np.sin(THETA)  # 辐射强度

    # 将极坐标转换为直角坐标
    X = U * np.sin(THETA) * np.cos(PHI)
    Y = U * np.sin(THETA) * np.sin(PHI)
    Z = U * np.cos(THETA)

    # 绘制三维辐射图
    fig = go.Figure()
    fig.add_trace(go.Surface(x=X, y=Y, z=Z))  # 三维图
    fig.update_layout(title="电流元的辐射图")
    fig.show()
