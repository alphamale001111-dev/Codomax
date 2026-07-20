# variables_data_types.py
"""
Lesson 1: Variables and Data Types in Python
--------------------------------------------
Variables are containers for storing data values. Python has no command for declaring a variable;
a variable is created the moment you first assign a value to it.

Python is dynamically typed, meaning you don't need to declare the type of a variable.
"""

def print_separator():
    print("\n" + "="*60 + "\n")

def run_lesson():
    print("============================================================")
    print("      🐍 LESSON 1: PYTHON VARIABLES & DATA TYPES 🐍        ")
    print("============================================================")
    
    # --- 1. VARIABLES ---
    print("\n1. VARIABLES:")
    print("Variables store data. We use the '=' operator to assign values.")
    
    x = 5          # x is of type int
    name = "Alice" # name is of type str (string)
    
    print(f"   Assigning: x = 5       -> Value: {x}, Type: {type(x)}")
    print(f"   Assigning: name = 'Alice' -> Value: '{name}', Type: {type(name)}")
    
    # Dynamic Typing: We can change the type of a variable easily
    x = "Now I am a string!"
    print(f"   Reassigning x: x = 'Now I am a string!' -> Value: '{x}', Type: {type(x)}")

    print_separator()

    # --- 2. DATA TYPES ---
    print("2. CORE DATA TYPES IN PYTHON:")
    
    # Integer
    my_int = 42
    print(f"   • Integer (int): Whole numbers.")
    print(f"     Example: my_int = {my_int} | Type: {type(my_int)}")
    
    # Float
    my_float = 3.14159
    print(f"   • Float (float): Decimal numbers.")
    print(f"     Example: my_float = {my_float} | Type: {type(my_float)}")
    
    # String
    my_str = "Hello, Python!"
    print(f"   • String (str): Ordered sequence of characters enclosed in quotes.")
    print(f"     Example: my_str = '{my_str}' | Type: {type(my_str)}")
    
    # Boolean
    my_bool = True
    print(f"   • Boolean (bool): Represents logical values: True or False.")
    print(f"     Example: my_bool = {my_bool} | Type: {type(my_bool)}")
    
    # List
    my_list = ["apple", "banana", "cherry", 42]
    print(f"   • List (list): Ordered, mutable collection of items (can hold mixed types).")
    print(f"     Example: my_list = {my_list} | Type: {type(my_list)}")
    print(f"     Access first item (my_list[0]): '{my_list[0]}'")
    
    # Tuple
    my_tuple = (10, 20, 30)
    print(f"   • Tuple (tuple): Ordered, immutable (cannot be changed) collection of items.")
    print(f"     Example: my_tuple = {my_tuple} | Type: {type(my_tuple)}")
    
    # Dictionary
    my_dict = {"name": "Alice", "age": 25, "role": "Intern"}
    print(f"   • Dictionary (dict): Unordered, mutable collection of key-value pairs.")
    print(f"     Example: my_dict = {my_dict} | Type: {type(my_dict)}")
    print(f"     Access key 'name' (my_dict['name']): '{my_dict['name']}'")
    
    # Set
    my_set = {1, 2, 3, 3, 2, 1} # Duplicates are removed automatically
    print(f"   • Set (set): Unordered collection of unique items.")
    print(f"     Example: my_set = {my_set} | Type: {type(my_set)}")

    print_separator()

    # --- 3. TYPE CASTING (CONVERSION) ---
    print("3. TYPE CASTING (CONVERTING BETWEEN TYPES):")
    print("Sometimes you need to convert a variable from one type to another.")
    
    str_num = "100"
    converted_int = int(str_num)
    print(f"   Convert string to int: int('{str_num}') -> {converted_int} (Type: {type(converted_int)})")
    
    float_num = 9.99
    converted_int_2 = int(float_num) # Truncates towards zero
    print(f"   Convert float to int (truncates): int({float_num}) -> {converted_int_2} (Type: {type(converted_int_2)})")
    
    int_num = 5
    converted_float = float(int_num)
    print(f"   Convert int to float: float({int_num}) -> {converted_float} (Type: {type(converted_float)})")
    
    converted_str = str(42)
    print(f"   Convert int to string: str(42) -> '{converted_str}' (Type: {type(converted_str)})")

    print_separator()

    # --- 4. INTERACTIVE CHALLENGE ---
    print("💡 MINI-CHALLENGE: Test Your Knowledge!")
    print("Solve the questions below. Think of the answer before typing it in.\n")
    
    score = 0
    
    # Question 1
    ans1 = input("1. If x = '5.5', is x a string or a float? (Enter 'string' or 'float'): ").strip().lower()
    if ans1 == "string":
        print("   ✅ Correct! Because it is wrapped in quotes.")
        score += 1
    else:
        print("   ❌ Incorrect. Since it is wrapped in quotes, it is a string ('str').")
        
    # Question 2
    ans2 = input("2. Which data type is ordered but immutable? (Enter 'list' or 'tuple' or 'set'): ").strip().lower()
    if ans2 == "tuple":
        print("   ✅ Correct! Tuples cannot be modified after creation.")
        score += 1
    else:
        print("   ❌ Incorrect. Tuples are ordered and immutable. Lists are mutable.")
        
    # Question 3
    ans3 = input("3. What is the output of int(3.9)? (Enter a number): ").strip()
    if ans3 == "3":
        print("   ✅ Correct! int() truncates decimal values towards zero.")
        score += 1
    else:
        print("   ❌ Incorrect. int(3.9) truncates the decimal, resulting in 3.")
        
    print(f"\nYour score: {score}/3")
    if score == 3:
        print("🎉 Perfect! You have mastered variables and data types!")
    else:
        print("👍 Good try! Review the code examples in variables_data_types.py and try again.")
    print("============================================================\n")

if __name__ == "__main__":
    run_lesson()
