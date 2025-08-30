import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model   import LinearRegression
from sklearn.metrics import mean_squared_error, root_mean_squared_error
import joblib
from etl import load_data, transform


def train_model(df: pd.DataFrame):
    """I shall use a linear regression algorithm to train a model on our dataset"""
    df['Day'] = pd.to_datetime(df['DateJoined'])
    df['DayOfWeek'] = df['Day'].dt.day_of_week

    X = df[['DayOfWeek']]
    y = df['user_count']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    rmse = root_mean_squared_error(y_test, preds)

    print(f"Model successfully trained.\n RMSE {rmse:.4f}\n MSE {mse:.4f}")

    # Saving the model
    joblib.dump(model, "models/trained_model.joblib")
    return model

if __name__== "__main__":
    df = load_data("dataset.json")
    daily = transform(df)
    train_model(daily)