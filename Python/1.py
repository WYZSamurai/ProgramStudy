import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(
    go.Barpolar(
        r=[77.5, 72.5, 70.0, 45.0, 22.5], name="A", marker_color="rgb(106,81,163)"
    )
)
fig.add_trace(
    go.Barpolar(
        r=[57.5, 50.0, 45.0, 35.0, 20.0], name="B", marker_color="rgb(158,154,200)"
    )
)
fig.add_trace(
    go.Barpolar(
        r=[40.0, 30.0, 30.0, 35.0, 7.5], name="C", marker_color="rgb(203,201,226)"
    )
)
fig.update_traces(text=["A", "B", "C", "D", "E"])
fig.update_layout(
    title="A Test",
    # font_size=16,
    legend_font_size=16,
    # polar_radialaxis_ticksuffix='%',
    polar_angularaxis_rotation=90,
)
fig.show()
