import json
import os
from shutil import copyfile

DATA_FILE = "data.json"
BACKUP_FILE = DATA_FILE + ".bak"
NORMALIZED_FILE = "data_normalized.json"

def normalize_entry(e, idx):
    # Accept dict-like entries, otherwise skip
    if not isinstance(e, dict):
        print(f"Warning: entry {idx} is not an object, skipping.")
        return None
    normalized = {}
    # amount -> float
    amt = e.get("amount", 0)
    try:
        # handle strings with commas
        if isinstance(amt, str):
            amt_clean = amt.replace(",", "").strip()
            amt_val = float(amt_clean) if amt_clean != "" else 0.0
        else:
            amt_val = float(amt)
    except Exception:
        print(f"Warning: could not parse amount for entry {idx} ('{amt}'), setting to 0.0")
        amt_val = 0.0
    normalized["amount"] = amt_val
    # date/category/description defaults
    normalized["date"] = str(e.get("date", "")) if e.get("date", "") is not None else ""
    normalized["category"] = str(e.get("category", "Uncategorized"))
    normalized["description"] = str(e.get("description", ""))
    return normalized

def main():
    if not os.path.exists(DATA_FILE):
        print(f"{DATA_FILE} not found. Nothing to validate.")
        return

    # Backup original if not already
    if not os.path.exists(BACKUP_FILE):
        try:
            copyfile(DATA_FILE, BACKUP_FILE)
            print(f"Backup created: {BACKUP_FILE}")
        except Exception as exc:
            print(f"Could not create backup: {exc}")

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw = f.read().strip()
            if raw == "":
                data = []
            else:
                data = json.loads(raw)
    except Exception as exc:
        print(f"Error reading/parsing {DATA_FILE}: {exc}")
        print("Aborting. Your original file is preserved as " + BACKUP_FILE)
        return

    # If single object, wrap into list
    if isinstance(data, dict):
        data = [data]
        print("Wrapped single JSON object into a list.")

    if not isinstance(data, list):
        print("JSON root is not a list; aborting to avoid data loss.")
        return

    normalized = []
    for idx, item in enumerate(data):
        n = normalize_entry(item, idx)
        if n is not None:
            normalized.append(n)

    # Write normalized file
    try:
        with open(NORMALIZED_FILE, "w", encoding="utf-8") as f:
            json.dump(normalized, f, indent=2, ensure_ascii=False)
        print(f"Normalized data written to {NORMALIZED_FILE}.")
        # Optionally overwrite original data.json (ask user? here we replace after making backup)
        os.replace(NORMALIZED_FILE, DATA_FILE)
        print(f"{DATA_FILE} replaced with normalized content. Original backed up at {BACKUP_FILE}.")
    except Exception as exc:
        print(f"Failed to write normalized file: {exc}")

if __name__ == "__main__":
    main()