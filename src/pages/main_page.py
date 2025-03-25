from dash import html, dcc
from graphs.scatter import get_scatter_figure

def get_main_page_content(data_df) -> html.Div:
    return html.Div(className='main-page', children=[
        html.Div(className='graph-container', children=[
            html.Div(className='graph-controls', children=[
                html.Button("Scatter Plot", className="header-button scatter-button active", id="scatter-button"),
                html.Button("Heatmap", className="header-button heatmap-button", id="heatmap-button")
            ]),
            html.Div(className='graph-and-filters', children=[
                html.Div(className='graph', id='main-graph-div', children=[
                    dcc.Graph(figure=get_scatter_figure(data_df), id='main-graph', config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ))
                ]),
                html.Div(id='filter-container', children=[
                    html.H3("Filters", className="filter-title"),
                    html.Div(className='filter', children=[
                        html.Label("Player"),
                        dcc.Dropdown(id='player-filter', multi=True, placeholder='Select player')
                    ]),
                    html.Div(className='filter', children=[
                        html.Label("Team"),
                        dcc.Dropdown(id='team-filter', multi=True, placeholder='Select team')
                    ]),
                    html.Div(className='filter', children=[
                        html.Label("Shot Type"),
                        dcc.Dropdown(id='shot-type-filter', multi=True, placeholder='Select shot type')
                    ]),
                    html.Div(className='filter', children=[
                        html.Label("Season"),
                        dcc.Dropdown(id='season-filter', multi=True, placeholder='Select season')
                    ]),
                ])
            ])
        ]),
    ])
