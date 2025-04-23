from dash import html, dcc
from components.filter import get_filter_container
from graphs.main_page_graphs.scatter.scatter import get_scatter_figure


def get_main_page_content(data_df) -> html.Div:
    return html.Div(
        className="main-page",
        children=[
            # Info button and hover popup
            html.Div(
                className="info-popup-container",
                children=[
                    html.Div(
                        className="tooltip-wrapper",
                        children=[
                            html.Button("i", id="info-button", className="info-button"),
                            html.Div(
                                className="tooltip-text",
                                children=[
                                    html.H4("Tableau de bord LNH – Saison 2023-2024"),
                                    html.P(
                                        "Ce tableau de bord vous permet de visualiser l'ensemble des buts marqués durant la saison 2023-2024 de la LNH à travers deux types de visualisations : un nuage de points et une carte thermique."
                                    ),
                                    html.Br(),
                                    html.H5("Filtres disponibles :"),
                                    html.Ul(
                                        [
                                            html.Li(
                                                [
                                                    html.B("Vue principale : "),
                                                    "Affiche toutes les données ou les regroupe par équipe, joueur, position ou gardien.",
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.B("Liste déroulante : "),
                                                    "Permet de sélectionner une ou plusieurs valeurs en fonction du filtre principal choisi.",
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.B("Latéralité du tireur : "),
                                                    "Filtrer les buts selon que le tireur est gaucher, droitier ou inclure tous.",
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.B("Type de match : "),
                                                    "Choisir entre tous les matchs, la saison régulière ou les séries éliminatoires.",
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.B("Type de tir : "),
                                                    "Filtrer selon la catégorie du tir : tir du poignet, lancer frappé, tir du revers ou déviation.",
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.B("Période : "),
                                                    "Filtrer selon la période durant laquelle le but a été marqué (1ère, 2e, 3e ou prolongation).",
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.B("Situation numérique : "),
                                                    "Filtrer selon le contexte du but : égalité numérique, avantage ou désavantage.",
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.B(
                                                        "Temps de glace défensif moyen : "
                                                    ),
                                                    "Utiliser le curseur pour sélectionner un minimum de temps moyen passé sur la glace par l'équipe défensive.",
                                                ]
                                            ),
                                        ]
                                    ),
                                    html.Br(),
                                    html.P(
                                        "Utilisez ces filtres dans le panneau à droite pour explorer les données selon vos critères."
                                    ),
                                ],
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
