# 💰 AI Budget Reconciler

[![CI](https://github.com/raghavhvr/budget-reconciler-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/raghavhvr/budget-reconciler-ai/actions/workflows/ci.yml)
[![Weekly Reconcile](https://github.com/raghavhvr/budget-reconciler-ai/actions/workflows/weekly.yml/badge.svg)](https://github.com/raghavhvr/budget-reconciler-ai/actions/workflows/weekly.yml)

AI-assisted tool to reconcile **planned budgets vs actual spend**.  
Automatically highlights overspend, forecasts end-of-year totals, and generates one-pager PPT reports for leadership reviews.  

---

## 🚀 Demo

### CLI
```powershell
python main.py --budget data/budget_plan.csv --actual data/actual_spend.csv --output artifacts/report.pptx
```

### Streamlit App
```powershell
streamlit run app_streamlit.py
```

Artifacts are saved to artifacts/:

report.pptx – one-pager reconciliation report

reconciled.csv – variance + anomaly table

## 📊 Example Output

### Variance summary

| Category   | Budget | Actual | Variance | Pct\_Variance | Flag         |
| ---------- | ------ | ------ | -------- | ------------- | ------------ |
| Marketing  | 100000 | 120000 | 20000    | 20%           | ⚠️ Overspend |
| HR         | 50000  | 45000  | -5000    | -10%          | OK           |
| IT         | 75000  | 82000  | 7000     | 9%            | OK           |
| Operations | 60000  | 70000  | 10000    | 17%           | OK           |


Overspend flagged when variance > 20% of budget. Threshold configurable in src/reconcile.py.

PPT Export

The auto-generated slide contains:

Title: Budget Reconciliation Report

Table: Budget, Actual, Variance, Flags, and Forecast EOY

## 🧰 Tech Stack

Data: CSV files (budget_plan, actual_spend)

Processing: Pandas (variance + anomaly detection)

Forecasting: Statsmodels (SimpleExponentialSmoothing)

Reports: python-pptx (PPTX export)

Visualization: Streamlit + Plotly dashboard

Automation: GitHub Actions (weekly refresh + CI)

## 📦 Project Structure
```yaml
budget-reconciler-ai/
├─ data/
│  ├─ budget_plan.csv         # planned spend
│  ├─ actual_spend.csv        # actual spend
├─ src/
│  ├─ load.py                 # load and validate CSVs
│  ├─ reconcile.py            # variance + anomaly detection
│  ├─ forecast.py             # end-of-year forecast
│  ├─ report.py               # export summary PPT
│  └─ __init__.py
├─ artifacts/                 # generated outputs
├─ app_streamlit.py           # interactive dashboard
├─ main.py                    # CLI entrypoint
├─ requirements.txt
├─ README.md
└─ .github/workflows/weekly.yml
```

## ⚙️ Configuration Notes

Budget and actuals must share a Category column.

Variance threshold defaults to 20%; adjust in reconcile.py.

Forecast currently uses simple exponential smoothing; can be upgraded to Prophet or ARIMA.

CLI output path defaults to artifacts/report.pptx.

## 🗺️ Roadmap

 Add Prophet/ARIMA-based forecasting for more robust projections

 Support multiple time periods (monthly reconciliation, not just totals)

 Generate PDF summary alongside PPT

 Extend Streamlit app: interactive anomaly slider + charts

 GitHub Action auto-release with attached PPT report

## 👨‍💻 Author

Portfolio project by Raghav
Part of the AI Automation Portfolio showcasing business-focused AI tools.