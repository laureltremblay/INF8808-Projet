def update_bar_chart_layout(fig):
    fig.update_layout(
        yaxis=dict(range=[0, 15], ticksuffix="%", gridcolor="lightgrey"),
        dragmode=False,
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="white",
            font_color="black",
        ),
        uniformtext_minsize=8,
        uniformtext_mode="hide",
        xaxis=dict(tickangle=-45),
        plot_bgcolor="rgba(255,255,255,255)",
        title_font=dict(size=22),
        font=dict(size=16),
    )

    fig.update_layout(
        xaxis_fixedrange=True,
        yaxis_fixedrange=True,
    )
