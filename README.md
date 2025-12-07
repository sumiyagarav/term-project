# Personal Expense Tracker CLI (KRW-format)

## Introduction
SEOULTECH OSS-Term Project

This is a simple personal expense tracker with cli, CSV export, and visualization.

## Prerequisites
- Python
- matplotlib (for visualization)

Install matplotlib:
```cmd
pip install matplotlib
```
## Key features
- Add, list, and delete expenses via an interactive CLI (`cli.py`).
- Export CSV reports with both raw and a formatted amounts (`report.py`). 
- Visualize expenses by category using Matplotlib (`visualize.py`).
- KRW formatting via `utils.py`.
- `data.json` - created automatically when you add the first expense.
- Helper script: data validator (`validate_data.py`).

## How To Run

1. Open Command Prompt and change directory to the project folder:
```cmd
cd C:\path\expense_tracker
```

2. Run the CLI:
```cmd
python cli.py
```
Menu options let you:
- Add/list/delete expenses
- Export CSV
- Show a category chart

3. Run visualization directly:
   ```cmd
   python visualize.py
   ```
      
## Notes:
   
Data format
- Each expense object should have:
  - amount: number
  - date: string (e.g., "2025-12-06")
  - category: string
  - description: string

  Example `data.json` entry:
```json
[
  {
    "amount": 8500.0,
    "date": "2025-12-06",
    "category": "Food",
    "description": "Lunch"
  }
]

- Test the formatter:
  ```cmd
  python -c "from utils import format_won; print(format_won(123456.87))"
  # Expected: ₩123,457
  ```

- Backup current data.json:
('from the project directory')
  ```cmd
  copy data.json data.json.bak
  ```
## Inspiration 
 - I daily use money manager application so i thought it would be cool if i could do it from my laptop. I'm not a cs major so it's not advanced but i tried my best. 
 ## Reference
 - Repository template - https://github.com/always0ne/repositoryTemplate
 - Python Documentation - https://docs.python.org
 - w3schools - https://www.w3schools.com/python/
 - opencv - https://opencv.org/
## License💳
This project is licensed under the MIT License 

