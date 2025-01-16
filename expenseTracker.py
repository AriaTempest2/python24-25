def add_expenses(expense, category, amount): # remove later
    if category not in expense:
        expense[category] = []

    expense[category].append(amount)
    return expense

def get_total_expenses(expenses):
    return sum(sum(amounts) for amounts in expenses.values) 

def get_category_summary():
    return {category: sum(amount) for category, amount in expenses.items}
    print(f"category")


def display_expense_report(expenses):
    category_summary = get_category_summary(expenses)
    category

expenses = {}

while True:
    print("#################################")
    print("###     MY EXPENSE TRACKER    ###")
    print("#################################")
    print("\n")
    print("!. Add Expense")
    print("2. View Total Expense")
    print("3. View Expense Report")
    print("4. Quit")

    choice = int(input("Enter your Choice: "))
    if choice == 1:
        category = input("Enter the Expense Category (e.g. food, transportation, utilities, etc): ")
        amount = float(input("Enter the expense amount: "))
        expense = add_expenses(expenses, category, amount)
        print("Expense added successfully")
    elif choice == 2:
        total = get_total_expenses(expenses)
        print(f"Total Expenses so far: ${total}")

    elif choice == 3:
        display_expense_report(expenses)

    elif choice == 4:
        break
    elif choice > 4:
        print("STOPPPPP!!! IVE PLAYED THESE GAMES BEFORE!!!")