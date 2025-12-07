import json
import os
from json import JSONDecodeError
from shutil import copyfile

DATA_FILE = "data.json"

def load_expenses():
    """
    Load expenses from DATA_FILE.
    Returns an empty list if the file does not exist, is empty, or contains invalid JSON.
    If the JSON is invalid, moves the corrupted file to DATA_FILE.bak.
    """
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except JSONDecodeError:
        # Move corrupted file aside and start fresh
        backup = DATA_FILE + ".bak"
        try:
            os.replace(DATA_FILE, backup)
        except Exception:
            try:
                copyfile(DATA_FILE, backup)
            except Exception:
                pass
        print(f"Warning: {DATA_FILE} contained invalid JSON and was moved to {backup}. Starting with an empty list.")
        return []
    except Exception as e:
        print(f"Error loading {DATA_FILE}: {e}")
        return []

def save_expenses(expenses):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(expenses, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving {DATA_FILE}: {e}")

def add_expense(amount, date, category, description):
    expenses = load_expenses()
    # Ensure amount is stored as a number (float)
    try:
        amt = float(amount)
    except Exception:
        amt = 0.0
    expenses.append({
        "amount": amt,
        "date": date,
        "category": category,
        "description": description
    })
    save_expenses(expenses)

def list_expenses():
    return load_expenses()

def delete_expense(index):
    expenses = load_expenses()
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)
        return True
    else:
        return False