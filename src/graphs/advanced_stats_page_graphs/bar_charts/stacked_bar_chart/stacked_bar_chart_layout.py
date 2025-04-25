def get_stacked_bar_char_template(mode):

    if mode == "Quantité":
        return (
            "<span style='color:#333'>"
            "<b>%{fullData.name}</b> : %{y}</span><extra></extra>"
        )
    elif mode == "Pourcentage":
        return (
            "<span style='color:#333'>"
            "<b>%{fullData.name}</b> : %{y:.2f}%</span><extra></extra>"
        )
    return "Invalid mode"


def set_title(fig):
    fig.update_layout(
        title=dict(
            text="Répartition des types de tirs selon l'événement précédent",
            x=0.05,
            xanchor="left",
            y=0.98,
            yanchor="top",
        )
    )


def set_legend(fig):
    fig.update_layout(
        legend=dict(
            orientation="v",
            x=1.02,
            y=1,
            xanchor="left",
            yanchor="top",
        )
    )


def set_hover_style(fig):
    fig.update_layout(
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="white",
            font_color="black",
        ),
    )


def set_background_and_margin(fig):
    fig.update_layout(
        plot_bgcolor="rgba(255,255,255,255)",
        margin=dict(l=50, r=120, t=120, b=100),
    )


def set_font(fig):
    fig.update_layout(font=dict(size=16))


def set_axes_labels_and_modes(fig, y_axis_config):
    fig.update_layout(
        barmode="stack",
        dragmode=False,
        xaxis_title="Événement précédent",
        yaxis=y_axis_config,
    )


def set_fixed_ranges(fig):
    fig.update_layout(
        xaxis_fixedrange=True,
        yaxis_fixedrange=True,
    )


def update_x_axis(fig):
    fig.update_xaxes(
        tickangle=-45,
        showgrid=False,
    )


def update_y_axis(fig):
    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(200, 200, 200, 0.3)",
    )


def update_stacked_bar_chart_layout(fig, y_axis_config):
    set_title(fig)
    set_legend(fig)
    set_hover_style(fig)
    set_background_and_margin(fig)
    set_font(fig)
    set_axes_labels_and_modes(fig, y_axis_config)
    set_fixed_ranges(fig)
    update_x_axis(fig)
    update_y_axis(fig)
