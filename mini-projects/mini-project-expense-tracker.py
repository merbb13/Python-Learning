income = {}
expense = {}
balance = 0
while True:
    print("\nWelcome to Expense Tracker")
    print(f"Your balance is: {balance}")
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Income")
    print("4. View Expense")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        desc = input("Enter Income Description: ")
        try:
            amount = int(input("Enter amount: "))
            if type(amount) == int:
                income[desc] = amount
                balance += amount
                print("Income added!")
            else:
                print("Invalid Amount Value")
        except ValueError:
            print("Value not a number.")
    elif choice == "2":
        desc = input("Enter Expense Description: ")
        try:
            amount = int(input("Enter amount: "))
            if type(amount) == int:
                expense[desc] = amount
                balance -= amount
                print("Expense added!")
            else:
                print("Invalid Amount Value")
        except ValueError:
            print("Value not a number.")
    elif choice == "3":
        print("\nHere is your Income")
        for key, value in income.items():
            print(f"{key}: {value}")
    elif choice == "4":
        print("\nHere is your Expense")
        for key, value in expense.items():
            print(f"{key}: {value}")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid input!")