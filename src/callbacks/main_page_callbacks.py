from dash import Input, Output, ctx
from graphs.main_page_graphs.heatmap.heatmap import get_heatmap_figure
from graphs.main_page_graphs.scatter.scatter import get_scatter_figure


def register_main_page_callbacks(app, data_df):
    """
    Registers the main callbacks for the dashboard.
    These control the main graph (scatter or heatmap) and the main-choice dropdown behavior.
    """

    def to_list(val):
        """Ensures the input is a list, used for filtering with .isin()."""
        return [val] if isinstance(val, str) else val

    def filter_by_main_choice(df, main_choice, selected_main):
        """
        Filters the dataframe based on the main choice (team, player, position, or goalie).
        Returns both the filtered dataframe and the column used for coloring in the scatter plot.
        """
        if not selected_main:
            return df, "teamCode"

        column_map = {
            "team": "teamCode",
            "player": "shooterName",
            "position": "playerPositionThatDidEvent",
            "goalie": "goalieNameForShot",
        }

        col = column_map.get(main_choice)
        if col:
            return df[df[col].isin(to_list(selected_main))], col

        return df, "teamCode"

    def filter_by_season(df, season_choice):
        """Filters the data to only include regular season or playoff games."""
        if season_choice == "regular_season":
            return df[df["isPlayoffGame"] == 0]
        if season_choice == "playoffs":
            return df[df["isPlayoffGame"] == 1]
        return df

    def filter_by_shot_type(df, shot_type_choice):
        """Filters the data by shot type, unless 'all' is selected."""
        return (
            df if shot_type_choice == "all" else df[df["shotType"] == shot_type_choice]
        )

    def filter_by_period(df, period_choice):
        """Filters the data by game period (1, 2, 3, etc.) unless 'all' is selected."""
        return df if period_choice == "all" else df[df["period"] == int(period_choice)]

    def filter_by_strength(df, n_play_choice):
        """
        Filters the data based on the number of players on the ice (even strength, power play, or short-handed).
        """
        shooting_total = (
            df["shootingTeamForwardsOnIce"] + df["shootingTeamDefencemenOnIce"]
        )
        defending_total = (
            df["defendingTeamForwardsOnIce"] + df["defendingTeamDefencemenOnIce"]
        )

        if n_play_choice == "even_strength":
            return df[shooting_total == defending_total]
        if n_play_choice == "powerplay":
            return df[shooting_total > defending_total]
        if n_play_choice == "short_handed":
            return df[shooting_total < defending_total]
        return df

    def filter_by_toi(df, toi_choice):
        """Filters the data where the defending team's average TOI exceeds the selected threshold."""
        return df[df["defendingTeamAverageTimeOnIce"] >= toi_choice]

    @app.callback(
        Output("main-graph", "figure"),
        Output("heatmap-button", "className"),
        Output("scatter-button", "className"),
        Input("scatter-button", "n_clicks"),
        Input("scatter-button", "className"),
        Input("heatmap-button", "n_clicks"),
        Input("main-choice", "value"),
        Input("main-choice-dropdown", "value"),
        Input("season-choice", "value"),
        Input("shot-type-choice", "value"),
        Input("period-choice", "value"),
        Input("num-players-choice", "value"),
        Input("defending-toi-slider", "value"),
    )
    def update_figure_and_main_choices(
        scatter_clicks,
        scatter_class,
        heatmap_clicks,
        main_choice,
        selected_main,
        season_choice,
        shot_type_choice,
        period_choice,
        n_play_choice,
        toi_choice,
    ):
        """
        Callback to update the main graph (heatmap or scatter) and button states,
        based on the currently selected filters and triggered input.
        """

        # Apply all filters step-by-step
        df, color_var = filter_by_main_choice(data_df, main_choice, selected_main)
        df = filter_by_season(df, season_choice)
        df = filter_by_shot_type(df, shot_type_choice)
        df = filter_by_period(df, period_choice)
        df = filter_by_strength(df, n_play_choice)
        df = filter_by_toi(df, toi_choice)

        # Determine which button triggered the callback
        triggered = ctx.triggered_id
        if triggered == "heatmap-button":
            return (
                get_heatmap_figure(df),
                "graph-button heatmap-button active",
                "graph-button scatter-button",
            )
        elif (
            triggered == "scatter-button"
            or scatter_class == "header-button scatter-button active"
        ):
            return (
                get_scatter_figure(df, color_var),
                "graph-button heatmap-button",
                "graph-button scatter-button active",
            )

    @app.callback(
        Output("main-choice-dropdown", "placeholder"),
        Output("main-choice-dropdown", "options"),
        Output("main-choice-dropdown", "disabled"),
        Input("main-choice", "value"),
    )
    def toggle_main_choice_dropdown(selected_value):
        """
        Updates the dropdown options dynamically based on the selected main choice (team/player/etc.).
        Disables the dropdown if the choice is invalid or empty.
        """

        def get_sorted_options(col, sort_by_last_name=False):
            """Returns sorted dropdown options from a column."""
            values = data_df[col].unique()
            if sort_by_last_name:
                values = sorted(values, key=lambda name: name.split()[-1])
            else:
                values = sorted(values)
            return [{"label": val, "value": val} for val in values]

        # Config for placeholder text and column names
        placeholders = {
            "team": "Choisir une équipe",
            "player": "Choisir un joueur",
            "position": "Choisir une position",
            "goalie": "Choisir un gardien",
        }

        columns = {
            "team": "teamCode",
            "player": "shooterName",
            "position": "playerPositionThatDidEvent",
            "goalie": "goalieNameForShot",
        }

        if selected_value in columns:
            col = columns[selected_value]
            sort_last = selected_value in ["player", "goalie"]
            return (
                placeholders[selected_value],
                get_sorted_options(col, sort_last),
                False,
            )

        return "---", [], True
