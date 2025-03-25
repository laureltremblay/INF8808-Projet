from dash import Input, Output, ctx

from graphs.scatter import get_scatter_figure


def register_main_page_callbacks(app, data_df):
    @app.callback(
        Output('main-graph', 'figure'),
        Output('heatmap-button', 'className'),
        Output('scatter-button', 'className'),
        [Input('scatter-button', 'n_clicks'),
         Input('heatmap-button', 'n_clicks')]
    )
    def update_figure(*_):
        if ctx.triggered_id == 'heatmap-button':
            return {
                'data': [],
                'layout': {}
            } , 'header-button heatmap-button active', 'header-button scatter-button'
        else:
            return get_scatter_figure(data_df), 'header-button heatmap-button', 'header-button scatter-button active'