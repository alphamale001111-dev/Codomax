# functions.py
"""
Lesson 4: Functions in Python
-----------------------------
A function is a block of organized, reusable code that is used to perform a single, related action.
Functions provide better modularity for your application and high degrees of code reusing.
"""

def print_separator():
    print("\n" + "="*60 + "\n")

# --- 1. BASIC FUNCTION DEFINITION ---
def greet(name):
    """This function greets the person passed in as a parameter."""
    return f"Hello, {name}! Welcome to Python Functions."

# --- 2. DEFAULT ARGUMENTS ---
def make_coffee(size="Medium", type="Espresso"):
    return f"Prepared a {size} size {type} coffee."

# --- 3. RETURN MULTIPLE VALUES ---
def min_max(numbers):
    # Returns a tuple
    return min(numbers), max(numbers)

# --- 4. VARIABLE ARGUMENTS (*args and **kwargs) ---
def add_all(*args):
    # *args collects positional arguments into a tuple
    return sum(args)

def print_user_profile(username, **kwargs):
    # **kwargs collects keyword arguments into a dictionary
    print(f"User: {username}")
    for key, value in kwargs.items():
        print(f"  {key.capitalize()}: {value}")

# --- 5. LAMBDA FUNCTIONS (Anonymous Functions) ---
# Small one-line anonymous functions defined using the lambda keyword
multiply = lambda x, y: x * y

def run_lesson():
    print("============================================================")
    print("           🐍 LESSON 4: PYTHON FUNCTIONS 🐍                ")
    print("============================================================")
    
    # 1. Basic Function Call
    print("\n1. DEFINING & CALLING FUNCTIONS:")
    message = greet("Alice")
    print(f"   Calling greet('Alice'):\n     '{message}'")
    
    print_separator()

    # 2. Default Arguments
    print("2. DEFAULT PARAMETER VALUES:")
    print("   If we don't pass values, defaults are used:")
    print(f"     make_coffee(): '{make_coffee()}'")
    print("   We can also overwrite them:")
    print(f"     make_coffee('Large', 'Cappuccino'): '{make_coffee('Large', 'Cappuccino')}'")

    print_separator()

    # 3. Returning Multiple Values
    print("3. RETURNING MULTIPLE VALUES:")
    my_numbers = [12, 45, 2, 99, 18]
    smallest, largest = min_max(my_numbers)
    print(f"   List: {my_numbers}")
    print(f"   Calling min_max(my_numbers) -> Returns tuple: ({smallest}, {largest})")
    print(f"   Unpacked variables -> Smallest: {smallest}, Largest: {largest}")

    print_separator()

    # 4. *args and **kwargs
    print("4. VARIABLE ARGUMENTS (*args & **kwargs):")
    print("   • *args (Arbitrary Positional Arguments - tuple):")
    total = add_all(10, 20, 30, 40)
    print(f"     add_all(10, 20, 30, 40) -> Total: {total}")
    
    print("\n   • **kwargs (Arbitrary Keyword Arguments - dictionary):")
    print("     Calling print_user_profile('johndoe', city='New York', status='Active'):")
    print_user_profile("johndoe", city="New York", status="Active")

    print_separator()

    # 5. Lambda Functions
    print("5. LAMBDA FUNCTIONS (Anonymous one-liner functions):")
    result = multiply(6, 7)
    print(f"   multiply = lambda x, y: x * y")
    print(f"   Calling multiply(6, 7): {result}")

    print_separator()

    # --- 6. INTERACTIVE CHALLENGE ---
    print("💡 MINI-CHALLENGE: Functions!")
    print("Let's see if you can trace function parameters:\n")
    
    score = 0
    
    # Question 1
    print("Question 1: Given this function:")
    print("   def func(a, b=5):\n"
          "       return a * b")
    ans1 = input("What is the output of func(3)? (Enter a number): ").strip()
    if ans1 == "15":
        print("   ✅ Correct! a = 3, and b defaults to 5. 3 * 5 = 15.")
        score += 1
    else:
        print("   ❌ Incorrect. a is 3, b uses default 5. 3 * 5 = 15.")
        
    # Question 2
    print("\nQuestion 2: Given the lambda function:")
    print("   square = lambda x: x ** 2")
    ans2 = input("What is the output of square(4)? (Enter a number): ").strip()
    if ans2 == "16":
        print("   ✅ Correct! 4 squared is 16.")
        score += 1
    else:
        print("   ❌ Incorrect. 4 ** 2 is 16.")
        
    print(f"\nYour score: {score}/2")
    if score == 2:
        print("🎉 Function Expert! You understand how functions process parameters and return values!")
    else:
        print("👍 Good try! Review function structures and arguments, then run again.")
    print("============================================================\n")

if __name__ == "__main__":
    run_lesson()
