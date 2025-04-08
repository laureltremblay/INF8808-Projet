import plotly.express as px
import base64
import os


# Encode the local image as base64
image_path = 'assets/rink.jpg'
image_url = None
if image_path and os.path.exists(image_path):
    with open(image_path, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode()
        image_url = f"data:image/jpg;base64,{encoded_image}"


def get_scatter_figure(data_df, color_var: str = 'teamCode'):
    fig = px.scatter(data_df, x='xCordAdjusted', y='yCordAdjusted', color=color_var)
    
    # Customize the plot layout
    fig.update_layout(
        # showlegend=False,
        legend=dict(
            itemclick=False,  # Prevent hiding a trace when clicking the legend
            itemdoubleclick=False  # Prevent isolating a trace on double-click
            
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        xaxis=dict(showgrid=False),  # Disable x-axis gridlines
        yaxis=dict(showgrid=False),  # Disable y-axis gridlines
    )
    
    # Update trace to make points smaller and more visible
    fig.update_traces(marker=dict(size=5))

    fig.update_layout(
    xaxis=dict(
        range=[0, 100],
        domain=[0, 0.9],  # Back to original size
        showgrid=False,
        zeroline=False,
    ),
    yaxis=dict(
        range=[-40, 40],
        showgrid=False,
        zeroline=False,
        scaleanchor="x"
    ),
    images=[
        dict(
            source=image_url,
            xref="x",
            yref="y",
            x=0,
            y=50,
            sizex=100,
            sizey=100,
            sizing="stretch",
            opacity=0.5,
            layer="below"
        )
    ],
    margin=dict(l=40, r=40, t=20, b=40),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    legend=dict(itemclick=False, itemdoubleclick=False)
)

    
    return fig