# TODO: Add preprocessing code here
def basic_filtering(df):
    """
    Filter out missed shots from the data.
    """
    df = df.dropna()
    df = df[df['event'] == 'GOAL']
    return df

