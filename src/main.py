from database import create_tables
from expenses import add_expense, view_expenses, delete_expense, edit_expense
from budget import set_budget, get_budget
from reports import show_report


def main():
    create_tables()

    while True:
        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Set Budget")
        print("6. View Budget")
        print("7. Expense Report")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter expense name: ")

            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Please enter a valid amount.")
                continue

            category = input("Enter category: ")
            date = input("Enter date (DD-MM-YYYY): ")

            add_expense(title, amount, category, date)

            print("Expense added successfully!")

        elif choice == "2":
            expenses = view_expenses()

            if not expenses:
                print("No expenses found.")
            else:
                print("\nYour Expenses:")
                print("--------------------------------")

                for expense in expenses:
                    print(
                        f"ID: {expense[0]} | "
                        f"{expense[1]} | "
                        f"₹{expense[2]:.2f} | "
                        f"{expense[3]} | "
                        f"{expense[4]}"
                    )

        elif choice == "3":
            try:
                expense_id = int(input("Enter expense ID to edit: "))
                title = input("Enter new expense name: ")
                amount = float(input("Enter new amount: "))
                category = input("Enter new category: ")
                date = input("Enter new date (DD-MM-YYYY): ")

                edit_expense(expense_id, title, amount, category, date)

                print("Expense updated successfully!")

            except ValueError:
                print("Please enter valid information.")

        elif choice == "4":
            try:
                expense_id = int(input("Enter expense ID to delete: "))
                delete_expense(expense_id)

                print("Expense deleted successfully!")

            except ValueError:
                print("Please enter a valid ID.")

        elif choice == "5":
            try:
                amount = float(input("Enter your monthly budget: "))
                set_budget(amount)

                print("Budget saved successfully!")

            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "6":
            budget = get_budget()

            if budget == 0:
                print("No budget has been set.")
            else:
                print(f"Your monthly budget is: ₹{budget:.2f}")

        elif choice == "7":
            show_report()

        elif choice == "8":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()