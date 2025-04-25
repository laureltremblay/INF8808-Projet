from dash import html, dcc

from graphs.advanced_stats_page_graphs.bar_charts.stacked_bar_chart.stacked_bar_chart import get_stacked_bar_chart_figure

def get_stacked_bar_chart_layout(data_df):
    return html.Div(
        className="stacked-section",
        children=[
            html.Div(
                className="graph stacked-graph flex-row",  # On applique .graph pour le fond translucide + survol
                children=[
                    html.Div(
                        className="flex-graph-area",
                        children=[
                            dcc.Graph(
                                figure=get_stacked_bar_chart_figure(data_df),
                                id="q5-stacked-bar-chart-graph",
                                config=dict(
                                    scrollZoom=False,
                                    showTips=False,
                                    showAxisDragHandles=False,
                                    doubleClick=False,
                                    displayModeBar=False,
                                ),
                                style={"width": "100%", "height": "100%"},
                            )
                        ],
                        style={"flex": "4"}
                    ),
                ]
            ),
        ]
    )
    
def update_stacked_bar_chart_layout(fig, y_axis_config):
    fig.update_layout(
        barmode="stack",
        title={
            "text": "Répartition des types de tirs selon l'événement précédent",
            "x": 0.05,
            "xanchor": "left",
            "y": 0.98,
            "yanchor": "top",
        },
        xaxis_title="Événement précédent",
        yaxis=y_axis_config,
        dragmode=False,
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="white",
            font_color="black",
        ),
        plot_bgcolor="rgba(255,255,255,255)",
        
        # Legend on the right.
        legend=dict(
            orientation="v",
            x=1.02,
            y=1,
            xanchor="left",
            yanchor="top",
        ),
        margin=dict(l=50, r=120, t=120, b=100),
        font=dict(
            # family="'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
            size=16
        ),
        xaxis_fixedrange=True,
        yaxis_fixedrange=True,
    )

    fig.update_xaxes(tickangle=-45, showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor="rgba(200, 200, 200, 0.3)")
