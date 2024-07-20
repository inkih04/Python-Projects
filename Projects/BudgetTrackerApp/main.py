expenses = []
budget = 0

def addExpense():
    global budget
    cost = float(input("Introduce the cost of the transaction: "))
    reason = input("Introduce the details of the transaction: ")
    expenses.append({"reason": reason, "cost": cost})
    budget -= cost

def ShowBudgetDetails():
    print(f"Current Budget: {budget}")
    for transaction in expenses:
        print(f"Cost: {transaction['cost']} {transaction['reason']}")

def main():
    global budget
    print("Welcome to the budget app")
    initial_budget = float(input("Please enter your initial budget: "))
    budget = initial_budget

    while True:
        print("What would you like to do ? ")
        print("1- Add an expense")
        print("2- Show budget details")
        print("3- Exit")

        num = int(input(""))
        if num == 1:
            addExpense()

        elif num == 2:
            ShowBudgetDetails()

        elif num == 3:
            exit(0)
        
        print(f"Current budget: {budget}")

if __name__ == "__main__":
    main()
