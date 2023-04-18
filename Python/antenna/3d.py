import plotly.graph_objects as go
import numpy as np

pi = np.pi
sin = np.sin
cos = np.cos

theta = np.linspace(0, pi, 180)
phi = np.linspace(0, 2 * pi, 360)
theta, phi = np.meshgrid(theta, phi)

if __name__ == "__main__":
    # 电流元
    u3 = sin(theta)
    with np.errstate(divide="ignore", invalid="ignore"):
        # 全波振子
        u1 = np.cos((np.pi / 2) * np.cos(theta)) / np.sin(theta)
        u1[~np.isfinite(u1)] = 0
        # 半波振子
        u2 = (np.cos(np.pi * np.cos(theta)) + 1) / (np.sin(theta) * 2)
        u2[~np.isfinite(u2)] = 0

    # 全波振子
    x1 = u1 * sin(theta) * cos(phi)
    y1 = u1 * sin(theta) * sin(phi)
    z1 = u1 * cos(theta)
    # 半波振子
    x2 = u2 * sin(theta) * cos(phi)
    y2 = u2 * sin(theta) * sin(phi)
    z2 = u2 * cos(theta)
    # 电流元
    x3 = u3 * sin(theta) * cos(phi)
    y3 = u3 * sin(theta) * sin(phi)
    z3 = u3 * cos(theta)

    fig = go.Figure()

    fig.add_trace(
        go.Surface(
            x=x1,
            y=y1,
            z=z1,
            opacity=0.5,
            name="半波振子",
            surfacecolor=x1**2 + y1**2,
            colorscale="Reds",
            text="半波振子",
        )
    )
    # fig.add_trace(
    #     go.Surface(
    #         x=x2,
    #         y=y2,
    #         z=z2,
    #         opacity=0.5,
    #         name="全波振子",
    #         surfacecolor=x1**2 + y1**2,
    #         colorscale="Greens",
    #         text="全波振子",
    #     )
    # )
    # fig.add_trace(
    #     go.Surface(
    #         x=x3,
    #         y=y3,
    #         z=z3,
    #         opacity=0.5,
    #         name="电流元",
    #         text="电流元",
    #         surfacecolor=x1**2 + y1**2,
    #         colorscale="Blues",
    #     )
    # )

    fig.update_layout(
        title="3D",
        title_font_color="black",
        # title_font_family="Courier New",
    )

    fig.show()
