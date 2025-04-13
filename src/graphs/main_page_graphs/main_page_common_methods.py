def add_rink_background(fig, image_uri):
    """
    Adds a rink image as the background of the plot and sets appropriate axis ranges and styling.
    """
    fig.update_layout(
        xaxis=dict(
            range=[0, 100],
            domain=[0, 0.9],
            showgrid=False,
            zeroline=False,
        ),
        yaxis=dict(
            range=[-40, 40],
            showgrid=False,
            zeroline=False,
            scaleanchor="x",
        ),
        images=[
            dict(
                source=image_uri,
                xref="x",
                yref="y",
                x=0,
                y=50,
                sizex=100,
                sizey=100,
                sizing="stretch",
                opacity=0.5,
                layer="below",
            )
        ],
        margin=dict(l=40, r=40, t=20, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )


def update_axes(fig):
    """
    Updates axis labels and hides gridlines for a cleaner plot.
    """
    fig.update_layout(
        xaxis=dict(showgrid=False, title="Coordonnée horizontale (en pieds)"),
        yaxis=dict(showgrid=False, title="Coordonnée verticale (en pieds)"),
    )
