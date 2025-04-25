from dash import Input, Output, ctx, html


def get_button_style_and_classes(triggered_id):
    base_shots = "header-button stack-button"
    base_team = "header-button team-button"
    base_pie = "header-button piecharts-button"

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

    # Default case for an unexpected triggered_id
    return (
        {"display": "block"},
        {"display": "none"},
        {"display": "none"},
        base_shots + " active",
        base_team,
        base_pie,
    )


def get_tooltip_content(triggered_id):
    tooltip_map = {
        "shots-analysis-button": [
            html.H2("Analyse des buts marqués par évenements précédents"),
            html.P(
                "Cette section permet d'explorer l'impact des événements précédents sur les buts marqués dans la LNH lors de la saison 2023-2024 : "
            ),
            html.Li(
                "La première visualisation présente le nombre de buts marqués en fonction de l'événement précédent, avec la possibilité, grâce au panneau à droite, de transformer ces données en pourcentage de tirs qui ont abouti à un but selon l'événement précédent."
            ),
            html.Br(),
            html.Li(
                "La deuxième visualisation, située plus bas, illustre la probabilité de marquer un but selon l'événement précédent, en se basant sur un modèle qui estime la probabilité qu'un tir soit transformé en but, en prenant en compte plusieurs facteurs."
            ),
            html.Br(),
        ],
        "team-analysis-button": [
            html.H2("Analyse des buts marqués par équipe"),
            html.P(
                "Cette section compare la performance offensive et défensive des équipes de la LNH lors de la saison 2023-2024, permettant de visualiser l'impact d'une équipe sur sa propre capacité à marquer des buts, ainsi que sur la force ou la faiblesse défensive de ses adversaires, ce qui influence la probabilité qu'un tir devienne un but."
            ),
            html.P(
                "Le nuage de points positionne chaque équipe selon les buts marqués (axe Y) et les buts accordés (axe X). Chaque point représente une équipe, et vous pouvez observer les moyennes sur chaque axe. Les différents cadrants indiquent si une équipe excelle dans un aspect spécifique (offensive, défensive, ou dans les deux), ou encore si elle n'excelle dans aucun de ces domaines."
            ),
        ],
        "pie-charts-button": [
            html.H2("Analyse des buts marqués par répartition"),
            html.H3(
                "Cette section permet d'explorer l'impact de la période de jeu, du type de partie jouée, ainsi que de l'emplacement où la partie est jouée sur les buts marqués : "
            ),
            html.Li(
                "La première visualisation (à gauche) présente la proportion de buts marqués selon la période de jeu : 1ère, 2e, 3e période ou prolongation."
            ),
            html.Br(),
            html.Li(
                "La deuxième visualisation (au centre) montre la proportion des buts marqués en fonction du type de match : saison régulière, séries éliminatoires ou les deux."
            ),
            html.Br(),
            html.Li(
                "La troisième visualisation (à droite) illustre la proportion des buts marqués par l'équipe locale par rapport à l'équipe visiteuse."
            ),
            html.Br(),
            html.H3(
                "Des filtres situés à droite permettent de personnaliser l’affichage simultanément pour toutes les visualisations selon les critères suivants :"
            ),
            html.Li(
                "Période : 1ère, 2e, 3e période, prolongation ou toutes les périodes."
            ),
            html.Br(),
            html.Li(
                "Type de match : Saison régulière, séries éliminatoires ou les deux."
            ),
            html.Br(),
            html.Li("Emplacement : Équipe locale, équipe visiteuse ou les deux."),
            html.Br(),
        ],
    }

    # Return the tooltip content or default to shots analysis if no match found
    return tooltip_map.get(triggered_id, tooltip_map["shots-analysis-button"])


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
        triggered_id = ctx.triggered_id or "shots-analysis-button"
        return get_button_style_and_classes(triggered_id)

    @app.callback(
        Output("tooltip-text-content-advanced", "children"),
        Input("shots-analysis-button", "n_clicks"),
        Input("team-analysis-button", "n_clicks"),
        Input("pie-charts-button", "n_clicks"),
    )
    def update_tooltip_text(shots_click, team_click, pie_click):
        triggered_id = ctx.triggered_id or "shots-analysis-button"
        return get_tooltip_content(triggered_id)
