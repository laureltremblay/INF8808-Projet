from assets.team_color import TEAM_COLOR_MAP
import plotly.express as px
import base64
import os


# Encode the local image as base64
image_path = "assets/rink.jpg"
image_url = None
if image_path and os.path.exists(image_path):
    with open(image_path, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode()
        image_url = f"data:image/jpg;base64,{encoded_image}"


def get_scatter_figure(data_df, color_var: str = "teamCode"):
    fig = px.scatter(
        data_df,
        x="xCordAdjusted",
        y="yCordAdjusted",
        color=color_var,
        color_discrete_map=TEAM_COLOR_MAP if color_var == "teamCode" else None,
        custom_data=[
            "shooterName",
            "teamCode",
            "xCordAdjusted",
            "yCordAdjusted",
            "shotDistance",
            "period",
            "playerPositionThatDidEvent",
            "shooterLeftRight",
            "shotType",
            "defendingTeamAverageTimeOnIce",
            "goalieNameForShot",
        ],
    )

    legend_title = "Équipes"

    if color_var == "shooterName":
        legend_title = "Joueurs"
    elif color_var == "goalieNameForShot":
        legend_title = "Gardiens"
    elif color_var == "playerPositionThatDidEvent":
        legend_title = "Positions"
    elif color_var == "playerPositionThatDidEvent":
        legend_title = "Positions"

    fig.update_layout(
        legend=dict(
            itemclick=False,
            itemdoubleclick=False,
            title=legend_title,
            title_font=dict(size=14),
        ),
        xaxis=dict(showgrid=False, title="Coordonnée horizontale (en pieds)"),
        yaxis=dict(showgrid=False, title="Coordonnée verticale (en pieds)"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    # Update the points size
    fig.update_traces(marker=dict(size=10))

    fig.update_layout(
        xaxis=dict(
            range=[0, 100],
            domain=[0, 0.9],
            showgrid=False,
            zeroline=False,
        ),
        yaxis=dict(range=[-40, 40], showgrid=False, zeroline=False, scaleanchor="x"),
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
                layer="below",
            )
        ],
        margin=dict(l=40, r=40, t=20, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    # Customize hover template
    fig.update_traces(
        hovertemplate=(
            "Tireur: %{customdata[0]}<br>"
            "Équipe: %{customdata[1]}<br>"
            "Coordonnée X: %{customdata[2]} pieds<br>"
            "Coordonnée Y: %{customdata[3]} pieds<br>"
            "Distance du tir: %{customdata[4]:.2f} pieds<br>"
            "Période: %{customdata[5]}<br>"
            "Position: %{customdata[6]}<br>"
            "Lancer: %{customdata[7]}<br>"
            "Type de tir: %{customdata[8]}<br>"
            "Temps moyen sur la glace de l'équipe adverse: %{customdata[9]}s<br>"
            "Gardien: %{customdata[10]}<br>"
            "<extra></extra>"
        ),
    )

    return fig
