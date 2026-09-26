from database import connect_database


def set_budget(amount):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS budget (
            id INTEGER PRIMARY KEY,
            amount REAL NOT NULL
        )
    """)

    cursor.execute("DELETE FROM budget")

    cursor.execute(
        "INSERT INTO budget (id, amount) VALUES (1, ?)",
        (amount,)
    )

    connection.commit()
    connection.close()


def get_budget():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS budget (
            id INTEGER PRIMARY KEY,
            amount REAL NOT NULL
        )
    """)

    cursor.execute("SELECT amount FROM budget WHERE id = 1")
    result = cursor.fetchone()

    connection.close()

    if result:
        return result[0]

    return 0