def set_bar_chart_y_axis(fig):
    fig.update_layout(yaxis=dict(range=[0, 15], ticksuffix="%", gridcolor="lightgrey"))


def set_bar_chart_hover_style(fig):
    fig.update_layout(
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="white",
            font_color="black",
        ),
    )


def set_bar_chart_uniform_text(fig):
    fig.update_layout(
        uniformtext_minsize=8,
        uniformtext_mode="hide",
    )


def set_bar_chart_x_axis(fig):
    fig.update_layout(xaxis=dict(tickangle=-45))


def set_bar_chart_background_and_fonts(fig):
    fig.update_layout(
        plot_bgcolor="rgba(255,255,255,255)",
        title_font=dict(size=22),
        font=dict(size=16),
    )


def set_bar_chart_fixed_ranges(fig):
    fig.update_layout(
        xaxis_fixedrange=True,
        yaxis_fixedrange=True,
    )


def set_bar_chart_dragmode(fig):
    fig.update_layout(dragmode=False)


def update_bar_chart_layout(fig):
    set_bar_chart_y_axis(fig)
    set_bar_chart_hover_style(fig)
    set_bar_chart_uniform_text(fig)
    set_bar_chart_x_axis(fig)
    set_bar_chart_background_and_fonts(fig)
    set_bar_chart_fixed_ranges(fig)
    set_bar_chart_dragmode(fig)
