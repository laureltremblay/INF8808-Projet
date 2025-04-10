from dash import Input, Output, ctx

from graphs.heatmap import get_heatmap_figure
from graphs.scatter import get_scatter_figure


def register_main_page_callbacks(app, data_df):

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
        filtered_df = data_df
        color_var = "teamCode"

        # Filter by main choice
        if selected_main:
            if main_choice == "team":
                filtered_df = data_df[
                    data_df["teamCode"].isin(
                        [selected_main]
                        if isinstance(selected_main, str)
                        else selected_main
                    )
                ]
            elif main_choice == "player":
                filtered_df = data_df[
                    data_df["shooterName"].isin(
                        [selected_main]
                        if isinstance(selected_main, str)
                        else selected_main
                    )
                ]
                color_var = "shooterName"
            elif main_choice == "position":
                filtered_df = data_df[
                    data_df["playerPositionThatDidEvent"].isin(
                        [selected_main]
                        if isinstance(selected_main, str)
                        else selected_main
                    )
                ]
                color_var = "playerPositionThatDidEvent"
            elif main_choice == "goalie":
                filtered_df = data_df[
                    data_df["goalieNameForShot"].isin(
                        [selected_main]
                        if isinstance(selected_main, str)
                        else selected_main
                    )
                ]
                color_var = "goalieNameForShot"

        # Filter by season choice
        if season_choice == "regular_season":
            filtered_df = filtered_df[filtered_df["isPlayoffGame"] == 0]
        elif season_choice == "playoffs":
            filtered_df = filtered_df[filtered_df["isPlayoffGame"] == 1]

        # Filter by shot type choice
        filtered_df = (
            filtered_df[filtered_df["shotType"] == shot_type_choice]
            if shot_type_choice != "all"
            else filtered_df
        )

        # Filter by period choice
        filtered_df = (
            filtered_df[filtered_df["period"] == int(period_choice)]
            if period_choice != "all"
            else filtered_df
        )

        # Filter by number of players choice
        # using (shootingTeamForwardsOnIce + shootingTeamDefencemenOnIce) and (defendingTeamForwardsOnIce + defendingTeamDefencemenOnIce)
        if n_play_choice == "even_strength":
            filtered_df = filtered_df[
                (
                    filtered_df["shootingTeamForwardsOnIce"]
                    + filtered_df["shootingTeamDefencemenOnIce"]
                )
                == (
                    filtered_df["defendingTeamForwardsOnIce"]
                    + filtered_df["defendingTeamDefencemenOnIce"]
                )
            ]
        elif n_play_choice == "powerplay":
            filtered_df = filtered_df[
                (
                    filtered_df["shootingTeamForwardsOnIce"]
                    + filtered_df["shootingTeamDefencemenOnIce"]
                )
                > (
                    filtered_df["defendingTeamForwardsOnIce"]
                    + filtered_df["defendingTeamDefencemenOnIce"]
                )
            ]
        elif n_play_choice == "short_handed":
            filtered_df = filtered_df[
                (
                    filtered_df["shootingTeamForwardsOnIce"]
                    + filtered_df["shootingTeamDefencemenOnIce"]
                )
                < (
                    filtered_df["defendingTeamForwardsOnIce"]
                    + filtered_df["defendingTeamDefencemenOnIce"]
                )
            ]

        # Filter by defending team avg time on ice
        filtered_df = filtered_df[
            filtered_df["defendingTeamAverageTimeOnIce"] >= toi_choice
        ]

        if ctx.triggered_id == "heatmap-button":
            return (
                get_heatmap_figure(filtered_df),
                "header-button heatmap-button active",
                "header-button scatter-button",
            )
        elif (
            ctx.triggered_id == "scatter-button"
            or scatter_class == "header-button scatter-button active"
        ):
            return (
                get_scatter_figure(filtered_df, color_var),
                "header-button heatmap-button",
                "header-button scatter-button active",
            )
        else:
            return (
                get_heatmap_figure(filtered_df),
                "header-button heatmap-button active",
                "header-button scatter-button",
            )

    @app.callback(
        Output("main-choice-dropdown", "placeholder"),
        Output("main-choice-dropdown", "options"),
        Output("main-choice-dropdown", "disabled"),
        Input("main-choice", "value"),
    )
    def toggle_main_choice_dropdown(selected_value):
        if selected_value == "team":
            options = [
                {"label": team, "value": team}
                for team in sorted(data_df["teamCode"].unique())
            ]
            return "Choisir une équipe", options, False

        elif selected_value == "player":
            options = [
                {"label": player, "value": player}
                for player in sorted(
                    data_df["shooterName"].unique(), key=lambda name: name.split()[-1]
                )
            ]
            return "Choisir un joueur", options, False

        elif selected_value == "position":
            options = [
                {"label": pos, "value": pos}
                for pos in sorted(data_df["playerPositionThatDidEvent"].unique())
            ]
            return "Choisir une position", options, False

        elif selected_value == "goalie":
            options = [
                {"label": goalie, "value": goalie}
                for goalie in sorted(
                    data_df["goalieNameForShot"].unique(),
                    key=lambda name: name.split()[-1],
                )
            ]
            return "Choisir un gardien", options, False

        return "---", [], True
