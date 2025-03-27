from dash import html, dcc

def get_filter_container():
    return html.Div(id='filter-container', children=[
        # html.H3('Filtres', className='filter-title'),
        html.Div(className='main-choice', children=[
            dcc.RadioItems(
                id='main-choice',
                options=[
                    {'label': 'Tous', 'value': 'all'},
                    {'label': 'Par équipe', 'value': 'team'},
                    {'label': 'Par joueur', 'value': 'player'},
                    {'label': 'Par position', 'value': 'position'},
                    {'label': 'Par gardien', 'value': 'goalie'}
                ],
                value='all',  # Sélection par défaut
                labelStyle={'display': 'block'}
            ),
        ]),
        html.Div(className='filter', children=[
            dcc.Dropdown(
                id='main-choice-dropdown', 
                multi=True, 
                placeholder='---', 
                disabled=True,
                searchable=True,           
                clearable=True,     
            )
        ]),
        html.Hr(),
        html.Div(children=[
            dcc.RadioItems(
                id='season-choice',
                options=[
                    {'label': 'Tous', 'value': 'all'},
                    {'label': 'Saison régulière', 'value': 'regular_season'},
                    {'label': 'Séries éliminatoires', 'value': 'playoffs'},
                ],
                value='all',  # Sélection par défaut
                labelStyle={'display': 'block'}
            ),
        ]),
        html.Hr(),
        html.Div(
            children=[
                html.P('Type de tir : '),
                dcc.Dropdown(
                    id='shot-type-choice',
                    options=[
                        {'label': 'Tous', 'value': 'all'},
                        {'label': 'Tirs du poignet', 'value': 'WRIST'},
                        {'label': 'Lancers frappés', 'value': 'SLAP'},
                        {'label': 'Tirs du revers', 'value': 'BACK'},
                        {'label': 'Déviations', 'value': 'TIP'},
                    ],
                    value='all',  # Sélection par défaut
                    clearable=False,
                    searchable=False
                )
            ]
        ),
        html.Hr(),
        html.Div(
            children=[
                dcc.RadioItems(
                    id='period-choice',
                    options=[
                        {'label': 'Toutes', 'value': 'all'},
                        {'label': '1ère période', 'value': '1'},
                        {'label': '2ème période', 'value': '2'},
                        {'label': '3ème période', 'value': '3'},
                        {'label': 'Prolongation', 'value': '4'}
                    ],
                    value='all',  # Sélection par défaut
                    labelStyle={'display': 'block'}
                )
            ]
        ),
        html.Hr(),
        html.Div(
            children=[
                dcc.RadioItems(
                    id='num-players-choice',
                    options=[
                        {'label': 'Tous', 'value': 'all'},
                        {'label': 'Égalité numérique', 'value': 'even_strength'},
                        {'label': 'Avantage numérique', 'value': 'powerplay'},
                        {'label': 'Désavantage numérique', 'value': 'short_handed'},
                    ],
                    value='all',  # Sélection par défaut
                    labelStyle={'display': 'block'}
                )
            ]
        ),
        html.Hr(),
        # add slider for defending team avg time on ice 
        html.Div(children=[
            html.P('Temps de glace moyen minimal de l\'équipe défensive : '),
            dcc.Slider(
                id='defending-toi-slider',
                min=0,
                max=220,
                value=0,
                tooltip={'placement': 'bottom'}
            ),
        ])
    ])