from expenses import add_expense, list_expenses, delete_expense
from report import export_csv
from visualize import plot_expenses_by_category
from utils import format_won

def show_menu():
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. List expenses")
    print("3. Delete expense")
    print("4. Export CSV report")
    print("5. Show category chart")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            amount = input("Amount (numbers allowed, decimals OK): ").strip()
            date = input("Date (YYYY-MM-DD): ").strip()
            category = input("Category: ").strip()
            description = input("Description: ").strip()
            add_expense(amount, date, category, description)
            print("Expense added.")
        elif choice == "2":
            expenses = list_expenses()
            if not expenses:
                print("No expenses yet.")
            for idx, e in enumerate(expenses):
                print(f"{idx}. {e.get('date','')} | {e.get('category','')} | {format_won(e.get('amount',0))} | {e.get('description','')}")
        elif choice == "3":
            try:
                idx = int(input("Index of expense to delete: ").strip())
            except ValueError:
                print("Please enter a valid integer index.")
                continue
            ok = delete_expense(idx)
            if ok:
                print("Expense deleted.")
            else:
                print("Index out of range.")
        elif choice == "4":
            filename = input("CSV filename [expenses_report.csv]: ").strip() or "expenses_report.csv"
            export_csv(filename)
        elif choice == "5":
            plot_expenses_by_category()
        elif choice == "6":
            print("Have a nice day!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()