import numpy as np
import plotly.graph_objects as go

if __name__ == "__main__":
    theta = np.linspace(0, 2 * np.pi, 100)  # 天顶角
    u3 = np.abs(np.sin(theta))
    with np.errstate(divide="ignore", invalid="ignore"):
        u1 = abs((np.cos(np.pi * np.cos(theta)) + 1) / (np.sin(theta) * 2))
        u1[~np.isfinite(u1)] = 0
        u2 = abs(np.cos((np.pi / 2) * np.cos(theta)) / np.sin(theta))
        u2[~np.isfinite(u2)] = 0

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=u1,
            theta=theta * 180 / np.pi,
            mode="lines",
            name="全波振子",
            line_color="darkviolet",
            opacity=0.8,
        )
    )
    fig.add_trace(
        go.Scatterpolar(
            r=u2,
            theta=theta * 180 / np.pi,
            mode="lines",
            name="半波振子",
            line_color="deepskyblue",
            opacity=0.8,
        )
    )
    fig.add_trace(
        go.Scatterpolar(
            r=u3,
            theta=theta * 180 / np.pi,
            mode="lines",
            name="电流元",
            line_color="peru",
            opacity=0.8,
        )
    )
    fig.update_layout(
        title="全波振子、半波振子、电流元E面图",
        showlegend=False,
        polar=dict(),
    )
    fig.show()
