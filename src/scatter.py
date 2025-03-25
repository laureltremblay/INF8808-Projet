import plotly.express as px

def get_scatter_figure(data_df):
    fig = px.scatter(data_df, x='xCord', y='yCord', color='teamCode')
    fig.update_traces(marker=dict(size=5))
    fig.update_layout(showlegend=False)
    return fig
