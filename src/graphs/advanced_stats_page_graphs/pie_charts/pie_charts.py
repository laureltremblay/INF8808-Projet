import plotly.graph_objects as go
from plotly.subplots import make_subplots

def get_pie_chart_figure(data_df):
    # Filtrer les données pour ne garder que les "GOAL"
    df = data_df[data_df["event"] == "GOAL"].copy()

    # 1) Préparation pour le diagramme par période
    period_labels = {
        1: "Première période",
        2: "Deuxième période",
        3: "Troisième période",
        4: "Prolongation",
        5: "Prolongation",
    }
    period_counts = df["period"].map(period_labels).value_counts()

    # 2) Préparation pour le diagramme par type de match
    game_type_labels = {0: "Saison régulière", 1: "Séries éliminatoires"}
    game_type_counts = df["isPlayoffGame"].map(game_type_labels).value_counts()

    # 3) Préparation pour le diagramme local/visiteur
    home_team_labels = {0: "Équipe visiteuse", 1: "Équipe locale"}
    home_team_counts = df["isHomeTeam"].map(home_team_labels).value_counts()

    # Création de la figure composite avec 3 subplots (domaines pour les pie charts)
    fig = make_subplots(
        rows=1,
        cols=3,
        specs=[[{"type": "domain"}, {"type": "domain"}, {"type": "domain"}]],
        subplot_titles=(
            "Buts par période",
            "Buts par type de parties",
            "Buts local/visiteur",
        ),
    )

    # Ajout du pie chart pour les périodes, assigné à legendgroup "group1"
    fig.add_trace(
        go.Pie(
            labels=period_counts.index,
            values=period_counts.values,
            hovertemplate="<b>%{label}</b><br><b>Nombre de buts : </b>%{value}<br><b>Pourcentage : </b>%{percent}<extra></extra>",
            textinfo="percent",
            textfont_size=14,
            marker=dict(line=dict(color="#ffffff", width=2)),
            pull=[0.03] * len(period_counts),
            hoverlabel = dict(font_color="white"),
            legendgroup="group1"
        ),
        row=1,
        col=1,
    )

    # Ajout du pie chart pour le type de match, assigné à legendgroup "group2"
    fig.add_trace(
        go.Pie(
            labels=game_type_counts.index,
            values=game_type_counts.values,
            hovertemplate="<b>%{label}</b><br><b>Nombre de buts : </b>%{value}<br><b>Pourcentage : </b>%{percent}<extra></extra>",
            textinfo="percent",
            textfont_size=14,
            marker=dict(line=dict(color="#ffffff", width=2)),
            pull=[0.03] * len(game_type_counts),
            hoverlabel = dict(font_color="white"),
            legendgroup="group2"
        ),
        row=1,
        col=2,
    )

    # Ajout du pie chart pour local/visiteur, assigné à legendgroup "group3"
    fig.add_trace(
        go.Pie(
            labels=home_team_counts.index,
            values=home_team_counts.values,
            hoverinfo="label+percent+value",
            hovertemplate="<b>%{label}</b><br><b>Nombre de buts : </b>%{value}<br><b>Pourcentage : </b>%{percent}<extra></extra>",
            textinfo="percent",
            textfont_size=14,
            marker=dict(line=dict(color="#ffffff", width=2)),
            pull=[0.03] * len(home_team_counts),
            hoverlabel = dict(font_color="white"),
            legendgroup="group3"
        ),
        row=1,
        col=3,
    )

    # Mise à jour du layout
    fig.update_layout(
        title_text="Répartition des Buts",
        title_x=0.5,
        title_font=dict(size=24, family="Arial, sans-serif"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            xanchor="center",
            x=0.5,
            itemclick=False,
            itemdoubleclick=False,
        ),
        autosize=True,
        margin=dict(l=10, r=10, t=80, b=50),
        transition=dict(duration=500),
    )

    return fig
