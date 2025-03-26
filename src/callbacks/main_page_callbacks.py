from dash import Input, Output, ctx

from graphs.heatmap import get_heatmap_figure
from graphs.scatter import get_scatter_figure

def register_main_page_callbacks(app, data_df):
    @app.callback(
        Output('main-graph', 'figure'),
        Output('heatmap-button', 'className'),
        Output('scatter-button', 'className'),
        Input('scatter-button', 'n_clicks'),
        Input('heatmap-button', 'n_clicks'),
        Input('main-choice-dropdown', 'value')  # Merge dropdown input
    )
    def update_figure(scatter_clicks, heatmap_clicks, selected_teams):
        print("Triggered:", ctx.triggered_id)

        # Determine which button was clicked
        if ctx.triggered_id == 'heatmap-button':
            return get_heatmap_figure(data_df), 'header-button heatmap-button active', 'header-button scatter-button'
        
        # If the scatter plot is selected, filter the data
        filtered_df = data_df
        if selected_teams:
            filtered_df = data_df[data_df['teamCode'].isin([selected_teams] if isinstance(selected_teams, str) else selected_teams)]
        
        return get_scatter_figure(filtered_df), 'header-button heatmap-button', 'header-button scatter-button active'

    @app.callback(
        Output('main-choice-dropdown', 'placeholder'),
        Output('main-choice-dropdown', 'options'),
        Output('main-choice-dropdown', 'disabled'), 
        Input('main-choice', 'value')  
    )
    def toggle_dropdown(selected_value):
        if selected_value == 'team':
            options = [{'label': team, 'value': team} for team in sorted(data_df['teamCode'].unique())]
            return 'Choisir une équipe', options, False
        return '---', [], True
