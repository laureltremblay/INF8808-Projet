'''
4e visualisation qui répond à :
Question cible 8 : Y avait-il des équipes plus efficaces pour marquer des buts en 2023-2024?
la question cible 9 : Y avait-il des équipes plus efficaces pour empêcher des buts en 2023-2024?
'''
import plotly.express as px
from PIL import Image
from pathlib import Path
from preprocess import get_scatter_plot_pictogram_data

def get_scatter_plot_pictogram_figure(goal_df):
    '''
    Processes the data to build the scatter plot pictogram

    args:
        df: The original shot DataFrame for the 2023-2024 season in the NHL
    returns:
        The scatter plot with pictograms instead of points representing the amount of goals scored
        and allowed by each team during the 2023-2024 NHL season
    '''
    
    # We get the preprocessed data to create the figure
    preprocessed_df = get_scatter_plot_pictogram_data(goal_df)
    
    # We create the scatter plot
    fig = px.scatter(preprocessed_df, x = 'goalsScoredAgainst', y = 'goalsScored')
    fig.update_layout(width = 900,
                      height = 900,
                      title = 'Amount of Goals Scored and Allowed by Each NHL Team in 2023-2024',
                      xaxis_title = 'Goals Allowed',
                      yaxis_title = 'Goal Scored',
                      plot_bgcolor = 'white',
                      xaxis = dict(
                          gridcolor = 'lightgray',
                          zerolinecolor = 'black',
                          showline = True,
                          linecolor = 'black',
                          range = [184, 304], # Change min and max
                          dtick = 10
                      ),
                      yaxis = dict(
                        gridcolor = 'lightgray',
                        zerolinecolor = 'black',
                        showline = True,
                        linecolor = 'black',
                        range = [128, 360], # Change min and max
                        dtick = 25                     
                        )
                    )
    
    # We change each point of the scatter plot to the team's logo
    images_path = Path(__file__).parent.parent / "assets" / "NHL Logos"
    image_paths = sorted(images_path.glob("*.png"))
    
    size_dictionnary = {
                        'ANA': {'sizex' : 13, 'sizey' : 13},
                        'ARI': {'sizex' : 13, 'sizey' : 13},
                        'BOS': {'sizex' : 12, 'sizey' : 12},
                        'BUF': {'sizex' : 12, 'sizey' : 12},
                        'CAR': {'sizex' : 19, 'sizey' : 19},
                        'CBJ': {'sizex' : 12, 'sizey' : 12},
                        'CGY': {'sizex' : 12, 'sizey' : 12},
                        'CHI': {'sizex' : 15, 'sizey' : 15},
                        'COL': {'sizex' : 15, 'sizey' : 15},
                        'DAL': {'sizex' : 13, 'sizey' : 13},
                        'DET': {'sizex' : 18, 'sizey' : 18},
                        'EDM': {'sizex' : 13, 'sizey' : 13},
                        'FLA': {'sizex' : 15, 'sizey' : 15},
                        'LAK': {'sizex' : 15, 'sizey' : 15},
                        'MIN': {'sizex' : 18, 'sizey' : 18},
                        'MTL': {'sizex' : 11, 'sizey' : 11},
                        'NJD': {'sizex' : 13, 'sizey' : 13},
                        'NSH': {'sizex' : 18, 'sizey' : 18},
                        'NYI': {'sizex' : 14, 'sizey' : 14},
                        'NYR': {'sizex' : 15, 'sizey' : 15}, 
                        'OTT': {'sizex' : 13, 'sizey' : 13},
                        'PHI': {'sizex' : 16, 'sizey' : 16},
                        'PIT': {'sizex' : 16, 'sizey' : 16},
                        'SEA': {'sizex' : 13, 'sizey' : 13},
                        'SJS': {'sizex' : 17, 'sizey' : 17},   
                        'STL': {'sizex' : 12, 'sizey' : 12},
                        'TBL': {'sizex' : 13, 'sizey' : 13},
                        'TOR': {'sizex' : 15, 'sizey' : 15},
                        'VAN': {'sizex' : 13, 'sizey' : 13},
                        'VGK': {'sizex' : 15, 'sizey' : 15},
                        'WPG': {'sizex' : 15, 'sizey' : 15},   
                        'WSH': {'sizex' : 20, 'sizey' : 20},           
                        }
    
    for x, y, img_path in zip(preprocessed_df['goalsScoredAgainst'], preprocessed_df['goalsScored'], image_paths):
        
        team_name = Path(img_path).stem
        
        fig.add_layout_image(
            x = x,
            y = y,
            source = Image.open(img_path),
            xref = "x",
            yref = "y",
            sizex = size_dictionnary[team_name]['sizex'],
            sizey = size_dictionnary[team_name]['sizey'],
            xanchor = "center",
            yanchor = "middle",
        )
        
    # We add the average line of goals allowed
    fig.add_shape(
    type = "line",
    x0 = (preprocessed_df['goalsScoredAgainst']).mean(),
    x1 = (preprocessed_df['goalsScoredAgainst']).mean(),
    y0 = 500,
    y1 = 0,
    line = dict(
                color = "red",
                width = 2,
                dash = "dot"
            ),
     layer = "below"
    )
    
    # We add the average line of goals scored
    fig.add_shape(
    type = "line",
    x0 = 0,
    x1 = 500,
    y0 = (preprocessed_df['goalsScored']).mean(),
    y1 = (preprocessed_df['goalsScored']).mean(),
    line = dict(
                color = "blue",
                width = 2,
                dash = "dot"
            ),
     layer = "below"
    )
    
    # We add anotations for each section of the scatter plot
    
    # We add the legend
    
    # We add hovertemplate
    
    
    return fig