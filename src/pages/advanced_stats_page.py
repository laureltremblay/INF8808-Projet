from dash import html, dcc

from graphs.advanced_stats_page_graphs.bar_charts.stacked_bar_chart.stacked_bar_chart_layout import get_stacked_bar_chart_layout
from graphs.advanced_stats_page_graphs.bar_charts.bar_chart.bar_chart import get_bar_chart_figure
from graphs.advanced_stats_page_graphs.scatter_plot.scatter_plot_pictogram import get_scatter_plot_pictogram_figure
from graphs.advanced_stats_page_graphs.pie_charts.pie_charts import get_pie_chart_figure
from components.filter import get_filter_pie_charts, get_filter_stacked_bar_chart


def get_advanced_content(data_df, team_logos=None):
    """
    Renvoie le contenu avancé de la page comprenant trois onglets :
      - "Analyse des tirs" : stacked bar chart et bar chart.
      - "Par équipe" : scatter plot pictogram.
      - "Pie Charts"   : figure composite regroupant 3 pie charts et un filtre,
                         disposés côte à côte (le filtre à droite).
    """
    # On crée la figure composite pour les pie charts.
    composite_pie_fig = get_pie_chart_figure(data_df)

    return html.Div(
        className="main-page",
        children=[
            html.Div(
                className="graph-container",
                children=[
                    # Boutons de contrôle pour basculer entre les onglets
                    html.Div(
    className="info-popup-container",
    children=[
        html.Div(
            className="tooltip-wrapper",
            children=[
                html.Button("i", id="info-button", className="info-button"),
                                    html.Div(
                                        className="tooltip-text",
                                        id = "tooltip-text-content-advanced",
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
                    # Contenu des graphiques et filtres
                    html.Div(
                        className="graph-and-filters graph-section fade-in",
                        id="advanced-page-content",
                        children=[
                            # Onglet : Par événement (par défaut)
                            html.Div(
                                className="stack-graph-section fade-in",
                                id="shots-analysis-section",
                                children=[
                                    html.Div(
                                        className="stacked-charts-and-filter-container",
                                        children=[
                                            # Colonne stacked bar chart
                                            html.Div(
                                                get_stacked_bar_chart_layout(data_df), style={"flex": "4", "height": "100%"}
                                            ),
                                            # Colonne du filtre (placé à droite)
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
                            # Onglet : Par équipe
                            html.Div(
                                className="team-graph-section fade-in",
                                id="team-analysis-section",
                                style={"display": "none"},  # Masqué par défaut
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
                            # Nouvel onglet : Pie Charts
                            html.Div(
                                className="graph-section fade-in",
                                id="pie-charts-section",
                                style={"display": "none"},  # Masqué par défaut
                                children=[
                                    html.Div(
                                        className="pie-charts-and-filter-container",
                                        children=[
                                            # Colonne des pie charts
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
                                            # Colonne du filtre (placé à droite)
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
