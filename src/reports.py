from database import connect_database
from budget import get_budget

def get_total_expenses():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    result = cursor.fetchone()

    connection.close()

    if result [0] is None:
        return 0
    return result[0]

def get_cateogory_summary():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    results = cursor.fetchall()

    connection.close()

    return results
def show_report():
    total = get_total_expenses()
    budget = get_budget()
    remaining = budget - total
    
    print("\n==============================")
    print("       EXPENSE REPORT")
    print("==============================")
    print(f"Total Expenses: ₹{total:.2f}")
    print(f"Budget: ₹{budget:.2f}")
    print(f"Remaining Budget: ₹{remaining:.2f}")
    
    print("\nSpending by Category:")
    print("------------------------------")
    
    cateogories = get_cateogory_summary()
    if not cateogories:
        print("No expenses found.")
    else:
        for category, amount in cateogories:
            print(f"{category}: ₹{amount:.2f}")
            