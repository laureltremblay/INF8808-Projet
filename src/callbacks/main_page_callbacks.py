from dash import Input, Output, ctx

from graphs.scatter import get_scatter_figure


def register_main_page_callbacks(app, data_df):
    @app.callback(
        Output('main-graph', 'figure'),
        [Input('scatter-button', 'n_clicks'),
         Input('heatmap-button', 'n_clicks')]
    )
    def update_figure(*_):
        if ctx.triggered_id == 'heatmap-button':
            return {
                'data': [],
                'layout': {}
            }
        else:
            return get_scatter_figure(data_df)