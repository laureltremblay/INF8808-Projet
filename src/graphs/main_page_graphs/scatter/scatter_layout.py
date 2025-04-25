from graphs.main_page_graphs.main_page_common_layout import (
    add_rink_background,
    update_axes,
)


def update_scatter_legend(fig, color_var):
    """
    Updates the legend title of the scatter plot figure based on the current grouping variable.
    """
    legend_title = "Équipes"  # Default legend title

    # Set the appropriate legend title based on the color variable
    if color_var == "shooterName":
        legend_title = "Joueurs"
    elif color_var == "goalieNameForShot":
        legend_title = "Gardiens"
    elif color_var == "playerPositionThatDidEvent":
        legend_title = "Positions"

    # Update the legend layout with fixed click behavior and font size
    fig.update_layout(
        legend=dict(
            itemclick=False,
            itemdoubleclick=False,
            title=legend_title,
            title_font=dict(size=14),
        ),
    )


def update_scatter_hover_template(fig):
    """
    Updates the hover template for each point in the scatter plot.
    Provides detailed information using the customdata attribute.
    """
    # Custom hover template string using indices of customdata
    fig.update_traces(
        hovertemplate=(
            "Tireur: %{customdata[0]}<br>"
            "Équipe: %{customdata[1]}<br>"
            "Coordonnée X: %{customdata[2]} pieds<br>"
            "Coordonnée Y: %{customdata[3]} pieds<br>"
            "Distance du tir: %{customdata[4]:.2f} pieds<br>"
            "Période: %{customdata[5]}<br>"
            "Position: %{customdata[6]}<br>"
            "Lancer: %{customdata[7]}<br>"
            "Type de tir: %{customdata[8]}<br>"
            "Temps moyen sur la glace de l'équipe adverse: %{customdata[9]:.2f}s<br>"
            "Gardien: %{customdata[10]}<br>"
            "<extra></extra>"
        ),
    )


def update_scatter_layout(fig, color_var, image_uri):
    update_axes(fig)
    update_scatter_legend(fig, color_var)
    add_rink_background(fig, image_uri)
    update_scatter_hover_template(fig)
