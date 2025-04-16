"""
4e visualisation qui répond à :
Question cible 8 : Y avait-il des équipes plus efficaces pour marquer des buts en 2023-2024?
la question cible 9 : Y avait-il des équipes plus efficaces pour empêcher des buts en 2023-2024?
"""

import plotly.express as px
import plotly.graph_objects as go
from preprocess import get_scatter_plot_pictogram_data
from assets.team_color import TEAM_COLOR_MAP


def get_scatter_plot_pictogram_figure(goal_df, team_logos):
    """
    Processes the data to build the scatter plot pictogram

    args:
        df: The original shot DataFrame for the 2023-2024 season in the NHL
    returns:
        The scatter plot with pictograms instead of points representing the amount of goals scored
        and allowed by each team during the 2023-2024 NHL season
    """

    # We get the preprocessed data to create the figure
    preprocessed_df = get_scatter_plot_pictogram_data(goal_df)

    # We create the scatter plot
    fig = px.scatter(
        preprocessed_df,
        x="goalsScoredAgainst",
        y="goalsScored",
    )
    fig.update_layout(
        width=1050,
        height=800,
        dragmode=False,
        title=dict(
        text="Comparaison des buts marqués et accordés par équipe en 2023-2024",
        font=dict(size=22),
        x=0.5,
        xanchor='center'
        ),
        xaxis_title="Buts accordés",
        yaxis_title="Buts marqués",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            gridcolor="gray",
            zerolinecolor="gray",
            showline=True,
            linecolor="gray",
            range=[184, 304],
            dtick=10,
        ),
        yaxis=dict(
            gridcolor="gray",
            zerolinecolor="gray",
            showline=True,
            linecolor="gray",
            range=[128, 360],
            dtick=25,
        ),
    )

    fig.update_traces(marker=dict(size=1, opacity=0), hoverinfo=None, visible=False)

    # We create a dictionnary to define the size of each logo
    size_dictionnary = {
        "ANA": {"sizex": 13, "sizey": 13},
        "ARI": {"sizex": 13, "sizey": 13},
        "BOS": {"sizex": 12, "sizey": 12},
        "BUF": {"sizex": 12, "sizey": 12},
        "CAR": {"sizex": 19, "sizey": 19},
        "CBJ": {"sizex": 12, "sizey": 12},
        "CGY": {"sizex": 12, "sizey": 12},
        "CHI": {"sizex": 15, "sizey": 15},
        "COL": {"sizex": 16, "sizey": 16},
        "DAL": {"sizex": 13, "sizey": 13},
        "DET": {"sizex": 18, "sizey": 18},
        "EDM": {"sizex": 13, "sizey": 13},
        "FLA": {"sizex": 15, "sizey": 15},
        "LAK": {"sizex": 15, "sizey": 15},
        "MIN": {"sizex": 18, "sizey": 18},
        "MTL": {"sizex": 11, "sizey": 11},
        "NJD": {"sizex": 13, "sizey": 13},
        "NSH": {"sizex": 18, "sizey": 18},
        "NYI": {"sizex": 14, "sizey": 14},
        "NYR": {"sizex": 15, "sizey": 15},
        "OTT": {"sizex": 13, "sizey": 13},
        "PHI": {"sizex": 16, "sizey": 16},
        "PIT": {"sizex": 16, "sizey": 16},
        "SEA": {"sizex": 13, "sizey": 13},
        "SJS": {"sizex": 17, "sizey": 17},
        "STL": {"sizex": 12, "sizey": 12},
        "TBL": {"sizex": 13, "sizey": 13},
        "TOR": {"sizex": 16, "sizey": 16},
        "VAN": {"sizex": 13, "sizey": 13},
        "VGK": {"sizex": 15, "sizey": 15},
        "WPG": {"sizex": 15, "sizey": 15},
        "WSH": {"sizex": 22, "sizey": 22},
    }

    # We create the hovertemplate
    hovertemplate = (
        f"<span style='font-weight: Bold'><b>Équipe</b></span>"
        "<span> : %{customdata[0]}</span><br>"
        f"<span style='font-weight: Bold'><b>Catégorie</b></span>"
        "<span> : %{customdata[1]}</span><br>"
        f"<span style='font-weight: Bold'><b>Buts marqués</b></span>"
        "<span> : %{y}</span><br>"
        f"<span style='font-weight: Bold'><b>Buts accordés</b></span>"
        "<span> : %{x}</span><br><extra></extra>"
    )

    # We turn each point of the scatter into the team's logo and we add a very small point to get the color of the team for
    # the hoverlabel's background color
    for i, row in preprocessed_df.iterrows():
        team_name = row["teamCode"]
        category = row["Category"]
        x = row["goalsScoredAgainst"]
        y = row["goalsScored"]

        if team_name in team_logos:
            fig.add_layout_image(
                x=x,
                y=y,
                source=team_logos[team_name],
                xref="x",
                yref="y",
                sizex=size_dictionnary[team_name]["sizex"],
                sizey=size_dictionnary[team_name]["sizey"],
                xanchor="center",
                yanchor="middle",
                name=f"{team_name}",
            )

            fig.add_trace(
                go.Scatter(
                    x=[x],
                    y=[y],
                    mode="markers",
                    marker=dict(
                        size=30,
                        opacity=0,
                        color=TEAM_COLOR_MAP.get(team_name, "black"),
                    ),
                    customdata=[[team_name, category]],
                    hovertemplate=hovertemplate,
                    hoverlabel=dict(font=dict(color="white")),
                    showlegend=False,
                )
            )

    # We add the average line of goals allowed
    fig.add_shape(
        type="line",
        x0=(preprocessed_df["goalsScoredAgainst"]).mean(),
        x1=(preprocessed_df["goalsScoredAgainst"]).mean(),
        y0=500,
        y1=0,
        line=dict(color="red", width=2, dash="dot"),
        layer="below",
    )

    # We add the average line of goals scored
    fig.add_shape(
        type="line",
        x0=0,
        x1=500,
        y0=(preprocessed_df["goalsScored"]).mean(),
        y1=(preprocessed_df["goalsScored"]).mean(),
        line=dict(color="blue", width=2, dash="dot"),
        layer="below",
    )

    # We add anotations for each section of the scatter plot

    fig.add_annotation(
        x=200,
        y=350,
        text=f"<span style='font-weight: Bold><b>Bon offensivement</b><br><b>Bon défensivement</b></span>",
        showarrow=False,
        font=dict(size=14),
        align="center",
    )

    fig.add_annotation(
        x=287,
        y=350,
        text=f"<span style='font-weight: Bold><b>Bon offensivement</b><br><b>Mauvais défensivement</b></span>",
        showarrow=False,
        font=dict(size=14),
        align="center",
    )

    fig.add_annotation(
        x=287,
        y=150,
        text=f"<span style='font-weight: Bold><b>Mauvais offensivement</b><br><b>Mauvais défensivement</b></span>",
        showarrow=False,
        font=dict(size=14),
        align="center",
    )

    fig.add_annotation(
        x=202,
        y=150,
        text=f"<span style='font-weight: Bold><b>Mauvais offensivement</b><br><b>Bon défensivement</b></span>",
        showarrow=False,
        font=dict(size=14),
        align="center",
    )

    # We add the legend
    fig.add_trace(
        go.Scatter(
            x=[None],
            y=[None],
            mode="lines",
            line=dict(color="red", dash="dot", width=2),
            name="Nombre moyen de buts accordés",
            showlegend=True,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[None],
            y=[None],
            mode="lines",
            line=dict(color="blue", dash="dot", width=2),
            name="Nombre moyen de buts marqués",
            showlegend=True,
        )
    )

    # Disable legend interactions globally
    fig.update_layout(legend=dict(itemclick=False, itemdoubleclick=False))

    return fig
