#Program to design a simple tracker to record daily expenses and generate reports. 
import os

# The name of the file where we will save data
FILE_NAME = "expenses.txt"

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        from datetime import date as d
        date = str(d.today())
        
    category = input("Enter category (e.g., Food, Rent): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    # Save to file immediately
    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{description},{amount}\n")
    print(" Expense saved successfully!")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    print("\n Expense List ")
    print(f"{'Date':<12} | {'Category':<12} | {'Description':<15} | {'Amount'}")
    print("-" * 50)
    
    with open(FILE_NAME, "r") as file:
        for line in file:
            date, cat, desc, amt = line.strip().split(",")
            print(f"{date:<12} | {cat:<12} | {desc:<15} | ${amt}")

def show_total():
    if not os.path.exists(FILE_NAME):
        print("No data to calculate.")
        return

    total = 0.0
    with open(FILE_NAME, "r") as file:
        for line in file:
            # We split the line and take the last item (the amount)
            parts = line.strip().split(",")
            total += float(parts[3])
            
    print(f"\nTotal Spending to date: ${total:.2f}")

#  Main Menu Loop 
while True:
    print("\n Simple Expense Tracker ")
    print("1. Add Expense")
    print("2. View All")
    print("3. Show Total Spent")
    print("4. Exit")
    
    choice = input("Choose an option: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        show_total()
    elif choice == '4':
        print("Closing tracker. Bye!")
        break
    else:
        print("Invalid choice, try again.")
 
