import plotly.graph_objects as go
from plotly.subplots import make_subplots

def get_pie_chart_figure(data_df):
    # Filtrer les données pour ne garder que les "GOAL"
    df = data_df[data_df['event'] == 'GOAL'].copy()

    # 1) Préparation pour le diagramme par période
    period_labels = {
        1: "Première période",
        2: "Deuxième période",
        3: "Troisième période",
        4: "Prolongation",
        5: "Prolongation"
    }
    period_counts = df['period'].map(period_labels).value_counts()

    # 2) Préparation pour le diagramme par type de match
    game_type_labels = {
        0: "Saison régulière",
        1: "Séries éliminatoires"
    }
    game_type_counts = df['isPlayoffGame'].map(game_type_labels).value_counts()

    # 3) Préparation pour le diagramme local/visiteur
    home_team_labels = {
        0: "Équipe visiteuse",
        1: "Équipe locale"
    }
    home_team_counts = df['isHomeTeam'].map(home_team_labels).value_counts()

    # Création de la figure composite avec 3 subplots (domaines pour les pie charts)
    fig = make_subplots(
        rows=1, cols=3,
        specs=[[{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}]],
        subplot_titles=("Buts par période", "Buts par type de match", "Buts local/visiteur"),
    )

    # Ajout du pie chart pour les périodes
    fig.add_trace(go.Pie(
        labels=period_counts.index,
        values=period_counts.values,
        hoverinfo='label+percent+value',
        textinfo='percent',
        textfont_size=14,
        marker=dict(line=dict(color='#ffffff', width=2)),
        pull=[0.03] * len(period_counts)
    ), row=1, col=1)

    # Ajout du pie chart pour le type de match
    fig.add_trace(go.Pie(
        labels=game_type_counts.index,
        values=game_type_counts.values,
        hoverinfo='label+percent+value',
        textinfo='percent',
        textfont_size=14,
        marker=dict(line=dict(color='#ffffff', width=2)),
        pull=[0.03] * len(game_type_counts)
    ), row=1, col=2)

    # Ajout du pie chart pour local/visiteur
    fig.add_trace(go.Pie(
        labels=home_team_counts.index,
        values=home_team_counts.values,
        hoverinfo='label+percent+value',
        textinfo='percent',
        textfont_size=14,
        marker=dict(line=dict(color='#ffffff', width=2)),
        pull=[0.03] * len(home_team_counts)
    ), row=1, col=3)

    # Personnalisation de la mise en page
    fig.update_layout(
        autosize=True,
        margin=dict(l=10, r=10, t=20, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        transition=dict(duration=500)
    )

    return fig
