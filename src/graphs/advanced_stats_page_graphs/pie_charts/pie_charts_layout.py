def set_pie_chart_title(fig):
    fig.update_layout(
        title_text="Répartition des Buts",
        title_x=0.5,
        title_font=dict(size=24, family="Arial, sans-serif"),
    )


def set_pie_chart_legend(fig):
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            xanchor="center",
            x=0.5,
            itemclick=False,
            itemdoubleclick=False,
        )
    )


def set_pie_chart_layout_style(fig):
    fig.update_layout(
        autosize=True,
        margin=dict(l=10, r=10, t=80, b=50),
        transition=dict(duration=500),
    )


def update_pie_chart_layout(fig):
    set_pie_chart_title(fig)
    set_pie_chart_legend(fig)
    set_pie_chart_layout_style(fig)
