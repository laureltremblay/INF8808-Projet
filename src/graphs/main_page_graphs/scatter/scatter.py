from assets.team_color import TEAM_COLOR_MAP
import plotly.express as px
from assets.image_rink_loading import image_uri
from graphs.main_page_graphs.scatter.scatter_layout import (
    update_scatter_layout,
)


def get_scatter_figure(data_df, color_var):
    # Create the base scatter plot with full opacity
    fig = px.scatter(
        data_df,
        x="xCordAdjusted",
        y="yCordAdjusted",
        color=color_var,
        color_discrete_map=TEAM_COLOR_MAP if color_var == "teamCode" else None,
        custom_data=[
            "shooterName",
            "teamCode",
            "xCordAdjusted",
            "yCordAdjusted",
            "shotDistance",
            "period",
            "playerPositionThatDidEvent",
            "shooterLeftRight",
            "shotType",
            "defendingTeamAverageTimeOnIce",
            "goalieNameForShot",
        ],
    )

    # Update points to be bigger
    fig.update_traces(
        marker=dict(
            size=10,
            opacity=1,
        ),
        selector=dict(mode="markers"),
    )

    update_scatter_layout(fig, color_var, image_uri)

    return fig
