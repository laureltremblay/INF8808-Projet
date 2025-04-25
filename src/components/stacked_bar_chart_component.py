from dash import html, dcc
from graphs.advanced_stats_page_graphs.bar_charts.stacked_bar_chart.stacked_bar_chart import (
    get_stacked_bar_chart_figure,
)


def get_stacked_bar_chart_component(data_df):
    return html.Div(
        className="stacked-section",
        children=[
            html.Div(
                className="graph stacked-graph flex-row",
                children=[
                    html.Div(
                        className="flex-graph-area",
                        children=[
                            dcc.Graph(
                                figure=get_stacked_bar_chart_figure(data_df),
                                id="q5-stacked-bar-chart-graph",
                                config=dict(
                                    scrollZoom=False,
                                    showTips=False,
                                    showAxisDragHandles=False,
                                    doubleClick=False,
                                    displayModeBar=False,
                                ),
                                style={"width": "100%", "height": "100%"},
                            )
                        ],
                        style={"flex": "4"},
                    ),
                ],
            ),
        ],
    )
