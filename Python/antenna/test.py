import plotly.graph_objs as go
import plotly.express as px
import numpy as np

if __name__ == "__main__":
    theta = np.linspace(0, 2 * np.pi, 360)
    r = np.sin(theta)

    fig = go.Figure()
    trace = go.Scatterpolar(r=r, theta=theta * 180 / np.pi)
    fig.add_trace

    fig.show()
