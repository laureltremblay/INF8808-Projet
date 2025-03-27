import base64
import os
import plotly.express as px
import plotly.graph_objs as go

# Encode the local image as base64
image_path = 'assets/rink.jpg'
image_url = None
if image_path and os.path.exists(image_path):
    with open(image_path, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode()
        image_url = f"data:image/jpg;base64,{encoded_image}"


def get_heatmap_figure(data_df):
    # Create the heatmap plot
    fig = go.Figure(go.Histogram2dContour(
        x=data_df['xCordAdjusted'], 
        y=data_df['yCordAdjusted'], 
        contours=dict(
            showlabels=True,
            labelfont=dict(
                size=12,
                color='white'
            )
        ),
        opacity=0.5
    ))

    
    # Customize the plot layout
    fig.update_layout(
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        xaxis=dict(showgrid=False),  # Disable x-axis gridlines
        yaxis=dict(showgrid=False),  # Disable y-axis gridlines
    )

    # TODO: FIX background image so that if fits better
    if image_url:
        fig.update_layout(
            images=[
                dict(
                    source=image_url,
                    xref="paper",
                    yref="paper",
                    x=0,
                    y=1,
                    sizex=1,
                    sizey=1,
                    sizing="stretch",
                    opacity=0.5,
                    layer="below"
                )
            ]
        )
    
    return fig