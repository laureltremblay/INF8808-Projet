from dash import html, dcc

def get_filter_container():
    return html.Div(id='filter-container', children=[
        html.H3('Filtres', className='filter-title'),
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
            dcc.Dropdown(id='main-choice-dropdown', multi=True, placeholder='---', disabled=True)  
    
        ]),
    ])