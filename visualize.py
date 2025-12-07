import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from expenses import list_expenses
from collections import defaultdict
from datetime import datetime

def format_won_ticks(x, pos):
    # x is float, show integer with comma and ₩ prefix
    try:
        return f"₩{int(round(x)):,}"
    except Exception:
        return f"₩{x}"

def plot_expenses_by_category():
    expenses = list_expenses()
    totals = defaultdict(float)
    for e in expenses:
        totals[e['category']] += float(e['amount'])

    categories = list(totals.keys())
    amounts = [totals[c] for c in categories]

    fig, ax = plt.subplots()
    ax.bar(categories, amounts)
    ax.set_xlabel('Category')
    ax.set_ylabel('Total Expense')
    ax.set_title('Expenses by Category')
    ax.yaxis.set_major_formatter(FuncFormatter(format_won_ticks))
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_expenses_by_category()