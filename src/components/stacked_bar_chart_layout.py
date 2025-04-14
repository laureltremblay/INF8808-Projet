from dash import html, dcc

from graphs.stacked_bar_chart import MODES, get_stacked_bar_chart_figure


def get_stacked_bar_chart_layout(data_df):
    return html.Div(
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
                                    html.Span("Mode d'affichage :", className="info-text")
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
                                    html.Span("Mode actuel : "),
                                    html.Span(MODES['count'], id='mode')
                                ]
                            )
                        ]
                    )
                ]
            ),
    