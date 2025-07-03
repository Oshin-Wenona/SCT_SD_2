import tkinter as tk
from tkinter import messagebox
import random

# Generate random number
secret_number = random.randint(1, 100)

# Function to check the user's guess
def check_guess():
    guess = entry.get()
    if not guess.isdigit():
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        return

    guess = int(guess)

    if guess < secret_number:
        result_label.config(text="🔼 Too low! Try again.", fg="blue")
    elif guess > secret_number:
        result_label.config(text="🔽 Too high! Try again.", fg="blue")
    else:
        result_label.config(text=f"✅ Correct! The number was {secret_number}", fg="green")
        messagebox.showinfo("Congratulations!", "You guessed it right!")

# Function to reset the game
def reset_game():
    global secret_number
    secret_number = random.randint(1, 100)
    result_label.config(text="")
    entry.delete(0, tk.END)

# GUI window setup
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("350x250")
root.resizable(False, False)

# Heading
title_label = tk.Label(root, text="🎲 Guess the Number!", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Instruction
instruction_label = tk.Label(root, text="I'm thinking of a number between 1 and 100")
instruction_label.pack()

# Entry field
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

# Submit button
guess_button = tk.Button(root, text="Submit Guess", command=check_guess, bg="lightgreen")
guess_button.pack()

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Play Again", command=reset_game, bg="lightblue")
reset_button.pack()

# Run the app
root.mainloop()