import tkinter as tk


window = tk.Tk()

label = tk.Label(window, text="Hello", font=("Arial", 40, "bold"), fg="black")
label.pack()

window.mainloop()