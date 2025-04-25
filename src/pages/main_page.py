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
                                    html.H2("Tableau de bord LNH – Saison 2023-2024"),
                                    html.P(
                                        "Ce tableau de bord vous permet de visualiser l'ensemble des buts marqués durant la saison 2023-2024 de la LNH à travers deux types de visualisations : un nuage de points et une carte carte isarithmique."
                                    ),
                                    html.Br(),
                                    html.H3("Filtres disponibles :"),
                                    html.Ul(
                                        [
                                            html.Li(
                                                [
                                                    html.B("Vue principale : "),
                                                    "Affiche tous les buts marqués ou uniquement ceux associés aux équipes, joueurs, positions sélectionnés, ou aux gardiens sélectionnés qui les ont accordés. La liste déroulante s’adapte dynamiquement en fonction des choix effectués.",
                                                ]
                                            ),
                                            html.Br(),
                                            html.Li(
                                                [
                                                    html.B("Latéralité du tireur : "),
                                                    "Filtre les buts selon que le marqueur est gaucher, droitier, ou inclut tous les marqueurs.",
                                                ]
                                            ),
                                            html.Br(),
                                            html.Li(
                                                [
                                                    html.B("Type de match : "),
                                                    "Choisir entre toutes les parties, uniquement les parties de saison régulière ou uniquement celles des séries éliminatoires.",
                                                ]
                                            ),
                                            html.Br(),
                                            html.Li(
                                                [
                                                    html.B("Type de tir : "),
                                                    "Filtre les buts selon la catégorie du tir : tir du poignet, lancer frappé, tir du revers ou déviation. La liste déroulante s’adapte dynamiquement en fonction de la sélection.",
                                                ]
                                            ),
                                            html.Br(),
                                            html.Li(
                                                [
                                                    html.B("Période : "),
                                                    "Filtre les buts selon la période durant laquelle ils ont été marqués : 1ère, 2e, 3e période ou prolongation.",
                                                ]
                                            ),
                                            html.Br(),
                                            html.Li(
                                                [
                                                    html.B("Situation numérique : "),
                                                    "Filtre selon le contexte dans lequel les buts ont été marqués : égalité numérique, avantage numérique ou désavantage numérique.",
                                                ]
                                            ),
                                            html.Br(),
                                            html.Li(
                                                [
                                                    html.B(
                                                        "Temps de glace défensif moyen : "
                                                    ),
                                                    "Utilisez le curseur pour sélectionner le temps moyen minimum passé sur la glace par l'équipe défensive.",
                                                ]
                                            ),
                                        ]
                                    ),
                                    html.Br(),
                                    html.P(
                                        "Utilisez ces filtres du panneau de droite pour explorer les données selon vos critères."
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
                                "Carte Isarithmique",
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
