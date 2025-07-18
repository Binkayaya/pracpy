import tkinter as tk
from tkinter import messagebox
import requests

def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()
        joke = response.json()
        return joke["setup"], joke["punchline"]
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Could not fetch joke from API.")
        return None, None

def show_setup():
    global current_setup, current_punchline
    guess_entry.delete(0, tk.END)
    response_label.config(text="")

    setup, punchline = get_joke()
    if setup:
        current_setup = setup
        current_punchline = punchline
        setup_label.config(text=setup)
    else:
        setup_label.config(text="Failed to load joke. Try again.")

def reveal_punchline():
    guess = guess_entry.get().strip()
    if not current_setup:
        response_label.config(text="Click 'Get Joke' first!")
        return

    if not guess:
        response_label.config(text="Enter a guess first!")
        return

    response_text = f"No! Not '{guess}'...\nBut: {current_punchline}"
    response_label.config(text=response_text)

# Create window
root = tk.Tk()
root.title("🤣 Joke Guesser")
root.geometry("900x300")
root.configure(bg="white")

current_setup = None
current_punchline = None

# Setup label
setup_label = tk.Label(root, text="", font=("Arial", 14), wraplength=450, bg="white", justify="center")
setup_label.pack(pady=20)

# Guess input
guess_entry = tk.Entry(root, font=("Arial", 12), width=40)
guess_entry.pack(pady=5)

# Submit guess button
submit_button = tk.Button(root, text="Submit Guess", command=reveal_punchline, bg="#4CAF50", fg="white")
submit_button.pack(pady=5)

# Response label
response_label = tk.Label(root, text="", font=("Arial", 12), wraplength=450, bg="white", fg="blue", justify="center")
response_label.pack(pady=10)

# Get joke button
get_button = tk.Button(root, text="Get New Joke", command=show_setup, bg="#2196F3", fg="white")
get_button.pack(pady=10)

# Start GUI loop
root.mainloop()