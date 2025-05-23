import plotly.express as px
import plotly.graph_objects as go
from graphs.advanced_stats_page_graphs.scatter_plot.scatter_plot_pictogram_layout import (
    update_scatter_plot_pictogram_layout,
)
from preprocess import get_scatter_plot_pictogram_data
from assets.team_color import TEAM_COLOR_MAP
from assets.team_logo_sizes import size_dictionnary


def get_scatter_plot_pictogram_figure(goal_df, team_logos):
    """
    Build the scatter plot pictogram

    args:
        df: The original shot DataFrame for the 2023-2024 season in the NHL
    returns:
        The scatter plot with team logos as the points representing the amount of goals scored
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

    update_scatter_plot_pictogram_layout(fig)
    fig.update_traces(marker=dict(size=1, opacity=0), hoverinfo=None, visible=False)

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
