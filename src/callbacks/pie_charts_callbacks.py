# pie_charts_callbacks.py

from dash import Input, Output
from graphs.pie_charts import build_pie_figures

def register_pie_charts_callbacks(app, data_df):
    @app.callback(
        [
            Output('pie-chart-1', 'figure'),
            Output('pie-chart-2', 'figure'),
            Output('pie-chart-3', 'figure'),
        ],
        [
            Input('season-choice', 'value'),
            Input('period-choice', 'value'),
            Input('home-away-choice', 'value'),
        ]
    )
    def update_pie_charts(season_choice, period_choice, home_away_choice):
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

        fig1, fig2, fig3 = build_pie_figures(filtered_df)

        return fig1, fig2, fig3
