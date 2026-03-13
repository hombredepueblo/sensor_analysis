import pandas as pd

def load_data():

    df = pd.read_csv("data/sensor_data.csv")

    return df


def basic_statistics(df):

    stats = {
        "mean": df["temperature"].mean(),
        "max": df["temperature"].max(),
        "min": df["temperature"].min()
    }

    return stats