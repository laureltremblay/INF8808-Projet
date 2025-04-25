from assets.event_types import event_category_map, event_types_map, MODES


def basic_filtering(df):
    """
    Filter out missed shots from the data and NaN values.
    """
    df = df.dropna()
    df = df[df["event"] == "GOAL"]
    return df


def get_stacked_bar_chart_data(df, mode):
    # Prepare the data.
    event_types = ["SHOT", "MISS", "GOAL"]
    df_filtered = df[df["event"].isin(event_types)]
    df_filtered["lastEventCategory"] = df_filtered["lastEventCategory"].map(
        event_category_map
    )
    df_filtered = df_filtered[df_filtered["lastEventCategory"].notna()]
    df_filtered["event"] = df_filtered["event"].map(event_types_map)
    processed_df = (
        df_filtered.groupby(["lastEventCategory", "event"]).size().unstack(fill_value=0)
    )

    processed_df["Total"] = processed_df.sum(axis=1)
    if mode == MODES["percent"]:
        # Ordering by the percentage of goals.
        processed_df["% But"] = processed_df["But"] / processed_df["Total"] * 100
        processed_df = processed_df.sort_values("% But", ascending=False)
    else:
        # Ordering by the total number of shots.
        processed_df = processed_df.sort_values("Total", ascending=False)

    event_types = ["Tir cadré", "Tir raté", "But"]
    processed_percent_df = (
        processed_df[event_types].div(processed_df["Total"], axis=0) * 100
    )

    return processed_df, processed_percent_df


def get_bar_chart_data(df):
    # Prepare the data.
    df["lastEventCategory"] = df["lastEventCategory"].map(event_category_map)
    processed_df = df.groupby("lastEventCategory", as_index=False)["xGoal"].mean()
    processed_df["xGoal_percent"] = processed_df["xGoal"] * 100
    processed_df = processed_df.sort_values("xGoal_percent", ascending=False)

    return processed_df


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
