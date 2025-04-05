from dash import html, dcc

from graphs.stacked_bar_chart import get_stacked_bar_chart_figure, get_bar_chart_figure

def get_advanced_content(data_df):
    return html.Div([
        html.H2("Advanced Statistics Page"),
        html.P("Here you can add advanced statistics or charts."),
        html.Div(className='graph', id='q5-stacked-bar-chart-graph-div', children=[
                    dcc.Graph(figure=get_stacked_bar_chart_figure(data_df), id='q5-stacked-bar-chart-graph', config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ))
                ]),
        html.Div(className='graph', id='q5-bar-chart-graph-div', children=[
                    dcc.Graph(figure=get_bar_chart_figure(data_df), id='q5-bar-chart-graph', config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ))
                ]),
        
])
 