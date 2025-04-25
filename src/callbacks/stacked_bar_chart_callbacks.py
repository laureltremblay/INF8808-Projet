from dash import Input, Output

from graphs.advanced_stats_page_graphs.bar_charts.stacked_bar_chart.stacked_bar_chart import (
    get_stacked_bar_chart_figure,
)


def register_stacked_bar_chart_callbacks(app, data_df):
    @app.callback(
        Output("q5-stacked-bar-chart-graph", "figure"),
        [Input("radio-items", "value")],
    )
    def radio_updated(mode):
        # Re renders the stacked barchart depending on the current mode from the radio buttons.
        df = data_df.copy(deep=True)
        new_fig = get_stacked_bar_chart_figure(data_df=df, mode=mode)
        return new_fig
