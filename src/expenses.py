from database import connect_database


def add_expense(title, amount, category, date):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO expenses (title, amount, category, date)
        VALUES (?, ?, ?, ?)
        """,
        (title, amount, category, date)
    )

    connection.commit()
    connection.close()


def view_expenses():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    connection.close()

    return expenses

def delete_expense(expense_id):
    connection = connect_database()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    connection.commit()
    connection.close()
    
def edit_expense(expense_id, title, amount, category, date):
    connection = connect_database()
    cursor = connection.cursor()
    
    cursor.execute(
        """
        UPDATE expenses
        SET title = ?, amount = ?, category = ?, date = ?
        WHERE id = ?
        """,
        (title, amount, category, date, expense_id)
    )
    
    connection.commit()
    connection.close()    