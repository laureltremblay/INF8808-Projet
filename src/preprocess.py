# TODO: Add preprocessing code here
def basic_filtering(df):
    """
    Filter out missed shots from the data.
    """
    df = df.dropna()
    df = df[df['event'] == 'GOAL']
    return df

def abs_xCord(df):
    """
    Take the absolute value of the xCord column.
    """
    df['xCord'] = df['xCord'].apply(lambda x: abs(x))
    return df
