# Version 2
# 3e visualisation qui répond à la question 5: Comment est-ce que
# l'événement qui précède le tir impacte la chance de marquer?

# x: Les évènements qui précèdent un tir (lastEventCategory).
# y: La probabilité moyenne de convertir un tir à un but (xGoal_percent).

import plotly.graph_objects as go
import pandas as pd

from graphs.advanced_stats_page_graphs.bar_charts.bar_chart.bar_chart_layout import update_bar_chart_layout
from preprocess import get_bar_chart_data

import plotly.express as px


def get_bar_chart_template():
    return "<span style='color:#333'>%{y:.2f}%</span><extra></extra>"


def get_bar_chart_figure(data_df: pd.DataFrame):
    df = data_df.copy(deep=True)

    # Get the processed data.
    processed_df = get_bar_chart_data(df)

    # Create the bar chart.
    fig = px.bar(
        processed_df,
        x="lastEventCategory",
        y="xGoal_percent",
        labels={
            "xGoal_percent": "Probabilité de but (%)",
            "lastEventCategory": "Événement précédent",
        },
        color_discrete_sequence=["#00CC96"],
        hover_data={"xGoal": ":.3f"},
        title="Probabilité de marquer selon l'événement précédent",
    )
    fig.update_traces(hovertemplate=get_bar_chart_template())

    # Customize the plot layout.
    update_bar_chart_layout(fig)

    return fig
