from graphs.main_page_graphs.main_page_common_layout import (
    add_rink_background,
    update_axes,
)


def update_heatmap_layout(fig, image_uri):
    update_axes(fig)
    add_rink_background(fig, image_uri)
