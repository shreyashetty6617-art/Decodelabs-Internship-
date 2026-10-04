# Expense Tracker - Project 2 | Shreya Shetty | DecodeLabs 2026
# Industrial Training Kit - Batch 2026

def expense_tracker():
    print(" Welcome to Shreya's Expense Tracker")
    print("--------------------------------------")
    total_spent = 0
    expense_list = []
    count = 0
    while True:
        user_input = input("\nEnter expense amount: ").strip()

        # Exit condition
        if user_input.lower() == 'done':
            break
        try:
            # Try to convert to float to allow decimals like 50.5
            expense = float(user_input)
            
            if expense < 0:
                print(" Expense cannot be negative! Try again.")
                continue
            total_spent += expense
            count += 1
            expense_list.append(expense)
            
            print(f" Added: ₹{expense} | Current Total: ₹{total_spent}")

        except ValueError:
            print(f" Invalid Data: '{user_input}' is not a number. Please enter like 100, 50.5, 20")
    print("\n========== EXPENSE REPORT ==========")
    print(f"Total Entries: {count}")
    if expense_list:
        print(f"Expenses: {expense_list}")
        print(f"Average Expense: ₹{total_spent/count:.2f}")
    print(f"💵 TOTAL SPENT: ₹{total_spent:.2f}")
    print("====================================")
    print("Thank you! Data processing complete.")
if __name__ == "__main__":
    expense_tracker()

