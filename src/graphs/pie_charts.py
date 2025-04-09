# pie_charts.py
import plotly.graph_objects as go
from dash import html, dcc

def build_pie_figures(data_df):
    # 1) On filtre les buts
    data_df = data_df[data_df['event'] == 'GOAL'].copy()

    # 2) Figure par période
    period_labels = {1: "Première période", 2: "Deuxième période", 3: "Troisième période", 4: "Prolongation", 5: "Prolongation"}
    period_counts = data_df['period'].map(period_labels).value_counts()

    fig1 = go.Figure(data=[go.Pie(labels=period_counts.index, values=period_counts.values)])
    fig1.update_layout(title_text="Buts par période", title_x=0.15)

    # 3) Figure par type de match
    game_type_labels = {0: "Saison régulière", 1: "Séries éliminatoires"}
    game_type_counts = data_df['isPlayoffGame'].map(game_type_labels).value_counts()

    fig2 = go.Figure(data=[go.Pie(labels=game_type_counts.index, values=game_type_counts.values)])
    fig2.update_layout(title_text="Buts par type de match", title_x=0.15)

    # 4) Figure par équipe locale/visiteuse
    home_team_labels = {0: "Équipe visiteuse", 1: "Équipe locale"}
    home_team_counts = data_df['isHomeTeam'].map(home_team_labels).value_counts()

    fig3 = go.Figure(data=[go.Pie(labels=home_team_counts.index, values=home_team_counts.values)])
    fig3.update_layout(title_text="Buts local/visiteur", title_x=0.15)

    return fig1, fig2, fig3

def get_pie_charts_layout(fig1, fig2, fig3):
    return html.Div(
        className='pie-charts-container',
        children=[
            html.Div(
                dcc.Graph(
                    figure=fig1,
                    id='pie-chart-1'
                ),
                className='pie-chart-div'
            ),
            html.Div(
                dcc.Graph(
                    figure=fig2,
                    id='pie-chart-2'
                ),
                className='pie-chart-div'
            ),
            html.Div(
                dcc.Graph(
                    figure=fig3,
                    id='pie-chart-3'
                ),
                className='pie-chart-div'
            ),
        ]
    )


def get_pie_chart_figure(data_df):
    """
    1) Construit les trois figures (via build_pie_figures).
    2) Retourne le layout (via get_pie_charts_layout).
    """
    fig1, fig2, fig3 = build_pie_figures(data_df)  # On appelle la fonction de construction
    layout = get_pie_charts_layout(fig1, fig2, fig3)
    return layout
