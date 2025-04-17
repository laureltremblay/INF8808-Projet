import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

def get_sunburst_figure(data_df: pd.DataFrame):
    required_cols = {"lastEventCategory", "event", "shotType", "goal"}
    if not required_cols.issubset(data_df.columns):
        return px.sunburst(title="Colonnes manquantes pour le Sunburst")

    # Filtrer pour n'inclure que les tirs ayant abouti à un but
    data_goals = data_df[data_df["goal"] == 1]
    
    # Agréger les données selon la hiérarchie désirée
    agg = data_goals.groupby(["lastEventCategory", "event", "shotType"]).size().reset_index(name="count")
    
    fig = px.sunburst(
        agg,
        path=["lastEventCategory", "event", "shotType"],
        values="count",
        title="Séquences d'événements pré-buts"
    )
    
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig