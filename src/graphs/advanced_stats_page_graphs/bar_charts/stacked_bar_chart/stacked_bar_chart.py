import plotly.graph_objects as go

from assets.event_types import MODES
from graphs.advanced_stats_page_graphs.bar_charts.stacked_bar_chart.stacked_bar_chart_layout import (
    get_stacked_bar_char_template,
    update_stacked_bar_chart_layout,
)
from preprocess import get_stacked_bar_chart_data

event_types_colors = {
    "Tir cadré": "#636EFA",
    "Tir raté": "#EF553B",
    "But": "#00CC96",
}


def get_stacked_bar_chart_figure(data_df, mode=MODES["count"]):
    df = data_df.copy(deep=True)

    # Get the preprocessed data.
    processed_df, processed_percent_df = get_stacked_bar_chart_data(df, mode=mode)
    event_types = ["Tir cadré", "Tir raté", "But"]

    fig = go.Figure()
    for event in event_types:
        # Select the correct data depending on shot type.
        y_data = (
            processed_percent_df[event]
            if mode == MODES["percent"]
            else processed_df[event]
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

    update_stacked_bar_chart_layout(fig, yaxis_config)

    return fig
