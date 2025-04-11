# 3e visualisation qui répond à la question 5: Comment est-ce que 
# l'événement qui précède le tir impacte la chance de marquer?

# x: Les évènements qui précèdent un tir (lastEventCategory).
# y: La probabilité moyenne de convertir un tir à un but (xGoal_percent).
import plotly.graph_objects as go
import pandas as pd

MODES = dict(count='Count', percent='Percent')
MODE_TO_COLUMN = {MODES['count']: 'ShotCount', MODES['percent']: 'ShotPercent'}

event_category_map = {
    'GIVE': 'Giveaway',
    'SHOT': 'Shot on Goal',
    'HIT': 'Hit',
    'TAKE': 'Takeaway',
    'MISS': 'Missed Shot',
    'FAC': 'Faceoff',
    'BLOCK': 'Blocked Shot',
    'DELPEN': 'Delayed Penalty',
    'STOP': 'Stoppage',
    'CHL': 'Challenge',
    'GOAL': 'Goal'
}

def get_stacked_bar_chart_figure(data_df: pd.DataFrame, mode = MODES['count']):
    df = data_df.copy(deep=True) # Deepcopy to not affect the global dataframe.
    
    # Prepare the data.
    event_types = ['SHOT', 'MISS', 'GOAL']
    df_filtered = df[df['event'].isin(event_types)]
    df_filtered['lastEventCategory'] = df_filtered['lastEventCategory'].map(event_category_map)
    df_pivot = df_filtered.groupby(['lastEventCategory', 'event']).size().unstack(fill_value=0)
    
    # Calculate the total and success columns.
    df_pivot['Total'] = df_pivot.sum(axis=1)
    df_pivot['Success'] = (df_pivot['GOAL'] / df_pivot['Total'] * 100).round(2)
    df_pivot = df_pivot.sort_values('Total', ascending=False)

    # Create the bar stacked chart.
    fig = go.Figure()
    colors = {'SHOT': '#636EFA', 'MISS': '#EF553B', 'GOAL': '#00CC96'}
    
    for event in event_types:
        fig.add_trace(go.Bar(
            x=df_pivot.index,
            y=df_pivot[event],
            name=event,
            marker_color=colors.get(event, 'gray'),
            hoverinfo='y+name',
            textposition='inside'
        ))

    # Customize the plot layout.
    fig.update_layout(
        barmode='stack',
        title='Répartition des types de tirs par événement précédent',
        xaxis_title='Événement précédent',
        yaxis_title='Nombre total de tirs',
        hovermode='x unified',
        plot_bgcolor='white',
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        margin=dict(b=100)  # Marge pour les annotations.
    )
    
    fig.update_xaxes(tickangle=-45)
    
    return fig


# Version 2
# 3e visualisation qui répond à la question 5: Comment est-ce que 
# l'événement qui précède le tir impacte la chance de marquer?

# x: Les évènements qui précèdent un tir (lastEventCategory).
# y: La probabilité moyenne de convertir un tir à un but (xGoal_percent).
import plotly.express as px

def get_bar_chart_figure(data_df: pd.DataFrame):
    df = data_df.copy(deep=True) # Deepcopy to not affect the global dataframe.
    
    # Prepare the data.
    df['lastEventCategory'] = df['lastEventCategory'].map(event_category_map)
    df_agg = df.groupby('lastEventCategory', as_index=False)['xGoal'].mean()
    df_agg['xGoal_percent'] = df_agg['xGoal'] * 100
    df_agg = df_agg.sort_values('xGoal_percent', ascending=False)
    
    # Create the bar chart.
    fig = px.bar(
        df_agg,
        x='lastEventCategory',
        y='xGoal_percent',
        labels={
            'xGoal_percent': 'Probabilité de but (%)',
            'lastEventCategory': 'Événement précédent'
        },
        color_discrete_sequence=['#1f77b4'],
        hover_data={'xGoal': ':.3f'},
        title="Probabilité de marquer selon l'événement précédent"
    )
    
    # Customize the plot layout.
    fig.update_layout(
        yaxis=dict(
            range=[0, 40],
            ticksuffix='%',
            gridcolor='lightgrey'
        ),
        plot_bgcolor='white',
        hovermode='x unified',
        uniformtext_minsize=8,
        uniformtext_mode='hide',
        xaxis=dict(tickangle=-45)
    )
    
    # Add black outline to each bar for better visibility.
    fig.update_traces(
        marker_line_color='black', 
        marker_line_width=1.5,
        opacity=0.8)
    
    return fig
