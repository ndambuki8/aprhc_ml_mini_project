import pandas as pd
from datetime import datetime, timedelta

def load_data(filepath: str) -> pd.DataFrame:
    # load the dataset.json dataset as a pandas dataframe
    df = pd.read_json(filepath)
    return df

def transform(df):
    # Parse timestamps
    df["DateJoined"] = pd.to_datetime(df["DateJoined"])

    # Example filter: last 120 days from the dataset max date
    filter_diff_value = df["DateJoined"].max() - pd.Timedelta(days=120)
    df = df[df["DateJoined"] >= filter_diff_value]

    # ✅ Set index for resampling
    df = df.set_index("DateJoined")

    # ✅ Aggregate per day (count of IDs)
    daily_counts = df.resample("D").count()

    # Clean up columns
    daily_counts = daily_counts.rename(columns={"ID": "user_count"}).reset_index()

    return daily_counts

if __name__== '__main__':
    df = load_data("dataset.json")
    daily = transform(df)
    print(daily.head())