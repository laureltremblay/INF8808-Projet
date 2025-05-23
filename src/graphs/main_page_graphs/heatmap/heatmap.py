import plotly.graph_objs as go

from assets.image_rink_loading import image_uri
from graphs.main_page_graphs.heatmap.heatmap_layout import update_heatmap_layout


def get_heatmap_figure(data_df):
    fig = go.Figure(
        go.Histogram2dContour(
            x=data_df["xCordAdjusted"],
            y=data_df["yCordAdjusted"],
            contours=dict(
                coloring="heatmap",
                showlabels=True,
                labelfont=dict(size=14, color="black"),
            ),
            colorscale=[
                [0.0, "rgba(0,0,0,0)"],
                [0.3, "blue"],
                [0.7, "orange"],
                [1.0, "red"],
            ],
            zmin=10,
            opacity=0.7,
            hovertemplate="Coordonée horizontale: %{x} pieds<br>Coordonnée verticale: %{y} pieds<br>Nombre de buts: %{z}<extra></extra>",
        )
    )

    update_heatmap_layout(fig, image_uri)

    return fig
