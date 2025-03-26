import dash
from dash import Input, Output, ctx, dcc, html
import plotly.express as px
import pandas as pd
from callbacks.main_page_callbacks import register_main_page_callbacks
from pages.main_page import get_main_page_content
from preprocess import abs_xCord

app = dash.Dash(__name__)
app.title = 'NHL Shot Data'

data_df = pd.read_csv('assets/shots_2023_2024.csv')
data_df = abs_xCord(data_df)

# Register all callbacks
register_main_page_callbacks(app, data_df)

app.layout = html.Div(className='content', children=[
    dcc.Location(id='url', refresh=False),  
    html.Header(children=[
        html.H1('2023-2024 NHL Shot Data'),
        html.Div(className='header-container', children=[
            html.Button("Vue d'ensemble", className='header-button active', id='main-page-button'),
            html.Button('Statistiques avancées', className='header-button', id='advanced-button')
        ])
    ]),
    html.Main(id='main-page-content', className='chosen-page', children=[
        get_main_page_content(data_df)  # Initial content
    ])
])

@app.callback(
    [
        Output('main-page-button', 'className'),
        Output('advanced-button', 'className'),
        Output('main-page-content', 'children') 
    ],
    [Input('main-page-button', 'n_clicks'),
     Input('advanced-button', 'n_clicks')]
)
def update_page(*_):
    if ctx.triggered_id == 'advanced-button':
        return "header-button", "header-button active", get_advanced_content()  
    return "header-button active", "header-button", get_main_page_content(data_df) 

# TODO: Move to its own file with own implementation
def get_advanced_content():
    return html.Div([
        html.H2("Advanced Statistics Page"),
        html.P("Here you can add advanced statistics or charts.")
    ])

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
