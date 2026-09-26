# Database Design

## Expenses Table

+-----------------------------+
|          expenses           |
+-----------------------------+
| id       : INTEGER (PK)     |
| title    : TEXT             |
| amount   : REAL             |
| category : TEXT             |
| date     : TEXT             |
+-----------------------------+


## Budget Table

+-----------------------------+
|           budget            |
+-----------------------------+
| id       : INTEGER (PK)     |
| amount   : REAL             |
+-----------------------------+


The Expense Tracker uses SQLite to store
expense and budget information.

The expenses table stores individual expenses.
The budget table stores the monthly budget.