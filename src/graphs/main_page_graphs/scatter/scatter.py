from assets.team_color import TEAM_COLOR_MAP
import plotly.express as px
import plotly.graph_objects as go
from graphs.main_page_graphs.main_page_common_methods import (
    add_rink_background,
    update_axes,
)
from assets.image_rink_loading import image_uri
from graphs.main_page_graphs.scatter.scatter_layout_methods import (
    update_scatter_hover_template,
    update_scatter_legend,
)


def get_scatter_figure(data_df, color_var: str = "teamCode"):
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

    # Update points to be fully visible but with a special class
    fig.update_traces(
        marker=dict(
            size=10,
            opacity=1,  # Set full opacity
        ),
        selector=dict(mode="markers"),
    )

    # Update axes names
    update_axes(fig)

    # Update legend
    update_scatter_legend(fig, color_var)

    # Update background
    add_rink_background(fig, image_uri)

    # Update hover template
    update_scatter_hover_template(fig)

    return fig
