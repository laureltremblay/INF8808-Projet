import dash
from dash import html, dcc, Output, Input, ctx
import plotly.express as px
import pandas as pd
from preprocess import abs_xCord, basic_filtering
from scatter import get_scatter_figure

app = dash.Dash(__name__)
app.title = 'NHL Shot Data'

data_df = pd.read_csv('assets/shots_2023_2024.csv')
# Common data filtering
data_df = basic_filtering(data_df)
data_df = abs_xCord(data_df)

# Generate figures
fig_main = get_scatter_figure(data_df)
fig_advanced = px.scatter() # TODO: Add figure for heatmap

app.layout = html.Div(className='content', style={'height': '100vh'}, children=[
    html.Header(children=[
        html.H1('2023-2024 NHL Shot Data'),
        html.Div(className='header-container', children=[
            html.Button("Vue d'ensemble", className='header-button active', id='main-page-button'),
            html.Button('Statistiques avancées', className='header-button', id='advanced-button')
        ])
    ]),
    html.Main(className='viz-container', children=[
        html.Div(className='graph-container', children=[
            dcc.Graph(className='graph', id='main-graph', figure=fig_main, config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
            ))
        ]),
        html.Div(className='filter-container', children=[
            html.Label('Filtre 1'),
            dcc.RadioItems(id='filter-1', options=[
                {'label': 'Option 1', 'value': 'opt1'},
                {'label': 'Option 2', 'value': 'opt2'}
            ], value='opt1'),
            html.Label('Filtre 2'),
            dcc.RadioItems(id='filter-2', options=[
                {'label': 'Option A', 'value': 'optA'},
                {'label': 'Option B', 'value': 'optB'}
            ], value='optA')
        ])
    ])
])

@app.callback(
    [Output('main-graph', 'figure'),
     Output('main-page-button', 'className'),
     Output('advanced-button', 'className')],
    [Input('main-page-button', 'n_clicks'),
     Input('advanced-button', 'n_clicks')]
)
def update_figure(*_):
    if ctx.triggered_id == 'advanced-button':
        return fig_advanced, "header-button", "header-button active"
    return fig_main, "header-button active", "header-button"

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
