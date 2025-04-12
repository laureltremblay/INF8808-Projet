from dash import Input, Output
from graphs.pie_charts import get_pie_chart_figure

def register_pie_charts_callbacks(app, data_df):
    @app.callback(
        Output('pie-charts-composite', 'figure'),
        [
            Input('season-choice', 'value'),
            Input('period-choice', 'value'),
            Input('home-away-choice', 'value'),
            Input('team-choice', 'value'),
        ]
    )
    def update_pie_charts(season_choice, period_choice, home_away_choice, team_choice):
        filtered_df = data_df.copy()

        if season_choice == 'regular_season':
            filtered_df = filtered_df[filtered_df['isPlayoffGame'] == 0]
        elif season_choice == 'playoffs':
            filtered_df = filtered_df[filtered_df['isPlayoffGame'] == 1]

        if period_choice != 'all':
            filtered_df = filtered_df[filtered_df['period'] == int(period_choice)]

        if home_away_choice == 'home':
            filtered_df = filtered_df[filtered_df['isHomeTeam'] == 1]
        elif home_away_choice == 'away':
            filtered_df = filtered_df[filtered_df['isHomeTeam'] == 0]

        if team_choice:
            filtered_df = filtered_df[filtered_df['teamCode'] == team_choice]

        # La fonction renvoie une seule figure composite
        fig = get_pie_chart_figure(filtered_df)
        return fig

    @app.callback(
        Output('team-choice', 'options'),
        Input('team-choice', 'id')  # Déclenchement unique pour remplir le dropdown
    )
    def populate_team_dropdown(_):
        teams = sorted(data_df['teamCode'].unique())
        return [{'label': team, 'value': team} for team in teams]
