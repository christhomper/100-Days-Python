import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import platform

# Character pools
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# OS-aware clipboard instructions
def get_clipboard_instruction():
    os_name = platform.system()
    if os_name == "Darwin":
        return "👉 Paste it using ⌘ Cmd + V (macOS)"
    elif os_name == "Linux":
        return "👉 Paste it using Ctrl + V or middle-click (Linux)"
    elif os_name == "Windows":
        return "👉 Paste it using Ctrl + V (Windows)"
    else:
        return "Paste it from your clipboard"

# Password Strength Rating
def get_password_strength(num_letters, num_symbols, num_numbers):
    total = num_letters + num_symbols + num_numbers
    if total >= 18 and num_letters >= 6 and num_symbols >= 6 and num_numbers >= 6:
        return "🔒 Strong"
    elif total >= 12 and (
        (num_letters >= 4 and num_symbols >= 4) or
        (num_letters >= 4 and num_numbers >= 4) or
        (num_symbols >= 4 and num_numbers >= 4)
    ):
        return "🔐 Moderate"
    else:
        return "⚠️ Weak"

# Main Password Generator Function
def generate_password():
    try:
        num_letters = int(letter_entry.get())
        num_symbols = int(symbol_entry.get())
        num_numbers = int(number_entry.get())
    except ValueError:
        messagebox.showerror("❌ Invalid Input", "Please enter numeric values only.")
        return

    total = num_letters + num_symbols + num_numbers
    if total < 12:
        messagebox.showwarning("⚠️ Too Short", "Password must be at least 12 characters.")
        return
    if num_letters > len(letters) or num_symbols > len(symbols) or num_numbers > len(numbers):
        messagebox.showerror("❌ Limit Exceeded", "Too many characters requested.")
        return

    password_letters = random.sample(letters, k=num_letters)
    password_symbols = random.sample(symbols, k=num_symbols)
    password_numbers = random.sample(numbers, k=num_numbers)

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    result_var.set(f"\n✅ {password}\n")
    strength_text = get_password_strength(num_letters, num_symbols, num_numbers)
    strength_var.set(strength_text)
    instruction_var.set(get_clipboard_instruction())
    pyperclip.copy(password)

# UI Setup
root = tk.Tk()
root.title("🔐 PyPassword Generator")
root.geometry("400x350")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Instructions
tk.Label(frame, text="How many letters would you like in your password?").grid(row=0, column=0, columnspan=2, sticky="w")
tk.Label(frame, text="🔤 Letters:").grid(row=1, column=0, sticky="w")
letter_entry = tk.Entry(frame, width=5)
letter_entry.grid(row=1, column=1)

tk.Label(frame, text="How many symbols would you like?").grid(row=2, column=0, columnspan=2, sticky="w")
tk.Label(frame, text="💠 Symbols:").grid(row=3, column=0, sticky="w")
symbol_entry = tk.Entry(frame, width=5)
symbol_entry.grid(row=3, column=1)

tk.Label(frame, text="How many numbers would you like?").grid(row=4, column=0, columnspan=2, sticky="w")
tk.Label(frame, text="🔢 Numbers:").grid(row=5, column=0, sticky="w")
number_entry = tk.Entry(frame, width=5)
number_entry.grid(row=5, column=1)

# Button
tk.Button(frame, text="✨ Generate Password", command=generate_password).grid(row=6, columnspan=2, pady=10)

# Output
result_var = tk.StringVar()
tk.Label(frame, textvariable=result_var, font=("Courier", 12), wraplength=300).grid(row=7, columnspan=2, pady=5)

strength_var = tk.StringVar()
tk.Label(frame, textvariable=strength_var, font=("Arial", 10, "bold"), fg="green").grid(row=8, columnspan=2)

instruction_var = tk.StringVar()
tk.Label(frame, textvariable=instruction_var, font=("Arial", 9, "italic"), fg="gray").grid(row=9, columnspan=2, pady=5)

# Run the app
root.mainloop()
