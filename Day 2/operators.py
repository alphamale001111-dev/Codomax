# operators.py
"""
Lesson 2: Operators in Python
-----------------------------
Operators are special symbols that perform operations on variables and values.
Python divides operators into several groups:
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity and Membership operators
"""

def print_separator():
    print("\n" + "="*60 + "\n")

def run_lesson():
    print("============================================================")
    print("            🐍 LESSON 2: PYTHON OPERATORS 🐍               ")
    print("============================================================")
    
    # --- 1. ARITHMETIC OPERATORS ---
    print("\n1. ARITHMETIC OPERATORS:")
    a = 15
    b = 4
    print(f"   Using a = {a} and b = {b}:")
    print(f"   • Addition (+):        a + b = {a + b}")
    print(f"   • Subtraction (-):     a - b = {a - b}")
    print(f"   • Multiplication (*):  a * b = {a * b}")
    print(f"   • Division (/):        a / b = {a / b}   (Always returns a float!)")
    print(f"   • Floor Division (//): a // b = {a // b}  (Rounds down to nearest integer)")
    print(f"   • Modulo (%):          a % b = {a % b}   (Remainder of division)")
    print(f"   • Exponentiation (**): a ** b = {a ** b} (a to the power of b)")

    print_separator()

    # --- 2. ASSIGNMENT OPERATORS ---
    print("2. ASSIGNMENT OPERATORS:")
    x = 10
    print(f"   Initial x: {x}")
    x += 5  # Same as: x = x + 5
    print(f"   • x += 5:  {x}")
    x -= 3  # Same as: x = x - 3
    print(f"   • x -= 3:  {x}")
    x *= 2  # Same as: x = x * 2
    print(f"   • x *= 2:  {x}")
    x /= 4  # Same as: x = x / 4
    print(f"   • x /= 4:  {x}")

    print_separator()

    # --- 3. COMPARISON OPERATORS ---
    print("3. COMPARISON OPERATORS (Return True or False):")
    x = 10
    y = 20
    print(f"   Using x = {x} and y = {y}:")
    print(f"   • Equal (==):            x == y is {x == y}")
    print(f"   • Not Equal (!=):        x != y is {x != y}")
    print(f"   • Greater Than (>):      x > y is {x > y}")
    print(f"   • Less Than (<):         x < y is {x < y}")
    print(f"   • Greater or Equal (>=): x >= 10 is {x >= 10}")
    print(f"   • Less or Equal (<=):    y <= 20 is {y <= 20}")

    print_separator()

    # --- 4. LOGICAL OPERATORS ---
    print("4. LOGICAL OPERATORS (Combine boolean conditions):")
    p = True
    q = False
    print(f"   Using p = {p} and q = {q}:")
    print(f"   • 'and' (True if both are True):         p and q = {p and q}")
    print(f"   • 'or'  (True if at least one is True):  p or q  = {p or q}")
    print(f"   • 'not' (Reverses the result):           not p   = {not p}")

    print_separator()

    # --- 5. MEMBERSHIP OPERATORS ---
    print("5. MEMBERSHIP OPERATORS (Check if item is in sequence):")
    fruits = ["apple", "banana", "cherry"]
    print(f"   fruits list = {fruits}")
    print(f"   • 'apple' in fruits:     {'apple' in fruits}")
    print(f"   • 'grape' not in fruits: {'grape' not in fruits}")

    print_separator()

    # --- 6. INTERACTIVE CHALLENGE ---
    print("💡 MINI-CHALLENGE: Math & Logic!")
    print("Answer the questions below to test your operational skills:\n")
    
    score = 0
    
    # Question 1
    ans1 = input("1. What is the output of 17 // 5? (Enter an integer): ").strip()
    if ans1 == "3":
        print("   ✅ Correct! 17 divided by 5 is 3 with a remainder of 2. Floor division gives 3.")
        score += 1
    else:
        print("   ❌ Incorrect. 17 // 5 performs floor division which returns 3.")
        
    # Question 2
    ans2 = input("2. What is the output of 17 % 5? (Enter an integer): ").strip()
    if ans2 == "2":
        print("   ✅ Correct! Modulo operator (%) returns the remainder, which is 2.")
        score += 1
    else:
        print("   ❌ Incorrect. 17 % 5 is the remainder of division, which is 2.")
        
    # Question 3
    ans3 = input("3. If x = True and y = False, what does (x or y) and (not y) evaluate to? (Enter 'True' or 'False'): ").strip().title()
    if ans3 == "True":
        print("   ✅ Correct! (x or y) is True, and (not y) is True. True and True is True.")
        score += 1
    else:
        print("   ❌ Incorrect. Let's break it down:\n      (True or False) is True.\n      (not False) is True.\n      True and True evaluates to True.")
        
    print(f"\nYour score: {score}/3")
    if score == 3:
        print("🎉 Outstanding! You are an Operator Master!")
    else:
        print("👍 Good try! Check the examples above and try running the file again.")
    print("============================================================\n")

if __name__ == "__main__":
    run_lesson()
