# Testing

## Testing Method

The Expense Tracker was tested using Python's pytest framework.

## Tests Performed

### 1. Add Expense Test
Checks whether a new expense can be added to the database successfully.

### 2. Delete Expense Test
Checks whether an existing expense can be deleted from the database.

## Manual Testing

The following features were also tested manually:

- Add Expense
- View Expenses
- Edit Expense
- Delete Expense
- Set Budget
- View Budget
- Expense Report
- Invalid amount input
- Invalid menu choice

## Test Result

The automated expense tests were executed using pytest.

Command used:

python -m pytest tests/test_expenses.py

The tests completed successfully.