import csv
from expenses import list_expenses
from utils import format_won

def export_csv(filename="expenses_report.csv"):
    expenses = list_expenses()
    if not expenses:
        print("No expenses to export.")
        return
    fieldnames = ["amount_raw", "amount_formatted", "date", "category", "description"]
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for e in expenses:
                amt = e.get("amount", 0)
                writer.writerow({
                    "amount_raw": amt,
                    "amount_formatted": format_won(amt),
                    "date": e.get("date", ""),
                    "category": e.get("category", ""),
                    "description": e.get("description", "")
                })
        print(f"Expenses exported to {filename}")
    except Exception as exc:
        print(f"Failed to export CSV: {exc}")