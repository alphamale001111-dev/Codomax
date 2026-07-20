# simple_programs/guess_number.py
"""
Number Guessing Game
--------------------
Demonstrates standard library usage (import random), loops (while/for),
conditionals (if/elif/else), variables, and input handling.
"""

import random

def play_game():
    print("====================================================")
    print("         🎯 PYTHON NUMBER GUESSING GAME 🎯          ")
    print("====================================================")
    print("I have selected a secret number between 1 and 100.")
    print("You have 7 attempts to guess it. Good luck!\n")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"Attempts remaining: {remaining}")
        
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter a whole number.")
            continue
            
        attempts += 1
        
        if guess < secret_number:
            print("📈 Too LOW! Try a higher number.\n")
        elif guess > secret_number:
            print("📉 Too HIGH! Try a lower number.\n")
        else:
            print(f"🎉 CONGRATULATIONS! You guessed the number {secret_number} in {attempts} attempts! 🏆")
            return
            
    print(f"💀 Game Over! The secret number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    play_game()
