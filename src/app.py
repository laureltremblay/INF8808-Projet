import dash
from dash import Input, Output, ctx, dcc, html
import plotly.express as px
import pandas as pd
from callbacks.main_page_callbacks import register_main_page_callbacks
from callbacks.pie_charts_callbacks import register_pie_charts_callbacks
from callbacks.stacked_bar_chart_callbacks import register_stacked_bar_chart_callbacks
from pages.advanced_stats_page import get_advanced_content
from pages.main_page import get_main_page_content
from preprocess import basic_filtering
from load_logos import TEAM_LOGOS

app = dash.Dash(__name__)
app.title = "NHL Shot Data 2023-2024"

data_df = pd.read_csv("assets/shots_2023_2024.csv")
non_filtered_data_df = data_df.copy(deep=True)
data_df = basic_filtering(data_df)  # This only keeps the goals!

# Register all callbacks
register_main_page_callbacks(app, data_df)
register_stacked_bar_chart_callbacks(app, non_filtered_data_df)

# Register callbacks for advanced stats page
register_pie_charts_callbacks(app, non_filtered_data_df)

app.layout = html.Div(
    className="content",
    children=[
        dcc.Location(id="url", refresh=False),
        html.Header(
            children=[
                html.Div(
                    className="header-container",
                    children=[
                        html.Button(
                            "Vue d'ensemble",
                            className="header-button active",
                            id="main-page-button",
                        ),
                        html.Button(
                            "Statistiques avancées",
                            className="header-button",
                            id="advanced-button",
                        ),
                    ],
                ),
            ]
        ),
        html.Main(
            id="main-page-content",
            className="chosen-page",
            children=[get_main_page_content(data_df)],  # Initial content
        ),
    ],
)


@app.callback(
    [
        Output("main-page-button", "className"),
        Output("advanced-button", "className"),
        Output("main-page-content", "children"),
    ],
    [Input("main-page-button", "n_clicks"), Input("advanced-button", "n_clicks")],
)
def update_page(*_):
    if ctx.triggered_id == "advanced-button":
        return (
            "header-button",
            "header-button active",
            get_advanced_content(non_filtered_data_df, TEAM_LOGOS),
        )
    return "header-button active", "header-button", get_main_page_content(data_df)


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
