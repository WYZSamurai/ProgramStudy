import plotly.graph_objects as go
import numpy as np

if __name__ == "__main__":
    r = 1
    theta = np.linspace(0, np.pi, 100)
    phi = np.linspace(0, 2 * np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    data = go.Surface(x=x, y=y, z=z)
    fig = go.Figure(data=data)

    fig.show()
