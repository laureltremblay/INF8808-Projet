import pandas as pd

def basic_filtering(df):
    """
    Filter out missed shots from the data and NaN values.
    """
    df = df.dropna()
    df = df[df["event"] == "GOAL"]
    return df


def get_scatter_plot_pictogram_data(df):
    """
    Processes the data to build the scatter plot pictogram

    args:
        df: The original shot DataFrame for the 2023-2024 season in the NHL
    returns:
        The dataframe containing the amount of goals scored and allowed by each
        team througout the 2023-2024 season in the NHL
    """
    # We only keep the shots that are goals
    goal_df = basic_filtering(df)

    # We get the amount of goals scored by each team
    teams_goal_scored = (
        goal_df.groupby("teamCode")
        .agg({"goal": "sum"})
        .rename(columns={"goal": "goalsScored"})
        .reset_index()
    )

    # We get the amount of goals scored against each team
    goal_df["teamCode"] = goal_df.apply(
        lambda x: x["awayTeamCode"] if x["team"] == "HOME" else x["homeTeamCode"],
        axis=1,
    )

    teams_goal_scored_against = (
        goal_df.groupby("teamCode")
        .agg({"goal": "sum"})
        .rename(columns={"goal": "goalsScoredAgainst"})
        .reset_index()
    )

    # We combine the two DataFrames to get the goals scored and allowed by each team througout the season
    scatter_plot_data = teams_goal_scored.merge(
        teams_goal_scored_against, "left", "teamCode"
    )

    # We add the category each team belongs to in terms of goals scored and goals allowed
    goals_scored_mean = scatter_plot_data["goalsScored"].mean()
    goals_allowed_mean = scatter_plot_data["goalsScoredAgainst"].mean()

    scatter_plot_data["Category"] = scatter_plot_data.apply(
        lambda x: (
            "Bon offensivement et Bon défensivement"
            if x["goalsScored"] > goals_scored_mean
            and x["goalsScoredAgainst"] <= goals_allowed_mean
            else (
                "Bon offensivement et Mauvais défensivement"
                if x["goalsScored"] > goals_scored_mean
                and x["goalsScoredAgainst"] > goals_allowed_mean
                else (
                    "Mauvais offensivement et Bon défensivement"
                    if x["goalsScored"] <= goals_scored_mean
                    and x["goalsScoredAgainst"] <= goals_allowed_mean
                    else "Mauvais offensivement et Mauvais défensivement"
                )
            )
        ),
        axis=1,
    )

    scatter_plot_data.sort_values(by="teamCode", ascending=True, inplace=True)

    return scatter_plot_data


def get_facet_line_chart_data(df):
    """
    Processes the data to build the facet line chart

    args:
        df: The original shot DataFrame for the 2023-2024 season in the NHL
    returns:
        The dataframe containing the amount of goals scored and allowed by each
        team througout the 2023-2024 season in the NHL
    """
    goal_df = basic_filtering(df)

    # 2 ── figure out who conceded each goal
    goal_df["teamCode"] = goal_df.apply(
        lambda x: x["awayTeamCode"] if x["team"] == "HOME" else x["homeTeamCode"],
        axis=1,
    )

    # 3 ── build two mirrored frames:
    #   • scoring team’s view  → goalsFor = 1, goalsAgainst = 0
    #   • conceding team’s view→ goalsFor = 0, goalsAgainst = 1
    scorer_view = (
        goal_df
        .assign(goalsFor=1, goalsAgainst=0)        # add flags
        .loc[:, ["teamCode", "goalsFor", "goalsAgainst", "game_id", "time"]]
    )

    conceder_view = (
        goal_df
        .assign(teamCode=goal_df["teamCode"],  # flip to opponent
                goalsFor=0,
                goalsAgainst=1)
        .loc[:, ["teamCode", "goalsFor", "goalsAgainst", "game_id", "time"]]
    )

    # 4 ── stack them; each row = one goal from one team’s perspective
    line_plot_data = pd.concat([scorer_view, conceder_view],
                                ignore_index=True)
    
    line_plot_data["time"] = (line_plot_data["time"] // 60).astype(int)

    return line_plot_data