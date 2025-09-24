import pandas as pd

def reconcile_budgets(budget: pd.DataFrame, actual: pd.DataFrame) -> pd.DataFrame:
    df = budget.merge(actual, on="Category", suffixes=("_budget", "_actual"))
    df["Variance"] = df["Amount_actual"] - df["Amount_budget"]
    df["Pct_Variance"] = df["Variance"] / df["Amount_budget"] * 100
    df["Flag"] = df["Pct_Variance"].apply(lambda x: "⚠️ Overspend" if x > 20 else "OK")
    return df