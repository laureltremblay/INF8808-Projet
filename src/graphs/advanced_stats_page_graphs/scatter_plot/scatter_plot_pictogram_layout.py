def get_layout_title():
    return dict(
        text="Comparaison des buts marqués et accordés par équipe en 2023-2024",
        font=dict(size=22),
        x=0.5,
        xanchor="center",
    )


def get_xaxis_config():
    return dict(
        title="Buts accordés",
        gridcolor="gray",
        zerolinecolor="gray",
        showline=True,
        linecolor="gray",
        range=[184, 304],
        dtick=10,
    )


def get_yaxis_config():
    return dict(
        title="Buts marqués",
        gridcolor="gray",
        zerolinecolor="gray",
        showline=True,
        linecolor="gray",
        range=[128, 360],
        dtick=25,
    )


def update_scatter_plot_pictogram_layout(fig):
    fig.update_layout(
        width=1050,
        height=800,
        dragmode=False,
        title=get_layout_title(),
        xaxis=get_xaxis_config(),
        yaxis=get_yaxis_config(),
        plot_bgcolor="rgba(255,255,255,255)",
    )
