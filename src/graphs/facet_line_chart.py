#period
#time
#teamCode
#game_id
#goal (0 or 1)
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from preprocess import get_facet_line_chart_data

def get_facet_line_figure(df):
    df = get_facet_line_chart_data(df)
    df["delta"] = df["goalsFor"] - df["goalsAgainst"]

    # STEP 3 ── Cumulative diff within each game & team ────────────
    df = (
        df
        .sort_values(["game_id", "teamCode", "time"])
        .assign(
            cumDiff=lambda d: (
                d.groupby(["game_id", "teamCode"])["delta"]
                .cumsum()
            )
        )
    )

    # STEP 4 ── Average across games at each second ────────────────
    avg_curve = (
        df
        .groupby(["teamCode", "time"])["cumDiff"]
        .mean()
        .reset_index()
    )

    # Optional: convert seconds → minutes for prettier ticks
    avg_curve["gameMin"] = avg_curve["time"] / 60

    # ──────────────────────────────────────────────────────────────
    #  PLOT: one small‑multiple line chart per team
    # ──────────────────────────────────────────────────────────────
    teams = sorted(avg_curve["teamCode"].unique())
    n_teams  = len(teams)
    n_cols   = 6                              # 6×6 grid (fits 32 teams)
    n_rows   = int(np.ceil(n_teams / n_cols))

    fig = make_subplots(rows=n_rows, cols=n_cols,
                        subplot_titles=teams,
                        shared_xaxes=True, shared_yaxes=True,
                        horizontal_spacing=0.02, vertical_spacing=0.04)

    row = col = 1
    for team in teams:
        team_df = avg_curve[avg_curve["teamCode"] == team]
        fig.add_trace(
            go.Scatter(
                x=team_df["gameMin"],
                y=team_df["cumDiff"],
                mode="lines",
                line=dict(width=2),
                name=team,
                showlegend=False
            ),
            row=row, col=col
        )
        col += 1
        if col > n_cols:
            col = 1
            row += 1

    fig.update_xaxes(title_text="Game Time (min)", dtick=10, zeroline=True, zerolinewidth=1)
    fig.update_yaxes(title_text="Average Score Differential", zeroline=True, zerolinewidth=1)
    fig.update_layout(
        height=230 * n_rows, width=225 * n_cols,
        title_text="Average Score Difference – 2024‑25 Season",
        margin=dict(t=80, l=40, r=40, b=40)
    )

    return fig