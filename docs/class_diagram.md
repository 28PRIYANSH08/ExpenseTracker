# Class / Component Diagram

Main Program
    |
    +--> Expense Management
    |       |
    |       +--> Add Expense
    |       +--> View Expenses
    |       +--> Edit Expense
    |       +--> Delete Expense
    |
    +--> Budget Management
    |       |
    |       +--> Set Budget
    |       +--> View Budget
    |
    +--> Reports
            |
            +--> Total Expenses
            +--> Category Summary
            +--> Remaining Budget

All components
    |
    v
Database Management
    |
    v
SQLite Database