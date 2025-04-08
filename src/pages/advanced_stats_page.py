from dash import html, dcc

from graphs.stacked_bar_chart import get_stacked_bar_chart_figure, get_bar_chart_figure
from graphs.scatter_plot_pictogram import get_scatter_plot_pictogram_figure

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
         html.Div(className = 'graph', id = 'scatter-plot-pictogram-div',
                  style= {'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}, 
                  children = [
                    dcc.Graph(figure = get_scatter_plot_pictogram_figure(data_df), id = 'scatter-plot-pictogram-graph', 
                        config = dict(
                        scrollZoom = False,
                        showTips = False,
                        showAxisDragHandles = False,
                        doubleClick = False,
                        displayModeBar = False
                    ))
                ])
])
 