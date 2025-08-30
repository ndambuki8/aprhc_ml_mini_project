import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model   import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
from app.etl import load_data, transform


def train_model(df: pd.DataFrame):
    """I shall use a linear regression algorithm to train a model on our dataset"""
    df