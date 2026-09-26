# System Architecture

User
  |
  v
main.py
  |
  +-------------------+
  |         |         |
  v         v         v
expenses.py budget.py reports.py
  |         |         |
  +---------+---------+
            |
            v
       database.py
            |
            v
       expenses.db