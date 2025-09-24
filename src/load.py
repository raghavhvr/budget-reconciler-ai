import pandas as pd

def load_data(budget_path, actual_path):
    budget = pd.read_csv(budget_path)
    actual = pd.read_csv(actual_path)
    return budget, actual