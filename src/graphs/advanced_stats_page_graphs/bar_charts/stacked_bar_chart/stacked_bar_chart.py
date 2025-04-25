# 3e visualisation qui répond à la question 5: Comment est-ce que
# l'événement qui précède le tir impacte la chance de marquer?

# x: Les évènements qui précèdent un tir (lastEventCategory).
# y: Pourcentage des tirs ou quantité de tirs selon l'événement précédent.
import plotly.graph_objects as go
import pandas as pd

from graphs.advanced_stats_page_graphs.bar_charts.stacked_bar_chart.stacked_bar_chart_layout import update_stacked_bar_chart_layout
from preprocess import get_stacked_bar_chart_data

MODES = dict(count="Quantité", percent="Pourcentage")

event_category_map = {
    "GIVE": "Perte de rondelle",
    "SHOT": "Tir au but",
    "HIT": "Mise en échec",
    "TAKE": "Récupération",
    "MISS": "Tir raté",
    "FAC": "Mise au jeu",
    "BLOCK": "Tir bloqué",
    "DELPEN": "Pénalité à retardement",
    "GOAL": "But",
}


event_types_map = {
    "SHOT": "Tir cadré",
    "MISS": "Tir raté",
    "GOAL": "But",
}

event_types_colors = {
    "Tir cadré": "#636EFA",
    "Tir raté": "#EF553B",
    "But": "#00CC96",
}


def get_stacked_bar_char_template(mode):

    if mode == "Quantité":
        return (
            "<span style='color:#333'>"
            "<b>%{fullData.name}</b> : %{y}</span><extra></extra>"
        )
    elif mode == "Pourcentage":
        return (
            "<span style='color:#333'>"
            "<b>%{fullData.name}</b> : %{y:.2f}%</span><extra></extra>"
        )
    return "Invalid mode"


def get_stacked_bar_chart_figure(data_df: pd.DataFrame, mode=MODES["count"]):
    df = data_df.copy(deep=True)

    # Get the preprocessed data.
    processed_df, processed_percent_df = get_stacked_bar_chart_data(df, mode=mode)
    event_types = ["Tir cadré", "Tir raté", "But"]
    
    fig = go.Figure()
    for event in event_types:
        # Select the correct data depending on shot type.
        y_data = (
            processed_percent_df[event] if mode == MODES["percent"] else processed_df[event]
        )

        fig.add_trace(
            go.Bar(
                x=processed_df.index,
                y=y_data,
                name=event,
                marker_color=event_types_colors[event],
                hovertemplate=get_stacked_bar_char_template(mode=mode),
            )
        )

    # Customize the plot layout.
    yaxis_config = {
        "title": (
            "Pourcentage des tirs (%)" if mode == MODES["percent"] else "Nombre de tirs"
        ),
        "range": [0, 100] if mode == MODES["percent"] else None,
    }

    # Update the axes and layout.
    update_stacked_bar_chart_layout(fig, yaxis_config)

    return fig
