# loops.py
"""
Lesson 3: Conditionals and Loops in Python
-----------------------------------------
Conditionals (if-elif-else) allow execution of code blocks based on conditions.
Loops allow repeating a block of code multiple times. Python has two main loop types:
- for loops: iterate over a sequence (list, tuple, string, range)
- while loops: repeat as long as a condition is True
"""

import time

def print_separator():
    print("\n" + "="*60 + "\n")

def run_lesson():
    print("============================================================")
    print("        🐍 LESSON 3: PYTHON CONDITIONALS & LOOPS 🐍         ")
    print("============================================================")
    
    # --- 1. CONDITIONALS (IF-ELIF-ELSE) ---
    print("\n1. CONDITIONALS (IF-ELIF-ELSE):")
    score = 85
    print(f"   For score = {score}:")
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
        
    print(f"   Code structure:\n"
          f"     if score >= 90: grade = 'A'\n"
          f"     elif score >= 80: grade = 'B'\n"
          f"     ...\n"
          f"   Resulting Grade: '{grade}'")

    print_separator()

    # --- 2. FOR LOOPS & RANGE ---
    print("2. FOR LOOPS (Iterating over collections or ranges):")
    
    # Iterating over a list
    fruits = ["Apple", "Banana", "Cherry"]
    print("   • Iterating over list elements:")
    for fruit in fruits:
        print(f"     Found fruit: {fruit}")
        
    # Iterating over a range(start, stop, step)
    # range(5) generates 0, 1, 2, 3, 4
    print("\n   • Iterating using range(1, 6, 2) (start=1, stop=6, step=2):")
    for num in range(1, 6, 2):
        print(f"     Number: {num}")

    print_separator()

    # --- 3. WHILE LOOPS ---
    print("3. WHILE LOOPS (Executing while a condition remains True):")
    count = 3
    print("   • Decrementing counter starting at 3:")
    while count > 0:
        print(f"     Count is {count}")
        count -= 1
    print("     Loop finished! count is now 0.")

    print_separator()

    # --- 4. LOOP CONTROL: BREAK, CONTINUE, PASS ---
    print("4. LOOP CONTROL STATEMENTS:")
    
    # break example
    print("   • 'break' (Exits the loop prematurely when conditions are met):")
    print("     Searching for number 3 in range(1, 10):")
    for n in range(1, 10):
        if n == 3:
            print(f"       -> Found {n}! Breaking out of the loop.")
            break
        print(f"       Checking: {n}")
        
    # continue example
    print("\n   • 'continue' (Skips the rest of the current iteration):")
    print("     Printing odd numbers from 1 to 5 (skipping evens):")
    for n in range(1, 6):
        if n % 2 == 0:
            continue # Skips printing even numbers
        print(f"       Odd number: {n}")
        
    # pass example
    print("\n   • 'pass' (A null statement, used as a placeholder):")
    print("     if True:\n"
          "         pass # Placeholder to avoid indentation error")
    if True:
        pass

    print_separator()

    # --- 5. INTERACTIVE CHALLENGE ---
    print("💡 MINI-CHALLENGE: Predict and Code!")
    print("Answer the following questions:\n")
    
    score_challenge = 0
    
    # Question 1
    print("Question 1: Look at the following loop:")
    print("   for i in range(2, 5):\n"
          "       print(i)")
    ans1 = input("What values of i will be printed? (Format: 2, 3, 4 or similar): ").strip().replace(" ", "")
    if ans1 in ["2,3,4", "234"]:
        print("   ✅ Correct! range(start, stop) goes up to stop - 1.")
        score_challenge += 1
    else:
        print("   ❌ Incorrect. range(2, 5) generates values starting from 2 up to, but not including, 5 (i.e. 2, 3, 4).")
        
    # Question 2
    print("\nQuestion 2: Look at this loop:")
    print("   x = 10\n"
          "   while x > 5:\n"
          "       x -= 2")
    ans2 = input("What is the final value of x after this loop completes? (Enter a number): ").strip()
    if ans2 == "4":
        print("   ✅ Correct! Loop runs when x = 10 (becomes 8), and x = 8 (becomes 6), and x = 6 (becomes 4). Then 4 > 5 is False.")
        score_challenge += 1
    else:
        print("   ❌ Incorrect. Let's trace it:\n"
              "      - Init: x = 10. 10 > 5? True. x becomes 8.\n"
              "      - Loop: x = 8. 8 > 5? True. x becomes 6.\n"
              "      - Loop: x = 6. 6 > 5? True. x becomes 4.\n"
              "      - Loop check: x = 4. 4 > 5? False. Loop ends. Final value is 4.")
        
    print(f"\nYour score: {score_challenge}/2")
    if score_challenge == 2:
        print("🎉 Loop Wizard! You understand conditionals and loop structures!")
    else:
        print("👍 Good try! Review loop constructs and try running again.")
    print("============================================================\n")

if __name__ == "__main__":
    run_lesson()
