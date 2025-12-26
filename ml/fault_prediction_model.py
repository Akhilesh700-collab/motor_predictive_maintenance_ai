import pandas as pd
from sklearn.ensemble import IsolationForest

def predict_fault():
    df = pd.read_csv("data/motor_sensor_data.csv", header=None)
    df.columns = ["temperature", "vibration", "current"]

    model = IsolationForest(contamination=0.15, random_state=42)
    model.fit(df)

    df["prediction"] = model.predict(df)
    latest = df.iloc[-1]

    if latest["prediction"] == -1:
        return "FAULT_PREDICTED", latest.to_dict()
    else:
        return "NORMAL", latest.to_dict()
