import argparse
from src.load import load_data
from src.reconcile import reconcile_budgets
from src.forecast import forecast_spend
from src.report import export_report

def run(args):
    budget, actual = load_data(args.budget, args.actual)
    reconciled = reconcile_budgets(budget, actual)
    forecast = forecast_spend(reconciled)
    export_report(reconciled, forecast, args.output)
    print(f"✅ Report saved to {args.output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Budget Reconciler")
    parser.add_argument("--budget", default="data/budget_plan.csv")
    parser.add_argument("--actual", default="data/actual_spend.csv")
    parser.add_argument("--output", default="artifacts/report.pptx")
    args = parser.parse_args()
    run(args)