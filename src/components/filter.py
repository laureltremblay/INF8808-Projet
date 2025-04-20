from dash import html, dcc

from graphs.stacked_bar_chart import MODES


def get_filter_container():
    return html.Div(
        id="filter-container",
        children=[
            html.Div(
                className="main-choice",
                children=[
                    dcc.RadioItems(
                        id="main-choice",
                        options=[
                            {"label": "Tous", "value": "all"},
                            {"label": "Par équipe", "value": "team"},
                            {"label": "Par joueur", "value": "player"},
                            {"label": "Par position", "value": "position"},
                            {"label": "Par gardien", "value": "goalie"},
                        ],
                        value="all",  # Sélection par défaut
                        labelStyle={"display": "block"},
                    ),
                ],
            ),
            html.Div(
                className="filter",
                children=[
                    dcc.Dropdown(
                        id="main-choice-dropdown",
                        multi=True,
                        placeholder="---",
                        disabled=True,
                        searchable=True,
                        clearable=True,
                    )
                ],
            ),
            html.Div(
                className="shooter-side-choice",
                children=[
                    html.P("Main dominante du tireur :"),
                    dcc.RadioItems(
                        id="shooter-side-choice",
                        options=[
                            {"label": "Tous", "value": "all"},
                            {"label": "Droitier", "value": "right"},
                            {"label": "Gaucher", "value": "left"},
                        ],
                        value="all",
                        labelStyle={"display": "block"},
                    ),
                ],
            ),
            html.Hr(),
            html.Div(
                children=[
                    dcc.RadioItems(
                        id="season-choice",
                        options=[
                            {"label": "Tous", "value": "all"},
                            {"label": "Saison régulière", "value": "regular_season"},
                            {"label": "Séries éliminatoires", "value": "playoffs"},
                        ],
                        value="all",  # Sélection par défaut
                        labelStyle={"display": "block"},
                    ),
                ]
            ),
            html.Hr(),
            html.Div(
                children=[
                    html.P("Type de tir : "),
                    dcc.Dropdown(
                        id="shot-type-choice",
                        options=[
                            {"label": "Tous", "value": "all"},
                            {"label": "Tirs du poignet", "value": "WRIST"},
                            {"label": "Lancers frappés", "value": "SLAP"},
                            {"label": "Tirs du revers", "value": "BACK"},
                            {"label": "Déviations", "value": "TIP"},
                        ],
                        value="all",  # Sélection par défaut
                        clearable=False,
                        searchable=False,
                    ),
                ]
            ),
            html.Hr(),
            html.Div(
                children=[
                    dcc.RadioItems(
                        id="period-choice",
                        options=[
                            {"label": "Toutes", "value": "all"},
                            {"label": "1ère période", "value": "1"},
                            {"label": "2ème période", "value": "2"},
                            {"label": "3ème période", "value": "3"},
                            {"label": "Prolongation", "value": "4"},
                        ],
                        value="all",  # Sélection par défaut
                        labelStyle={"display": "block"},
                    )
                ]
            ),
            html.Hr(),
            html.Div(
                children=[
                    dcc.RadioItems(
                        id="num-players-choice",
                        options=[
                            {"label": "Tous", "value": "all"},
                            {"label": "Égalité numérique", "value": "even_strength"},
                            {"label": "Avantage numérique", "value": "powerplay"},
                            {"label": "Désavantage numérique", "value": "short_handed"},
                        ],
                        value="all",  # Sélection par défaut
                        labelStyle={"display": "block"},
                    )
                ]
            ),
            html.Hr(),
            # add slider for defending team avg time on ice
            html.Div(
                children=[
                    html.P("Temps de glace moyen minimal de l'équipe défensive : "),
                    dcc.Slider(
                        id="defending-toi-slider",
                        min=0,
                        max=220,
                        value=0,
                        tooltip={"placement": "bottom"},
                    ),
                ]
            ),
        ],
    )


def get_filter_pie_charts():
    return html.Div(
        id="filter-container",  # Identifiant modifié pour éviter conflit
        children=[
            html.Div(
                children=[
                    html.Label("Filtrer par équipe :"),
                    dcc.Dropdown(
                        id="team-choice",
                        options=[],  # sera rempli dynamiquement
                        placeholder="Choisir une équipe",
                        clearable=True,
                    ),
                ]
            ),
            html.Hr(),
            html.Div(
                children=[
                    dcc.RadioItems(
                        id="period-choice",
                        options=[
                            {"label": "Toutes", "value": "all"},
                            {"label": "1ère période", "value": "1"},
                            {"label": "2ème période", "value": "2"},
                            {"label": "3ème période", "value": "3"},
                            {"label": "Prolongation", "value": "4"},
                        ],
                        value="all",
                        labelStyle={"display": "block"},
                    )
                ]
            ),
            html.Hr(),
            html.Div(
                children=[
                    dcc.RadioItems(
                        id="season-choice",
                        options=[
                            {"label": "Tous", "value": "all"},
                            {"label": "Saison régulière", "value": "regular_season"},
                            {"label": "Séries éliminatoires", "value": "playoffs"},
                        ],
                        value="all",
                        labelStyle={"display": "block"},
                    ),
                ]
            ),
            html.Hr(),
            html.Div(
                children=[
                    dcc.RadioItems(
                        id="home-away-choice",
                        options=[
                            {"label": "Toutes", "value": "all"},
                            {"label": "Équipe locale", "value": "home"},
                            {"label": "Équipe visiteuse", "value": "away"},
                        ],
                        value="all",
                        labelStyle={"display": "block"},
                    )
                ]
            ),
        ],
    )
    
def get_filter_stacked_bar_chart():
    return html.Div(
            id="filter-container",
            children=[
                html.Div(
                    className="stacked-mode-info",
                    children=[
                        html.I(className="fas fa-info-circle"),
                        html.Span("Mode d'affichage:", className="info-text"),
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
            ],
            style={"flex": "1", "marginLeft": "20px"}  # 1 part sur 4, petite colonne à droite
        )
