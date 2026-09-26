# Sequence Diagram

User
  |
  | Enter expense details
  v
main.py
  |
  | Call add_expense()
  v
expenses.py
  |
  | Send expense data
  v
database.py
  |
  | Insert data
  v
expenses.db
  |
  | Save expense
  v
database.py
  |
  | Success
  v
expenses.py
  |
  | Return result
  v
main.py
  |
  | Display "Expense added successfully!"
  v
User