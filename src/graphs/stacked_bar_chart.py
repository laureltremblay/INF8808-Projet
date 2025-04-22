# 3e visualisation qui répond à la question 5: Comment est-ce que
# l'événement qui précède le tir impacte la chance de marquer?

# x: Les évènements qui précèdent un tir (lastEventCategory).
# y: La probabilité moyenne de convertir un tir à un but (xGoal_percent).
import plotly.graph_objects as go
import pandas as pd

MODES = dict(count="Quantité", percent="Pourcentage")

event_category_map = {
    "GIVE": "Perte de rondelle",
    "SHOT": "Tir au but",
    "HIT": "Mise en échec",
    "TAKE": "Récupération",
    "MISS": "Tir raté",
    "FAC": "Mise au jeu",
    "BLOCK": "Tir bloqué",
    "DELPEN": "Pénalité à retardement",
    "GOAL": "But",
    # 'GIVE': 'Giveaway',
    # 'SHOT': 'Shot on Goal',
    # 'HIT': 'Hit',
    # 'TAKE': 'Takeaway',
    # 'MISS': 'Missed Shot',
    # 'FAC': 'Faceoff',
    # 'BLOCK': 'Blocked Shot',
    # 'DELPEN': 'Delayed Penalty',
    # 'STOP': 'Stoppage',
    # 'CHL': 'Challenge',
    # 'GOAL': 'Goal'
}


event_types_map = {
    "SHOT": "Tir cadré",
    "MISS": "Tir raté",
    "GOAL": "But",
}

event_types_colors = {
    "Tir cadré": "#636EFA",
    "Tir raté": "#EF553B",
    "But": "#00CC96",
}


def get_stacked_bar_char_template(mode):

    if mode == "Quantité":
        return (
            "<span style='color:#333'>"
            "<b>%{fullData.name}</b> : %{y}</span><extra></extra>"
        )
    elif mode == "Pourcentage":
        return (
            "<span style='color:#333'>"
            "<b>%{fullData.name}</b> : %{y:.2f}%</span><extra></extra>"
        )
    return "Invalid mode"


def get_stacked_bar_chart_figure(data_df: pd.DataFrame, mode=MODES["count"]):
    df = data_df.copy(deep=True)

    # Prepare the data.
    event_types = ["SHOT", "MISS", "GOAL"]
    df_filtered = df[df["event"].isin(event_types)]
    df_filtered["lastEventCategory"] = df_filtered["lastEventCategory"].map(
        event_category_map
    )
    df_filtered = df_filtered[df_filtered["lastEventCategory"].notna()]
    df_filtered["event"] = df_filtered["event"].map(event_types_map)
    df_pivot = (
        df_filtered.groupby(["lastEventCategory", "event"]).size().unstack(fill_value=0)
    )

    df_pivot["Total"] = df_pivot.sum(axis=1)
    if mode == MODES["percent"]:
        # Ordering by the percentage of goals.
        df_pivot["% But"] = df_pivot["But"] / df_pivot["Total"] * 100
        df_pivot = df_pivot.sort_values("% But", ascending=False)
    else:
        # Ordering by the total number of shots.
        df_pivot = df_pivot.sort_values("Total", ascending=False)

    event_types = ["Tir cadré", "Tir raté", "But"]
    df_pivot_percent = df_pivot[event_types].div(df_pivot["Total"], axis=0) * 100

    fig = go.Figure()
    for event in event_types:
        # Select the correct data depending on shot type.
        y_data = (
            df_pivot_percent[event] if mode == MODES["percent"] else df_pivot[event]
        )

        fig.add_trace(
            go.Bar(
                x=df_pivot.index,
                y=y_data,
                name=event,
                marker_color=event_types_colors[event],
                hovertemplate=get_stacked_bar_char_template(mode=mode),
            )
        )

    # Customize the plot layout.
    yaxis_config = {
        "title": (
            "Pourcentage des tirs (%)" if mode == MODES["percent"] else "Nombre de tirs"
        ),
        "range": [0, 100] if mode == MODES["percent"] else None,
    }

    fig.update_layout(
        barmode="stack",
        title={
            "text": "Répartition des types de tirs selon l'événement précédent",
            "x": 0.05,
            "xanchor": "left",
            "y": 0.98,
            "yanchor": "top",
        },
        xaxis_title="Événement précédent",
        yaxis=yaxis_config,
        dragmode=False,
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="white",
            font_color="black",
        ),
        plot_bgcolor="rgba(255,255,255,255)",
        # Positionnement de la légende à droite de la figure
        legend=dict(
            orientation="v",
            x=1.02,  # Légende à droite, hors de l'aire de tracé
            y=1,
            xanchor="left",
            yanchor="top",
        ),
        # On augmente la marge droite pour laisser de la place à la légende
        margin=dict(l=50, r=120, t=120, b=100),
        font=dict(
            # family="'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
            size=16
        ),
        xaxis_fixedrange=True,
        yaxis_fixedrange=True,
    )

    fig.update_xaxes(tickangle=-45, showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor="rgba(200, 200, 200, 0.3)")

    return fig


# Version 2
# 3e visualisation qui répond à la question 5: Comment est-ce que
# l'événement qui précède le tir impacte la chance de marquer?

# x: Les évènements qui précèdent un tir (lastEventCategory).
# y: La probabilité moyenne de convertir un tir à un but (xGoal_percent).
import plotly.express as px


def get_bar_chart_template():
    return "<span style='color:#333'>%{y:.2f}%</span><extra></extra>"


def get_bar_chart_figure(data_df: pd.DataFrame):
    df = data_df.copy(deep=True)  # Deepcopy to not affect the global dataframe.

    # Prepare the data.
    df["lastEventCategory"] = df["lastEventCategory"].map(event_category_map)
    df_agg = df.groupby("lastEventCategory", as_index=False)["xGoal"].mean()
    df_agg["xGoal_percent"] = df_agg["xGoal"] * 100
    df_agg = df_agg.sort_values("xGoal_percent", ascending=False)

    # Create the bar chart.
    fig = px.bar(
        df_agg,
        x="lastEventCategory",
        y="xGoal_percent",
        labels={
            "xGoal_percent": "Probabilité de but (%)",
            "lastEventCategory": "Événement précédent",
        },
        color_discrete_sequence=["#00CC96"],
        hover_data={"xGoal": ":.3f"},
        title="Probabilité de marquer selon l'événement précédent",
    )
    fig.update_traces(hovertemplate=get_bar_chart_template())

    # Customize the plot layout.
    fig.update_layout(
        yaxis=dict(range=[0, 15], ticksuffix="%", gridcolor="lightgrey"),
        dragmode=False,
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="white",
            font_color="black",
        ),
        uniformtext_minsize=8,
        uniformtext_mode="hide",
        xaxis=dict(tickangle=-45),
        plot_bgcolor="rgba(255,255,255,255)",
        title_font=dict(size=22),
        font=dict(size=16),
    )

    fig.update_layout(
        xaxis_fixedrange=True,
        yaxis_fixedrange=True,
    )
    # # Add black outline to each bar for better visibility.
    # fig.update_traces(marker_line_color="black", marker_line_width=1.5, opacity=0.8)

    return fig
