from dash import html, dcc

from graphs.stacked_bar_chart import MODES, get_stacked_bar_chart_figure, get_bar_chart_figure
from graphs.scatter_plot_pictogram import get_scatter_plot_pictogram_figure
from graphs.pie_charts import get_pie_chart_figure
from components.filter import get_filter_pie_charts


def get_advanced_content(data_df, team_logos = None):
    return html.Div(
        [
            html.H2("Advanced Statistics Page"),
            html.P("Here you can add advanced statistics or charts."),
            html.Div(
                className="stacked-section",
                children=[
                    html.Div(
                        className="graph stacked-graph",
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
                            )
                        ],
                    ),
                    html.Div(
                        className="stacked-controls-container",
                        children=[
                            html.Div(
                                className="stacked-mode-info",
                                children=[
                                    html.I(className="fas fa-info-circle"),
                                    html.Span("Mode d'affichage:", className="info-text")
                                ]
                            ),
                            dcc.RadioItems(
                                id='radio-items',
                                options=[
                                    {'label': MODES['count'], 'value': MODES['count']},
                                    {'label': MODES['percent'], 'value': MODES['percent']},
                                ],
                                value=MODES['count'],
                                className="stacked-radio-items"
                            ),
                            html.Div(
                                className="current-mode-badge",
                                children=[
                                    html.Span("Mode actuel: "),
                                    html.Span(MODES['count'], id='mode')
                                ]
                            )
                        ]
                    )
                ]
            ),
            html.Div(
                className="graph",
                id="q5-bar-chart-graph-div",
                children=[
                    dcc.Graph(
                        figure=get_bar_chart_figure(data_df),
                        id="q5-bar-chart-graph",
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False,
                        ),
                    )
                ],
            ),
            html.Div(
                className="graph",
                id="scatter-plot-pictogram-div",
                style={
                    "display": "flex",
                    "justifyContent": "center",
                    "alignItems": "center",
                },
                children=[
                    dcc.Graph(
                        figure=get_scatter_plot_pictogram_figure(data_df, team_logos),
                        id="scatter-plot-pictogram-graph",
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False,
                        ),
                    )
                ],
            ),
            # Conteneur Flex pour ( Filtre | 3 Pie Charts )
            html.Div(
                className="pie-charts-and-filter-container",
                children=[
                    # Colonne de droite :
                    html.Div(get_pie_chart_figure(data_df), className="pie-charts-div"),
                    # Colonne de droite :
                    html.Div(get_filter_pie_charts(), className="pie-filter-div"),
                ],
            ),
        ]
    )
