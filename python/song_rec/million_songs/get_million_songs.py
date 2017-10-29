import pandas as pd


# Generic function that calls specific function on each element in dataframe.
def apply_each_line(func):
    df = get_df_from_csv()
    songs = df[df.Title]

    for i in len(df[df.SongNumber]):
        func(songs[i])


# Warning: eventual trouble on windows
def get_df_from_csv():
    df = pd.read_csv('../../../data/SongCSV.csv', header=0)

    return df
