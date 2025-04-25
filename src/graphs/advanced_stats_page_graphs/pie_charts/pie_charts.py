import plotly.graph_objects as go
from plotly.subplots import make_subplots

from graphs.advanced_stats_page_graphs.pie_charts.pie_charts_layout import (
    update_pie_chart_layout,
)


def get_pie_chart_figure(data_df):
    # Filter the data to keep only "GOAL" events
    df = data_df[data_df["event"] == "GOAL"].copy()

    # 1) Preparation for the period pie chart
    period_labels = {
        1: "Première période",
        2: "Deuxième période",
        3: "Troisième période",
        4: "Prolongation",
        5: "Prolongation",
    }
    period_counts = df["period"].map(period_labels).value_counts()

    # 2) Preparation for the game type pie chart
    game_type_labels = {0: "Saison régulière", 1: "Séries éliminatoires"}
    game_type_counts = df["isPlayoffGame"].map(game_type_labels).value_counts()

    # 3) Preparation for the home/away team pie chart
    home_team_labels = {0: "Équipe visiteuse", 1: "Équipe locale"}
    home_team_counts = df["isHomeTeam"].map(home_team_labels).value_counts()

    # Create the composite figure with 3 subplots (domains for pie charts)
    fig = make_subplots(
        rows=1,
        cols=3,
        specs=[[{"type": "domain"}, {"type": "domain"}, {"type": "domain"}]],
        subplot_titles=(
            "Buts par période",
            "Buts par type de parties",
            "Buts local/visiteur",
        ),
    )

    # Add pie chart for periods, assigned to legendgroup "group1"
    fig.add_trace(
        go.Pie(
            labels=period_counts.index,
            values=period_counts.values,
            hovertemplate="<b>%{label}</b><br><b>Nombre de buts : </b>%{value}<br><b>Pourcentage : </b>%{percent}<extra></extra>",
            textinfo="percent",
            textfont_size=14,
            marker=dict(line=dict(color="#ffffff", width=2)),
            pull=[0.03] * len(period_counts),
            hoverlabel=dict(font_color="white"),
            legendgroup="group1",
        ),
        row=1,
        col=1,
    )

    # Add pie chart for game type, assigned to legendgroup "group2"
    fig.add_trace(
        go.Pie(
            labels=game_type_counts.index,
            values=game_type_counts.values,
            hovertemplate="<b>%{label}</b><br><b>Nombre de buts : </b>%{value}<br><b>Pourcentage : </b>%{percent}<extra></extra>",
            textinfo="percent",
            textfont_size=14,
            marker=dict(line=dict(color="#ffffff", width=2)),
            pull=[0.03] * len(game_type_counts),
            hoverlabel=dict(font_color="white"),
            legendgroup="group2",
        ),
        row=1,
        col=2,
    )

    # Add pie chart for home/away, assigned to legendgroup "group3"
    fig.add_trace(
        go.Pie(
            labels=home_team_counts.index,
            values=home_team_counts.values,
            hoverinfo="label+percent+value",
            hovertemplate="<b>%{label}</b><br><b>Nombre de buts : </b>%{value}<br><b>Pourcentage : </b>%{percent}<extra></extra>",
            textinfo="percent",
            textfont_size=14,
            marker=dict(line=dict(color="#ffffff", width=2)),
            pull=[0.03] * len(home_team_counts),
            hoverlabel=dict(font_color="white"),
            legendgroup="group3",
        ),
        row=1,
        col=3,
    )

    update_pie_chart_layout(fig)

    return fig
