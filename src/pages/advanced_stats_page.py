from dash import html, dcc

from graphs.stacked_bar_chart import get_stacked_bar_chart_figure, get_bar_chart_figure
from graphs.pie_charts import get_pie_chart_figure
from components.filter import get_filter_pie_charts

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

        # Conteneur Flex pour ( Filtre | 3 Pie Charts )
        html.Div(
            className='pie-charts-and-filter-container',
            children=[
                # Colonne de droite :
                html.Div(
                    get_pie_chart_figure(data_df),
                    className='pie-charts-div'
                ),
                # Colonne de droite :
                                html.Div(
                    get_filter_pie_charts(),
                    className='pie-filter-div'
                )
            ]
        ),
])
 