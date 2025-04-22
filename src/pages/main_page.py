from dash import html, dcc
from components.filter import get_filter_container
from graphs.main_page_graphs.scatter.scatter import get_scatter_figure


def get_main_page_content(data_df) -> html.Div:
    return html.Div(
        className="main-page",
        children=[
            html.Div(
                className="graph-container",
                children=[
                    html.Div(
                        className="graph-controls",
                        children=[
                            html.Button(
                                "Nuage de points",
                                className="header-button scatter-button active",
                                id="scatter-button",
                            ),
                            html.Button(
                                "Heatmap",
                                className="header-button heatmap-button",
                                id="heatmap-button",
                            ),
                        ],
                    ),
                    html.Div(
                        className="main-graph-section graph-and-filters",
                        children=[
                            html.Div(
                                className="graph",
                                id="main-graph-div",
                                children=[
                                    html.Button(
                                        " Dézoomer",
                                        id="unzoom-button",
                                        className="unzoom",
                                    ),
                                    dcc.Graph(
                                        figure=get_scatter_figure(data_df, None),
                                        id="main-graph",
                                        config=dict(
                                            scrollZoom=False,
                                            showTips=False,
                                            showAxisDragHandles=False,
                                            doubleClick=False,
                                            displayModeBar=False,
                                        ),
                                        style={"height": "75vh"},
                                    ),
                                ],
                            ),
                            get_filter_container(),
                        ],
                    ),
                ],
            ),
        ],
    )
