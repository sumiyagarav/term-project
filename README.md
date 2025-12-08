# Personal Expense Tracker CLI (KRW-format)

## Introduction
SEOULTECH OSS-Term Project

This is a simple personal expense tracker with cli, csv export, and visualization.

## Prerequisites
- Python
- `matplotlib` (for visualization)

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
cd C:\path\expense_tracker (e.g. cd C:\Users\Admin\term-project).
```

2. Run the CLI:
```cmd
python cli.py
```
Menu options let you:
- Add/list/delete expenses
- Export CSV
- Show a category chart
<img width="1130" height="760" alt="run" src="https://github.com/user-attachments/assets/e803baba-52c5-4e1f-839a-b284c2391920" />

3. Run visualization directly:
   ```cmd
   python visualize.py
   ```
   - In this screenshot you can see that I only ran the visualization because I already installed `matplotlib`. 
<img width="1838" height="825" alt="visualize" src="https://github.com/user-attachments/assets/9e5468d8-a05b-4cb9-a03a-aa8635819430" />

## Notes:
   
Data format
- Each expense object should have:
  - amount: number
  - date: string (e.g., "2025-12-06")
  - category: string
  - description: string

- Backup current data.json:
('from the project directory')
  ```cmd
  copy data.json data.json.bak
 
 - I daily use money manager application so i thought it would be cool if i could do it from my laptop. I'm not a cs major so it's not advanced but i tried my best. 
 ## Reference
 - Repository template - https://github.com/always0ne/repositoryTemplate
 - Python Documentation - https://docs.python.org
 - w3schools - https://www.w3schools.com/python/
 - opencv - https://opencv.org/
## License💳
This project is licensed under the MIT License 

