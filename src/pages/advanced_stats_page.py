from components.stacked_bar_chart_component import get_stacked_bar_chart_component
from dash import html, dcc

from graphs.advanced_stats_page_graphs.bar_charts.bar_chart.bar_chart import (
    get_bar_chart_figure,
)
from graphs.advanced_stats_page_graphs.scatter_plot.scatter_plot_pictogram import (
    get_scatter_plot_pictogram_figure,
)
from graphs.advanced_stats_page_graphs.pie_charts.pie_charts import get_pie_chart_figure
from components.filters import get_filter_pie_charts, get_filter_stacked_bar_chart


def get_advanced_content(data_df, team_logos=None):
    """
    Returns the advanced content of the page, including three tabs:
      - "Analyse des tirs": stacked bar chart and bar chart.
      - "Par équipe": scatter plot pictogram.
      - "Pie Charts": composite figure with 3 pie charts and a filter,
                      arranged side-by-side (filter on the right).
    """
    # Create the composite figure for the pie charts
    composite_pie_fig = get_pie_chart_figure(data_df)

    return html.Div(
        className="main-page",
        children=[
            html.Div(
                className="graph-container",
                children=[
                    # Control buttons to switch between tabs
                    html.Div(
                        className="info-popup-container",
                        children=[
                            html.Div(
                                className="tooltip-wrapper",
                                children=[
                                    html.Button(
                                        "i", id="info-button", className="info-button"
                                    ),
                                    html.Div(
                                        className="tooltip-text",
                                        id="tooltip-text-content-advanced",
                                        children=[],
                                    ),
                                ],
                            ),
                        ],
                        style={
                            "position": "absolute",
                            "top": "10px",
                            "right": "10px",
                            "zIndex": 10,
                        },
                    ),
                    html.Div(
                        className="graph-controls",
                        children=[
                            html.Button(
                                "Par événement",
                                className="graph-control-button stack-button active",
                                id="shots-analysis-button",
                            ),
                            html.Button(
                                "Par équipe",
                                className="graph-control-button team-button",
                                id="team-analysis-button",
                            ),
                            html.Button(
                                "Par répartition",
                                className="graph-control-button piecharts",
                                id="pie-charts-button",
                            ),
                        ],
                    ),
                    # Graph and filter content
                    html.Div(
                        className="graph-and-filters graph-section fade-in",
                        id="advanced-page-content",
                        children=[
                            # Tab: By Event (default)
                            html.Div(
                                className="stack-graph-section fade-in",
                                id="shots-analysis-section",
                                children=[
                                    html.Div(
                                        className="stacked-charts-and-filter-container",
                                        children=[
                                            # Stacked bar chart column
                                            html.Div(
                                                get_stacked_bar_chart_component(
                                                    data_df
                                                ),
                                                style={"flex": "4", "height": "100%"},
                                            ),
                                            # Filter column (on the right)
                                            html.Div(
                                                className="stacked-filter-div",
                                                children=get_filter_stacked_bar_chart(),
                                                style={"flex": "1", "height": "100%"},
                                            ),
                                        ],
                                    ),
                                    html.Div(
                                        children=[
                                            dcc.Graph(
                                                className="graph stacked-graph",
                                                id="q5-bar-chart-graph",
                                                figure=get_bar_chart_figure(data_df),
                                                config={
                                                    "scrollZoom": False,
                                                    "showTips": False,
                                                    "showAxisDragHandles": False,
                                                    "doubleClick": False,
                                                    "displayModeBar": False,
                                                },
                                                style={
                                                    "width": "100%",
                                                    "height": "400px",
                                                },
                                            )
                                        ],
                                    ),
                                ],
                            ),
                            # Tab: By Team
                            html.Div(
                                className="team-graph-section fade-in",
                                id="team-analysis-section",
                                style={"display": "none"},  # Hidden by default
                                children=[
                                    html.Div(
                                        className="graph",
                                        id="scatter-plot-pictogram-div",
                                        children=[
                                            dcc.Graph(
                                                id="scatter-plot-pictogram-graph",
                                                figure=get_scatter_plot_pictogram_figure(
                                                    data_df, team_logos
                                                ),
                                                clear_on_unhover=True,
                                                config={
                                                    "scrollZoom": False,
                                                    "showTips": False,
                                                    "showAxisDragHandles": False,
                                                    "doubleClick": False,
                                                    "displayModeBar": False,
                                                },
                                                style={
                                                    "width": "100%",
                                                    "height": "100%",
                                                },
                                            )
                                        ],
                                    ),
                                ],
                            ),
                            # New tab: Pie Charts
                            html.Div(
                                className="graph-section fade-in",
                                id="pie-charts-section",
                                style={"display": "none"},  # Hidden by default
                                children=[
                                    html.Div(
                                        className="pie-charts-and-filter-container",
                                        children=[
                                            # Pie charts column
                                            html.Div(
                                                className="pie-charts-div",
                                                children=[
                                                    dcc.Graph(
                                                        id="pie-charts-composite",
                                                        figure=composite_pie_fig,
                                                        config={
                                                            "scrollZoom": False,
                                                            "showTips": False,
                                                            "showAxisDragHandles": False,
                                                            "doubleClick": False,
                                                            "displayModeBar": False,
                                                        },
                                                        style={"width": "100%"},
                                                    ),
                                                ],
                                            ),
                                            # Filter column (on the right)
                                            html.Div(
                                                className="pie-filter-div",
                                                children=get_filter_pie_charts(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
