import sys
sys.path.append("src")

from expenses import add_expense, view_expenses, delete_expense

def test_add_expense():
    add_expense("Test Expense", 100, "test", "26-09-2026")
    
    expenses = view_expenses()
    assert len(expenses) > 0
    
def test_delete_expense():
    expenses = view_expenses()
        
    expense_id = expenses[-1][0]
    delete_expense(expense_id)
    updated_expenses = view_expenses()
    ids = [expense[0] for expense in updated_expenses]
    assert expense_id not in ids
        
print("Expenses tests passed successfully!")