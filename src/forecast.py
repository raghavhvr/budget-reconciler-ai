import pandas as pd
from statsmodels.tsa.api import SimpleExpSmoothing

def forecast_spend(df: pd.DataFrame) -> pd.DataFrame:
    # naive forecast using exponential smoothing
    forecast = {}
    for _, row in df.iterrows():
        series = pd.Series([row["Amount_budget"], row["Amount_actual"]])
        model = SimpleExpSmoothing(series).fit()
        forecast[row["Category"]] = model.forecast(1).iloc[0]
    return pd.DataFrame(forecast.items(), columns=["Category", "Forecast_EOY"])