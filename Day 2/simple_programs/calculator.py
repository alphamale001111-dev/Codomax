# simple_programs/calculator.py
"""
Simple Calculator
-----------------
A basic command-line calculator that demonstrates functions, conditionals, and loops.
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def display_menu():
    print("\n--- Simple Calculator Menu ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

def main():
    print("====================================================")
    print("           🧮 PYTHON SIMPLE CALCULATOR 🧮           ")
    print("====================================================")
    
    while True:
        display_menu()
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '5':
            print("\nExiting calculator. Goodbye! 👋")
            break
            
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input! Please enter numeric values.")
                continue
                
            if choice == '1':
                print(f"👉 Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"👉 Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"👉 Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(f"👉 Result: {result}")
                else:
                    print(f"👉 Result: {num1} / {num2} = {result}")
        else:
            print("❌ Invalid Choice! Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
