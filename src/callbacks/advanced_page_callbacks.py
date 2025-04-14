from dash import Input, Output, State, ctx

def register_advanced_page_callbacks(app):
    @app.callback(
        [
            Output("shots-analysis-section", "style"),
            Output("team-analysis-section", "style"),
            Output("pie-charts-section", "style"),
            Output("shots-analysis-button", "className"),
            Output("team-analysis-button", "className"),
            Output("pie-charts-button", "className"),
        ],
        [
            Input("shots-analysis-button", "n_clicks"),
            Input("team-analysis-button", "n_clicks"),
            Input("pie-charts-button", "n_clicks"),
        ],
    )
    def switch_advanced_tabs(shots_click, team_click, pie_click):
        triggered_id = ctx.triggered_id

        # Remplace "scatter-button" par "stack-button" 
        # et "heatmap-button" par "team-button"
        base_shots = "header-button stack-button"   
        base_team = "header-button team-button"
        base_pie = "header-button piecharts-button"

        # Par défaut, on affiche "Par événement"
        if not triggered_id:
            return (
                {"display": "block"},
                {"display": "none"},
                {"display": "none"},
                base_shots + " active",
                base_team,
                base_pie,
            )

        if triggered_id == "shots-analysis-button":
            return (
                {"display": "block"},
                {"display": "none"},
                {"display": "none"},
                base_shots + " active",
                base_team,
                base_pie,
            )
        elif triggered_id == "team-analysis-button":
            return (
                {"display": "none"},
                {"display": "block"},
                {"display": "none"},
                base_shots,
                base_team + " active",
                base_pie,
            )
        elif triggered_id == "pie-charts-button":
            return (
                {"display": "none"},
                {"display": "none"},
                {"display": "block"},
                base_shots,
                base_team,
                base_pie + " active",
            )

        # Au cas où
        return (
            {"display": "block"},
            {"display": "none"},
            {"display": "none"},
            base_shots + " active",
            base_team,
            base_pie,
        )


    @app.callback(
        Output("scatter-plot-pictogram-graph", "figure"),
        Input("scatter-plot-pictogram-graph", "hoverData"),
        State("scatter-plot-pictogram-graph", "figure"),
        prevent_initial_call=True
    )
    def update_image_opacity_on_hover(hoverData, fig):
        if not fig or "layout" not in fig or "images" not in fig["layout"]:
            return fig

        # No hover: reset all images to default opacity
        if not hoverData:
            for img in fig["layout"]["images"]:
                # Flicker fix: avoid reloading the image
                src = img["source"]
                img["source"] = ""
                img["source"] = src
                img["opacity"] = 1
                img["layer"] = "above"
            return fig

        # Hovered team name from customdata
        hovered_team = None
        if "points" in hoverData:
            point = hoverData["points"][0]
            if "customdata" in point and len(point["customdata"]) > 0:
                hovered_team = point["customdata"][0]

        # Update image opacities
        for img in fig["layout"]["images"]:
            src = img["source"]
            img["source"] = ""
            img["source"] = src

            if "name" in img and img["name"] == hovered_team:
                img["opacity"] = 1.0
                img["layer"] = "above"
            else:
                img["opacity"] = 0.5
                img["layer"] = "below"

        return fig



